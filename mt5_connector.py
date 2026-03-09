import MetaTrader5 as mt5

def connect():

    if not mt5.initialize():
        print("MT5 connection failed")
        quit()

    print("Connected to MetaTrader 5")
