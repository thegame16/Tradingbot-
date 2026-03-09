def detect_trend(df):

    df['ema200'] = df['close'].ewm(span=200).mean()

    if df['close'].iloc[-1] > df['ema200'].iloc[-1]:
        return "bullish"

    return "bearish"
