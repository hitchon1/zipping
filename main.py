from pathlib import Path
import zipfile

root_dir = Path('files')

for i in range(10,21):
  filename = str(i) +'.txt'
  (root_dir / Path(filename)).touch()

archive_path = root_dir / Path('archive.zip')

with zipfile.ZipFile(archive_path, 'w') as zf:
  for path in root_dir.rglob("*.txt"):
    zf.write(path)
    path.unlink()