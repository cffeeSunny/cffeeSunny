def energie_preis_deckel(prev_year: int, this_year: int, price_per_kwh: float) -> float:
    discount_rate = 0.4
    if this_year <= 0.8*(float(prev_year)) && discount_rate < price_per_kwh:
        ammount_this_year = discount_rate*float(this_year)
    else:
        ammount_this_year = price_per_kwh *float(this_year)
    return print(round(ammount_this_year,2))
