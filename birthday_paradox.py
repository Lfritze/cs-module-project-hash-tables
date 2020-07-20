import random
import hashlib

def hash_function(random_key):
  return int(hashlib.sha256(f'{random_key}'.encode()).hexdigest(), 16)

def how_many_before_collision(number_of_buckets):
  # make random keys
  tried = set()
  number_tries = 0

  while True:
    random_key = random.random()
    hashed_key = hash_function(random_key) % number_of_buckets 

    if hashed_key not in tried:
      tried.add(hashed_key)
      number_tries +=1
    else:
      break
  return number_tries

print(how_many_before_collision(4))
print(how_many_before_collision(512))
print(how_many_before_collision(1024))