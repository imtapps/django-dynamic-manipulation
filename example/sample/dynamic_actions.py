from dynamic_rules import site
from django import forms

from dynamic_manipulation.dynamic_actions import BaseDynamicManipulation
from sample import models

@site.register
class FreeShippingPromotion(BaseDynamicManipulation):
    key = "free_shipping_promo"

    fields = {
        'cart_total':forms.DecimalField(),
        'shipping_charge':forms.DecimalField(),
    }

    def __init__(self, rule_model, shopping_cart):
        super(FreeShippingPromotion, self).__init__(rule_model, shopping_cart)
        self.cart = shopping_cart

    def do_manipulations(self, *args, **kwargs):
        if self.cart.total < self.rule_model.dynamic_fields['cart_total']:
            shipping_charge_amount = self.rule_model.dynamic_fields['shipping_charge']
            shipping_item = models.Item.objects.create(name="shipping charge", amount=shipping_charge_amount, cart=self.cart)
            self.log_manipulation(shipping_item)



