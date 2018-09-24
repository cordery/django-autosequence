from django.db import models

from autosequence import AutoSequenceField


class SimpleModel(models.Model):
    sequence = AutoSequenceField()


class ModelWithStartAt(models.Model):
    sequence = AutoSequenceField(start_at=100)


class ModelWithUnique(models.Model):
    name = models.CharField(max_length=200)
    sequence = AutoSequenceField(unique_with='name')


class ModelWithUniqueCombo(models.Model):
    name = models.CharField(max_length=200)
    simple_model = models.ForeignKey(SimpleModel, on_delete=models.CASCADE)
    sequence = AutoSequenceField(unique_with=('simple_model', 'name'))
