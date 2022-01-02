import copy
import json
import requests
import time
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





