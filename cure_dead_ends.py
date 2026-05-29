import os
from pathlib import Path

def cure_dead_ends(wiki_dir="docs/wiki"):
    """
    Sweeps the wiki directory and appends a 'Back to Master Index' footer 
    to every markdown file, calculating the correct relative path.
    """
    wiki_root = Path(wiki_dir).resolve()
    
    if not wiki_root.exists():
        print(f"❌ Error: Could not find directory {wiki_dir}")
        return

    md_files = list(wiki_root.rglob("*.md"))
    cured_count = 0

    print(f"🩺 Scanning {len(md_files)} wiki files for Dead Ends...")

    for file_path in md_files:
        # We don't want the index linking to itself
        if file_path.name.lower() == "index.md":
            continue

        # Calculate how many directories up we need to go to hit the root index.md
        rel_to_root = os.path.relpath(wiki_root, file_path.parent)
        index_path = Path(rel_to_root) / "index.md"
        
        # Format the relative path safely for web/markdown
        clean_index_path = index_path.as_posix()

        footer = f"\n\n---\n\n**[⬅️ Back to Master Index]({clean_index_path})**\n"

        try:
            content = file_path.read_text(encoding="utf-8")

            # Prevent double-injection if you run the script twice
            if "[⬅️ Back to Master Index]" not in content:
                with open(file_path, "a", encoding="utf-8") as f:
                    f.write(footer)
                cured_count += 1
                
        except Exception as e:
            print(f"⚠️ Failed to patch {file_path.name}: {e}")

    print(f"✅ Success! Cured {cured_count} dead ends.")

if __name__ == "__main__":
    cure_dead_ends()