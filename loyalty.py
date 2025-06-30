def calculate_loyalty_points(amount_spent):
    points = amount_spent // 10
    if amount_spent > 500:
        points += 50
    return int(points)
