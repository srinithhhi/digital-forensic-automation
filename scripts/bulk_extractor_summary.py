from pathlib import Path
import json

# 1️⃣ Paths
be_output_dir = Path("outputs/bulk_extractor")
summary_path = Path("outputs/bulk_extractor/summary.json")

# 2️⃣ Initialize summary dictionary
summary = {}

# 3️⃣ Loop through all .txt files in Bulk Extractor output
for artifact_file in be_output_dir.glob("*.txt"):
    artifact_name = artifact_file.stem  # e.g., email, url, path
    with artifact_file.open("r", errors="ignore") as f:
        # Count non-empty lines
        lines = [line.strip() for line in f if line.strip()]
        summary[artifact_name] = len(lines)

# 4️⃣ Print summary to console
print("Bulk Extractor Summary")
print("---------------------")
for k, v in summary.items():
    print(f"{k}: {v}")

# 5️⃣ Save summary as JSON
summary_path.parent.mkdir(parents=True, exist_ok=True)
with summary_path.open("w") as f:
    json.dump(summary, f, indent=4)

print(f"[✓] Bulk Extractor summary saved to {summary_path}")
