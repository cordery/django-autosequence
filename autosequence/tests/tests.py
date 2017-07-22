# coding: utf-8
from django.test import TestCase

from autosequence.tests.models import SimpleModel, ModelWithStartAt, ModelWithUnique, \
    ModelWithUniqueCombo


class AutoSequenceFieldTestCase(TestCase):
    def test_simple_model(self):
        a = SimpleModel()
        a.save()
        self.assertEqual(a.sequence, 1)
        a.save()
        self.assertEqual(a.sequence, 1)

        b = SimpleModel()
        b.save()
        self.assertEqual(b.sequence, 2)
        b.save()
        self.assertEqual(b.sequence, 2)

    def test_delete_simple_model(self):
        a = SimpleModel()
        a.save()

        b = SimpleModel()
        b.save()
        b.delete()

        c = SimpleModel()
        c.save()
        self.assertEqual(c.sequence, 2)
        c.save()
        self.assertEqual(c.sequence, 2)

    def test_starts_at(self):
        a = ModelWithStartAt()
        a.save()
        self.assertEqual(a.sequence, 100)
        a.save()
        self.assertEqual(a.sequence, 100)

        b = ModelWithStartAt()
        b.save()
        self.assertEqual(b.sequence, 101)
        b.save()
        self.assertEqual(b.sequence, 101)

    def test_unique(self):
        name1 = 'testName1'
        name2 = 'testName2'

        a = ModelWithUnique(name=name1)
        a.save()
        self.assertEqual(a.sequence, 1)
        a.save()
        self.assertEqual(a.sequence, 1)

        b = ModelWithUnique(name=name1)
        b.save()
        self.assertEqual(b.sequence, 2)
        b.save()
        self.assertEqual(b.sequence, 2)

        c = ModelWithUnique(name=name2)
        c.save()
        self.assertEqual(c.sequence, 1)
        c.save()
        self.assertEqual(c.sequence, 1)

        d = ModelWithUnique(name=name2)
        d.save()
        self.assertEqual(d.sequence, 2)
        d.save()
        self.assertEqual(d.sequence, 2)

    def test_unique_combo(self):
        simple1 = SimpleModel()
        simple1.save()

        simple2 = SimpleModel()
        simple2.save()

        name1 = 'testName1'
        name2 = 'testName2'

        a = ModelWithUniqueCombo(name=name1, simple_model=simple1)
        a.save()
        self.assertEqual(a.sequence, 1)
        a.save()
        self.assertEqual(a.sequence, 1)

        b = ModelWithUniqueCombo(name=name1, simple_model=simple2)
        b.save()
        self.assertEqual(b.sequence, 1)
        b.save()
        self.assertEqual(b.sequence, 1)

        c = ModelWithUniqueCombo(name=name2, simple_model=simple1)
        c.save()
        self.assertEqual(c.sequence, 1)
        c.save()
        self.assertEqual(c.sequence, 1)

        d = ModelWithUniqueCombo(name=name2, simple_model=simple2)
        d.save()
        self.assertEqual(d.sequence, 1)
        d.save()
        self.assertEqual(d.sequence, 1)
