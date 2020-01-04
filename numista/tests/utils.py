class Consts:
    COUNTRY_NAME_1='CON1'
    COUNTRY_CODE_1='COC1'

    COUNTRY_NAME_2='CON2'
    COUNTRY_CODE_2='COC2'

    CURRENCY_NAME_1='CUN1'
    CURRENCY_CODE_1=1

    CURRENCY_NAME_2='CUN2'
    CURRENCY_CODE_2=2


class RunOnce:
    def __init__(self, func):
        self.func = func
        self.ran = False

    def __call__(self, *args):
        if not self.ran:
            self.func(*args)
            self.ran = True
