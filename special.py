import string
import collections as ct


special_chars = string.punctuation
sum(m for n, m in ct.Counter(text).items() if n in special_chars)
