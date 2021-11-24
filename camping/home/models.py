from django.db import models

# Create your models here.
class CampingPlace(models.Model):
    label = models.AutoField(db_column='LABEL', primary_key=True)  # Field name made lowercase.
    camping_name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='INFO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_score = models.FloatField(db_column='AVG_SCORE', blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='IMAGE', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAMPING_PLACE'


class ReviewUkc(models.Model):
    user_id = models.CharField(db_column='USER_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    camping_name = models.CharField(db_column='CAMPING_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='RATING', blank=True, null=True)  # Field name made lowercase.
    review = models.CharField(db_column='REVIEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'REVIEW_UKC'
