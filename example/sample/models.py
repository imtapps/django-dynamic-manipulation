from django.db import models

from dynamic_rules import models as rule_models
from django.contrib.sites import models as site_models


class Cart(models.Model):
    name = models.CharField(max_length=30)

    def view_cart(self):
        current_site = site_models.Site.objects.get_current()
        rules = rule_models.Rule.objects.get_by_group_object(current_site)

        for rule in rules:
            rule.run_action(self)

    @property
    def total(self):
        return sum(i.amount for i in self.items.all())


class Item(models.Model):
    cart = models.ForeignKey(Cart, related_name="items")
    name = models.CharField(max_length=30)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
