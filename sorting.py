# is order in a hash table guaranteed? - NO
# has table scrambles keys to unpredictable indices


# goal - sort the dictionary by the keys
d = {
  "foo": 1,
  "bar": 99,
  "qux": 42,
}

# cant sor a dictionary
# but we can sort a list - make it into a list


for pair in d.items():
  print(pair)

dict_list = list(d.items())
dict_list.sort(reverse=True) # reveres=True makes it backwards / optional
print(dict_list)


# or sorted(dict_list - return a new list, not mutate the old list in place)

# how do we sort by value, not by key? - Lambda 
dict_list.sort(key=lambda pair: pair[1])

# sort decending by value using
dict_list.sort(key=lambda pair: pair[1], reverse = True)