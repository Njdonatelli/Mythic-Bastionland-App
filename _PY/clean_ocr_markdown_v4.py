import re
import os

def clean_ocr_markdown_v3(input_file, output_file):
    """
    Reads a raw OCR Markdown file, cleans artifacts, corrects typos, 
    standardizes formatting, and writes to a new file.
    """
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    print(f"Processing '{input_file}'...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tracking changes for the summary
    stats = {
        'artifacts_removed': 0,
        'typos_fixed': 0,
        'formatting_updates': 0
    }

    # =========================================================================
    # 1. Artifact Removal (Regex)
    # =========================================================================
    
    # Patterns to remove entirely
    artifact_patterns = [
        # Internal PDF Links: matches [p16](#page-15-0), [\(p10\)](#page-9-0)
        # CHANGED: Uses [^\]]* instead of .* to prevent greedy matching deleting valid text
        r'\[[^\]]*p\d+[^\]]*\]\(#page-\d+-\d+\)',
        
        # Wrapped Internal Links: matches ([p17](#page-16-0))
        # CHANGED: Uses [^\]]* for safety
        r'\(\[[^\]]*p\d+[^\]]*\]\(#page-\d+-\d+\)\)',
        
        # HTML Spans: <span id="page-21-0"></span>
        r'<span id="page-\d+-\d+"></span>',
        
        # Empty LaTeX Arrays: $\begin{array}{c} \end{array}$
        r'\$\\begin\{array\}\{c\}\s*\\end\{array\}\$',
        
        # Image Tags: ![](_page_19_Picture_32.jpeg) OR ![](_page_106_Figure_0.jpeg)
        # Matches both "Picture" and "Figure"
        r'!\[\]\(_page_\d+_(?:Picture|Figure)_\d+\.jpeg\)',
        
        # OCR Noise Characters: 禁, 张, 弘, 姓
        r'[禁张弘姓]',
        
        # Fragmented Headers & Page Numbers: 
        # Removes lines containing ONLY digits, spaces, hashes (#), or closing parentheses )
        r'(?m)^[\s\d#\)]+$'
    ]

    for pattern in artifact_patterns:
        # subn returns a tuple (new_string, number_of_subs)
        content, count = re.subn(pattern, '', content)
        stats['artifacts_removed'] += count

    # Cleanup: Remove excessive newlines created by deleting whole lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    # =========================================================================
    # 2. Typo Correction (Dictionary Mapping)
    # =========================================================================
    
    typo_map = {
        # Original Typos
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
        
        # New Typos (Added in V2)
        "Bome Knight": "Tome Knight",
        "Relignary Knight": "Reliquary Knight",
        "Choul Knight": "Ghoul Knight",
        "Dobe Knight": "Dove Knight",
        "Hallows Knight": "Gallows Knight",
        "Kazer Knight": "Gazer Knight",
        "Eity Auest": "City Quest"
    }

    for typo, correction in typo_map.items():
        # Using re.escape to ensure the typo string is treated literally
        pattern = re.escape(typo)
        content, count = re.subn(pattern, correction, content)
        stats['typos_fixed'] += count

    # =========================================================================
    # 3. Formatting Standardization
    # =========================================================================

    # Stats Formatting
    # Identify lines like: VIG 10, CLA 12, SPI 8, 4GD
    stats_pattern = r'(?m)^(.*VIG \d+, CLA \d+, SPI \d+, \d+GD.*)$'
    content, count_stats = re.subn(stats_pattern, r'> \1', content)
    stats['formatting_updates'] += count_stats

    # Spark Tables
    # Pattern: **Key**: value ~ **Key**: value
    spark_pattern = r'(?m)(\*\*.*?\*\*:.*?)\s*~\s*(\*\*.*?\*\*:.*?)'
    content, count_spark = re.subn(spark_pattern, r'\1 ~ \2', content)
    stats['formatting_updates'] += count_spark

    # =========================================================================
    # Output
    # =========================================================================
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print("-" * 30)
    print("Cleaning Complete.")
    print("-" * 30)
    print(f"Artifacts Removed:   {stats['artifacts_removed']}")
    print(f"Typos Corrected:     {stats['typos_fixed']}")
    print(f"Formatting Updates:  {stats['formatting_updates']}")
    print(f"Output saved to:     {output_file}")
    print("-" * 30)

def get_next_version_path(directory, base_filename):
    """
    Checks the directory for existing versions and returns the next sequential filename.
    Format: base_filename_v{n}.md
    """
    version = 1
    while True:
        filename = f"{base_filename}_v{version}.md"
        full_path = os.path.join(directory, filename)
        if not os.path.exists(full_path):
            return full_path
        version += 1

if __name__ == "__main__":
    # User-specified absolute path
    # Using raw string (r"") to handle Windows backslashes correctly
    INPUT_FILENAME = r"Mythic-Bastionland-Cleaned_v2.md"
    
    # Base name for the output file
    OUTPUT_BASE = "Mythic-Bastionland-Cleaned"

    if os.path.exists(INPUT_FILENAME):
        # Determine output directory (same as input)
        output_dir = os.path.dirname(INPUT_FILENAME)
        
        # Calculate next version
        OUTPUT_FILENAME = get_next_version_path(output_dir, OUTPUT_BASE)
        
        # Execute cleaning
        clean_ocr_markdown_v3(INPUT_FILENAME, OUTPUT_FILENAME)
        
    else:
        # Fallback for testing/Canvas environment if the local path doesn't exist
        print(f"Warning: Specific path '{INPUT_FILENAME}' not found in this environment.")
        print("Checking for local file...")
        
        local_input = "Mythic-Bastionland-Cleaned_v2.md"
        if os.path.exists(local_input):
            OUTPUT_FILENAME = get_next_version_path(".", OUTPUT_BASE)
            clean_ocr_markdown_v3(local_input, OUTPUT_FILENAME)
        else:
            print("Error: Source file not found.")