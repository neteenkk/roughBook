from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing Paypal payment of ${amount}")



class PaymentProcessor:
    def process(self, payment_method: PaymentMethod, amount):
        payment_method.process_payment(amount)


class CheckoutService:
    def process_payment(self, method: PaymentMethod, amount):
        processor = PaymentProcessor()
        processor.process(method, amount)


checkout = CheckoutService()
checkout.process_payment(CreditCardPayment(), 100.00)
checkout.process_payment(PayPalPayment(), 100.00)

