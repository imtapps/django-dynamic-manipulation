import unittest
from django.core.exceptions import ValidationError
from dynamic_manipulation.models import ManipulationLog
from dynamic_manipulation.tests.test_app.models import Sample


class ManipulationLogUnitTests(unittest.TestCase):

    def test_requires_side_effect_model_or_uri(self):
        log = ManipulationLog()
        with self.assertRaises(ValidationError) as error_context:
            log.clean()
        self.assertEqual(["Side effect URI -or- Model is required."], error_context.exception.messages)

    def test_valid_when_side_effect_uri(self):
        log = ManipulationLog(side_effect_uri="foo")
        with self.assertRaises(AssertionError):
            with self.assertRaises(ValidationError):
                log.clean()

    def test_valid_when_side_effect_model(self):
        side_effect_model = Sample(pk=1)
        log = ManipulationLog()
        log.side_effect_model = side_effect_model
        with self.assertRaises(AssertionError):
            with self.assertRaises(ValidationError):
                log.clean()
