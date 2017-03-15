word = "mexico"
print sum([1 for ch1,ch2 in zip(word,word[::-1]) if ch1==ch2]) == len(word)
