from dynamic_manipulation import models

__all__ = ('BaseDynamicManipulation',)

class BaseDynamicManipulation(object):

    def __init__(self, rule_model, trigger_model):
        self.rule_model = rule_model
        self.trigger_model = trigger_model

    def clear_existing(self):
        manipulation_logs = models.ManipulationLog.objects.get_by_rule(self.rule_model, self.trigger_model)
        for log in manipulation_logs:
            log.side_effect_model.delete()
        manipulation_logs.delete()

    def run(self, *args, **kwargs):
        self.clear_existing()
        self.do_thing()

    def do_thing(self):
        pass
