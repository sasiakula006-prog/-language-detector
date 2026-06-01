import os
import string
from collections import defaultdict


# Lowercase conversion
def to_lower(s):
    return s.lower()


# Tokenize input string
def tokenize(line):
    words = []
    for word in line.split():
        word = word.translate(str.maketrans('', '', string.punctuation))
        if len(word) > 1:
            words.append(to_lower(word))
    return words


# Levenshtein Distance (DP)
def edit_distance(a, b):
    m, n = len(a), len(b)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # deletion
                    dp[i][j - 1],      # insertion
                    dp[i - 1][j - 1]   # substitution
                )

    return dp[m][n]


# Load all dictionaries from directory
def load_dictionaries(directory):
    lang_dict = {}

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            lang_name = filename[:-4]  # remove .txt

            word_freq = {}

            filepath = os.path.join(directory, filename)

            with open(filepath, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.split()

                    if len(parts) >= 2:
                        word = parts[0].lower()
                        freq = int(parts[1])

                        word_freq[word] = freq

            lang_dict[lang_name] = word_freq

    return lang_dict


# Detect language of input string
def detect_language(text, lang_dict):
    input_words = tokenize(text)

    scores = defaultdict(int)

    for word in input_words:

        for lang, dictionary in lang_dict.items():

            if word in dictionary:
                # Exact match boost
                scores[lang] += 10 + dictionary[word]

            else:
                # Try edit distance up to 2
                best_dist = 3

                for dict_word, freq in dictionary.items():

                    dist = edit_distance(word, dict_word)

                    if dist <= 2 and dist < best_dist:
                        scores[lang] += 3 - dist
                        best_dist = dist

    if not scores:
        return "Unknown"

    return max(scores, key=scores.get)


def main():
    print("Loading language dictionaries...")

    print(os.getcwd())

    lang_dict = load_dictionaries("dictionaries")

    print(f"Loaded {len(lang_dict)} languages.")

    user_input = input("Enter a sentence: ")

    detected = detect_language(user_input, lang_dict)

    print(f"\nDetected Language: {detected}")


if __name__ == "__main__":
    main()