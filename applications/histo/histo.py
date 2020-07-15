# Your code here
ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

def histogram():
  counts = {}

  with open("robin.txt") as document:
    wording = document.read()
    word_splitter = wording.split()

  for word in word_splitter:
    histo_gramo = ""
    for char in word:
      if char not in ignore:
        histo_gramo += char
    word = histo_gramo.lower()

    if word in counts:
      counts[word] += 1
    elif word == "" or word == " ":
      break
    else:
      counts[word] = 1

    items = list(counts.items())
    items.sort(key = lambda e: (-e[1], e[0]))
    counts = (dict(items))
    for (string, value) in counts.items():
        max_len = len(max(string, key=len))
        print(f'{string} {" " * max_len} {"#" * value}')


print(histogram())


