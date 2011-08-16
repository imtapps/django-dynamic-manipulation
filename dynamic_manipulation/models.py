from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models


class ManipulationLogManager(models.Manager):

    def get_by_rule(self, rule_model, trigger_model):
        content_type = ContentType.objects.get_for_model(trigger_model)
        return self.filter(
            trigger_content_type=content_type,
            trigger_model_id=trigger_model.pk,
            rule=rule_model,
        )

class ManipulationLog(models.Model):
    rule = models.ForeignKey('dynamic_rules.Rule', related_name='manipulation_logs')

    trigger_content_type = models.ForeignKey('contenttypes.ContentType', related_name="manipulation_triggers")
    trigger_model_id = models.PositiveIntegerField(db_index=True)
    trigger_model = generic.GenericForeignKey(fk_field='trigger_model_id')

    side_effect_content_type = models.ForeignKey('contenttypes.ContentType', related_name="manipulation_side_effects")
    side_effect_model_id = models.PositiveIntegerField(db_index=True)
    side_effect_model = generic.GenericForeignKey(fk_field='side_effect_model_id')

    objects = ManipulationLogManager()
