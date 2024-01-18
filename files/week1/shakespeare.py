from urllib.request import urlopen

# no such address
# shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')

shakespeare = urlopen("https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt")
print(shakespeare)

words = set(shakespeare.read().decode().split())
print("Length of words ->", len(words))

subset = {w for w in words if len(w) == 6 and w[::-1] in words}
print(subset)
