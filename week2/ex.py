def energie_preis_deckel(previous_year_kwh, this_year_kwh, price_per_kwh):
    # Calculate 80% of the previous year's consumption
    discounted_kwh_limit = 0.8 * previous_year_kwh

    # Determine the effective discounted rate
    discounted_rate = min(0.40, price_per_kwh)

    # Calculate the cost for the discounted portion
    if this_year_kwh <= discounted_kwh_limit:
        total_cost = this_year_kwh * discounted_rate
    else:
        discounted_cost = discounted_kwh_limit * discounted_rate
        standard_cost = (this_year_kwh - discounted_kwh_limit) * price_per_kwh
        total_cost = discounted_cost + standard_cost

    # Return the total cost rounded to two decimal places
    return round(total_cost, 2)


# Example usage:
previous_year_kwh = 5000
this_year_kwh = 4500
price_per_kwh = 0.50

total_payment = energie_preis_deckel(previous_year_kwh, this_year_kwh, price_per_kwh)
print(f"Total payment due: €{total_payment}")

energie_preis_deckel(2794,8739,0.718287935419121)
