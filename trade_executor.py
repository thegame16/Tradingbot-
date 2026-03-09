import MetaTrader5 as mt5

def place_trade(symbol, lot, entry, stop, target):

    request = {

        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "price": entry,
        "sl": stop,
        "tp": target,
        "deviation": 20,
        "magic": 100,
        "comment": "SmartMoneyBot"

    }

    mt5.order_send(request)
