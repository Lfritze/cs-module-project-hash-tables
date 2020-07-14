

def letter_count(string):
  counts = {}

  for char in string:
    if char.isalpha():
      if char in counts:
        counts[char] += 1

      else:
        counts[char] = 1
  
  return counts

# stage 2 initiate sorting phase
## print them all, but start with the key that occurs the most often
# only accept alphabet letters, and ensure they are lowercase

def print_sorted_letter_count(string):
  letters = letter_count(string)
  letter_list = list(letters.items())
  letter_list.sort(key=lambda pair: pair[1], reverse=True)

  for pair in letter_list:
    print(f'Letter: {pair[0]} count is {pair[1]}')

print(letter_count('Hello!'))
print(letter_count('Hello the mann is not that great'))