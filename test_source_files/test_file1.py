class MyClass(object):
    def __init__(self,name):
        self.name = name

    def classfun1(self,a):
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




import copy
import json
import requests
import time
import settings

def myfun():
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