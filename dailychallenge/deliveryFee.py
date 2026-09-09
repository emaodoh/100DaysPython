# DeliveryFee


# Instructions

# Implement delivery_fee(order_total, distance_km, is_member). If order_total is below 0 or distance_km is below 0, return Invalid input. If is_member is true and order_total is at least 5000, return 0. If distance_km is less than or equal to 5, return 500. If distance_km is less than or equal to 15, return 1000. Otherwise return 2000.


def delivery_fee(order_total, distance_km, is_member):
    if order_total < 0 or distance_km < 0:
        return "Invalid input"

    if is_member and order_total >= 5000:
        return 0

    if distance_km <= 5:
        return 500

    if distance_km <= 15:
        return 1000

    return 2000
