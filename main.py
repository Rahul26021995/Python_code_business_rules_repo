from pricing import calculate_discount
from shipping import get_shipping_fee
from returns import is_return_eligible
from loyalty import calculate_loyalty_points

def main():
    price = 100
    customer_type = "premium"
    discounted_price = calculate_discount(price, customer_type)
    print(f"Discounted price for {customer_type} customer: ${discounted_price}")

    weight = 2
    location = "international"
    shipping_fee = get_shipping_fee(weight, location)
    print(f"Shipping fee for {location} location: ${shipping_fee}")

    days_since_purchase = 15
    item_condition = "new"
    eligible_for_return = is_return_eligible(days_since_purchase, item_condition)
    print(f"Item eligible for return: {eligible_for_return}")

    amount_spent = 600
    loyalty_points = calculate_loyalty_points(amount_spent)
    print(f"Loyalty points for ${amount_spent} spent: {loyalty_points}")

if __name__ == "__main__":
    main()
