from django.db import models


class Transaction(models.Model):
    amount = models.DecimalFieldField(max_digits=7, decimal_places=2)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    catagory = models.ForeignKey('Catagory', on_delete=models.CASCADE)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)


class Location(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)


class Catagory(models.Model):
    name = models.CharField(max_length=128)
    budget = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.name)
