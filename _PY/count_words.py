import re
from collections import Counter

file_path = '_MD/Mythic-Bastionland-Cleaned_v5.md'

omit_words = {
    'the', 'and', 'in', 'a', 'if', 'or', 'yet', 'when', 'are', 'they', 'them', 'do', 'not', 'next', 'from', 'this', 'may', 'lose', 'lost', 'where', 'why',
    'of', 'to', 'is', 'it', 'for', 'with', 'on', 'as', 'by', 'at', 'that', 'which', 'who', 'what', 'how', 'each', 'all', 'any', 'some', 'one', 'two',
    'be', 'has', 'have', 'his', 'her', 'their', 'was', 'were', 'been', 'an', 'but', 'can', 'will', 'your', 'my', 'their', 'our', 'up', 'down', 'out',
    'into', 'than', 'then', 'about', 'more', 'most', 'other', 'only', 'so', 'just', 'more', 'much', 'no', 'yes', 'we', 'us', 'you', 'he', 'she', 'him'
}

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read().lower()

# Remove symbols and split by non-alphanumeric characters
words = re.findall(r'\b[a-z]{2,}\b', text) # only words with 2+ letters

filtered_words = [w for w in words if w not in omit_words]

counts = Counter(filtered_words)

# Sort by count descending
sorted_counts = counts.most_common()

# Print top 200 for brevity or all if requested? User said "all words".
# I'll print them all but if it's too many I might need to paginate.
# Let's see how many unique words there are.
print(f"Unique words: {len(counts)}")
for word, count in sorted_counts:
    print(f"{word}: {count}")
