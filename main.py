from scanner.market_scanner import scan_market
from notifications.telegram_bot import send_message

markets = ["EURUSD","GBPUSD","XAUUSD"]

for symbol in markets:

    signal = scan_market(symbol)

    if signal:

        message = f"""
SIGNAL

Symbol: {symbol}
Entry: {signal['entry']}
Stop: {signal['stop']}
Target: {signal['target']}
"""

        send_message(message)
