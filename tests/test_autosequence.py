# coding: utf-8
import pytest
from django.db import transaction

from tests.models import ModelWithStartAt, ModelWithUnique, ModelWithUniqueCombo, SimpleModel


@pytest.mark.django_db
class TestAutoSequenceField:
    def test_simple_model(self):
        a = SimpleModel()
        a.save()
        assert 1 == a.sequence
        a.save()
        assert 1 == a.sequence

        b = SimpleModel()
        b.save()
        assert 2 == b.sequence
        b.save()
        assert 2 == b.sequence

    def test_delete_simple_model(self):
        a = SimpleModel()
        a.save()

        b = SimpleModel()
        b.save()
        b.delete()

        c = SimpleModel()
        c.save()
        assert 2 == c.sequence
        c.save()
        assert 2 == c.sequence

    def test_starts_at(self):
        a = ModelWithStartAt()
        a.save()
        assert 100 == a.sequence
        a.save()
        assert 100 == a.sequence

        b = ModelWithStartAt()
        b.save()
        assert 101 == b.sequence
        b.save()
        assert 101 == b.sequence

    def test_unique(self):
        name1 = 'testName1'
        name2 = 'testName2'

        a = ModelWithUnique(name=name1)
        a.save()
        assert 1 == a.sequence
        a.save()
        assert 1 == a.sequence

        b = ModelWithUnique(name=name1)
        b.save()
        assert 2 == b.sequence
        b.save()
        assert 2 == b.sequence

        c = ModelWithUnique(name=name2)
        c.save()
        assert 1 == c.sequence
        c.save()
        assert 1 == c.sequence

        d = ModelWithUnique(name=name2)
        d.save()
        assert 2 == d.sequence
        d.save()
        assert 2 == d.sequence

    def test_unique_combo(self):
        simple1 = SimpleModel.objects.create()
        simple2 = SimpleModel.objects.create()
        name1 = 'testName1'
        name2 = 'testName2'

        a = ModelWithUniqueCombo(name=name1, simple_model=simple1)
        a.save()
        assert 1 == a.sequence
        a.save()
        assert 1 == a.sequence

        b = ModelWithUniqueCombo(name=name1, simple_model=simple2)
        b.save()
        assert 1 == b.sequence
        b.save()
        assert 1 == b.sequence

        c = ModelWithUniqueCombo(name=name2, simple_model=simple1)
        c.save()
        assert 1 == c.sequence
        c.save()
        assert 1 == c.sequence

        d = ModelWithUniqueCombo(name=name2, simple_model=simple2)
        d.save()
        assert 1 == d.sequence
        d.save()
        assert 1 == d.sequence


@pytest.mark.django_db(transaction=True)
class TestAutoSequenceFieldTransaction:
    def test_unique_within_transaction(self):
        with transaction.atomic():
            a = SimpleModel()
            a.save()
            b = SimpleModel()
            b.save()
        assert [1, 2] == list(
            SimpleModel.objects.values_list('sequence', flat=True))
