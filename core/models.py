from django.db import models

class TimeStampedModel(models.Model):

    ''' Time Stamped Model '''

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
        # 데이터베이스에 나타나지 않게 하기 위함