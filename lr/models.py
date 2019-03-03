# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Events(models.Model):
    dateevents = models.DateField(db_column='dateEvents')  # Field name made lowercase.
    nameevent = models.CharField(db_column='nameEvent', max_length=200)  # Field name made lowercase.
    description = models.CharField(max_length=400)
    idlandfillevent = models.ForeignKey('Landfill', models.DO_NOTHING, db_column='idLandfillEvent')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'events'


class Landfill(models.Model):
    location = models.CharField(max_length=500)
    datefind = models.DateField(db_column='dateFind')  # Field name made lowercase.
    datestatement = models.DateField(db_column='dateStatement')  # Field name made lowercase.
    photolocation = models.CharField(db_column='photoLocation', max_length=300)  # Field name made lowercase.
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'landfill'


class Volunteers(models.Model):
    datevolunteers = models.DateField(db_column='dateVolunteers')  # Field name made lowercase.
    countvolunteers = models.IntegerField(db_column='countVolunteers')  # Field name made lowercase.
    description = models.CharField(max_length=500)
    idlandfillvolunt = models.ForeignKey(Landfill, models.DO_NOTHING, db_column='idLandfillVolunt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'volunteers'
