from django.utils import unittest
from django.contrib.contenttypes.models import ContentType
import mock

from dynamic_manipulation import models


class ModelTests(unittest.TestCase):

    def setUp(self):
        self.rule_model = mock.Mock()
        self.trigger_model = mock.Mock()

    @mock.patch.object(ContentType.objects, 'get_for_model')
    def test_get_content_type_for_model_in_get_by_validation_object(self, get_for_model):
        manager = mock.Mock(spec_set=models.ManipulationLogManager)
        models.ManipulationLogManager.get_by_rule(manager, self.rule_model, self.trigger_model)
        get_for_model.assert_called_once_with(self.trigger_model)

    @mock.patch.object(ContentType.objects, 'get_for_model')
    def test_get_by_validation_object_returns_rules_for_related_object(self, get_for_model):
        manager = mock.Mock(spec_set=models.ManipulationLogManager)
        logs = models.ManipulationLogManager.get_by_rule(manager, self.rule_model, self.trigger_model)

        manager.filter.assert_called_once_with(
            trigger_content_type=get_for_model.return_value,
            trigger_model_id=self.trigger_model.pk,
            rule=self.rule_model,
        )
        self.assertEqual(manager.filter.return_value, logs)