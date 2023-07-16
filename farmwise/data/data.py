from pathlib import Path

import geopandas as gpd
import pandas as pd

DATA_DIR = Path(Path(__file__).absolute().parents[2]) / "data"


def load_county_boundaries(state_code):
    """Load county boundaries from census bureau data

    Parameters
    ----------
    state_code : int
        Numeric state code

    Returns
    -------
    df : geopandas.GeoDataFrame
        GeoDataFrame of county boundaries
    """
    CB_DATA_DIR = DATA_DIR / "cb/cb_2022_us_county_500k.shp"

    # load data
    df = gpd.read_file(CB_DATA_DIR)
    df[["STATEFP", "COUNTYFP"]] = df[["STATEFP", "COUNTYFP"]].apply(pd.to_numeric)

    # subsample based on state
    df = df[df["STATEFP"] == state_code]

    return df
