
# CLI Expense Tracker

A beginner-friendly command-line expense tracker built with Python. It stores expense records in a local JSON file.

## Features

- Add expenses with amount, category, description, and date

<img width="453" height="512" alt="Screenshot 2026-10-26 154726" src="https://github.com/user-attachments/assets/1d3aaad2-acd8-4ae0-aed5-16f8c8d57c5f" />

- View saved expenses

<img width="1396" height="368" alt="Screenshot 2026-10-26 154958" src="https://github.com/user-attachments/assets/4479263c-96cf-4860-b125-cde4e801d2dc" />

- Delete expenses
- View total and average spending
- View today's spending

<img width="562" height="702" alt="Screenshot 2026-10-26 154835" src="https://github.com/user-attachments/assets/be203600-4c22-47d6-a9d7-53d6bc12a06e" />

- View category-wise expense statistics
- Store expense data locally using JSON

## Tech Stack

- Python
- JSON
- `datetime` module

## Getting Started

### Prerequisites
- Python 3 installed

### Run the application

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

## Data Storage

The application uses a local `expenses.json` file for persistence. The file is generated or updated when expenses are saved.

## Current Status

Early version — improvements to input validation, date handling, and summary calculations are in progress.

## What I Learned

- Working with loops and conditionals
- Reading and writing JSON files
- Handling user input and exceptions
- Calculating expense statistics
- Building an interactive CLI application

## Planned Improvements

- Improve error handling and input validation
- Support custom categories in summary statistics
- Add monthly and weekly summaries
- Add automated tests
