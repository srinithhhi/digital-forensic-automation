import subprocess
from pathlib import Path

# Paths
IMAGE_PATH = Path("evidence/image.gen0.dmg")
OUTPUT_DIR = Path("outputs/filesystem")
OUTPUT_FILE = OUTPUT_DIR / "file_listing.txt"

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("[+] Running fls on disk image...")

try:
    result = subprocess.run(
        ["fls", "-r", "-p", str(IMAGE_PATH)],
        capture_output=True,
        text=True,
        check=True
    )

    OUTPUT_FILE.write_text(result.stdout)
    print(f"[✓] File listing saved to {OUTPUT_FILE}")

except subprocess.CalledProcessError as e:
    print("[!] Error running fls")
    print(e.stderr)
