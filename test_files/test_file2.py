import copy
import json
import requests
import time
import settings

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
