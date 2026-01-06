import re
import csv
from collections import Counter

file_path = '_MD/Mythic-Bastionland-Cleaned_v5.md'
output_csv = 'word_counts.csv'

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
