"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).

You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.

The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".

Example 1:

```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```

Example 2:

```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```

Example 3:

```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```

Notes:

- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""
def are_words_sorted(words, alpha_order):
  alpha_map = {char: ind for ind, char in enumerate(alpha_order)}
  # keep track of whether we've come across any words out of order
  flag = True
  for index in range(1, len(words)):
    if flag == True:
      flag = compareWords(words[index - 1], words[index], alpha_map)
  return flag
def compareWords(word1, word2, char_map):
  least_length = min(len(word1), len(word2))
  print(f'{word1}, {word2}')
  if len(word1) < len(word2) and word1 == word2[:(len(word1))]:
    return True
  if len(word1) > len(word2) and word2 == word1[:(len(word2))]:
    return False
  for ind, char in enumerate(word1[:least_length]):
    # if the chars are in correct alphabetical order
    # return True
    if char_map[word1[ind]] < char_map[word2[ind]]:
      return True
    # if they are in incorrect alphabetical order
    # return False
    if char_map[word1[ind]] > char_map[word2[ind]]:
      return False 
  return True
words = ["abcde", "abcdef", 'abcdefg']
order = "abcdefghijklmnopqrstuvwxyz"
print(are_words_sorted(words, order))

