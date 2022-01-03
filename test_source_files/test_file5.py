import copy
import json
import requests
import time
import settings


class Myclass(object):
    def __init__(self,name):
        self.name = name

    def classfun1(self,a,b,c):
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


def myfun():
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

a=3

def myfun2(e,a):
    env = settings.env
    base_url = get_url(env)

    # while (base_url is not None):
    env += 1
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





