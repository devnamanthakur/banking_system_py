# Python Terminal Banking System

A simple, interactive terminal-based banking system written in Python. This project demonstrates basic banking operations such as account creation, deposit, withdrawal, transfer, and balance inquiry, with persistent storage using JSON files.

## Features
- Create new bank accounts
- Deposit and withdraw funds
- Transfer funds between accounts
- Check account balances
- List all accounts
- Data persistence using JSON
- User-friendly terminal interface

## Project Structure
```
banking_system_py/
├── src/
│   ├── main.py                # Entry point for the application
│   ├── bank/
│   │   ├── bank.py            # Bank class: manages accounts and operations
│   │   └── account/
│   │       └── account.py     # Account class: represents a single account
│   └── io/
│       └── io_util.py         # Terminal input/output utilities
├── pyproject.toml             # Project metadata and dependencies
├── README.md                  # Project documentation
└── ...
```

## Requirements
- Python 3.13+

## Setup
1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd banking_system_py
   ```
   
2. **Install dependencies:**
   ```sh
   uv pip install --system --all
   ```

## Usage
Run the application from the `src` directory:
```sh
python src/main.py
```

Follow the on-screen menu to perform banking operations.

## Data Persistence
- Account data is stored in `data/accounts.json` (created automatically).
- All changes (create, deposit, withdraw, transfer) are saved immediately.

## Code Overview
- **src/main.py**: Main menu loop and user interaction.
- **src/bank/bank.py**: `Bank` class for managing accounts and operations.
- **src/bank/account/account.py**: `Account` class for individual account logic.
- **src/io/io_util.py**: Utility functions for input/output and screen management.

## Development
- Linting: `ruff` is included for code quality.
- To add features or fix bugs, edit the relevant files in `src/`.

## License
MIT (add your license here)

---
*This project is for educational/demo purposes. Not for production banking use.*
