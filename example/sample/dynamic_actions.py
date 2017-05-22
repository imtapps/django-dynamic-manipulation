from django import forms

from dynamic_rules import site

from dynamic_manipulation.dynamic_actions import BaseDynamicManipulation
from sample import models


@site.register
class FreeShippingPromotion(BaseDynamicManipulation):
    key = "free_shipping_promo"
    trigger_model_name = 'shopping_cart'

    fields = {
        'cart_total': forms.DecimalField(),
        'shipping_charge': forms.DecimalField(),
    }

    def do_manipulations(self, *args, **kwargs):
        if self.shopping_cart.total < self.rule_model.dynamic_fields['cart_total']:
            shipping_charge_amount = self.rule_model.dynamic_fields['shipping_charge']
            shipping_item = models.Item.objects.create(
                name="shipping charge", amount=shipping_charge_amount, cart=self.shopping_cart
            )
            self.log_manipulation(shipping_item)
