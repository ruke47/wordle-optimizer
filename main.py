alphabet = "abcdefghijklmnopqrstuvwxyz"
wordlist = []
letter_used_counts = {l: 0 for l in alphabet}
letter_in_position = {i: {l: 0 for l in alphabet} for i in range(5)}

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

best_yellow_score = max(yellow_scores.values())
tied_yellow = [word for word, score in yellow_scores.items() if score == best_yellow_score]
best_yellow = max(tied_yellow, key=lambda word: green_scores[word])

print(f"Best Yellow: {best_yellow}\n\t score: y={yellow_scores[best_yellow]}, g={green_scores[best_yellow]}")

best_green_score = max(green_scores.values())
tied_green = [word for word, score in green_scores.items() if score == best_green_score]
best_green = max(tied_green, key=lambda word: yellow_scores[word])

print(f"Best Green: {best_green}\n\t score: g={green_scores[best_green]}, y={yellow_scores[best_green]}")