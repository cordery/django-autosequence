========
Usage
========

To use the AutoSequenceField in your models::

    from autosequence import AutoSequenceField

    class ModelWithStartAt(Model):
        sequence = AutoSequenceField(start_at=100)


    class ModelWithUnique(Model):
        name = CharField(max_length=200)
        sequence = AutoSequenceField(unique_with='name')


    class ModelWithUniqueCombo(Model):
        name = CharField(max_length=200)
        simple_model = ForeignKey(SimpleModel, on_delete=CASCADE)
        sequence = AutoSequenceField(unique_with=('simple_model', 'name'))
