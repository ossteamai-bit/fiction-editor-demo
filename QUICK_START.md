# Fiction Editor Agent - Quick Start Guide

## Get Started in 5 Minutes

### 1. Setup (One-Time)

```bash
# Make the script executable
chmod +x fiction_editor.py

# Test it works
python3 fiction_editor.py --help
```

### 2. Your First Analysis

For a quick test with the sample:
```bash
python3 fiction_editor.py full-report sample_manuscript.txt
```

For your own manuscript:
```bash
python3 fiction_editor.py full-report your_chapter.txt -o analysis_report.txt
```

### 3. Most Useful Commands

**Developmental Stage** (before line-editing):
```bash
# Get the big-picture view
python3 fiction_editor.py dev-analysis your_manuscript.txt -o dev_report.txt

# Check story concept
python3 fiction_editor.py concept your_manuscript.txt

# Check pacing
python3 fiction_editor.py rhythm your_manuscript.txt
```

**Copyediting Stage** (polish pass):
```bash
# Full copyedit analysis
python3 fiction_editor.py copyedit your_manuscript.txt -o copyedit_report.txt

# Check character/place consistency
python3 fiction_editor.py consistency your_manuscript.txt

# Analyze dialogue
python3 fiction_editor.py dialogue your_manuscript.txt

# Generate style sheet
python3 fiction_editor.py style-sheet your_manuscript.txt
```

---

## The Three Essential Principles

### 1. "It's Not My Book"
Respect your own choices as author. The agent flags potential issues but YOU decide what to change.

### 2. "Is This How People Talk?"
Don't "fix" natural dialogue or first-person narration to formal grammar. Characters should sound authentic.

### 3. "If It Ain't Broke, Don't Fix It"
Don't change intentional fragments, comma splices, or stylistic choices. They're often deliberate.

---

## What the Agent Does

**✅ DOES:**
- Identifies potential inconsistencies in character names, places, timeline
- Tracks repeated elements and themes
- Analyzes sentence rhythm and pacing patterns
- Counts dialogue instances and tags
- Flags years/dates for fact-checking
- Creates comprehensive style sheet
- Generates professional editing reports

**❌ DOES NOT:**
- Make changes to your manuscript
- Rewrite anything
- Judge your creative choices
- Tell you what must be changed
- Replace human editorial judgment

**Think of it as:** Your systematic first reader who takes meticulous notes.

---

## Typical Workflow: Editing a Chapter

### Step 1: Big Picture Check (5 minutes)
```bash
python3 fiction_editor.py rhythm chapter_05.txt
python3 fiction_editor.py narrative chapter_05.txt
```

**Review:** Is the pacing right? Does the timeline work?

### Step 2: Consistency Check (5 minutes)
```bash
python3 fiction_editor.py consistency chapter_05.txt
python3 fiction_editor.py dialogue chapter_05.txt
```

**Review:** Are character names consistent? Does dialogue sound natural?

### Step 3: Final Polish (10 minutes)
```bash
python3 fiction_editor.py copyedit chapter_05.txt -o chapter_05_report.txt
```

**Review:** Read the report, address genuine issues, ignore non-issues.

---

## For Your Albanian Variation / Spy Trilogy

### Recommended Workflow:

**Phase 1: After First Draft**
```bash
# Check each chapter for pacing
python3 fiction_editor.py rhythm chapter_*.txt

# Generate full dev analysis
python3 fiction_editor.py dev-analysis the_albanian_variation_draft1.txt -o dev_analysis.txt
```

**Phase 2: After Structural Revisions**
```bash
# Check consistency across the book
python3 fiction_editor.py consistency the_albanian_variation_draft2.txt -o consistency_check.txt

# Build comprehensive style sheet
python3 fiction_editor.py style-sheet the_albanian_variation_draft2.txt
```

**Phase 3: Final Pass**
```bash
# Full copyedit before publication
python3 fiction_editor.py copyedit the_albanian_variation_final.txt -o final_copyedit.txt

# Fact-check historical/technical details
python3 fiction_editor.py facts the_albanian_variation_final.txt
```

### Special Attention Points:

1. **Historical Accuracy** - The agent flags years (1923, 1987, etc.). Verify against your research.
2. **Geographic Consistency** - Track Albanian locations, Soviet-era details across all three books.
3. **Character Voice** - Ensure Aya and Amina maintain distinct speech patterns.
4. **Action Pacing** - Check that average sentence length drops during action scenes.

---

## Understanding the Reports

### Developmental Report Shows:

- **Word count** - Overall length tracking
- **Chapter structure** - How many chapters, are they balanced?
- **Frequent themes** - What words/concepts appear most?
- **Time markers** - Timeline elements found
- **Average sentence length** - Pacing proxy (5-10 words = fast, 20+ = slow)
- **Key questions** - Professional editing questions to consider

### Copyediting Report Shows:

- **Character tracking** - Names and frequency (watch for variants)
- **Dialogue analysis** - How much dialogue, what tags used
- **Grammar patterns** - Fragments, sentence starters (NOT "errors" - patterns)
- **Years/dates mentioned** - For fact-checking
- **Editor checklist** - Professional standards to verify

### Style Sheet Contains:

- Characters (names, descriptions, speech patterns)
- Places (locations, details, geography)
- Timeline (events, dates, sequences)
- Queries (questions for author - you!)
- Style decisions (punctuation, spelling, formatting)

---

## Pro Tips

### 1. Run Multiple Times
The agent doesn't change your manuscript, so run it as many times as you want:
- After each draft
- Before major revisions
- During final polish
- Different commands for different focuses

### 2. Combine with Claude Conversations
Use the reports in conversations:
```
"The fiction editor flagged 44 potential fragments in my chapter. 
Can you help me identify which are intentional for style vs. 
which are accidental errors?"
```

### 3. Build Series-Wide Style Sheet
For your trilogy, maintain one master style sheet:
```bash
# Start with Book 1
python3 fiction_editor.py style-sheet book1.txt

# For Books 2-3, manually merge the JSON files
# This ensures Aya's eye color doesn't change between books
```

### 4. Track Manuscript Versions
```bash
# Name reports clearly
python3 fiction_editor.py copyedit albanian_variation_v1.txt -o albanian_v1_report.txt
python3 fiction_editor.py copyedit albanian_variation_v2.txt -o albanian_v2_report.txt

# Compare what changed between drafts
```

---

## Common Questions

**Q: Will this edit my manuscript?**
A: No! It only reads and analyzes. Your manuscript is never changed.

**Q: Should I fix everything it flags?**
A: No! It identifies patterns and potential issues. You decide what's actually a problem.

**Q: Why does it flag so many fragments?**
A: Because fiction uses fragments deliberately. The agent counts them so you can verify they're intentional.

**Q: Can I use it for non-fiction?**
A: Yes, but it's optimized for fiction. Some "fiction rules" don't apply to non-fiction.

**Q: How do I add entries to the style sheet manually?**
A: Edit the `[manuscript_name]_style_sheet.json` file in any text editor.

---

## What to Read Next

1. **FICTION_EDITOR_README.md** - Complete documentation (30 min read)
2. **EDITING_BEST_PRACTICES.md** - Methodologies extracted from the Chicago Guides (1 hour read)
3. **sample_output.txt** - Example of what the agent produces

---

## Troubleshooting

**"File not found":**
```bash
# Make sure you're in the right directory
ls  # Should show your manuscript file

# Or use full path
python3 fiction_editor.py copyedit /full/path/to/manuscript.txt
```

**"No module named...":**
```bash
# Script uses only Python standard library
# Should work with Python 3.7+
python3 --version  # Check your version
```

**"Permission denied":**
```bash
chmod +x fiction_editor.py
```

---

## Immediate Next Steps

1. ✅ Run the sample to see output:
   ```bash
   python3 fiction_editor.py full-report sample_manuscript.txt
   ```

2. ✅ Try it on one of your chapters:
   ```bash
   python3 fiction_editor.py consistency your_chapter.txt
   ```

3. ✅ Review the report and identify 2-3 genuine issues to fix

4. ✅ Read the EDITING_BEST_PRACTICES.md for deeper understanding

---

## Integration with Claude Code

This IS a Claude Code agent! Use it in your terminal:

```bash
# Standard usage
python3 fiction_editor.py <command> manuscript.txt

# With output file
python3 fiction_editor.py <command> manuscript.txt -o report.txt

# Pipe to file
python3 fiction_editor.py <command> manuscript.txt > analysis.txt
```

Then discuss results with Claude in conversation mode.

---

**You're ready to go! Start with the sample, then try one of your own chapters.** 📚✨

---

*Based on The Chicago Guide to Copyediting Fiction (Schneider, 2023) and Developmental Editing: A Handbook (Norton, 2023)*
