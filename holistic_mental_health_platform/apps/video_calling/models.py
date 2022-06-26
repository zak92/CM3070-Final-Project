from django.db import models

# Create your models here.
class VideoConferenceRoomMember(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=200)
    in_session = models.BooleanField(default=True)

    def __str__(self):
        return self.name