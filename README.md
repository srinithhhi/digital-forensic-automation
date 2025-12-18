# Digital Forensics Automation (DFA)

A beginner-friendly **Digital Forensics Automation tool** that automates forensic investigations using **Sleuth Kit** and **Bulk Extractor**. This project demonstrates how to extract filesystem information, parse artifacts, and generate structured reports automatically.

## Features

- Run `fls` on disk images to list files and directories
- Parse filesystem output to generate JSON summaries
- Extract artifacts (emails, URLs, paths) using Bulk Extractor
- Generate professional HTML reports combining all summaries
- Fully automated workflow for repeatable investigations

## Tools & Technologies

- Python 3 (virtual environment recommended)
- Sleuth Kit (`fls`)
- Bulk Extractor
- Jinja2 (HTML report generation)
- ReportLab (optional for PDF reports)

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd digital-forensics-automation
```

2. Create virtual environment and activate:

```bash
python3 -m venv dfa
source dfa/bin/activate
```

3. Install required Python packages:

```bash
pip install -r requirements.txt
```

4. Ensure Sleuth Kit and Bulk Extractor are installed on your system.

## Project Structure

```
digital-forensics-automation/
├── scripts/                   # Python automation scripts
├── templates/                 # HTML report templates
├── outputs/                   # Auto-generated outputs (ignored in Git)
├── evidence/                  # Disk images (ignored in Git)
├── dfa/                       # Virtual environment (ignored in Git)
├── requirements.txt
└── README.md
```

## Usage

1. Add your disk image in `evidence/disk.dd`.
2. Run file system analysis:

```bash
python scripts/run_fls.py
python scripts/filesystem_summary.py
```

3. Run Bulk Extractor:

```bash
bulk_extractor -o outputs/bulk_extractor evidence/disk.dd
python scripts/bulk_extractor_summary.py
```

4. Generate the final HTML report:

```bash
python scripts/generate_report.py
```

5. Open the report:

```
reports/forensic_report.html
```

## Notes

- Ensure the virtual environment is activated before running scripts.
- `outputs/`, `reports/`, `dfa/`, and `evidence/` are ignored in Git (`.gitignore`).

## Future Enhancements

- Automatic end-to-end workflow with a single script
- PDF report generation
- Timeline creation from filesystem artifacts
- Support for multiple disk images and bulk processing

## Author

**Srinithi** – Engineering Student | Cybersecurity Enthusiast | Open Source
