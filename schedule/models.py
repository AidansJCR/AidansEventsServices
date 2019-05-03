from django.db import models

# Create your models here.
class ScheduleEvent(models.Model):
    name = models.CharField(
            blank=True,
            max_length=20,
            help_text="Please enter the name of the ent being held at your event"
        )

    description = models.TextField(
        blank=False
    )

    # todo: Need to add location tie-ins (as foreign key from separate app).

    # todo: need to add images for the event, if required.