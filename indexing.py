# given a list of records, be able to quiclkly report everyone in aparticular category.

records = [
  ("Corey", "iOS"),
  ("Tyler", "DS"),
  ("Anika", "DS"),
  ("Leighton", "web"),
  ("Nico", "web"),
  ("Carl", "web"),
  ("MIchael", "iOS")
]

# for records in records:
#   if redord[1] == 'iOS':

# return [student for student in records if student[1] == 'web]

def build_index(records):
  index = {}

  # loop over records
  for record in (records):
    name, track = record

  # key is track
  # if ke is not in dict, add it
    if track not in index:
      index [track] = []

    index[track].append(name)

  ## value list of names
  return index

index = build_index(records)#prints the keys  
for track in index:
    print(track)

print(index["web"])
print(index["iOS"])

# how to handle updated records
# update index directly
# or loop over records every once in a while and handle de-duplication

# Project Euler
# PRimes cant be divided by another number
# Primes are like atoms of other numbers
# 21: 7 * 3
# 42: 2 * 3 * 7