---
modified:
  - 2025-01-16T20:18:30-05:00
---

# Publish-Dataview-To-Web

**Frontmatter Detection**
- Checks if file starts with frontmatter (`---`)
- Finds the end of frontmatter block
- Splits content at that point

**Content Insertion**
- Preserves frontmatter exactly as is
- Inserts table immediately after frontmatter
- Maintains proper spacing
- Preserves all remaining content

**This script will:**
1. Keep frontmatter intact
2. Insert the `dataview` table right after frontmatter
3. Preserve all other content below the table

# Frontmatter-Setup
**Frontmatter Handling**
- Checks if frontmatter exists
- Preserves existing content after frontmatter
- Only replaces or adds frontmatter section

**Content Preservation**
- Keeps all existing content below frontmatter
- Maintains proper spacing
- Doesn't duplicate or remove existing content

**The script will:**
1. Check if frontmatter exists
2. Replace only the frontmatter if it exists
3. Add frontmatter if it doesn't exist
4. Preserve all other content in the file