from collections import Counter 
def anagrams(s1, s2):
  #return sorted(s1) == sorted(s2)
  return Counter(s1) == Counter(s2)