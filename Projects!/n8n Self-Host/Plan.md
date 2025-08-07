1. Provision DigitalOcean droplet
Create a $10/mo “Basic” droplet running **Ubuntu 22.04 LTS** from the control-panel or via `doctl`:
  2. Choose closest region + IPv6.  
  3. Add your existing SSH public key.  
  4. Name it `n8n-prod`.  
After creation, note the public IP.  
Log in as **root** and create a limited sudo user:  
```bash
adduser deploy && usermod -aG sudo deploy
```  
Harden server:  
```bash
ufw allow OpenSSH && ufw allow 80,443/tcp && ufw enable
sed -i 's/^#Port 22/Port 2222/' /etc/ssh/sshd_config && systemctl restart sshd
```  
Test new user/port before closing the root session.
2. Install Docker & Compose on droplet
```bash
su - deploy
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
docker --version
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker compose version          # v2.x expected
```
3. Create local project skeleton (Windows)
```powershell
cd C:\Users\nucle\Projects
mkdir n8n-selfhost; cd n8n-selfhost
ni docker-compose.yml, traefik.yml, .env, .dockerignore, README.md, acme.json
```
Set empty `acme.json` to 600 later on the server. Populate `.env` placeholders:  
```
DOMAIN=n8n.chron0.tech
EMAIL=you@example.com
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=<strongPW>
N8N_ENCRYPTION_KEY=<32-char-key>
```
4. Write docker-compose.yml
```yaml
version: '3.9'
services:
  traefik:
    image: traefik:v3.0
    restart: unless-stopped
    command:
      - "--providers.docker=true"
      - "--providers.docker.network=proxy"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--entrypoints.web.http.redirections.entryPoint.to=websecure"
      - "--certificatesresolvers.le.acme.email=${EMAIL}"
      - "--certificatesresolvers.le.acme.storage=/letsencrypt/acme.json"
      - "--certificatesresolvers.le.acme.httpchallenge.entrypoint=web"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - "./acme.json:/letsencrypt/acme.json"
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
    networks:
      - proxy

  n8n:
    image: n8nio/n8n:latest
    restart: unless-stopped
    environment:
      - N8N_HOST=${DOMAIN}
      - WEBHOOK_URL=https://${DOMAIN}/
      - N8N_PROTOCOL=https
      - TZ=UTC
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=${N8N_BASIC_AUTH_USER}
      - N8N_BASIC_AUTH_PASSWORD=${N8N_BASIC_AUTH_PASSWORD}
      - N8N_ENCRYPTION_KEY=${N8N_ENCRYPTION_KEY}
    volumes:
      - n8n_data:/home/node/.n8n
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.n8n.rule=Host(`${DOMAIN}`)"
      - "traefik.http.routers.n8n.entrypoints=websecure"
      - "traefik.http.routers.n8n.tls.certresolver=le"
    networks:
      - proxy

volumes:
  n8n_data:

networks:
  proxy:
    external: true
```
5. Write traefik.yml (optional file-based extras)
If you prefer static-file config instead of CLI flags, mirror the same options in `traefik.yml` and mount it.  
Ensure `acme.json` gets **chmod 600** on the droplet:  
```bash
chmod 600 acme.json
```
6. Configure Cloudflare DNS
Create an **A record**  
```
Name: n8n
IPv4: <droplet-IP>
Proxy: DNS only (grey cloud) until SSL issued
TTL: Auto
```  
Wait a few minutes; verify with  
```
nslookup n8n.chron0.tech
```
7. Transfer project to droplet & prepare network
On Windows PowerShell:  
```powershell
scp -P 2222 -r C:\Users\nucle\Projects\n8n-selfhost deploy@<droplet-IP>:~
```
SSH in:  
```bash
docker network create proxy
cd ~/n8n-selfhost
chmod 600 acme.json
```
8. Deploy stack
```bash
docker compose pull
docker compose up -d
docker compose logs -f traefik
```
Watch for `Server contacted` & `Certificate obtained`.  
9. Verify and finalize
10. Browse to https://n8n.chron0.tech – should display valid Let’s Encrypt certificate.  
11. Complete n8n onboarding, set timezone, create workflows.  
12. Re-enable Cloudflare **orange-cloud** (proxy) if desired; certificate is already in place.  
13. Maintenance & backups
Optional:  
  - Add Watchtower or cron to auto-update images.  
  - Schedule `docker exec n8n n8n export:workflow --all` backups + volume snapshot.  
  - Monitor with UptimeRobot.