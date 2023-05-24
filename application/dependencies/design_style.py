from pathlib import Path

with open(f'{Path(Path.cwd(), "static", "files", "style.qss")}', 'r') as f:
    DESIGN_STYLE = f.read()
