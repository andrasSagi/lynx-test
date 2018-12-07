def _find(data, key):
  counter = 0
  for i in data:
    if i == key:
      return counter
    else:
      counter++
  return -1

threshold = 10


def find(data, key):
  half = len(data) / 2
  data_frst = data[0:half]
  data_second = data[half:]

  if len(data) <= threshold:
    return find(data, key)
  elif key < data[half]:
    return find(data_first, key)
  else:
    return find(data_second, key)


# Indentation is two space instead of four
# Function names are too similar
# I don't exactly understand what use the first function has
# There is no ++ increment operator in Python 3.7
# Threshold variable is redundant, if it's a global constant then it is in the wrong place and should be capitalized
# half won't always be an integer
# data_first variable is misspelled on line 15
# Specifying zero index as starting point is redundant too
# Second function doesn't return values and  will loop forever
# Conditional is not meaningful