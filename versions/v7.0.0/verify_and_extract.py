from pathlib import Path, PurePosixPath
import argparse, hashlib, json, zipfile
root=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
manifest=json.loads((root/'MANIFEST.json').read_text(encoding='utf-8'))
for name,h in manifest.items():
 q=PurePosixPath(name)
 if q.is_absolute() or '..' in q.parts or ':' in name or '\\' in name:raise ValueError('Unsafe path')
 if hashlib.sha256((root/name).read_bytes()).hexdigest()!=h:raise ValueError('Hash mismatch: '+name)
if args.out.exists():raise FileExistsError('Use a fresh output directory')
with zipfile.ZipFile(root/'complete_reader_frozen_r2.zip') as z:
 if z.testzip() is not None:raise ValueError('CRC mismatch')
 if len(z.namelist())!=len(set(z.namelist())):raise ValueError('Duplicate member')
 for name in z.namelist():
  q=PurePosixPath(name)
  if q.is_absolute() or '..' in q.parts or ':' in name or '\\' in name:raise ValueError('Unsafe member')
 args.out.mkdir(parents=True)
 for i in z.infolist():
  if i.is_dir():continue
  p=args.out/i.filename;p.parent.mkdir(parents=True,exist_ok=True)
  with p.open('xb') as f:f.write(z.read(i))
print('Integrity verified; frozen reader extracted. No scientific execution performed.')
