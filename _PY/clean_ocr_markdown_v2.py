import re
import os

def clean_ocr_markdown_v2(input_file, output_file):
    """
    v2 Cleaning Script:
    - Expanded Regex to catch 'Figure' images and escaped link brackets.
    - Aggressive removal of 'garbage' lines (isolated numbers/symbols).
    - Expanded dictionary for remaining Knight/Quest typos.
    """

    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    print(f"Processing '{input_file}'...")

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    stats = {
        'artifacts_removed': 0,
        'typos_fixed': 0,
        'formatting_updates': 0
    }

    # =========================================================================
    # 1. Advanced Artifact Removal
    # =========================================================================

    artifact_patterns = [
        # Internal PDF Links (Robust):
        # Captures standard [p1]... and escaped [\(p1\)]... variations
        r'\[\\?\(?p\d+\\?\)?\]\(#page-\d+-\d+\)',

        # Wrapped Internal Links:
        r'\(\[p\d+\]\(#page-\d+-\d+\)\)',

        # HTML Spans:
        r'<span id="page-\d+-\d+"></span>',

        # Empty LaTeX Arrays:
        r'\$\\begin\{array\}\{c\}\s*\\end\{array\}\$',

        # Image Tags (Catches both Picture and Figure):
        r'!\[\]\(_page_\d+_(Picture|Figure)_\d+\.jpeg\)',

        # OCR Noise Characters:
        r'[禁张弘姓]',

        # Isolated Page Numbers / Garbage Lines:
        # Matches lines containing only digits, spaces, #, or )
        # Examples caught: "12", "# 1 5", "3 10)", "4 7"
        r'(?m)^[#\s\d\)]+$'
    ]

    for pattern in artifact_patterns:
        content, count = re.subn(pattern, '', content)
        stats['artifacts_removed'] += count

    # Cleanup: Remove excessive newlines
    content = re.sub(r'\n{3,}', '\n\n', content)

    # =========================================================================
    # 2. Expanded Typo Correction
    # =========================================================================

    typo_map = {
        # Previous Fixes
        "Brue Knight": "True Knight",
        "Snarr Knight": "Snare Knight",
        "The Ourney Knight": "The Tourney Knight",
        "Filded Knight": "Gilded Knight",
        "Borde Knight": "Horde Knight",
        "The hain Knight": "The Chain Knight",
        "Brail Knight": "Trail Knight",
        "Stal Knight": "Seal Knight",
        "Burtle Knight": "Turtle Knight",
        "Renight": "Key Knight",
        "Bankard Knight": "Tankard Knight",
        "Wil Knight": "Owl Knight",
        "Booded Knight": "Hooded Knight",
        "Tance Knight": "Lance Knight",
        "Auesting Knight": "Questing Knight",
        "Endgel": "The Cudgel",
        "Procr": "The Order",
        "Pnderworld": "The Underworld",
        "Bower !": "The Tower",
        "Andge": "The Judge",
        "Fron Knight": "Iron Knight",
        "Balo Knight": "Halo Knight",
        "Biger Knight": "Tiger Knight",
        "Teat Knight": "Leaf Knight",
        "Bive Knight": "Hive Knight",
        "Aull Knight": "Gull Knight",

        # NEW Fixes identified in review
        "Bome Knight": "Tome Knight",
        "Relignary Knight": "Reliquary Knight",
        "Choul Knight": "Ghoul Knight",
        "Dobe Knight": "Dove Knight",
        "Hallows Knight": "Gallows Knight",
        "Kazer Knight": "Gazer Knight",
        "Eity Auest": "City Quest",
        "Apon": "Upon",
        "Poble rest": "Noble rest",
        "ofust": "of dust"
    }

    for typo, correction in typo_map.items():
        # Case-insensitive replacement for robustness
        pattern = re.compile(re.escape(typo), re.IGNORECASE)
        content, count = pattern.subn(correction, content)
        if count > 0:
            stats['typos_fixed'] += count

    # =========================================================================
    # 3. Formatting Standardization
    # =========================================================================

    # Stats: VIG _, CLA _, SPI _, _GD -> Blockquote
    stats_pattern = r'(?m)^(.*VIG \d+, CLA \d+, SPI \d+, \d+GD.*)$'
    content, count_stats = re.subn(stats_pattern, r'> \1', content)
    stats['formatting_updates'] += count_stats

    # Spark Tables: Consolidate lines with tildes
    spark_pattern = r'(?m)(\*\*.*?\*\*:.*?)\s*~\s*(\*\*.*?\*\*:.*?)'
    content, count_spark = re.subn(spark_pattern, r'\1 ~ \2', content)
    stats['formatting_updates'] += count_spark

    # =========================================================================
    # Output
    # =========================================================================

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print("-" * 30)
    print("Cleaning Complete (v2).")
    print("-" * 30)
    print(f"Artifacts Removed:   {stats['artifacts_removed']}")
    print(f"Typos Corrected:     {stats['typos_fixed']}")
    print(f"Formatting Updates:  {stats['formatting_updates']}")
    print(f"Output saved to:     {output_file}")
    print("-" * 30)

# Example Usage:
# clean_ocr_markdown_v2('Mythic-Bastionland-Cleaned.md', 'Mythic-Bastionland-Final.md')