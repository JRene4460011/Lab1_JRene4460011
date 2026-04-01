## Project Overview

This project is made of two scripts working together to evaluate student grades stored in a CSV file and manage archival of processed grade records.

- **`grade-evaluator.py`** – A Python terminal-based program that reads CSV files like `grades.csv`, validates the data, calculates the final grade and GPA, determines pass/fail status, and identifies assignments that are eligible for resubmission.
- **`organizer.sh`** – A Bash shell script that archives the current `grades.csv` by adding a generated timestamp on the file name, creates an empty CSV, and logs the operation.

---

## File Structure

```
Lab1_JRene4460011/
├── grade-evaluator.py   # Python grade evaluation script
├── grades.csv           # Input CSV with assignment records
├── organizer.sh         # Bash archival/logging script
└── README.md            # This file
```

When one runs `organizer.sh`, the following are created:

```
├── archive/
│   └── grades_YYYY-MM-DD_HH-MM-SS.csv   # Timestamped backup
└── organizer.log                          # Archival log
```

---

## grades.csv Format

The CSV file contain the following columns:

| Column | Description |
|---|---|
| `assignment` | Name of the assignment |
| `group` | Category: `Formative` or `Summative` |
| `score` | Percentage score (0–100) |
| `weight` | Weight of the assignment (must total 100%) |

**Weight constraints:**
- Total weight across all assignments = **100%**
- Formative assignments = **60%**
- Summative assignments = **40%**

---

## How to Run

### Grade Evaluator (Python)

```bash
python grade-evaluator.py
```

When prompted, enter the CSV filename (e.g., `grades.csv`). The program will:

1. **Validate scores** – ensures all scores are between 0 and 100.
2. **Validate weights** – enforces the 60/40 Formative/Summative split totalling 100%.
3. **Calculate Final Grade & GPA** – weighted average mapped to a 5.0 GPA scale.
4. **Determine Pass/Fail** – requires ≥ 50% in **both** Formative and Summative groups.
5. **Identify resubmission candidates** – failed Formative assignments (< 50%) with the highest weight are flagged for resubmission.

### File Organizer (Bash)

```bash
bash organizer.sh
```

This script will:

1. Create an `archive/` directory (if it doesn't exist).
2. Move `grades.csv` into `archive/` with a timestamp (e.g., `grades_2026-04-01_14-30-00.csv`).
3. Create a new empty `grades.csv` in the working directory.
4. Append the archival record to `organizer.log`.

---

## Error Handling

| Scenario | Behaviour |
|---|---|
| `grades.csv` missing | Python: prints error, exits. Shell: prints "File does not exist." |
| `grades.csv` empty | Python: detects no records, prints error, exits. |
| Score out of 0–100 range | Python: prints which assignment is invalid, exits. |
| Weights don't total 100% | Python: prints the incorrect total, exits. |
| Formative weight ≠ 60% | Python: prints the incorrect weight, exits. |
| Summative weight ≠ 40% | Python: prints the incorrect weight, exits. |
| `mv` or `touch` fails in shell | Shell: prints failure message, skips dependent steps. |

---

## Example Output

```
Enter the name of the CSV file to process (e.g., grades.csv): grades.csv

--- Processing Grades ---

Score for 'Quiz' is valid: 85.0%
Score for 'Group Exercise' is valid: 40.0%
Score for 'Functions and Debugging Lab' is valid: 45.0%
Score for 'Midterm Project - Simple Calculator' is valid: 70.0%
Score for 'Final Project - Text-Based Game' is valid: 60.0%

Validating assignment weights......

Total assignments weight is valid: 100.0%
Total Summative weights is valid: 40.0%
Total Formative weights is valid: 60.0%

The Final Grade is 60.00%
The GPA is 3.00

Status: PASSED

The assignment 'Group Exercise' has the highest weight (20.0%) among the failed formative assignments and is eligible for resubmission.
The assignment 'Functions and Debugging Lab' has the highest weight (20.0%) among the failed formative assignments and is eligible for resubmission.

--------- Final Decision ---------
Overall Status: PASSED

Eligible assignment(s) for resubmission:
- Group Exercise (Score: 40.0%, Weight: 20.0%)
- Functions and Debugging Lab (Score: 45.0%, Weight: 20.0%)
```

---

## Requirements

- **Python 3.6+** (uses f-strings)
- **Bash** (for `organizer.sh`)