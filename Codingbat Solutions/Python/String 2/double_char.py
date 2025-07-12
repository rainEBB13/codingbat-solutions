# Link: https://codingbat.com/prob/p170842

def double_char(str):
  # we need to return the string but with every char
  # doubled, so "Hello" becomes "HHeelloo"
  # How do i return double char for string?
  new = ""
  for i in range(len(str)):
    new += str[i] * 2
  return new