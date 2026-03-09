from data.market_data import get_data
from strategy.trend_detector import detect_trend
from strategy.entry_model import check_entry

def scan_market(symbol):

    df = get_data(symbol)

    trend = detect_trend(df)

    entry = check_entry(df, trend)

    return entry
