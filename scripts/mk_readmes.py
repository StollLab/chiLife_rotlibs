from pathlib import Path
import zipfile
import numpy as np


def _print_monofunc(files):
    lines = []
    for file in files:
        with np.load(file, allow_pickle=True) as f:
            for key in f.keys():
                resname = f['resname']
                if 'description' in f:
                    descr = f['description']
                else:
                    descr = "No description"

        lines.append(f'{resname:<8} : {descr}  \n')
    return lines


def _print_bifunc(files):

    lines = []
    for file in files:
        with zipfile.ZipFile(file, 'r') as archive:
            name = archive.namelist()[0]
            resname = name[:3]
            context = name[3:6]
            with archive.open(name) as of:
                with np.load(of, allow_pickle=True) as f:
                    if 'description' in f:
                        descr = f['description']
                    else:
                        descr = "No description"

        lines.append(f'{resname:<4}{context:<4} : {descr}  \n')
    return lines


def write_readme(path):

    base_README = path / '_README.md'
    if base_README.exists():
        with open(base_README, 'r') as f:
            lines = f.readlines()

        lines.append("\n\n")

    else:
        lines = []

    lines.append("## rotamer library descriptions\n")

    monofunctional = list(path.glob('*_rotlib.npz'))
    bifunctional = list(path.glob('*_drotlib.zip'))


    if len(monofunctional) > 0: lines += _print_monofunc(monofunctional)
    if len(bifunctional) > 0: lines += _print_bifunc(bifunctional)

    print(path / 'README.md')
    with open(path / 'README.md', 'w') as f:
        f.writelines(lines)


folders = ['AV Only FluorLabels', 'AV Only SpinLabels', 'dSpinLabels', 'MMM Rotlibs', 'SpinLabels']

for fold in folders:
    fpath = Path('..') / fold
    write_readme(fpath)