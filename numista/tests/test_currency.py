from django.test import TestCase
from numista.models import Currency
from numista.tests.utils import Consts
import django.db.utils

class test_numista_model(TestCase):
    databases = {'numista'}

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # FixtureLanguages.init_languages()
        # FixtureMessages.init_messages()
      
    def test_add(self):
        crrcy=Currency(
            numistaId = Consts.CURRENCY.NUMISTA_ID_1,
            name = Consts.CURRENCY.NAME_1
        )
        crrcy.save()

        result=Currency.objects.get(numistaId = Consts.CURRENCY.NUMISTA_ID_1)

        # self.assertEqual(result.count, 1)
        self.assertEqual(result.name, Consts.CURRENCY.NAME_1)
        self.assertEqual(str(result), '{}: {}'.format(Consts.CURRENCY.NUMISTA_ID_1, Consts.CURRENCY.NAME_1))

    def test_add_duplicate_fails(self):
        crrcy=Currency(
            numistaId = Consts.CURRENCY.NUMISTA_ID_1,
            name = Consts.CURRENCY.NAME_1
        )
        crrcy.save()

        crrcy=Currency(
            numistaId = Consts.CURRENCY.NUMISTA_ID_1,
            name = Consts.CURRENCY.NAME_2
        )

        with self.assertRaises(django.db.utils.IntegrityError):
            crrcy.save()

    def test_add_duplicate_name(self):
        crrcy=Currency(
            numistaId = Consts.CURRENCY.NUMISTA_ID_1,
            name = Consts.CURRENCY.NAME_1
        )
        crrcy.save()

        crrcy=Currency(
            numistaId = Consts.CURRENCY.NUMISTA_ID_2,
            name = Consts.CURRENCY.NAME_1
        )
        crrcy.save()

        result = Currency.objects.filter(name = Consts.CURRENCY.NAME_1).all()

        self.assertEqual(result.count(), 2)        

