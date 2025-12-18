from pathlib import Path
import json

# 1️⃣ Define paths
file_listing_path = Path("outputs/filesystem/file_listing.txt")
summary_path = Path("outputs/filesystem/summary.json")

# 2️⃣ Initialize counters
total_entries = 0
deleted_entries = 0
directories = 0

# 3️⃣ Read file listing line by line
with file_listing_path.open("r", errors="ignore") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        total_entries += 1
        if "*" in line:
            deleted_entries += 1
        if line.startswith("d/") or line.startswith("r/r") and ":" in line:
            directories += 1

# 4️⃣ Print summary to console
print("Filesystem Summary")
print("------------------")
print(f"Total entries: {total_entries}")
print(f"Deleted entries: {deleted_entries}")
print(f"Directories: {directories}")

# 5️⃣ Save summary to JSON
summary = {
    "total_entries": total_entries,
    "deleted_entries": deleted_entries,
    "directories": directories
}

summary_path.parent.mkdir(parents=True, exist_ok=True)  # ensure folder exists
with summary_path.open("w") as f:
    json.dump(summary, f, indent=4)

print(f"[✓] Summary saved to {summary_path}")
