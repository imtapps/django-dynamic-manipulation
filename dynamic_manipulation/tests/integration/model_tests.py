from django import test
from django.core.exceptions import ValidationError
from dynamic_manipulation.models import ManipulationLog
from dynamic_rules.models import Rule
from dynamic_manipulation.tests.test_app.models import Sample


class ManipulationLogTests(test.TestCase):

    def test_side_effect_uri_is_not_required_when_side_effect_model(self):
        side_effect = Sample.objects.create()
        group_object = Sample.objects.create()
        trigger = Sample.objects.create()
        rule = Rule.objects.create(group_object=group_object)
        log = ManipulationLog(rule=rule, trigger_model=trigger, side_effect_model=side_effect)

        with self.assertRaises(AssertionError):
            with self.assertRaises(ValidationError):
                log.full_clean()

    def test_side_effect_model_is_not_required_when_side_effect_uri(self):
        group_object = Sample.objects.create()
        trigger = Sample.objects.create()
        rule = Rule.objects.create(group_object=group_object)
        log = ManipulationLog(rule=rule, trigger_model=trigger, side_effect_uri="http://localhost/sample")

        with self.assertRaises(AssertionError):
            with self.assertRaises(ValidationError):
                log.full_clean()

    def test_either_side_effect_model_or_uri_is_required(self):
        group_object = Sample.objects.create()
        trigger = Sample.objects.create()
        rule = Rule.objects.create(group_object=group_object)
        log = ManipulationLog(rule=rule, trigger_model=trigger)

        with self.assertRaises(ValidationError):
            log.full_clean()
