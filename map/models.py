from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class Location(models.Model):
    """ 
    A location where an event can be held.

    This will be displayed on the map page, and will correspond to the schedule.
    These are often used locations (e.g. JCR, Bar). These are the main venue areas.
    """
    name = models.CharField(
        max_length=20,
        blank=False
    )

    map_coordinates = gis_models.PointField(blank=False)

