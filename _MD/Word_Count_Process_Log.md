# Word Count Generation Log

This document records the steps and code used to generate the `word_counts.csv` file from `_MD/Mythic-Bastionland-Cleaned_v5.md`.

## Process Overview

1.  **Analyze Request**: The goal was to count word frequencies in the source Markdown file, excluding specific common words (stop words), and output the result to a CSV file.
2.  **Develop Script**: A Python script was written to read the file, normalize text to lowercase, use regex to extract words (ignoring symbols and 1-letter words), filter out the specified stop words, count occurrences, and write the sorted results to a CSV.
3.  **Execution**: The script was executed in the shell.

## Code Used

The following Python code was saved to `create_word_count_csv.py` and executed:

```python
import re
import csv
from collections import Counter

file_path = '_MD/Mythic-Bastionland-Cleaned_v5.md'
output_csv = 'word_counts.csv'

# Set of words to omit from the count
omit_words = {
    'the', 'and', 'in', 'a', 'if', 'or', 'yet', 'when', 'are', 'they', 'them', 'do', 'not', 'next', 'from', 'this', 'may', 'lose', 'lost', 'where', 'why',
    'of', 'to', 'is', 'it', 'for', 'with', 'on', 'as', 'by', 'at', 'that', 'which', 'who', 'what', 'how', 'each', 'all', 'any', 'some', 'one', 'two',
    'be', 'has', 'have', 'his', 'her', 'their', 'was', 'were', 'been', 'an', 'but', 'can', 'will', 'your', 'my', 'their', 'our', 'up', 'down', 'out',
    'into', 'than', 'then', 'about', 'more', 'most', 'other', 'only', 'so', 'just', 'more', 'much', 'no', 'yes', 'we', 'us', 'you', 'he', 'she', 'him'
}

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()

    # Remove symbols and split by non-alphanumeric characters, keeping only words with 2+ letters
    words = re.findall(r'\b[a-z]{2,}\b', text)

    filtered_words = [w for w in words if w not in omit_words]

    counts = Counter(filtered_words)

    # Sort by count descending
    sorted_counts = counts.most_common()

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Count'])
        writer.writerows(sorted_counts)

    print(f"Successfully wrote {len(sorted_counts)} unique words to {output_csv}")

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Execution Command

The script was run using the following command:

```bash
python create_word_count_csv.py
```

## Output

The script successfully created `word_counts.csv` containing 7,094 unique words.
