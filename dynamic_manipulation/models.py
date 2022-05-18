from django.contrib.contenttypes import generic
from django.core.exceptions import ValidationError
from django.db import models

from dynamic_rules.ext import RuleExtensionManager


class ManipulationLog(models.Model):
    rule = models.ForeignKey('dynamic_rules.Rule', related_name='manipulation_logs')

    trigger_content_type = models.ForeignKey('contenttypes.ContentType', related_name="manipulation_triggers")
    trigger_model_id = models.PositiveIntegerField(db_index=True)
    trigger_model = generic.GenericForeignKey(fk_field='trigger_model_id', ct_field='trigger_content_type')

    side_effect_content_type = models.ForeignKey(
        'contenttypes.ContentType', related_name="manipulation_side_effects", null=True, blank=True
    )
    side_effect_model_id = models.PositiveIntegerField(db_index=True, null=True, blank=True)
    side_effect_model = generic.GenericForeignKey(fk_field='side_effect_model_id', ct_field='side_effect_content_type')

    side_effect_uri = models.URLField(null=True, blank=True)

    objects = RuleExtensionManager()

    def clean(self):
        if not self.side_effect_uri and not self.side_effect_model:
            raise ValidationError("Side effect URI -or- Model is required.")
