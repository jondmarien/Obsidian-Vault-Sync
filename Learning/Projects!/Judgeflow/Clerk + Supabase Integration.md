
##  Project Analysis (Recap)

- **Frontend:** React (Vite), no current auth logic.
- **Backend:** Rust, currently uses Supabase service key for backend operations.
- **Goal:** Use Clerk for authentication, integrate with Supabase for secure, user-aware data access.

---

## 2. Clerk + Supabase Integration Plan (with Latest Docs)

### Step 1: Set Up Clerk in the Frontend
- **Install Clerk:**  
	- `npm install @clerk/clerk-react`
- **Initialize ClerkProvider:**  
	- Wrap your app in`<ClerkProvider publishableKey={process.env.CLERK_PUBLISHABLE_KEY}>` in `main.js`
- **Add Auth UI:**  
    Use Clerk components `SignIn`, `SignUp`, `UserButton` in your React pages.
- **Protect Routes:**  
    Use Clerk hooks `useUser`, `SignedIn`, `SignedOut` to guard routes/components.

### Step 2: Configure Clerk to Issue JWTs
- **Enable JWT Templates:**  
    In the Clerk dashboard, create a JWT template.
    - Include the user’s external ID as a claim:
        `{ "userId": "{{user.external_id || user.id}}" }`
    - Add custom claims if you need group/role-based access:
        `{ "groups": ["org:admin", "org:member"] }`
- **Frontend: Get JWT for API Requests:**  
    Use Clerk’s session API to get the JWT:
    `const token = await clerk.session.getToken({ template: 'YOUR_TEMPLATE' });`
    Attach this token as a Bearer token in requests to your backend.

### Step 3: Backend — Verify Clerk JWT
- **Fetch Clerk’s JWKS:**  
    Your backend must verify JWTs using Clerk’s public keys (JWKS endpoint).
- **Rust JWT Verification:**
    - Use a crate like `jsonwebtoken`
         to verify the token’s signature and claims.
    - Validate standard claims (`exp`, `nbf`) and custom claims (e.g., `userId`)
    - Optionally, check the `azp` (Authorized Party) claim for allowed origins.
- **Example (from Clerk docs, TypeScript, adapt to Rust):**
    - Retrieve token from `Authorization`header.
    - Verify with Clerk’s public key.
    - Check claims and expiration.

### Step 4: Backend — Connect to Supabase
- **Option 1: Backend as Proxy (Recommended for Rust):**
    - Backend receives requests with Clerk JWT.
    - After verifying, use Supabase service key for privileged actions, but enforce access control based on the verified Clerk user ID.
    - (Optional) Map Clerk user ID to Supabase user or roles for RLS.
- **Option 2: Direct Supabase Access from Frontend (Advanced):**
    - Configure Supabase to trust Clerk JWTs for Row Level Security (RLS).
    - Supabase policies use the Clerk user ID claim for access control.
    - This requires setting up Supabase JWT secrets and policies accordingly.

### Step 5: (Optional) Supabase RLS with Clerk JWT
- **Supabase JWT Secret:**  
    If using direct access, set up Supabase to accept Clerk JWTs by configuring the JWT secret or JWKS URL in Supabase settings.
- **RLS Policies:**  
    Write policies that use the `userId` claim from Clerk JWT for row-level access.

---

## 3. Key Implementation Notes
- **Frontend:**
    - Always retrieve and attach the latest Clerk JWT to API requests.
    - Use Clerk hooks for session state.
- **Backend:**
    - Fetch and cache Clerk JWKS for JWT verification.
    - Use a robust JWT validation library.
    - Enforce all sensitive logic on the backend, using the verified user identity.
- **Supabase:**
    - If using RLS, ensure policies reference the correct claim (e.g., `userId`)
    - If not using RLS, restrict all access through backend logic.

---

## 4. References (from Docs)
- Clerk JWT verification:
    - [Manual JWT Verification Example](https://github.com/clerk/clerk-docs/blob/main/docs/backend-requests/manual-jwt.mdx)
- Clerk React integration:
    - [ClerkProvider Example](https://github.com/clerk/javascript/blob/main/packages/expo/CHANGELOG.md)
- Supabase JWT/RLS:
    - [Custom JWT Claims in Supabase](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/auth/third-party/auth0.mdx)
    - [Supabase RLS Policies](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/auth/auth-hooks/custom-access-token-hook.mdx)

---

## 5. Review Points
- Do you want your frontend to access Supabase directly (with RLS), or should all DB access go through your backend?
- Should user roles/groups be encoded in Clerk JWTs for use in Supabase policies?
- Is your backend ready to fetch and cache JWKS for JWT verification?

---

