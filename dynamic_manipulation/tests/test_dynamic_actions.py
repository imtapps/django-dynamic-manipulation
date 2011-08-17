
import mock
from django.utils import unittest

from dynamic_manipulation.dynamic_actions import BaseDynamicManipulation
from dynamic_manipulation import models

__all__ = (
    'BaseDynamicManipulationTests',
)

class BaseDynamicManipulationTests(unittest.TestCase):

    def setUp(self):
        self.rule_model = mock.Mock()
        self.trigger_model = mock.Mock()
        self.manipulation = BaseDynamicManipulation(self.rule_model, self.trigger_model)

    @mock.patch.object(BaseDynamicManipulation, 'do_manipulations', mock.Mock())
    @mock.patch.object(BaseDynamicManipulation, 'clear_existing')
    def test_run_calls_clear_existing(self, clear_existing):
        self.manipulation.run()
        clear_existing.assert_called_once_with()

    @mock.patch.object(BaseDynamicManipulation, 'clear_existing', mock.Mock())
    @mock.patch.object(BaseDynamicManipulation, 'do_manipulations')
    def test_run_calls_do_manipulations(self, do_manipulations):
        self.manipulation.run()
        do_manipulations.assert_called_once_with()

    @mock.patch('dynamic_manipulation.models.ManipulationLog.objects.get_by_rule')
    def test_clear_existing_gets_manipulation_logs_by_rule_model(self, get_by_rule):
        get_by_rule.return_value = mock.MagicMock()

        self.manipulation.clear_existing()
        get_by_rule.assert_called_once_with(self.rule_model, self.trigger_model)

    @mock.patch('dynamic_manipulation.models.ManipulationLog.objects.get_by_rule')
    def test_clear_existing_deletes_side_effects_related_to_manipulation_log(self, get_by_rule):
        log_one = mock.Mock(spec_set=models.ManipulationLog())
        log_two = mock.Mock(spec_set=models.ManipulationLog())
        logs = mock.MagicMock()
        logs.__iter__.return_value = iter([log_one, log_two])

        get_by_rule.return_value = logs

        self.manipulation.clear_existing()

        log_one.side_effect_model.delete.assert_called_once_with()
        log_two.side_effect_model.delete.assert_called_once_with()
        logs.delete.assert_called_once_with()

    @mock.patch.object(models.ManipulationLog.objects, 'create')
    def test_log_manipulation_logs_manipulation_with_rule_trigger_model_and_side_effect_model(self, create_log):
        side_effect_model = mock.Mock()

        self.manipulation.log_manipulation(side_effect_model)
        create_log.assert_called_once_with(
            rule=self.rule_model,
            trigger_model=self.trigger_model,
            side_effect_model=side_effect_model,)



        
        
