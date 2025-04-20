from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    left_parent = models.ForeignKey('self', on_delete=models.PROTECT, related_name="left_parent_child", null=True)
    right_parent = models.ForeignKey('self', on_delete=models.PROTECT, related_name="right_parent_child", null=True)
    spouse = models.ForeignKey('self', on_delete=models.PROTECT, null=True)
    birth = models.DateField(null=True)
    death = models.DateField(null=True)
