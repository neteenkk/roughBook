# Adapter
# The translator. It implements the Target interface and holds a reference to the Adaptee, delegating calls with the necessary translation.

from abc import ABC, abstractmethod
import time

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float, currency: str):
        pass


class InHousePaymentProcessor(PaymentProcessor):
    def __init__(self):
        self._transaction_id = None
        self._payment_successful = None

    def process_payment(self, amount, currency):
        self._transaction_id = f"TXN_{self._transaction_id}"
        self._payment_successful = True
        print(f"InHousePaymentProcessor: Success. Txn ID: {self._transaction_id}")


class LegacyGateway:
    def __init__(self):
        self._transaction_reference = None
        self._payment_successful = False

    def execute_transaction(self, total_amount: float, currency: str):
        self._transaction_reference = time.time_ns()
        self._payment_successful = True
        print(f"LegacyGateway: Done. Ref: {self._transaction_reference}")


class LegacyAdapter(PaymentProcessor):
    def __init__(self, legacy_gateway):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        self.legacy_gateway = legacy_gateway
        self.current_ref = None

    def process_payment(self, amount, currency):
        print(f"Adapter: Translating processPayment() for {amount} {currency}")
        self.legacy_gateway.execute_transaction(amount, currency)


class CheckoutService:
    def __init__(self, payment_processor: PaymentProcessor):
        self._processor = payment_processor

    def checkout(self, amount: float, currency: str):
        print(f"Checkout: Processing order for ${amount} {currency}")
        self._processor.process_payment(amount, currency)

class ECommerceAPIV2:
    @staticmethod
    def main():
       processor = InHousePaymentProcessor()
       modern_checkout = CheckoutService(processor)
       print("--- Using Modern Processor ---")
       modern_checkout.checkout(199.99, "USD")

       # Legacy gateway through adapter
       print("\n--- Using Legacy Gateway via Adapter ---")
       legacy = LegacyGateway()
       processor = LegacyAdapter(legacy)
       legacy_checkout = CheckoutService(processor)
       legacy_checkout.checkout(75.50, "USD")

if __name__ == "__main__":
    ECommerceAPIV2.main()