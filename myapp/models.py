from django.db import models


# the meme data models (on DBS)
class Meme(models.Model):
    path = models.TextField(max_length=500)
    reach = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)

    def __str__(self):
        return self.path

    @property
    def Engagement(self):
        point = (self.like + self.share + self.comment) / self.reach
        return point
