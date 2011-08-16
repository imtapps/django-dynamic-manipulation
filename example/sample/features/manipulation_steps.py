
from decimal import Decimal
from hamcrest import assert_that, equal_to
from lettuce import step, world

from sample import models

@step(u'Given a shopping cart named "(.*)"')
def given_a_shopping_cart_named(step, cart_name):
    world.cart = models.Cart.objects.create(name=cart_name)

@step(u'(?:And|When) I add an item with a name of "(.*)" and price of "(.*)" dollars')
def given_a_shopping_cart_with_a_total_of_amount(step, item_name, amount):
    models.Item.objects.create(name=item_name, amount=amount, cart=world.cart)

@step(u'And I view my shopping cart')
def view_shopping_cart(step):
    world.cart.view_cart()

@step(u'Then I expect the cart total to be "(.*)" dollars')
def then_i_expect_a_discount_to_be_applied_to_the_shopping_cart(step, amount):
    assert_that(world.cart.total, equal_to(Decimal(amount)))

@step(u'Given I have a shopping cart with a total of "(.*)" dollars')
def given_i_have_a_shopping_cart_with_a_total(step, cart_total):
    world.cart = models.Cart.objects.create(name="new cart")
    models.Item.objects.create(name='new item', amount=cart_total, cart=world.cart)

@step(u'And I have a "(.*)" dollar shipping charge')
def and_i_have_a_shipping_charge(step, shipping_charge):
    world.cart.view_cart()
