alphabet = "abcdefghijklmnopqrstuvwxyz"
wordlist = []
letter_used_counts = {l: 0 for l in alphabet}
letter_in_position = {i: {l: 0 for l in alphabet} for i in range(5)}

# Note: you can use any source of dictionary words that you'd like,
# but linux comes with Webster's Second International Dictionary
# I generated my words.txt with:
# cat /usr/share/dict/web2 /usr/share/dict/propernames | sort | uniq -c | grep -v 2 | awk "{$1=1};1" | cut -f 2 -d ' '
# to combine the "all words" list with the "proper nouns" list, remove the duplicates, and re-isolate the word part
with open("words.txt") as file:
    for line in file:
        word = line.strip().lower()
        if len(word) == 5:
            wordlist.append(word)
            for letter in set(word):
                letter_used_counts[letter] += 1
            for i, letter in enumerate(word):
                letter_in_position[i][letter] += 1

yellow_scores = {}
green_scores = {}
for word in wordlist:
    yellow_scores[word] = 0
    green_scores[word] = 0
    for letter in set(word):
        yellow_scores[word] += letter_used_counts[letter]
    for i, letter in enumerate(word):
        green_scores[word] += letter_in_position[i][letter]

print(f"Valid 5-letter words: {len(wordlist)}")

best_yellow = max(yellow_scores, key=yellow_scores.get)
print(f"Best Yellow: {best_yellow}; score: {yellow_scores[best_yellow]}")

best_green = max(green_scores, key=green_scores.get)
print(f"Best Green: {best_green}; score: {green_scores[best_green]}")

