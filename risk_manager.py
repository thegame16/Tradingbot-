def position_size(balance, risk_percent, stop_distance):

    risk_amount = balance * risk_percent

    lot_size = risk_amount / stop_distance

    return round(lot_size, 2)
