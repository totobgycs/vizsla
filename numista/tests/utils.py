class Consts:

    class __code_base:
        CODE_1 = 'Co1'
        CODE_2 = 'C02'

    class __name_base:
        NAME_1 = 'Name1'
        NAME_2 = 'Name2'

    class __numista_id_base:
        NUMISTA_ID_1 = 1
        NUMISTA_ID_2 = 2

    class __year_base:
        YEAR_1 = 2019
        YEAR_2 = 2020

    class COUNTRY(__code_base, __name_base):
        pass

    class CURRENCY(__numista_id_base, __name_base):
        pass

    class ISSUE(__numista_id_base, __year_base):
        pass

    class COIN(__numista_id_base, __name_base):
        pass

    # region JSON_COIN
    class JSON_COIN(COIN, COUNTRY, CURRENCY, __year_base):

        TITLE = 'Title'
        URL = 'Url'
        TYPE = 'Type'
        VALUE = 'Value'
        SHAPE = 'Shape'
        COMPOSITION = 'Composition'
        WEIGHT = 10.5
        SIZE = 29
        THICKNESS = 1.3
        OBVERSE_PICTURE = 'Obverse picture'
        OBVERSE_THUMBNAIL = 'Obverse thumbnail'
        REVERSE_PICTURE = 'Reverse picture'
        REVERSE_THUMBNAIL = 'Reverse thumbnail'

        VIZSLA_ID = 179241

        @classmethod
        def init_json(cls):
            cls.COIN_JSON_MINIMAL_1 = {
                "id": cls.NUMISTA_ID_1,
                "title": cls.TITLE
            }
            cls.COIN_JSON_MINIMAL_2 = {
                "id": cls.NUMISTA_ID_2,
                "title": cls.TITLE
            }
            cls.COIN_JSON = {
                "id": cls.NUMISTA_ID_1,
                "url": cls.URL,
                "title": cls.TITLE,
                "country": {
                    "code": cls.CODE_1,
                    "name": cls.NAME_1
                },
                "minYear": cls.YEAR_1,
                "maxYear": cls.YEAR_2,
                "type": cls.TYPE,
                "value": {
                    "text": cls.VALUE,
                    "currency": {
                        "id": cls.NUMISTA_ID_2,
                        "name": cls.NAME_2
                    }
                },
                "shape": cls.SHAPE,
                "composition": {
                    "text": cls.COMPOSITION
                },
                "weight": cls.WEIGHT,
                "size": cls.SIZE,
                "obverse": {
                    "picture": cls.OBVERSE_PICTURE,
                    "thumbnail": cls.OBVERSE_THUMBNAIL
                },
                "reverse": {
                    "picture": cls.REVERSE_PICTURE,
                    "thumbnail": cls.REVERSE_THUMBNAIL
                }
            }
            cls.COIN_JSON_NO_COUNTRY = {
                "id": cls.NUMISTA_ID_1,
                "url": cls.URL,
                "title": cls.TITLE,
                "minYear": cls.YEAR_1,
                "maxYear": cls.YEAR_2,
                "type": cls.TYPE,
                "value": {
                    "text": cls.VALUE,
                    "currency": {
                        "id": cls.NUMISTA_ID_2,
                        "name": cls.NAME_2
                    }
                },
                "shape": cls.SHAPE,
                "composition": {
                    "text": cls.COMPOSITION
                },
                "weight": cls.WEIGHT,
                "size": cls.SIZE,
                "obverse": {
                    "picture": cls.OBVERSE_PICTURE,
                    "thumbnail": cls.OBVERSE_THUMBNAIL
                },
                "reverse": {
                    "picture": cls.REVERSE_PICTURE,
                    "thumbnail": cls.REVERSE_THUMBNAIL
                }
            }
            cls.COIN_JSON_VALUE_NO_CURRENCY = {
                "id": cls.NUMISTA_ID_1,
                "url": cls.URL,
                "title": cls.TITLE,
                "country": {
                    "code": cls.CODE_1,
                    "name": cls.NAME_1
                },
                "minYear": cls.YEAR_1,
                "maxYear": cls.YEAR_2,
                "type": cls.TYPE,
                "value": {
                    "text": cls.VALUE,
                },
                "shape": cls.SHAPE,
                "composition": {
                    "text": cls.COMPOSITION
                },
                "weight": cls.WEIGHT,
                "size": cls.SIZE,
                "obverse": {
                    "picture": cls.OBVERSE_PICTURE,
                    "thumbnail": cls.OBVERSE_THUMBNAIL
                },
                "reverse": {
                    "picture": cls.REVERSE_PICTURE,
                    "thumbnail": cls.REVERSE_THUMBNAIL
                }
            }
            cls.COIN_JSON_NO_VALUE = {
                "id": cls.NUMISTA_ID_1,
                "url": cls.URL,
                "title": cls.TITLE,
                "country": {
                    "code": cls.CODE_1,
                    "name": cls.NAME_1
                },
                "minYear": cls.YEAR_1,
                "maxYear": cls.YEAR_2,
                "type": cls.TYPE,
                "shape": cls.SHAPE,
                "composition": {
                    "text": cls.COMPOSITION
                },
                "weight": cls.WEIGHT,
                "size": cls.SIZE,
                'thickness': cls.THICKNESS,
                "obverse": {
                    "picture": cls.OBVERSE_PICTURE,
                    "thumbnail": cls.OBVERSE_THUMBNAIL
                },
                "reverse": {
                    "picture": cls.REVERSE_PICTURE,
                    "thumbnail": cls.REVERSE_THUMBNAIL
                }
            }

        @classmethod
        def init_vizsla(cls):
            cls.VIZSLA_JSON = {
                "id": 179241,
                "url": "https://en.numista.com/catalogue/pieces179241.html",
                "title": "2000 Forint (Hungarian Vizsla)",
                "country": {
                    "code": "hongrie",
                    "name": "Hungary"
                },
                "minYear": 2019,
                "maxYear": 2019,
                "type": "Non-circulating coin",
                "value": {
                    "text": "2000 Forint",
                    "currency": {
                        "id": 71,
                        "name": "Forint"
                    }
                },
                "shape": "Round",
                "composition": {
                    "text": "Nickel silver (75%copper, 4%nickel, 21%zinc)"
                },
                "weight": 16,
                "size": 34,
                "obverse": {
                    "picture": "https://en.numista.com/catalogue/photos/hongrie/4118-original.jpg",
                    "thumbnail": "https://en.numista.com/catalogue/photos/hongrie/4118-180.jpg"
                },
                "reverse": {
                    "picture": "https://en.numista.com/catalogue/photos/hongrie/4119-original.jpg",
                    "thumbnail": "https://en.numista.com/catalogue/photos/hongrie/4119-180.jpg"
                }
            }

            import json
            cls.VIZSLA_TEXT = json.dumps(cls.VIZSLA_JSON)

    # as there are no class constructors we have to call the initialisation *after* the class is defined.
    JSON_COIN.init_json()
    JSON_COIN.init_vizsla()

    # endregion

    # region JSON_ISSUE
    class JSON_ISSUE(ISSUE, __year_base):

    # numistaId = models.IntegerField(unique=True)
    # numistaId.json_id = 'id'
    # isDated = models.BooleanField()
    # year = models.IntegerField()
    # calendar = models.CharField(max_length=200)
    # gregorianYear = models.IntegerField(null=True)
    # minYear = models.IntegerField(null=True)
    # maxYear = models.IntegerField(null=True)
    # mintLetter = models.CharField(max_length=20)
    # comment = models.TextField()

        MAX_YEAR_1 = 2010
        MIN_YEAR_1 = 2009
        MAX_YEAR_2 = 2008
        MIN_YEAR_2 = 2007
        MINT_LETTER_1 = 'B'
        MINT_LETTER_2 = 'D'
        COMMENT_1 = '(fr) Coincard'
        COMMENT_2 = 'BU'

        @classmethod
        def init_json(cls):
            cls.ISSUE_JSON_MINIMAL = {
                    "id": cls.NUMISTA_ID_1,
                    "isDated": True,
                    "year": cls.YEAR_1,
            }
            
            cls.ISSUE_JSON_FULL = {
                    "id": cls.NUMISTA_ID_1,
                    "isDated": True,
                    "year": cls.YEAR_1,
                    "calendar": "Gregorian",
                    "gregorianYear": cls.YEAR_2,
                    "minYear": cls.MIN_YEAR_1,
                    "maxYear": cls.MAX_YEAR_1,
                    "mintLetter": cls.MINT_LETTER_1,
                    "comment": "(fr) Coincard"
                }

            cls.ISSUE_JSON_NO_MINMAX = {
                    "id": cls.NUMISTA_ID_2,
                    "isDated": True,
                    "year": cls.YEAR_2,
                    "calendar": "Gregorian",
                    "gregorianYear": cls.YEAR_1,
                    "comment": cls.COMMENT_2
                }
            
            cls.ONE_ISSUE_JSON = [cls.ISSUE_JSON_MINIMAL]
            cls.TWO_ISSUES_JSON = [cls.ISSUE_JSON_FULL, cls.ISSUE_JSON_NO_MINMAX]

    JSON_ISSUE.init_json()

    # endregion

class RunOnce:
    def __init__(self, func):
        self.func = func
        self.ran = False

    def __call__(self, *args):
        if not self.ran:
            self.func(*args)
            self.ran = True
