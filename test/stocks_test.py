

from pandas import DataFrame

from app.stocks import fetch_stocks_csv, format_usd


def test_formatting():
    assert format_usd(10) == "$10.00"
    assert format_usd(1234.5678) == "$1234.57"
    assert format_usd(0.12) == "$0.12"


def test_data_fetching():

    stocks_df = fetch_stocks_csv("GOOGL")

    assert isinstance(stocks_df, DataFrame)

    assert "timestamp" in stocks_df.columns
    assert "adjusted_close" in stocks_df.columns

    assert len(stocks_df) >= 100