import random
import json

def handle(data):
  ss_password = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(22))
  ss_password = json.dumps({"ss_password": ss_password})

  return ss_password
