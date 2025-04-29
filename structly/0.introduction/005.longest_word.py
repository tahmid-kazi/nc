def longest_word(sentence):

  arr = sentence.split(" ")
  word1 = ""
  for word in arr:
    if len(word) >= len(word1):
      word1 = word
  return word1