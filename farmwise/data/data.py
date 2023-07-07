import geopandas as gpd
from pathlib import Path

DATA_DIR = Path(Path(__file__).absolute().parents[2]) / "data"


def load_county_boundaries(state_code):
    """Load county boundaries from census bureau data

    Parameters
    ----------
    state_code : str
        Numeric state code

    Returns
    -------
    df : geopandas.GeoDataFrame
        GeoDataFrame of county boundaries
    """
    CB_DATA_DIR = DATA_DIR / "cb/cb_2022_us_county_500k.shp"

    # load data
    df = gpd.read_file(CB_DATA_DIR)

    # subsample based on state
    df = df[df["STATEFP"] == state_code]

    return df
