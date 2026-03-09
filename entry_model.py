def check_entry(df, trend):

    sweep = detect_liquidity_sweep(df)

    if trend == "bullish" and sweep:

        entry = df['close'].iloc[-1]
        stop = df['low'].iloc[-1]

        target = entry + (entry - stop) * 3

        return {
            "entry": entry,
            "stop": stop,
            "target": target
        }

    return None
