import pytest

from libs import build_processed_dataset
from libs.datasets import CommonFields


def test_get_testing_df_by_state():
    testing_df = build_processed_dataset.get_testing_timeseries_by_state("MA")
    assert testing_df is not None


# Check San Francisco and Houston (Harris County, TX)
@pytest.mark.parametrize(
    "fips", ["06075", "48201"],
)
def test_get_testing_by_fips(fips):
    df = build_processed_dataset.get_testing_timeseries_by_fips(fips)
    assert CommonFields.POSITIVE_TESTS in df.columns
    assert CommonFields.NEGATIVE_TESTS in df.columns
    print(df)
    df.set_index(CommonFields.DATE, inplace=True)
    assert df.loc["2020-04-01", CommonFields.POSITIVE_TESTS] > 0
