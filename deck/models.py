from django.db import models

class Deck(models.Model):
    value = models.CharField(max_length=15)
    suit = models.CharField(max_length=15)
    color = models.CharField(max_length=10, default="Black")
    face = models.BooleanField(default=False)

    def set_color_face(self):
        if self.value in ("King", "Queen", "Jack"):
            self.face = True
        if self.suit in ("Hearts", "Diamonds"):
            self.color = "Red"
