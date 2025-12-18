from pathlib import Path
import json
from jinja2 import Environment, FileSystemLoader

# 1️⃣ Paths
fs_summary_path = Path("outputs/filesystem/summary.json")
be_summary_path = Path("outputs/bulk_extractor/summary.json")
template_dir = Path("templates")
report_output = Path("reports/forensic_report.html")

# Ensure reports folder exists
report_output.parent.mkdir(parents=True, exist_ok=True)

# 2️⃣ Load summaries
with fs_summary_path.open() as f:
    fs_summary = json.load(f)

with be_summary_path.open() as f:
    be_summary = json.load(f)

# 3️⃣ Setup Jinja2 environment
env = Environment(loader=FileSystemLoader(str(template_dir)))
template = env.get_template("report_template.html")

# 4️⃣ Render template with data
rendered_report = template.render(fs=fs_summary, be=be_summary)

# 5️⃣ Save report
report_output.write_text(rendered_report)
print(f"[✓] Report generated at {report_output}")
