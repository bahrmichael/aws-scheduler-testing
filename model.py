from pynamodb.attributes import (
    UnicodeAttribute,
    NumberAttribute)
from pynamodb.models import Model


class MeasuredDuration(Model):

    class Meta:
        table_name = 'aws-scheduler-testing'

    id = UnicodeAttribute(hash_key=True)
    delay = NumberAttribute()
