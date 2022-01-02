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