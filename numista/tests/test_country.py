from django.test import TestCase
from numista.models import Country
from numista.tests.utils import Consts
import django.db.utils


class test_numista_country(TestCase):
    databases = {'numista'}

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_add(self):
        cntry = Country(
            code=Consts.COUNTRY.CODE_1,
            name=Consts.COUNTRY.NAME_1
        )
        cntry.save()

        result = Country.objects.get(code=Consts.COUNTRY.CODE_1)

        # self.assertEqual(result.count, 1)
        self.assertEqual(result.name, Consts.COUNTRY.NAME_1)
        self.assertEqual(str(result), '{}: {}'.format(
            Consts.COUNTRY.CODE_1, Consts.COUNTRY.NAME_1))

    def test_add_duplicate_fails(self):
        cntry = Country(
            code=Consts.COUNTRY.CODE_1,
            name=Consts.COUNTRY.NAME_1
        )
        cntry.save()

        cntry = Country(
            code=Consts.COUNTRY.CODE_1,
            name=Consts.COUNTRY.NAME_2
        )

        with self.assertRaises(django.db.utils.IntegrityError):
            cntry.save()

    def test_add_duplicate_name(self):
        cntry = Country(
            code=Consts.COUNTRY.CODE_1,
            name=Consts.COUNTRY.NAME_1
        )
        cntry.save()

        cntry = Country(
            code=Consts.COUNTRY.CODE_2,
            name=Consts.COUNTRY.NAME_1
        )
        cntry.save()

        result = Country.objects.filter(name=Consts.COUNTRY.NAME_1).all()

        self.assertEqual(result.count(), 2)
