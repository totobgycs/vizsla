from django.test import TestCase
from numista.models import Country
from numista.tests.utils import Consts
import django.db.utils

class test_numista_model(TestCase):
    databases = {'numista'}

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # FixtureLanguages.init_languages()
        # FixtureMessages.init_messages()

      
    def test_add_country(self):
        cntry=Country(
            code = Consts.COUNTRY_CODE_1,
            name = Consts.COUNTRY_NAME_1
        )
        cntry.save()

        result=Country.objects.get(code = Consts.COUNTRY_CODE_1)

        # self.assertEqual(result.count, 1)
        self.assertEqual(result.name, Consts.COUNTRY_NAME_1)

    def test_add_duplicate_country_fails(self):
        cntry=Country(
            code = Consts.COUNTRY_CODE_1,
            name = Consts.COUNTRY_NAME_1
        )
        cntry.save()

        cntry=Country(
            code = Consts.COUNTRY_CODE_1,
            name = Consts.COUNTRY_NAME_1
        )

        with self.assertRaises(django.db.utils.IntegrityError):
            cntry.save()

    def test_add_duplicate_country_name(self):
        cntry=Country(
            code = Consts.COUNTRY_CODE_1,
            name = Consts.COUNTRY_NAME_1
        )
        cntry.save()

        cntry=Country(
            code = Consts.COUNTRY_CODE_2,
            name = Consts.COUNTRY_NAME_1
        )
        cntry.save()

        result = Country.objects.filter(name = Consts.COUNTRY_NAME_1).all()

        self.assertEqual(result.count(), 2)        