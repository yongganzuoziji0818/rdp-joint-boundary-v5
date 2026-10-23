from pathlib import Path, PurePosixPath
import argparse,hashlib,json,zipfile
R=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--dest');args=p.parse_args()
index=json.loads((R/'ARTIFACT_INDEX.json').read_text(encoding='utf-8'))
for n,h in index['files'].items():
    assert hashlib.sha256((R/n).read_bytes()).hexdigest()==h,n
archives=index['components']
for n in archives:
    with zipfile.ZipFile(R/n) as z:
        assert z.testzip() is None,n
        for name in z.namelist():
            q=PurePosixPath(name);assert not q.is_absolute() and '..' not in q.parts and not q.drive
if args.dest:
    dest=Path(args.dest);dest.mkdir(parents=False,exist_ok=False)
    for n,sub in archives.items():
        with zipfile.ZipFile(R/n) as z:
            for name in z.namelist():
                q=dest/sub/Path(*PurePosixPath(name).parts);q.parent.mkdir(parents=True,exist_ok=True)
                with q.open('xb') as f:f.write(z.read(name))
print(json.dumps({'state':'integrity_verified','extracted':bool(args.dest),'scientific_jobs_executed':0}))
