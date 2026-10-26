# CLI Expense Tracker

A beginner-friendly command-line expense tracker built with Python. It stores expense records in a local JSON file.

## Features

- Add expenses with amount, category, description, and date
- View saved expenses
- Delete expenses
- View total and average spending
- View today's spending
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
