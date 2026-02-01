from nltk import *

REGEX = [r"[A-Za-z]+", # words with only letters
         r"[A-Z][a-z]*", # title case words
         r"\d+(\.\d+)?", # ints and floats
         r"p[aeiou]{,2}t"] # words that start with p and ending in t, with an option to have one or two lowercase vowels in the middle

TEXT = "Check answers in Python 109, 1.09 patch pitch pt piiiit"

for pattern in REGEX:
    re_show(pattern, TEXT)

tk = RegexpTokenizer('(b+(ab)*)*', gaps=True)
print(tk.tokenize("bbabab babab ab aaa ba"))