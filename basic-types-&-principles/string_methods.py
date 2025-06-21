import re

str = "The BodyGuard"

str_split = (str.split('d'))    # separator is a symbol from the string
print(str_split)

x = "some#words#that#are#separated"
print(x.split('#'))
print(x.split('#', 2))

s1 = "I want to write my own synthesizer"

pattern = r"synth"

res = re.search(pattern, s1)
res_index = s1.find(pattern)

if res:
    print("match found!")
else:
    print("match not found...")

print(type(res), res_index)

#Regular expressions (RegEx) are patterns used to match and manipulate strings of text. There are several special sequences in RegEx that can be used to match specific characters or patterns.
#
#| Special Sequence | Meaning                 | 	Example             |
#| -----------  | ----------------------- | ----------------------|
#| \d    |Matches any digit character (0-9)                                 |"123" matches "\d\d\d"|
#|\D |Matches any non-digit character                                       |"hello" matches "\D\D\D\D\D"|
#|\w |Matches any word character (a-z, A-Z, 0-9, and _)                     |"hello_world" matches "\w\w\w\w\w\w\w\w\w\w\w"|
#|\W |Matches any non-word character                                        |	"@#$%" matches "\W\W\W\W"|
#|\s |Matches any whitespace character (space, tab, newline, etc.)          |"hello world" matches "\w\w\w\w\w\s\w\w\w\w\w"|
#|\S |Matches any non-whitespace character                                  |"hello_world" matches "\S\S\S\S\S\S\S\S\S\S\S"|
#|\b |Matches the boundary between a word character and a non-word character        |"cat" matches "\bcat\b" in "The cat sat on the mat"|
#|\B |Matches any position that is not a word boundary                              |"cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"|

pattern_ = r"\d\d\d\d\d\d\d\d\d\d" # matches any 10 consecutive digits
text = "My first synthesizer were Behringer-1013456789"
match = re.search(pattern_, text)

if match:
    print("Synth model number is:", match.group())
else:
    print("Model not found")

non_word = r"\W"
text = "Hello, Behringer!"
matches = re.findall(non_word, text)

print("Found matches:", matches)

s2 = "My first song that I've made was named\nafter my sister's name 'Lucy'"
res2 = re.findall("st", s2)
print(res2, "of the length:", len(res2))

split_array = re.split(r"\s", s2)
print(split_array, len(split_array))

s3 = r"Dmitry Kovyazin is the best"
replacement = r"Moscow\nlegend"

new_s3 = re.sub("the best", "a "+ replacement + "!", s3, flags=re.IGNORECASE)

print(new_s3)
