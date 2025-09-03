import os

# Folder containing the .md files
md_folder = r'C:\md-notes'
output_md = os.path.join(md_folder, 'merged_notes.md')

# Keywords to help order chapters
priority_keywords = [
    'overview', 'industry', 'computer', 'os', 'coding', 'variables', 'data-type',
    'conditional', 'if', 'loop', 'function', 'debug', 'oops', 'class',
    'recursion', 'ds', 'data-structure', 'complexity', 'time', 'others'
]

# Function to sort based on keywords
def sort_key(filename):
    name = filename.lower()
    for index, keyword in enumerate(priority_keywords):
        if keyword in name:
            return index
    return len(priority_keywords) + 1  # Put unknown topics at the end

# Get all .md files
md_files = [f for f in os.listdir(md_folder) if f.endswith('.md')]
md_files.sort(key=sort_key)

print(f"Found {len(md_files)} markdown files. Merging into one file...\n")

# Merge content
with open(output_md, 'w', encoding='utf-8') as merged_file:
    for md_file in md_files:
        file_path = os.path.join(md_folder, md_file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add a level-1 title separator between files
        merged_file.write(f"# {os.path.splitext(md_file)[0]}\n\n")
        merged_file.write(content + '\n\n---\n\n')

        print(f"✔ Added: {md_file}")

print(f"\n✅ Final merged Markdown file created at: {output_md}")
