import numpy as np


__title__ = "pandas-refract"
__version__ = "1"
__author__ = "Nicholas Lawrence"
__license__ = "MIT"
__copyright__ = "Copyright 2018-2019 Nicholas Lawrence"


def refract(df, conditional, reset_index=False):
    """

    Return pair of Dataframes split against Truthy and Falseyness of provided array. Option to reset index in place.

    / >>> data = {'temperature': ['high', 'low', 'low', 'high'],
                  'overcast': [True, False, True, False]
                  }

    / >>> df = pandas.DataFrame(data)

    / >>> hot_df, cold_df = refract(df, df.temperature == 'high')

    / >>> overcast_df, not_overcast_df = refract(df, df.overcast, reset_index=True)

    / >>> print(overcast_df.iloc[0], not_overcast_df.iloc[0])

    """
    _conditional = np.asarray(conditional, bool)

    t_df = df[_conditional]
    f_df = df[~_conditional]

    if reset_index:
        return t_df.reset_index(drop=True),\
               f_df.reset_index(drop=True)

    return t_df, f_df
