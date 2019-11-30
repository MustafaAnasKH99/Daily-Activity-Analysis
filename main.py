log_file = open("log.txt", "r+")

chars = 0
lines = 0
letters = []
counted = {}

for i in log_file.read():
    if i == '\n':
        lines += 1
    chars += 1
    letters.append(i)

key_string = "".join(letters)
word_string = key_string.replace('\n', " ")
final_keywords_list = word_string.split()

for letter in final_keywords_list:
    letr = str(letter)
    if letr in counted:
        counted[letr] += 1
    else:
        counted[letr] = 1

print(lines, "Lines", " || ", chars, "Character", " || ", len(final_keywords_list), "Words")
print('\n')
for i in counted:
    print(i, counted[i])
