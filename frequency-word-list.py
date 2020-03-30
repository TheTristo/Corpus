import re
from collections import Counter
text = "We assume you are familiar with Python development and already have some form of Python installed on your system (Python 2.7, Python 3.6/3.7, Anaconda, or others). Screenshots and demos for Ubuntu and Windows are provided. Because Visual Studio Code runs on all major platforms, you may see slightly different UI elements and may need to modify certain commands."

#cleaning
text_re = (re.sub("[\.,\(\)]", "", text))
text_list = text_re.split(" ")
sort_list = sorted(text_list)
pre_frequency = Counter(text_list)
print("\nWORD LIST (alphabetically)")

for a, b in enumerate(sort_list, start=1):
   print(a,b)

print("\nFREQUENCY LIST:")
for value, key in sorted(pre_frequency.items(), key=lambda x: (-x[1], x[0])):    #key=lambda x: (-x[1], x[0])  makes ascending sort
	print(key, value)
