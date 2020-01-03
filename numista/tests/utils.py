class Consts:
    COUNTRY_NAME_1='CN1'
    COUNTRY_CODE_1='CC1'

    COUNTRY_NAME_2='CN2'
    COUNTRY_CODE_2='CC2'


class RunOnce:
    def __init__(self, func):
        self.func = func
        self.ran = False

    def __call__(self, *args):
        if not self.ran:
            self.func(*args)
            self.ran = True
