import random as r
import unittest

import pandas as pd

from pandas_refract import refract

_n = 10000000
_iter = range(_n)

_data = {
    "Trues": [True] * _n,
    "Falses": [False] * _n,
    "Ints": _iter,
    "Floats": [r.random() for i in _iter],
    "Bools": [r.choice([True, False]) for i in _iter],
    "Strs": [r.choice(["high", "mid", "low"]) for i in _iter],
}


_df = pd.DataFrame(_data)


class TestRefract(unittest.TestCase):
    def test_all_falses(self):
        tdf, fdf = refract(_df, _df.Falses)
        assert tdf.empty
        assert len(fdf) == len(_df)

    def test_all_trues(self):
        tdf, fdf = refract(_df, _df.Trues)
        assert fdf.empty
        assert len(tdf) == len(_df)

    def test_ints(self):
        tdf, fdf = refract(_df, _df.Ints)
        assert len(tdf) == (len(_df) - 1)
        assert len(fdf) == 1

    def test_bools(self):
        tdf, fdf = refract(_df, _df.Bools)
        assert {True} == set(tdf.Bools)
        assert {False} == set(fdf.Bools)

    def test_strs(self):
        for value in ["high", "mid", "low"]:
            tdf, fdf = refract(_df, _df.Strs == value)
            assert {value} == set(tdf.Strs)
            assert value not in set(fdf.Strs)


if __name__ == "__main__":
    unittest.main()
