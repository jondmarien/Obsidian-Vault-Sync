# Automated Removal of Dummy Deployment Commits from Main Branch (GPT-4.1/AI Instructions)

_These instructions are written for use by an AI terminal/code agent (such as GPT-4.1) to programmatically remove all "chore: dummy commit to trigger deployment" commits from the `main` branch while preserving the rest of the history and commit messages._

---

## Safety Precautions

- **Always create a backup branch before history rewriting!**
- Notify collaborators: force-pushes rewrite history and break existing clones.
- Complete/merge in-flight PRs or coordinate rebase after rewrite.
- Ensure working directory is clean, or stash any local changes.

---

## Step-by-Step AI Scripted Workflow

### 1. Create a Safety Backup

```powershell
git checkout main
git checkout -b main-backup
```

### 2. Identify the Start Point for Rebase

Find the SHA of the commit just before the **first** dummy commit (AI: substitute the result as needed):

```powershell
$firstDummy = git log --reverse --grep="chore: dummy commit to trigger deployment" --format="%H" | Select-Object -First 1
$parentSHA = git rev-parse "$firstDummy^"
echo "Parent SHA: $parentSHA"
```

### 3. Start the Interactive Rebase

```powershell
git checkout main
git rebase -i $parentSHA
```
(The editor will open. Close it immediately; you’ll automate editing the todo file next.)

### 4. Scripted Modification of the Rebase Todo File

Automate converting all dummy commits from `pick` to `drop`:

```powershell
(Get-Content .git\rebase-merge\git-rebase-todo) -replace '^pick (\w+) chore: dummy commit to trigger deployment$', 'drop $1 chore: dummy commit to trigger deployment' | Set-Content .git\rebase-merge\git-rebase-todo
```

🛈 You can run similar scripts again if there are a large number of duplicate lines.

### 5. Complete the Rebase

```powershell
git rebase --continue
```
Repeat `git rebase --continue` until finished. If there are conflicts, resolve them and run the command again.

### 6. Verification

- Ensure the dummy commits are gone:

    ```powershell
    git log --grep="chore: dummy commit to trigger deployment" --oneline
    ```

- Check that all "real" commits/messages remain correct.

---

## 7. Force Push to Remote

```powershell
git push --force-with-lease origin main
```

---

## 8. Post-Cleanup Steps

- Instruct all collaborators to rebase or reclone their branches.
- Monitor build pipelines and deployment integrations (Vercel, CI/CD).
- Keep your backup branch until all issues are resolved.

---

## Troubleshooting

- **Abort a broken rebase:**
  ```powershell
  git rebase --abort
  ```

- **Restore from your backup:**
  ```powershell
  git checkout main-backup
  git checkout main
  git reset --hard main-backup
  git push --force-with-lease origin main
  ```

---

## Notes for Future AI Agents

- This workflow is proven for hundreds of nearly-identical commits.
- For more advanced filtering or mass history tasks, consider `git filter-repo` instead.
- Always work with copies and ensure communication with the team.

