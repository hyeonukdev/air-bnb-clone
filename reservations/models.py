from django.db import models
from django.utils import timezone
from core import models as core_models
from django.utils.dateparse import parse_date


class Reservation(core_models.TimeStampedModel):
    ''' Reservation Model Reservation '''

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confrimed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.room} - {self.check_in}'

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True


def get_now_date():
    now = timezone.localtime()  # 2020-10-11 02:03:49

    # type 이 datetime 형식으로 받아오기, 날짜 비교를 위해서
    now = parse_date(timezone.localtime().strftime("%Y-%m-%d"))
    return now
