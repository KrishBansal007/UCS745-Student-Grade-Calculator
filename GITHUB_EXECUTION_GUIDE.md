# Q1 – GitHub project execution guide

## 0. Prerequisites
Install Git and Python 3. Create a NEW empty GitHub repository named `UCS745-Student-Grade-Calculator`. Do not initialize it with a README, license or .gitignore because the local project already contains these files. Copy the repository HTTPS URL.

## 1. Open terminal in the project folder
```bash
cd path/to/UCS745_Cloud_DevOps_Assignment/Q1_Student_Grade_Calculator
git --version
python3 --version
```
On Windows PowerShell, use `py --version` and run the program with `py grade_calculator.py` if `python3` is not recognized.

## 2. Initialize, commit, connect and push
Replace the URL with the HTTPS URL of your own empty GitHub repository.
```bash
git init -b main
git status
git add .
git status
git commit -m "Initial commit: student grade calculator"
git remote add origin https://github.com/YOUR-USERNAME/UCS745-Student-Grade-Calculator.git
git remote -v
git push -u origin main
git pull origin main
```
If your Git version does not support `git init -b main`, run `git init` followed by `git branch -M main`. If GitHub authentication is requested, authenticate using the browser/Git Credential Manager or an approved personal access token; never put a token in the remote URL or screenshots.

## 3. Create first branch (feature-ui)
```bash
git switch -c feature-ui
```
Open `README.md` and change only this exact line:
`Project Status: Basic grade calculator.`
to:
`Project Status: Grade calculator with an interactive menu.`
Save, then:
```bash
git diff
git add README.md
git commit -m "Update project status for interactive menu"
git push -u origin feature-ui
```

## 4. Create second branch from main (feature-report)
```bash
git switch main
git switch -c feature-report
```
Open `README.md` and change the SAME original line:
`Project Status: Basic grade calculator.`
to:
`Project Status: Grade calculator with a class-wise report.`
Save, then:
```bash
git diff
git add README.md
git commit -m "Update project status for class-wise report"
git push -u origin feature-report
```
Both branches changed the same line differently. This is the deliberate cause of the conflict.

## 5. Merge first branch into main
```bash
git switch main
git pull origin main
git merge feature-ui
git status
git push origin main
```
The first merge should succeed because main has not yet incorporated the competing edit.

## 6. Attempt second merge and capture the conflict
```bash
git merge feature-report
```
Git should report a content conflict in `README.md`. Now run:
```bash
git status
git diff
```
Capture a screenshot showing the conflict markers in README.md and the `git status` output. The file will contain markers similar to:
```text
<<<<<<< HEAD
Project Status: Grade calculator with an interactive menu.
=======
Project Status: Grade calculator with a class-wise report.
>>>>>>> feature-report
```
The exact branch labels/commit text may vary.

## 7. Resolve manually
Edit `README.md`, remove all conflict markers, and keep a combined final line:
`Project Status: Grade calculator with an interactive menu and a class-wise report.`
Save the file. Then:
```bash
git diff
git status
git add README.md
git status
git commit -m "Resolve README merge conflict"
git push origin main
```
Capture a screenshot after resolution showing the clean `git status` and successful resolution commit. `git status` should say the working tree is clean after the commit.

## 8. Verify final result
```bash
git log --oneline --graph --decorate --all
git branch -a
git remote -v
git show HEAD:README.md
python3 grade_calculator.py
```
Run the sample input `Krish` and `85 90 78`. Expected average is `84.33`, grade `B`.

## 9. Screenshot list for report
- GitHub repository page showing repository name and files.
- Initial `git init`, initial commit and remote/push evidence.
- Both feature branches and their commits.
- `git merge feature-ui` success.
- `git merge feature-report` conflict plus `git status`/`git diff`.
- README conflict markers before editing.
- Final resolved README and successful resolution commit.
- Final `git log --graph` and clean `git status`.
- Program execution with sample input/output.

## 10. Common issues
- `Author identity unknown`: run `git config --global user.name "Your Name"` and `git config --global user.email "your_verified_github_email@example.com"`, then retry the commit.
- `remote origin already exists`: inspect `git remote -v`; use `git remote set-url origin YOUR_REPOSITORY_URL` rather than adding a second origin.
- Push rejected because GitHub repo is not empty: preferably create a genuinely empty repo. If it is already initialized, stop and reconcile histories rather than force-pushing.
- `git merge` says already up to date: check you created `feature-report` from `main` before merging `feature-ui`, and that the branches changed the same original README line differently.
- Conflict did not occur: run `git status` and inspect the branch history. Do not fabricate a conflict screenshot; correct the branch sequence and repeat from a clean starting state.
- If a merge is in a bad state before resolution, `git merge --abort` returns to the pre-merge state. Do not use it after you have completed and committed the resolution.
