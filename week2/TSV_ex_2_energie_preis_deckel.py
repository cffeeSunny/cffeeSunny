def energie_preis_deckel(prev_year: int, this_year: int, price_per_kwh: float) -> float:
    discount_rate = 0.4
    if float(this_year) <= (float(prev_year)*0.8) and (discount_rate < price_per_kwh):
        ammount_this_year = discount_rate*0.8*float(this_year)+0.2*float(this_year)*price_per_kwh
    else:
        ammount_this_year = price_per_kwh *float(this_year)
    return round(ammount_this_year,2)
    pass
