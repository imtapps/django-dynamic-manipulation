
from dynamic_rules.dynamic_actions import BaseDynamicAction

from dynamic_manipulation import models
from dynamic_manipulation.models import ManipulationLog

__all__ = ('BaseDynamicManipulation',)

class BaseDynamicManipulation(BaseDynamicAction):

    def clear_existing(self):
        """
        Both Side Effect Models and Manipulation Logs may have been
        created for a particular rule and trigger. This method
        deletes all of them.
        """
        manipulation_logs = models.ManipulationLog.objects.get_by_rule(self.rule_model, self.trigger_model)
        for log in manipulation_logs:
            log.side_effect_model.delete()
        manipulation_logs.delete()

    def run(self, *args, **kwargs):
        self.clear_existing()
        self.do_manipulations(*args, **kwargs)

    def do_manipulations(self, *args, **kwargs):
        """
        Implement this method on your custom rule classes.
        """
        pass

    def log_manipulation(self, side_effect_model):
        ManipulationLog.objects.create(
            rule=self.rule_model,
            trigger_model=self.trigger_model,
            side_effect_model=side_effect_model,
        )
