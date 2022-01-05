Wordle Optimizer
===

There is a Correct first guess each day for wordle, and I aim to discover it.

See https://www.powerlanguage.co.uk/wordle/

I generated my wordlist from the Webster's Second International dictionary, included in linux/mac in `/usr/share/dict`:

```
cat /usr/share/dict/web2 /usr/share/dict/propernames | sort | uniq -c | grep -v 2 | awk "{$1=1};1" | cut -f 2 -d ' ' > words.txt
```

This will combine the "all words" dictionary with the "proper names" dictionary, sort them, count how many times each word appears, remove any words with duplicates, (clean up any leading whitespace), and then select only the "word" portion of the count+word construct.
