from lettuce import before

from django.db import connection
from django.core.management import call_command
from django.contrib.sites import models as site_models

from dynamic_rules import models as rule_models
from sample import dynamic_actions
from south.management.commands import patch_for_test_db_setup


@before.all
def setup_test_database():
    patch_for_test_db_setup()
    connection.creation.create_test_db(verbosity=1, autoclobber=True)


@before.each_scenario
def clean_db(scenario):
    call_command('flush', interactive=False)

    current_site = site_models.Site.objects.get_current()
    rule_models.Rule.objects.create(
        group_object=current_site,
        name="Free Shipping on orders over $10",
        key=dynamic_actions.FreeShippingPromotion.key,
        dynamic_fields=dict(cart_total=10, shipping_charge=2)
    )
