# Lab 1 – Grade Evaluator & File Organizer

## Overview

This project contains two scripts:

- **`grade-evaluator.py`** – Reads a CSV of student assignments, validates the data, calculates the final grade and GPA, determines pass/fail status, and lists assignments eligible for resubmission.
- **`organizer.sh`** – Archives the CSV file with a timestamp, creates a fresh empty CSV, and logs the operation.

## Requirements

- Python 3.6+
- Bash

## CSV Format

The input file must be a CSV with the following columns:

| Column | Description |
|--------|-------------|
| `assignment` | Name of the assignment |
| `score` | Grade received (0–100) |
| `weight` | Weight of the assignment (%) |
| `group` | Either `Formative` or `Summative` |

Weights must total **100%**, split exactly **60% Formative / 40% Summative**.

## How to Run

### Grade Evaluator (Python)

```bash
python grade-evaluator.py
```

When prompted, enter the name of the CSV file (e.g., `grades.csv`). The program will:

1. Validate that scores are between 0–100 and weights total 100%.
2. Enforce the 60/40 Formative/Summative weight split.
3. Calculate the final grade and GPA (out of 5.0).
4. Determine pass/fail — requires **≥ 50%** in **both** Formative and Summative groups.
5. List any Formative assignments below 50% that are eligible for resubmission.

### File Organizer (Shell)

```bash
bash organizer.sh
```

The script will:

1. Create an `archive/` directory (if it doesn't exist).
2. Move `grades.csv` into `archive/` with a timestamp (e.g., `grades_2026-04-01_14-30-00.csv`).
3. Create a fresh empty `grades.csv`.
4. Log the operation to `organizer.log`.

## Error Handling

- **Missing file** – Both scripts check if the file exists before proceeding.
- **Empty CSV** – The Python script detects an empty file and exits with a clear message.
- **Invalid scores/weights** – The Python script validates all values and reports errors before calculating.