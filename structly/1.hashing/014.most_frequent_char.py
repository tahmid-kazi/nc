from collections import Counter
def most_frequent_char(s):
  char_freq = Counter(s)
  max_key, max_val = "", 0
  for key, val in char_freq.items():
    if val > max_val:
      max_val = val
      max_key = key
  return max_key