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
