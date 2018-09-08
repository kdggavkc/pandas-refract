import random as r
import unittest

import pandas as pd

from pandas_refract import refract, disperse

_n = 10000000
_iter = range(_n)

_data = {
    "Trues": [True] * _n,
    "Falses": [False] * _n,
    "Ints": _iter,
    "Floats": [r.random() for i in _iter],
    "Bools": [r.choice([True, False]) for i in _iter],
    "Strs": [r.choice(["high", "mid", "low", None]) for i in _iter],
}

_df = pd.DataFrame(_data)

class TestRefractions(unittest.TestCase):
    def test_refract_all_falses(self):
        tdf, fdf = refract(_df, _df.Falses)
        assert tdf.empty
        assert len(fdf) == len(_df)

    def test_refract_all_trues(self):
        tdf, fdf = refract(_df, _df.Trues)
        assert fdf.empty
        assert len(tdf) == len(_df)

    def test_refract_ints(self):
        tdf, fdf = refract(_df, _df.Ints)
        assert len(tdf) == (len(_df) - 1)
        assert len(fdf) == 1

    def test_refract_bools(self):
        tdf, fdf = refract(_df, _df.Bools)
        assert {True} == set(tdf.Bools)
        assert {False} == set(fdf.Bools)

    def test_refract_strs(self):
        for value in ["high", "mid", "low"]:
            tdf, fdf = refract(_df, _df.Strs == value)
            assert {value} == set(tdf.Strs)
            assert value not in set(fdf.Strs)
            assert len(tdf) + len(fdf) == len(_df)

    def test_disperse_strs(self):
        datadict = disperse(_df, 'Strs')
        assert len(datadict.keys()) == len(set(_df['Strs']))
        assert sum([len(v) for k,v in datadict.items()]) == len(_df)


if __name__ == "__main__":
    unittest.main()
