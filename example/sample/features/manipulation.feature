Feature: Shopping Cart Discounts and Surcharges

    Scenario: Free shipping promotion added to cart on orders over $10
        Given a shopping cart named "First Cart"
        When I add an item with a name of "ItemOne" and price of "11" dollars
        And I view my shopping cart
        Then I expect the cart total to be "11" dollars

    Scenario: Add $2 shipping charge on orders under $10
        Given a shopping cart named "Second Cart"
        When I add an item with a name of "ItemTwo" and price of "8" dollars
        And I view my shopping cart
        Then I expect the cart total to be "10" dollars

    Scenario: Remove shipping charge when an existing shopping cart exceeds $10
        Given I have a shopping cart with a total of "8" dollars
        And I have a "2" dollar shipping charge
        When I add an item with a name of "ItemThree" and price of "8" dollars
        And I view my shopping cart
        Then I expect the cart total to be "16" dollars
