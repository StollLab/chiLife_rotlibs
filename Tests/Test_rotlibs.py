import chilife as xl
import numpy as np
from pathlib import Path
import pytest

mono_rotlibs = list(Path('../MMM Rotlibs').glob('*.npz')) + list(Path('../SpinLabels').glob('*.npz'))
av_rotlibs = list(Path('../AV Only SpinLabels').glob('*.npz')) + list(Path('../AV Only FluorLabels').glob('*.npz'))
drotlibs = list(Path('../dSpinLabels').glob('*.zip'))
nuc_labels = ['CNR', 'R3P', 'R5P', 'R5T', 'RTT', 'TUM', 'TUP']
prot = xl.fetch('1ubq')
RNA = xl.fetch('4tna')


@pytest.mark.parametrize('lib', mono_rotlibs)
def test_mono_rotlibs(lib):
    libname = lib.name[:3]
    if libname in nuc_labels:
        SL = xl.SpinLabel('TST', 33, RNA, rotlib=str(lib))
    else:
        SL = xl.SpinLabel('TST', 28, prot, rotlib=str(lib))

    if not Path(f'test_data/{lib.stem}.npy').exists():
        np.save(f'test_data/{lib.stem}.npy', SL.coords)

    ans = np.load(f'test_data/{lib.stem}.npy')
    np.testing.assert_almost_equal(SL.coords, ans)


@pytest.mark.parametrize('lib', av_rotlibs)
def test_av_rotlibs(lib):
    np.random.seed(1)

    SL = xl.SpinLabel('TST', 28, prot, rotlib=str(lib), sample=100)

    if not Path(f'test_data/{lib.stem}.npy').exists():
        np.save(f'test_data/{lib.stem}.npy', SL.coords)

    ans = np.load(f'test_data/{lib.stem}.npy')
    np.testing.assert_almost_equal(SL.coords, ans)


@pytest.mark.parametrize('lib', drotlibs)
def test_drotlibs(lib):
    if 'ip4' in str(lib):
        site = 28, 32
    elif 'ip3' in str(lib):
        site = 28, 31
    elif 'ip2' in str(lib):
        site = 66, 68

    print(lib)

    SL= xl.dSpinLabel(lib.name[:3], site, prot, rotlib=str(lib))

    if not Path(f'test_data/{lib.stem}.npy').exists():
        np.save(f'test_data/{lib.stem}.npy', SL.coords)

    ans = np.load(f'test_data/{lib.stem}.npy')
    np.testing.assert_almost_equal(SL.coords, ans, decimal=2)
    assert np.all(~np.isnan(SL.coords))