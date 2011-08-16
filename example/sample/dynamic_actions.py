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

    def do_thing(self, *args, **kwargs):
        # get manipulation_logs for self.rule_model and self.cart
        # delete manipulation side effect models
        # delete manipulation_logs

        # get new side effect models
        # create manipulation_logs

        if self.cart.total < self.rule_model.dynamic_fields['cart_total']:
            shipping_charge_amount = self.rule_model.dynamic_fields['shipping_charge']
            models.Item.objects.create(name="shipping charge", amount=shipping_charge_amount, cart=self.cart)

