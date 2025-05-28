# Implementing a Detailed Backup & Restoration Plan for a Web Application

## Assumptions
- **Web Server:** Apache
- **Database:** MySQL
- **Programming Language:** Python (using Django Framework)
- **Linux Distribution:** Ubuntu Server 20.04 LTS

------------
## Backup Software Utilities
1. **`rsync:`** Primary Tool for system backups, including code, configuration, and static assets
- If not installed by default, can be installed with: `sudo apt-get install rsync`
2. **`mysqldump:`** Dedicated tool to create consistent, portable backups of the MySQL database
	- Part of the MySQL server package, can be installed with: `sudo apt-get install mysql-client`
3. **`tar:`** Bundles together the individual backups into a single, optionally compressed backup file for easier management and off-site storage 
	- Pre-installed on most if not all Linux systems
4. **`cron:`** Automates the backup process based on your defined backup schedule
	- Pre-installed on most if not all Linux systems

**Example Usage**
Let's show what a sample `cron` job would look like for a daily differential backup:

1. **Create a backup script:** Make a file named `backup.sh` with the `rsync`, `mysqldump`, and `tar` commands.
2. **Make it executable:** `chmod +x backup.sh`
3. **Edit crontab:** `crontab -e`
4. **Add the schedule. Example for daily at 11 PM:**
	```
    0 23 * * * /path/to/backup.sh 
    ```

-------

## Backup Procedure #backup_procedure
1. Application Code & Configurations (Using `rsync` gives us flexibility and efficiency):
```bash
rsync -avz /var/www/html/mywebapp /backup/code_backup 
rsync -avz /etc/apache2 /backup/config_backup
```
- `-a`: archive mode; Preserves file permissions, ownerships, and timestamps.
- `-v`: verbose; Provides output for progress monitoring.
- `-z`: compression; Compresses data during transfer, especially useful for large files and when sending backups over networks


**Important:**
- Consider excluding temporary directories since they can change frequently and increase backup size without real value
  
---------------------------

2. Database Backup (`mysqldump` provides options for a tailored database export):
```bash
mysqldump -u [username] -p [database_name] > /backup/database_backup.sql
```
- `-u [username]`: Specifies the user's database with appropriate permissions
- `-p`: Prompts the user's password for security
- `[database_name]`: The name of the database you want to backup

**Important:**
- If your database is very large, consider adding the `--quick` option to `mysqldump` for potentially faster backups
  
---------------------

3. Compression and Archiving (Using `tar` bundles the backup pieces for convenience):
```bash
tar -czvf /backup/full_backup_$(date +%Y-%m-%d).tar.gz /backup/code_backup
/backup/config_backup /backup/database_backup.sql
```
- `-c`: create; Creates a new archive.
- `-z`: `gzip` compression; Compresses the archive to save space.
- `-v`: verbose; Shows progress of compression.
- `-f`: filename; Specifies the name of the output archive file. The specifier `$(date +%Y-%m-%d)` dynamically adds the current date to easily identify backup timestamps.

**Important:**
- Ensure you have sufficient storage space for your compressed backups.
- Decide on a specific compression method based on the desired speed vs compression ratio (`gzip` vs. `bzip2`).

-------

4. Off-site Backup (Optional, but **highly** recommended; `rclone` offers versatility for various cloud providers):
	- First, employ a cloud storage provider like AWS S3 or Google Cloud Storage
	- Then, utilize a tool like `rclone` to sync backup files to cloud storage:
```bash
rclone sync /backup/ aws-s3:my-backup-bucket  

```
- `rclone` needs configuration with credentials and details for your chosen cloud storage system
- The above command synchronizes changes, sending only new or modified files to the cloud

**Important:**
- Off-site backups are crucial protection against disasters that could affect your primary server location 

-------

## Example Full Backup Script
```bash
#!/bin/bash

# Backup directories
CODE_BACKUP_DIR="/backup/code_backup"
CONFIG_BACKUP_DIR="/backup/config_backup"
DATABASE_BACKUP_FILE="/backup/database_backup.sql"
FULL_BACKUP_DIR="/backup"

# Backup application code and configurations
rsync -avz /var/www/html/mywebapp $CODE_BACKUP_DIR
rsync -avz /etc/apache2 $CONFIG_BACKUP_DIR

# Backup database
mysqldump -u [username] -p [database_name] > $DATABASE_BACKUP_FILE

# Create compressed archive
tar -czvf $FULL_BACKUP_DIR/full_backup_$(date +%Y-%m-%d).tar.gz $CODE_BACKUP_DIR $CONFIG_BACKUP_DIR $DATABASE_BACKUP_FILE

# Optional: Sync to cloud storage
rclone sync $FULL_BACKUP_DIR aws-s3:my-backup-bucket

```

**CRON**
====
```bash
crontab -e
```
- Open your user's crontab file for editing
```bash
0 1 * * * /path/to/backup.sh
```
- `0`: Minute (0)
- `1`: Hour (1 AM)
- `*`: Every day of the month
- `*`: Every month
- `*`: Every day of the week
- `/path/to/backup.sh`: The full path to the backup script

Other Possible Variations:
- **Weekly at Midnight Sunday:**
```bash
0 0 * * 0 /path/to/backup.sh 
```
- **Twice a Day (Noon and Midnight):**
```bash
0 0,12 * * * /path/to/backup.sh 
```
- **First day of Every Month at 3 AM:** ```
```bash
0 3 1 * * /path/to/backup.sh
```

------------

## Restoration Procedure
0. Pre-Restoration Checks: 
   - Verify your backup's integrity before attempting a restoration
   - Ensure you have sufficient disk space for restoring the backup
   - Order of restoration might matter. For example, if the code expects the database to be running during setup, then restore the database before the code assets.
   - Possible slight environment changes (i.e., the database connection details if the server's IP address has changed)
1. Install Bash Dependencies: Start with a fresh install of the base OS. After, we need the core components to run the application
```bash
sudo apt-get update
sudo apt-get install apache2 mysql-server python3-django # And other core dependencies
```
- `apache2`: Your web server software.
- `mysql-server`: Database server to run MySQL.
- `python3-django`: The core Python framework and any other dependencies required by the web application.

**Important:**
- Ensure you are keeping compatibility between versions. (installing the same versions as the ones you uninstalled)
- Consider having a dedicated requirements.txt for Python-based apps that will ease the installation.

----

2. Restore Application Code & Configurations: `rsync` efficiently brings back code and configs from backup
```bash
rsync -avz /backup/code_backup /var/www/html/mywebapp
rsync -avz /backup/config_backup /etc/apache2 
```
- `-a`: archive mode; Preserves file permissions, ownerships, and timestamps.
- `-v`: verbose; Provides output for progress monitoring.
- `-z`: compression; Compresses data during transfer, especially useful for large files and when sending backups over networks
- Same flags as in #backup_procedure part 1.

**Important:**
- If major changes were made to the server environment, like directory paths changing, adjust your restoration `rsync` commands accordingly.
  
------

3. Restore Databases: Reimport the database dump created by `mysqldump`
```bash
mysql -u [username] -p [database_name] < /backup/database_backup.sql
```
- `-u [username] -p`: Provide the credentials (user and password) to create and modify the database.
- `[database_name]`: If the database doesn't exist, it will be created. Be careful if the database name pre-exists to avoid overwriting existing data.

**Important:**
- Consider using the `--one-transaction` option with `mysqldump` when backing up your database if your database engine supports it. This helps maintain data consistency during restoration.
  
----

4. Apply Permissions and Restart Services: Ensures the web application can be access and modified by your web server
```bash
sudo chown -R www-data:www-data /var/www/html/mywebapp # Adjust ownership
sudo systemctl restart apache2 
sudo systemctl restart mysql
```
- `chown -R www-data:www-data /var/www/html/mywebapp`: Sets the ownership of the web application directory to the user and group that your web server runs as (which is often 'www-data').
- `systemctl restart apache2`: Restarts the Apache service to apply configuration settings.
- `systemctl restart mysql`: Restarts the MySQL service to ensure the database is accessible.
  
----

## Backup Schedule
- **Daily Differential Backups**:
	-  Backing up changes since the last full backup. This keeps smaller backup files.
- **Weekly Full Backups**:
	- Creates a complete, independent backup.
- **Monthly Off-site Backups:**
	- Sends a full backup to cloud storage for disaster recovery.
## Backup Retention
- Keep the latest **7 daily backups**
- Keep the latest **4 weekly backups**
- Keep the latest **6 monthly backups**

----
## Testing Plan
1. **Frequency**: Quarterly or after any major code/infrastructure changes.
2. **Test Environment**: Set up a separate staging server that mirrors the production environment.
3. **Procedure**:
	- Perform a simulated full restoration using backups on the staging server.
	- Verify the application runs properly, including the database data.
	- Use a checklist to track all restoration procedure for any deviations or needed updates.