# SmartGit: A Smart Version Control Tool

SmartGit is a lightweight, Git-inspired version control system written in Rust, enhanced with AI-driven goal management and optional cloud sync via Firebase. Use it just like Git—initialize repositories, stage and commit changes—but also set project goals, auto-commit on inactivity, and generate AI-powered task lists.

---

## Prerequisites

* **Executable:** Download or build the `smartgit` (or `smartgit.exe`) binary and place it in your project folder or add it to your `PATH`.
* **Rust (optional):** Only required if you want to compile from source. Install from [https://rust-lang.org](https://rust-lang.org).
* **Environment Variables (AI & Cloud features):**

  * `FIREBASE_API_KEY` & `FIREBASE_PROJECT_ID` for Firestore sync.
  * `GROQ_API_KEY` (and optionally `GROQ_MODEL`) for AI goal generation.

---

## Quick Start

1. **Place the binary**

   ```bash
   cp smartgit /path/to/your/project/
   cd /path/to/your/project/
   ```

2. **Initialize a repository**

   ```bash
   ./smartgit init
   ```

   Creates a `.smartgit/` folder and `.smartgitignore`.

3. **Stage and commit**

   ```bash
   ./smartgit add src/main.rs
   ./smartgit commit --message "Initial commit"
   ```

4. **View status and history**

   ```bash
   ./smartgit status
   ./smartgit log
   ```

5. **Auto-commit watcher (optional)**

   ```bash
   # Start watching for changes (default 10m timeout)
   ./smartgit watch --on

   # Customize timeout to 5 minutes
   ./smartgit watch --time 5

   # Stop watcher
   ./smartgit watch --off
   ```

6. **Set and track AI project goals**

   ```bash
   ./smartgit goal set "Build a web server in Rust"
   ./smartgit goal tasks     # Generate checkpoint tasks via AI
   ./smartgit progress       # View XP and task status
   ```

7. **Cloud sync with Firebase (optional)**

   ```bash
   # Log in or sign up
   ./smartgit signup --email you@example.com --password secret
   ./smartgit login  --email you@example.com --password secret

   # Sync local commits and goals
   ./smartgit sync

   # Pull updates from cloud
   ./smartgit pull
   ```

---

## Common Commands

| Command                                   | Description                                        |                    |                            |
| ----------------------------------------- | -------------------------------------------------- | ------------------ | -------------------------- |
| `./smartgit init`                         | Initialize a SmartGit repository                   |                    |                            |
| `./smartgit add <file>`                   | Stage a file for commit                            |                    |                            |
| `./smartgit commit --message <msg>`       | Commit staged changes                              |                    |                            |
| `./smartgit status`                       | Show working directory and staging status          |                    |                            |
| `./smartgit log`                          | Show commit history                                |                    |                            |
| `./smartgit diff [--from <i>] [--to <j>]` | Show differences                                   |                    |                            |
| `./smartgit history <file>`               | Show file-specific history                         |                    |                            |
| \`./smartgit watch --on                   | --off                                              | --time <minutes>\` | Manage auto-commit watcher |
| `./smartgit goal set <desc>`              | Set project goal for AI task generation            |                    |                            |
| `./smartgit goal tasks`                   | Generate or list AI-powered checkpoint tasks       |                    |                            |
| `./smartgit goal task set`                | Set or change a specific task by number            |                    |                            |
| `./smartgit goal task prompt`             | Prompt about a specific task with a custom prompt  |                    |                            |
| `./smartgit progress`                     | Display XP and task progress                       |                    |                            |
| `./smartgit signup/login`                 | Create or access your cloud account                |                    |                            |
| `./smartgit sync`                         | Push local state to Firestore                      |                    |                            |
| `./smartgit pull [--project <name>]`      | Fetch cloud state locally                          |                    |                            |
| `./smartgit revert <i>`                   | Create a commit that undoes commit `i`             |                    |                            |
| `./smartgit reset <i>`                    | Hard-reset to commit `i`, discarding later commits |                    |                            |
| `./smartgit export [--output <path>]`     | Bundle repository into a ZIP archive               |                    |                            |

---

## Building from Source (Optional)

```bash
git clone https://github.com/LucasFranco12/SmartGit-main.git
cd SmartGit-main
cargo build --release
# Binary at target/release/smartgit (.exe on Windows)
```

---

**Happy versioning!** 🚀
