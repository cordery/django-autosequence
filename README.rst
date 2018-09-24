=============================
Django AutoSequence
=============================

.. image:: https://badge.fury.io/py/django-autosequence.png
    :target: https://badge.fury.io/py/django-autosequence

.. image:: https://travis-ci.org/cordery/django-autosequence.png?branch=master
    :target: https://travis-ci.org/cordery/django-autosequence

.. image:: https://codecov.io/gh/cordery/django-autosequence/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/cordery/django-autosequence

A model field for Django that provides for a configurable automatic sequence of values

Documentation
-------------

The full documentation is at https://django-autosequence.readthedocs.org.

Quickstart
----------

Install Django AutoSequence::

    pip install django-autosequence

Add the AutoSequenceField to your models like so::


    class ModelWithStartAt(Model):
        sequence = AutoSequenceField(start_at=100)


    class ModelWithUnique(Model):
        name = CharField(max_length=200)
        sequence = AutoSequenceField(unique_with='name')


    class ModelWithUniqueCombo(Model):
        name = CharField(max_length=200)
        simple_model = ForeignKey(SimpleModel, on_delete=CASCADE)
        sequence = AutoSequenceField(unique_with=('simple_model', 'name'))


Description
--------
AutoSequenceField is an AutoField that is available for non primary keys and can be configured with unique_with to have separate sequences based on other model fields.

For example, say you have a model Invoices that tracks Invoices you have issued to different customers and you would like the invoice number to be autoincrementing but unique for each customer.  You would add a field like::
    class Invoice(models.Model):
        customer = models.ForeignKey('Customer')
        invoice_number = AutoSequenceField(unique_with='customer')

It does this but running a select query against the model to find the highest sequence number for the given set of unique_with fields.  This means that if you delete the last object created, the sequence number of that object will be reused next time you create a new object.

This behavior may be undesirable in some circumstances however in general this field type is intended to be used with models where deletions are infrequent or disabled entirely.

It is non editable and unique, either unique for all rows in the table or unique_with another field or fields in the table.

The following keywords may be passed to AutoSequenceField:

**start_at**: *integer*: the starting number of the sequence, defaults to 1.  Ex:  start_at=100

**unique_with**: *string or tuple of strings*: the name or names of other fields on this model that this sequence will be unique with.  Ex:  unique_with='category'



Running Tests
--------------

Does the code actually work?

::

    $ pip install pipenv
    $ pipenv install -d --three
    $ pytest


Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
