s = "I Love Python Programming"

split =s.split()
print(split)

s = "aabbc"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
