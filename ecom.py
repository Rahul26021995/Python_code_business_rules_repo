class ecom:

    @staticmethod
    def calculate_discount(price, customer_type):
        if customer_type == "premium": 
            return price * 0.80
        elif customer_type == "regular":
            return price * 0.90
        elif customer_type == "new":
            return price * 0.95
        else:
            return price

    @staticmethod
    def is_return_eligible(days_since_purchase, item_condition):
        return days_since_purchase <= 30 and item_condition in ['new', 'like new']

    @staticmethod
    def get_shipping_fee(weight, location):
        if weight < 1 and location == "local":
            return 0
        elif location == "national":
            return 50
        elif location == "international":
            return 100
        else:
            return 75
