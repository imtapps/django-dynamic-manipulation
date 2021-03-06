import mock
from django.utils import unittest

from dynamic_manipulation.dynamic_actions import BaseDynamicManipulation
from dynamic_manipulation import models

__all__ = ('BaseDynamicManipulationTests', )


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
        args = ["arg"]
        kwargs = {'kwarg': 'something'}

        self.manipulation.run(*args, **kwargs)
        do_manipulations.assert_called_once_with(*args, **kwargs)

    @mock.patch('dynamic_manipulation.models.ManipulationLog.objects.get_by_rule')
    def test_clear_existing_gets_manipulation_logs_by_rule_model(self, get_by_rule):
        get_by_rule.return_value = mock.MagicMock()

        self.manipulation.clear_existing()
        get_by_rule.assert_called_once_with(self.rule_model, self.trigger_model)

    @mock.patch.object(BaseDynamicManipulation, 'clear_side_effect_model')
    @mock.patch('dynamic_manipulation.models.ManipulationLog.objects.get_by_rule')
    def test_clear_existing_calls_clear_side_effect_for_each_log(self, get_by_rule, clear_side_effect):
        log_one = mock.Mock(spec_set=models.ManipulationLog())
        log_one.side_effect_uri = ""
        log_two = mock.Mock(spec_set=models.ManipulationLog())
        log_two.side_effect_uri = ""
        logs = mock.MagicMock()
        logs.__iter__.return_value = iter([log_one, log_two])

        get_by_rule.return_value = logs

        self.manipulation.clear_existing()
        self.assertEqual(
            [
                ((log_one.side_effect_model, ), {}),
                ((log_two.side_effect_model, ), {}),
            ], clear_side_effect.call_args_list
        )

    @mock.patch.object(BaseDynamicManipulation, 'clear_side_effect_uri')
    @mock.patch('dynamic_manipulation.models.ManipulationLog.objects.get_by_rule')
    def test_clear_existing_calls_clear_side_effect_uri_when_side_effect_uri_and_no_model(
        self, get_by_rule, clear_side_effect
    ):
        log_one = models.ManipulationLog(side_effect_uri='one')
        log_two = models.ManipulationLog(side_effect_uri='two')
        logs = mock.MagicMock()
        logs.__iter__.return_value = iter([log_one, log_two])

        get_by_rule.return_value = logs

        self.manipulation.clear_existing()
        self.assertEqual(
            [
                ((log_one.side_effect_uri, ), {}),
                ((log_two.side_effect_uri, ), {}),
            ], clear_side_effect.call_args_list
        )

    @mock.patch.object(BaseDynamicManipulation, 'clear_side_effect_model')
    @mock.patch.object(BaseDynamicManipulation, 'clear_side_effect_uri')
    @mock.patch('dynamic_manipulation.models.ManipulationLog.objects.get_by_rule')
    def test_clear_existing_calls_clear_side_effect_uri_and_model_when_both_exist(
        self, get_by_rule, clear_uri, clear_model
    ):
        log_one = models.ManipulationLog(side_effect_uri='one')
        log_two = mock.Mock(spec_set=models.ManipulationLog())
        log_two.side_effect_uri = ""
        logs = mock.MagicMock()
        logs.__iter__.return_value = iter([log_one, log_two])

        get_by_rule.return_value = logs

        self.manipulation.clear_existing()
        self.assertEqual([
            ((log_one.side_effect_uri, ), {}),
        ], clear_uri.call_args_list)
        self.assertEqual([
            ((log_two.side_effect_model, ), {}),
        ], clear_model.call_args_list)

    def test_clear_side_effect_model_calls_delete_on_model(self):
        model = mock.Mock()
        self.manipulation.clear_side_effect_model(model)
        model.delete.assert_called_once_with()

    def test_clear_side_effect_model_returns_none_when_model_is_none(self):
        self.assertEqual(None, self.manipulation.clear_side_effect_model(None))

    @mock.patch.object(models.ManipulationLog.objects, 'create')
    def test_log_manipulation_logs_manipulation_with_rule_trigger_model_and_side_effect_model(self, create_log):
        side_effect_model = mock.Mock()

        self.manipulation.log_manipulation(side_effect_model)
        create_log.assert_called_once_with(
            rule=self.rule_model,
            trigger_model=self.trigger_model,
            side_effect_model=side_effect_model,
        )

    @mock.patch.object(models.ManipulationLog.objects, 'create')
    def test_log_manipulation_logs_manipulation_with_rule_trigger_model_and_side_effect_uri(self, create_log):
        self.manipulation.log_manipulation(side_effect_uri="asdf")
        create_log.assert_called_once_with(
            rule=self.rule_model,
            trigger_model=self.trigger_model,
            side_effect_uri="asdf",
        )

    def test_clear_side_effect_uri_raises_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.manipulation.clear_side_effect_uri("x")
