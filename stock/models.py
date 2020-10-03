from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=50)

    def __str__(self):
        return f"({self.id}) {self.name} color: {self.color} size: {self.size}"
