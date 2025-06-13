# Contributing to Python Terminal Banking System

Thank you for your interest in contributing! This guide will help you get started and ensure a smooth contribution process.

## Project Structure
```
banking_system_py/
├── src/
│   ├── main.py                # Entry point for the application
│   ├── bank/
│   │   ├── bank.py            # Bank class: manages accounts and operations
│   │   └── account/
│   │       └── account.py     # Account class: represents a single account
│   │
│   └── io/
│       └── io_util.py         # Terminal input/output utilities
├── pyproject.toml             # Project metadata and dependencies
├── Makefile                   # Helper commands for development
├── README.md                  # Project documentation
└── ...
```

## Setup Instructions

This project uses [uv](https://github.com/astral-sh/uv) for dependency management and running commands. Please ensure you have `uv` installed:

```sh
brew install uv 
```

### Install Dependencies and running project

Uv handles installing dependencies and running the file so just run the run command as below
```sh
uv run -m src.main
```

> Note: `-m` cause `src` is also a module/package due to `__init__.py` file so here `-m` means run inside the module `src`

OR you can use make file which runs the exact same command
```
make run
```

### 2. Using the Makefile
The `Makefile` provides helpful shortcuts:
- `make run` or `make`    — Run the banking system application
- `make format` — Format code using ruff
- `make help`   — Show available commands

### 3. Running the Application
```sh
make run
```

### 4. Formatting Code
```sh
make format
```

## Contribution Process
1. **Check Open Issues:**
   - Browse the [issues](../../issues) and look for ones labeled `good first issue` or any that interest you.
   - If you want to work on an issue, comment on it and wait for a maintainer to assign it to you before starting work.

2. **Discuss Before You Code:**
   - If you have questions or want to propose a new feature, open an issue or start a discussion first.

3. **Branching & Pull Requests:**
   - Create a new branch from `main` for your fix or feature.
   - Make your changes, ensuring you:
     - Add clear and descriptive comments to your code.
     - Test your changes thoroughly.
   - Run `make format` to ensure code style consistency.
   - Open a Pull Request (PR) to the `main` branch.
   - In your PR description, mention the issue it closes/fixes (if applicable) and describe your changes.

4. **Code Review:**
   - Be responsive to feedback from maintainers.
   - Update your PR as needed until it is approved and merged.

## Best Practices
- **Comment your code:** Add meaningful comments and docstrings to help maintainers and future contributors understand your logic.
- **Test thoroughly:** Only submit PRs after verifying your changes work as expected.
- **Keep commits focused:** Each commit should address a single purpose or fix.
- **Be respectful:** Communicate clearly and respectfully with other contributors and maintainers.

## Getting Help
If you have any questions, open an issue or reach out to the maintainers.

Happy contributing! 