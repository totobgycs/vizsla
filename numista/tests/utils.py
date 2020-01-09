class Consts:

    class __code_base:
        CODE_1='Co1'
        CODE_2='C02'

    class __name_base:
        NAME_1='Name1'
        NAME_2='Name2'

    class __numista_id_base:
        NUMISTA_ID_1=1
        NUMISTA_ID_2=2

    class __year_base:
        YEAR_1=2019
        YEAR_2=2020

    class COUNTRY(__code_base, __name_base): pass
    class CURRENCY(__numista_id_base, __name_base): pass
    class ISSUE(__numista_id_base, __year_base): pass



class RunOnce:
    def __init__(self, func):
        self.func = func
        self.ran = False

    def __call__(self, *args):
        if not self.ran:
            self.func(*args)
            self.ran = True
