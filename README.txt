

Django Dynamic Manipulation
--------------------------------------------------------------------------

depends on:
  - django-dynamic-rules: an app that allows you to create dynamic rules
      related to a particular model.
      https://github.com/imtapps/django-dynamic-rules

When a dynamic rule is triggered, it can use a Dynamic Manipulation to
create some other model (referred to as a side effect model). When the
rules are run all of the side effect models will be deleted and re-created
if necessary (as determined by the rule).

A manipulation log keeps track of the rule, side effect model, and the
model that triggered the side effect. This is how we know what changes
occurred as a result of the dynamic rule.

See the example app for a sample of what this might look
in a shopping cart application. There are lettuce tests that
clearly show a simplified shopping cart use case.

(run "./manage.py harvest -a sample -S" to run the lettuce tests)