from pathlib import Path
Path("data/child_out.txt").write_text("child wrote this\n")
print("child done")
