# Reflection: GitHub Project with an Intentional Merge Conflict

The Student Grade Calculator was managed using Git and GitHub to demonstrate repository initialization, staging, commits, remote configuration, pushing, pulling, branching, merging and conflict resolution.

The conflict was intentionally created by making two independent branches from the same `main` commit. The `feature-ui` branch changed the project-status line in `README.md` to describe an interactive menu. The `feature-report` branch changed that exact original line to describe a class-wise report. Since both branches modified the same line differently, Git could not automatically decide which version should be retained when the second branch was merged after the first.

I first merged `feature-ui` into `main`. That merge completed successfully. I then attempted to merge `feature-report`. Git identified a content conflict in `README.md` and marked the file as unmerged. I used `git status` to identify the conflicted file and `git diff` to inspect the competing changes. I manually edited the file, removed the conflict markers, and retained a combined project-status statement that represented both contributions. I staged the corrected file with `git add`, committed the resolution, and pushed the updated `main` branch to GitHub.

This exercise showed that Git tracks changes across branches but cannot always infer the intended meaning when concurrent edits overlap. A merge conflict is not data loss by itself; it is a request for the developer to make an explicit decision. I learned to inspect repository status before acting, review diffs rather than blindly accepting one side, stage only the resolved files, and verify the final history. The graph view of the commit history also helped me understand how branches diverge and later become integrated.

The exercise reinforced the value of small commits, clear commit messages, frequent synchronization with the remote repository, and communication when multiple contributors work on shared files. In a team project, conflicts can be reduced by coordinating ownership of files, keeping changes focused and merging regularly. When a conflict does occur, it should be resolved deliberately and verified before the result is pushed.

**Evidence note:** Update this reflection after completing the actual commands. Mention any differences you encountered, and attach your own screenshots. Do not claim a command succeeded unless you observed it succeed.
