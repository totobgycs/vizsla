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

    class JSON(COIN, COUNTRY, CURRENCY, __year_base):

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
                    "thumbnail": "https://en.numista.com/catalogue/photos/hongrie/4118-135.jpg"
                },
                "reverse": {
                    "picture": "https://en.numista.com/catalogue/photos/hongrie/4119-original.jpg",
                    "thumbnail": "https://en.numista.com/catalogue/photos/hongrie/4119-135.jpg"
                }
            }

            import json
            cls.VIZSLA_TEXT = json.dumps(cls.VIZSLA_JSON)

    # as there are no class constructors we have to call the initialisation *after* the class is defined.
    JSON.init_json()
    JSON.init_vizsla()


class RunOnce:
    def __init__(self, func):
        self.func = func
        self.ran = False

    def __call__(self, *args):
        if not self.ran:
            self.func(*args)
            self.ran = True
