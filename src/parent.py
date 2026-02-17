import subprocess, sys
from pathlib import Path
Path("data/parent_out.txt").write_text("parent wrote this\n")
subprocess.run([sys.executable, "src/child.py"], check=True)
print("parent done")
