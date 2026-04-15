class InvalidCouponException(Exception):
    pass
class InsufficientFundsException(Exception):
    pass
class PricingService:
    def __init__(self, coupons: dict, shipping_fee: float):
        """
        coupons: {"BLACK50": 0.5}
        shipping_fee: valor fixo do frete
        """
        self.coupons = coupons
        self.shipping_fee = shipping_fee

    def apply_coupon(self, amount: float, coupon_code: str) -> float:
        if coupon_code not in self.coupons:
            raise InvalidCouponException("Cupom inválido")
        discount = self.coupons[coupon_code]
        return amount * (1 - discount)
      
    def calculate_total(self, amount: float, coupon_code: str) -> float:
        discounted_amount = self.apply_coupon(amount, coupon_code)
        total_with_shipping = discounted_amount + self.shipping_fee
        return total_with_shipping

    def validate_balance(self, total_amount: float, user_balance: float) -> None:
        if user_balance < total_amount:
            raise InsufficientFundsException(
                "Saldo insuficiente para concluir a compra"
            )
    def process_purchase(self, amount: float, coupon_code: str, user_balance: float) -> float:
        total = self.calculate_total(amount, coupon_code)
        self.validate_balance(total, user_balance)
        return total
