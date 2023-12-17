from django.db import models

class adm(models.Model):
    todo =models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    reg =models.CharField(max_length=20)

    class Meta:
        db_table="todo"

# Create your models here.
