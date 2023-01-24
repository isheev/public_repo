import random, string, json

def handle(data):
  random_string = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(22))
  random_string = json.dumps({"random_string": random_string})
  return random_string
