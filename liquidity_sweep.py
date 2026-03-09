def detect_liquidity_sweep(df):

    high1 = df['high'].iloc[-3]
    high2 = df['high'].iloc[-2]
    current_high = df['high'].iloc[-1]

    if abs(high1 - high2) < 0.0005 and current_high > high1:
        return True

    return False
