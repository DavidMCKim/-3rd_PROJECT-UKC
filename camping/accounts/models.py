from django.db import models

# Create your models here.
class CampingPlace(models.Model):
    label = models.IntegerField(db_column='LABEL', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    info1 = models.CharField(max_length=200, blank=True, null=True)
    avg = models.FloatField(db_column='AVG', blank=True, null=True)  # Field name made lowercase.
    info2 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CAMPING_PLACE'

class Users(models.Model):
    user_id = models.CharField(db_column='USER_ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birth = models.CharField(db_column='BIRTH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERS'
