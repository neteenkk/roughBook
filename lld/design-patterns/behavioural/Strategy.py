from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, order) -> float:
        pass


class FlatRateShipping(ShippingStrategy):
    def __init__(self, rate):
        self.rate = rate

    def calculate_cost(self, order):
        print(f"Calculating with Flat Rate Strategy ${self.rate}")
        return self.rate


class WeightBasedShipping(ShippingStrategy):
    def __init__(self, rate_per_kg):
        self.rate_per_kg = rate_per_kg

    def calculate_cost(self, order):
        print(f"Calc with Weight-Based Strategy ${self.rate_per_kg}/kg")
        return order.get_total_weight() * self.rate_per_kg


class ShippingCostService:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate_shipping_cost(self, order):
        cost = self.strategy.calculate_cost(order)
        print(f"ShippingCostService: Final Calculated Shipping Cost: ${cost} "
              f"(using {self.strategy.__class__.__name__})")
        return cost


class Order:
    def __init__(self, kg):
        self.kg = kg

    def get_total_weight(self):
        return self.kg


def ecommerce_app_v2():
    order1 = Order(10)

    flat_rate = FlatRateShipping(100)
    weight_based_rate = WeightBasedShipping(200)

    shipping_service = ShippingCostService(flat_rate)
    print("--- Order 1: Using Flat Rate (initial) ---")
    shipping_service.calculate_shipping_cost(order1)

    shipping_service.set_strategy(weight_based_rate)
    print("--- Order 2: Using Weight Based Rate (initial) ---")
    shipping_service.calculate_shipping_cost(order1)


if __name__ == "__main__":
    ecommerce_app_v2()