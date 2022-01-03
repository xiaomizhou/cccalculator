import unittest

from cccalculator.cccalculate.calculate import do_calculate_from_code

if_else = """
def myfun():
    import settings
    env = settings.env
    base_url = get_url(env)
    if base_url == 'eeee':
        print(33333)
    elif base_url == 'rrrrrrrrrrr':
        print(3456)
    elif base_url == 'dddddddd':
        print(678776)
    elif base_url == 'aaaaaaaaa':
        print(678987656789)
"""

while_statement = """
def myfun():
    import settings
    env = settings.env
    base_url = get_url(env)
    while base_url is not None:
        if base_url == 'eeee':
            print(33333)
        elif base_url == 'rrrrrrrrrrr':
            print(3456)
        elif base_url == 'dddddddd':
            print(678776)
        elif base_url == 'aaaaaaaaa':
            print(678987656789)
        else:
            print(66666)
        env += 1
        base_url = get_url(env)
"""

try_catch = """
def myfun():
    import settings
    import Exception1,Exception2
    env = settings.env
    base_url = get_url(env)
    try:
        a = base_url.name
    except Exception1 as e:
        print(str(e))
    except Exceptio2 as e:
        print(1111)
    else:
        print(33333)
"""

for_loop = """
def myfun():
    import settings
    env_list = settings.ENV
    for env in env_list:
        base_url = get_url(env)
        if base_url == 'eeee':
            print(33333)
        elif base_url == 'rrrrrrrrrrr':
            print(3456)
        elif base_url == 'dddddddd':
            print(678776)
        elif base_url == 'aaaaaaaaa':
            print(678987656789)
        else:
            print(11111)
"""

recursive_statement = """
def myfun():
    import settings
    env_list = settings.ENV
    try:
        for env in env_list:
            base_url = get_url(env)
            if base_url == 'eeee':
                print(33333)
            elif base_url == 'rrrrrrrrrrr':
                print(3456)
            elif base_url == 'dddddddd':
                print(678776)
            else:
                print(11111)
    except Exception1 as e:
        print(str(e))
    except Exceptio2 as e:
        print(1111)
"""

multiple_fun_statement = """
def myfun1():
    import settings
    env_list = settings.ENV
    try:
        for env in env_list:
            base_url = get_url(env)
            if base_url == 'eeee':
                print(33333)
            elif base_url == 'rrrrrrrrrrr':
                print(3456)
            elif base_url == 'dddddddd':
                print(678776)
            else:
                print(11111)
    except Exception1 as e:
        print(str(e))
    except Exceptio2 as e:
        print(1111)

rcache = Redis()
        
def myfun():
    import settings
    env_list = settings.ENV
    for env in env_list:
        base_url = get_url(env)
        if base_url == 'eeee':
            print(33333)
        elif base_url == 'rrrrrrrrrrr':
            print(3456)
        elif base_url == 'dddddddd':
            print(678776)
        elif base_url == 'aaaaaaaaa':
            print(678987656789)
        else:
            print(11111)
"""


class Test_cccalculator(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_if_else(self):
        cc_complex = do_calculate_from_code(if_else)
        self.assertEqual(cc_complex, [5])

    def test_while_statement(self):
        cc_complex = do_calculate_from_code(while_statement)
        self.assertEqual(cc_complex, [6])

    def test_try_catch(self):
        cc_complex = do_calculate_from_code(try_catch)
        self.assertEqual(cc_complex, [3])

    def test_for_loop(self):
        cc_complex = do_calculate_from_code(for_loop)
        self.assertEqual(cc_complex, [6])

    def test_recursive_statement(self):
        cc_complex = do_calculate_from_code(recursive_statement)
        self.assertEqual(cc_complex, [7])

    def test_multiple_def(self):
        cc_complex = do_calculate_from_code(multiple_fun_statement)
        self.assertEqual(cc_complex, [7,6])


if __name__ == '__main__':
    unittest.main()