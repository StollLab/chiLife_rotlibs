import chilife as xl
import numpy as np
from pathlib import Path
import pytest

mono_rotlibs = list(Path('../MMM Rotlibs').glob('*.npz')) + list(Path('../SpinLabels').glob('*.npz'))
av_rotlibs = list(Path('../AV Only SpinLabels').glob('*.npz')) + list(Path('../AV Only FluorLabels').glob('*.npz'))
prot = xl.fetch('1ubq')


@pytest.mark.parametrize('lib', mono_rotlibs)
def test_mono_rotlibs(lib):
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