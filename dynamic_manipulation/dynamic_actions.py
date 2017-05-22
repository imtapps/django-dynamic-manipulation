from dynamic_rules.dynamic_actions import BaseDynamicAction

from dynamic_manipulation import models
from dynamic_manipulation.models import ManipulationLog

__all__ = ('BaseDynamicManipulation', )


class BaseDynamicManipulation(BaseDynamicAction):

    def clear_existing(self):
        """
        Both Side Effect Models and Manipulation Logs may have been
        created for a particular rule and trigger. This method
        deletes all of them.
        """
        manipulation_logs = models.ManipulationLog.objects.get_by_rule(self.rule_model, self.trigger_model)
        for log in manipulation_logs:
            if log.side_effect_uri:
                self.clear_side_effect_uri(log.side_effect_uri)
            else:
                self.clear_side_effect_model(log.side_effect_model)

        manipulation_logs.delete()

    def clear_side_effect_model(self, model):
        """
        If the side effect model is deleted somewhere before the dynamic
        manipulation action requests it, Django may not cascade delete,
        so we could end up with a log without a side effect model.
        """
        if model:
            model.delete()

    def clear_side_effect_uri(self, uri):
        raise NotImplementedError

    def run(self, *args, **kwargs):
        self.clear_existing()
        self.do_manipulations(*args, **kwargs)

    def do_manipulations(self, *args, **kwargs):
        """
        Implement this method on your custom rule classes.
        """
        pass

    def log_manipulation(self, side_effect_model=None, side_effect_uri=None):
        data = dict(rule=self.rule_model, trigger_model=self.trigger_model)

        if side_effect_uri:
            data['side_effect_uri'] = side_effect_uri

        if side_effect_model:
            data['side_effect_model'] = side_effect_model

        ManipulationLog.objects.create(**data)
