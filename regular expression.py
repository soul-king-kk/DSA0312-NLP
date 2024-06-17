import re
text = "Regular expression are a powerful tool for text processing.They can be used for pattern matching,tokenization,and more."
word_pattern=r'\w+'
words=re.findall(word_pattern,text)
print(words)
