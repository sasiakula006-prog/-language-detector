# Language Detector

A Python-based language detection tool that uses dictionary matching and edit distance algorithms to identify the language of input text.

## Features

- **Multi-language Support**: Detects languages based on dictionary files in the `dictionaries/` directory
- **Fuzzy Matching**: Uses Levenshtein distance (edit distance) to handle misspellings and variations
- **Frequency-based Scoring**: Weights words by their frequency in each language dictionary
- **Fast Performance**: Efficient DP-based edit distance calculation

## How It Works

The detector uses a three-tier matching strategy:

1. **Exact Match**: If a word exists in a language dictionary, it receives a high score (10 + word frequency)
2. **Fuzzy Match**: If no exact match is found, the algorithm checks for similar words within edit distance of 2
3. **Scoring**: The language with the highest cumulative score is returned as the detected language

### Algorithm Details

- **Edit Distance**: Implements Levenshtein distance using dynamic programming to find the minimum number of single-character edits (insertions, deletions, substitutions) needed to transform one word into another
- **Tokenization**: Converts input to lowercase, removes punctuation, and splits into words (minimum 2 characters)
- **Language Scoring**: Each language maintains a score based on word matches found in the input text

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sasiakula006-prog/-language-detector.git
cd -language-detector
```

2. Ensure you have Python 3.6+ installed

3. Create a `dictionaries/` directory and add language dictionary files (see below)

## Usage

### Running the Detector

```bash
python langauge_detect.py
```

The program will prompt you to enter a sentence. It will then detect and display the language:

```
Loading language dictionaries...
/path/to/project
Loaded 3 languages.
Enter a sentence: Hello world
Detected Language: english
```

### Dictionary Format

Dictionary files should be placed in the `dictionaries/` directory with the following format:

**File naming**: `{language_name}.txt` (e.g., `english.txt`, `spanish.txt`, `french.txt`)

**File format**: Each line should contain a word and its frequency, separated by space:
```
word1 150
word2 342
word3 89
...
```

Example structure:
```
dictionaries/
├── english.txt
├── spanish.txt
├── french.txt
└── german.txt
```

## Project Structure

```
-language-detector/
├── README.md
├── langauge_detect.py
└── dictionaries/
    └── (language dictionary files)
```

## API Reference

### `tokenize(line)`
Converts input text to a list of lowercase words with punctuation removed.

**Parameters**: 
- `line` (str): Input text

**Returns**: 
- `list`: List of tokenized words

### `edit_distance(a, b)`
Calculates the Levenshtein distance between two strings using dynamic programming.

**Parameters**:
- `a` (str): First string
- `b` (str): Second string

**Returns**:
- `int`: Minimum edit distance

### `load_dictionaries(directory)`
Loads all language dictionaries from the specified directory.

**Parameters**:
- `directory` (str): Path to dictionaries folder

**Returns**:
- `dict`: Dictionary mapping language names to word-frequency dictionaries

### `detect_language(text, lang_dict)`
Detects the language of the input text.

**Parameters**:
- `text` (str): Input text to analyze
- `lang_dict` (dict): Language dictionaries (from `load_dictionaries()`)

**Returns**:
- `str`: Detected language name or "Unknown" if no match found

## Example

```python
from langauge_detect import load_dictionaries, detect_language

# Load dictionaries
lang_dict = load_dictionaries("dictionaries")

# Detect language
text = "Bonjour le monde"
language = detect_language(text, lang_dict)
print(f"Detected: {language}")  # Output: Detected: french
```

## Performance Notes

- **Time Complexity**: O(n × m × k²) where n is number of input words, m is average dictionary size, and k is average word length
- **Edit Distance**: Uses O(k²) space and time for each word comparison
- **Optimization**: Only checks dictionary words within edit distance ≤ 2 to avoid unnecessary comparisons

## Limitations

- Requires pre-built dictionary files for each language
- May struggle with very short texts or mixed-language inputs
- Accuracy depends on dictionary comprehensiveness and word frequency data quality
- Misspelled words are handled through fuzzy matching but may reduce accuracy

## Future Improvements

- N-gram analysis for better language detection
- Machine learning-based classification
- Support for language confidence scores
- Unicode and special character handling enhancements
- Batch processing capabilities

## License

This project is open source. Feel free to use and modify as needed.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
