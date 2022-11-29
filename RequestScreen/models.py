from django.db import models

# Create your models here.


class VisitRequestDetails(models.Model):
    # Field name made lowercase.
    visitid = models.AutoField(db_column='VisitID', primary_key=True)
    # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100)
    # Field name made lowercase.
    visitstartdatetime = models.DateTimeField(db_column='VisitStartDateTime')
    # Field name made lowercase.
    visitenddatetime = models.DateTimeField(db_column='VisitEndDateTime')
    # Field name made lowercase.
    # values for visit status
    VisitType = models.TextChoices(
        'VisitType', 'pending approved rejected revision')

    visitstatus = models.CharField(
        db_column='VisitStatus', max_length=8, choices=VisitType.choices)
    # Field name made lowercase.
    additionalcomments = models.TextField(
        db_column='AdditionalComments', blank=True, null=True)
    # Field name made lowercase.
    visitlocationname = models.CharField(
        db_column='VisitLocationName', max_length=100)
    # Field name made lowercase.
    maplink = models.CharField(
        db_column='MapLink', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    certifiedbyemail = models.CharField(
        db_column='CertifiedByEmail', max_length=100)
    # Field name made lowercase.
    certifiedbyname = models.CharField(
        db_column='CertifiedByName', max_length=100)
    # Field name made lowercase.
    createdbyemail = models.EmailField(
        db_column='CreatedByEmail', max_length=100)

    class Meta:
        managed = False
        db_table = 'VisitRequestDetails'
