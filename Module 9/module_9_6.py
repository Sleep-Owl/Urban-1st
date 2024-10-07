def all_variants(text):
  lenght = len(text)
  for i in range(lenght + 1):
    for j in range(i + 1, lenght + 1):
      yield text[i:j]


a = all_variants("abc")
for i in a:
  print(i)
