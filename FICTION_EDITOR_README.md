# Fiction Editor Agent for Claude Code

## Professional Editing Based on Chicago Guide Methodologies

This Claude Code agent implements professional fiction editing techniques from two authoritative University of Chicago Press guides:

- **"The Chicago Guide to Copyediting Fiction"** by Amy J. Schneider (2023)
- **"Developmental Editing: A Handbook for Freelancers, Authors, and Publishers"** by Scott Norton (2023)

---

## 🎯 Core Philosophy

### The Fiction Editor's Mindset (Schneider)

**Three Essential Mottoes:**

1. **"It's not my book"** - Respect the author's choices and voice
2. **"Is this how people talk?"** - Don't "fix" natural dialogue or first-person narration  
3. **"If it ain't broke, don't fix it"** - Don't rewrite to avoid tricky grammar

**What Fiction Editing Is NOT:**
- ❌ Not your chance to pretend you're the author
- ❌ Not the place to apply your moral code
- ❌ Not the time to apply your grammar hammer
- ✅ Focus on supporting suspension of disbelief
- ✅ Ensure internal consistency (not just factual accuracy)
- ✅ Preserve the author's voice while catching errors

---

## 📚 Editing Stages

### STAGE 1: Developmental Editing (Norton's Methodology)

**Purpose:** Shape the big-picture elements before line-editing

#### 1. Concept Analysis (Norton Ch.1)
- Locate the central concept
- Profile the target audience
- Evaluate market potential
- Bring the vision into focus

#### 2. Thesis Analysis (Norton Ch.3)
- Cull theses from topics
- Identify the "so what?" factor
- Create a working title
- Find the emotional hook

#### 3. Narrative Analysis (Norton Ch.4)
- Untangle timelines from arguments
- Find the main timelines
- Brainstorm timeline strategies
- Identify pacing issues

#### 4. Rhythm & Pacing (Norton Ch.7)
- Balance chapter weights
- Edit for pace
- Identify passages that drag
- Ensure chapter endings hook readers

### STAGE 2: Copyediting (Schneider's Methodology)

**Purpose:** Polish mechanics while preserving author's voice

#### 1. Internal Consistency Check
- Track character names and descriptions
- Verify place descriptions match
- Check timeline for impossible sequences
- Ensure fictional "facts" don't contradict

#### 2. Dialogue Analysis (Schneider Ch.8)
- Ensure dialogue sounds natural, not stilted
- Check characters have distinct voices
- Verify dialect/accent consistency
- Confirm dialogue punctuation
- **Don't "correct" informal speech to formal grammar**

#### 3. Grammar in Fiction (Schneider Ch.7)
- Recognize intentional fragments and comma splices
- Respect creative grammar choices
- First-person narration follows dialogue-like rules
- Query only genuinely confusing passages

#### 4. Fact-Checking Fiction (Schneider Ch.9)
- Verify historical events match stated years
- Check technology references match time period
- Confirm real locations accurately described
- Respect author's deliberate anachronisms
- Balance real-world facts with fictional license

---

## 🚀 Quick Start

### Installation

```bash
# Make the script executable
chmod +x fiction_editor.py

# Run without installation
python3 fiction_editor.py --help
```

### Basic Usage

```bash
# Full developmental analysis
python3 fiction_editor.py dev-analysis your_manuscript.txt

# Full copyediting analysis  
python3 fiction_editor.py copyedit your_manuscript.txt

# Complete report (both stages)
python3 fiction_editor.py full-report your_manuscript.txt -o complete_report.txt

# Individual analyses
python3 fiction_editor.py concept your_manuscript.txt
python3 fiction_editor.py dialogue your_manuscript.txt
python3 fiction_editor.py consistency your_manuscript.txt
```

---

## 📋 Complete Command Reference

### Developmental Commands

| Command | Purpose | Based On |
|---------|---------|----------|
| `dev-analysis` | Full developmental edit analysis | Norton Chs. 1-7 |
| `concept` | Analyze story concept and premise | Norton Ch. 1 |
| `thesis` | Identify central theme/thesis | Norton Ch. 3 |
| `narrative` | Analyze narrative structure and timeline | Norton Ch. 4 |
| `rhythm` | Analyze pacing and rhythm | Norton Ch. 7 |

### Copyediting Commands

| Command | Purpose | Based On |
|---------|---------|----------|
| `copyedit` | Full copyediting analysis | Schneider Chs. 1-9 |
| `consistency` | Check internal consistency | Schneider Ch. 1 |
| `dialogue` | Analyze dialogue | Schneider Ch. 8 |
| `grammar` | Check grammar (fiction-appropriate) | Schneider Ch. 7 |
| `facts` | Fact-check fiction elements | Schneider Ch. 9 |

### Utility Commands

| Command | Purpose |
|---------|---------|
| `style-sheet` | Generate/update style sheet |
| `full-report` | Run complete analysis (dev + copy) |

---

## 📝 The Style Sheet System

The agent automatically creates and maintains a comprehensive style sheet tracking:

### General Style
- Punctuation choices
- Spelling variations
- Capitalization
- Number handling
- Italics usage
- Special terminology

### Characters
- Name spellings and variants
- Physical descriptions
- Background details
- Speech patterns
- Relationships

### Places
- Location names and spellings
- Geographic details
- Descriptions
- Internal geography consistency

### Timeline
- Event sequences
- Date tracking
- Time passage
- Flashback structure

### Queries
- Questions for the author
- Potential inconsistencies
- Fact-check items
- Style decisions needed

---

## 🎨 Workflow Example: Editing Your Novel

### Phase 1: Developmental Review (Before Line Editing)

```bash
# Step 1: Analyze the big picture
python3 fiction_editor.py concept the_albanian_variation.txt

# Step 2: Check narrative structure
python3 fiction_editor.py narrative the_albanian_variation.txt

# Step 3: Examine pacing
python3 fiction_editor.py rhythm the_albanian_variation.txt

# Step 4: Generate full dev report
python3 fiction_editor.py dev-analysis the_albanian_variation.txt -o dev_report.txt
```

**Review the report and address structural issues before proceeding.**

### Phase 2: Copyediting Pass

```bash
# Step 1: Check consistency
python3 fiction_editor.py consistency the_albanian_variation.txt

# Step 2: Review dialogue
python3 fiction_editor.py dialogue the_albanian_variation.txt

# Step 3: Fact-check
python3 fiction_editor.py facts the_albanian_variation.txt

# Step 4: Generate style sheet
python3 fiction_editor.py style-sheet the_albanian_variation.txt

# Step 5: Full copyedit report
python3 fiction_editor.py copyedit the_albanian_variation.txt -o copyedit_report.txt
```

### Phase 3: Comprehensive Final Review

```bash
# Generate complete analysis
python3 fiction_editor.py full-report the_albanian_variation.txt -o complete_analysis.txt
```

---

## 🔧 Advanced Features

### 1. Style Sheet Integration

The agent creates a JSON file (`[manuscript]_style_sheet.json`) that tracks:
- All characters and their attributes
- All locations and descriptions
- Timeline events
- Style decisions
- Editor queries

This file persists across editing sessions and can be manually edited.

### 2. Automated Tracking

The agent automatically:
- Identifies character names by frequency
- Detects potential name variants/misspellings
- Extracts timeline markers
- Analyzes sentence rhythm
- Counts dialogue instances
- Identifies setting references

### 3. Query Generation

The agent generates professional queries for the author, such as:
- "Character name appears as both 'Jon' and 'John' - which is correct?"
- "Timeline shows character in two places simultaneously on Day 3"
- "This technology wouldn't exist in 1987 - intentional anachronism?"

---

## 📖 Methodology Details

### Norton's Developmental Editing Approach

**Ground Rules:**
1. Be realistic - set ambitious but achievable goals
2. Make a plan - don't "wing it"
3. Address logistics up front
4. Proceed with enthusiasm
5. Leave well enough alone
6. Remember the reader
7. Set milestones
8. Be tactful
9. Be candid
10. Listen actively
11. Brainstorm together
12. Keep the plan current

**Key Techniques:**
- **Untangle timelines from arguments** - Separate chronological events from thematic arguments
- **Balance chapter weights** - Ensure chapters are proportional to their importance
- **Create opening/closing transitions** - Strong hooks and satisfying conclusions
- **Harmonize voices** - Consistent narrative voice throughout

### Schneider's Copyediting Approach

**Breaking the Rules:**
- Comma splices can create pace and tension
- Sentence fragments establish voice
- Repetition can be deliberate technique
- Dialogue doesn't follow formal grammar
- First-person narration is dialogue-like

**Supporting Suspension of Disbelief:**
- Ensure internal consistency in fictional worlds
- Track all "facts" (real and invented)
- Call out potential problems without assuming error
- Verify real-world facts don't break story
- Check that fictional facts don't contradict

**Critical Distinctions:**
- Copyediting is mechanical, not creative
- Focus on clarity, not rewriting
- Preserve author's voice and style choices
- Query problems, don't assume solutions

---

## 🎯 For Your Specific Use Case

### Archaeological Thrillers (Aya Amrani Adventures)

**Additional Checks Recommended:**

1. **Historical Accuracy**
   ```bash
   python3 fiction_editor.py facts manuscript.txt
   ```
   Pay special attention to:
   - Historical dates and events
   - Archaeological terminology
   - Cultural details from research locations
   - Period-appropriate technology

2. **Setting Consistency**
   Track your extensively researched locations:
   - Galata Tower details
   - Istanbul geography
   - Atlas Mountains descriptions
   - Soviet-era Albanian locations
   - Georgian settings
   - Arctic Pyramiden details

3. **Series Continuity**
   Maintain style sheet across books:
   - Character development arcs
   - Mythology elements (artifacts, powers)
   - Recurring locations
   - Series timeline

4. **Action Sequence Pacing**
   ```bash
   python3 fiction_editor.py rhythm manuscript.txt
   ```
   Ensure Dan Brown-style pacing with:
   - Short sentences during action
   - Cliffhanger chapter endings
   - Balance of action/exposition

---

## 💡 Tips for Maximum Effectiveness

### 1. Run Analyses at Different Stages

**First Draft Complete:**
- Run `dev-analysis` to check structure
- Focus on concept, thesis, narrative flow
- Don't worry about line-level issues yet

**Second Draft (Post-Structural Revisions):**
- Run `rhythm` to check pacing
- Run `consistency` for character/place tracking
- Begin building style sheet

**Final Draft (Before Publication):**
- Run `copyedit` for full mechanical pass
- Run `dialogue` and `grammar` checks
- Run `facts` for accuracy review
- Generate complete `full-report`

### 2. Interpret Results Intelligently

The agent **flags potential issues**, it doesn't dictate fixes:
- Review each flagged item in context
- Remember "It's not my book"
- Trust your authorial intent
- Use queries to double-check, not auto-fix

### 3. Maintain the Style Sheet

After each editing pass:
- Review and update character entries
- Add new locations discovered
- Document style decisions made
- Record queries for author (yourself)

### 4. Use with Claude Conversations

This agent generates reports that you can then discuss with Claude:

```
"I ran the fiction editor on Chapter 5. It flagged potential pacing 
issues - the average sentence length is 32 words during the chase scene. 
Can you help me rewrite this section with shorter, punchier sentences?"
```

---

## 🔬 Technical Notes

### Supported File Formats
- Plain text (.txt)
- Markdown (.md)
- Any UTF-8 encoded text file

### Output Formats
- Plain text reports
- JSON data (for programmatic use)
- Style sheet JSON (for tracking)

### Performance
- Handles manuscripts up to 150,000 words efficiently
- Analysis typically completes in <30 seconds
- Style sheet operations are near-instantaneous

---

## 📚 Further Reading

### Primary Sources
- Schneider, Amy J. *The Chicago Guide to Copyediting Fiction*. University of Chicago Press, 2023.
- Norton, Scott. *Developmental Editing: A Handbook for Freelancers, Authors, and Publishers*. 2nd ed. University of Chicago Press, 2023.

### Complementary Resources
- *The Chicago Manual of Style* (CMOS) - Standard reference
- Einsohn & Schwartz, *The Copyeditor's Handbook* - General copyediting
- Mulvany, *Indexing Books* - If you need indexes
- Borel, *The Chicago Guide to Fact-Checking* - Deep dive on facts

### Online Resources
- Copyeditors' Knowledge Base: kokedit.com/ckb.php
- Right Touch Editing (Zombie Rules): righttouchediting.com
- Writers and Editors: writersandeditors.com

---

## 🤝 Integration with Your Workflow

### For One Small Step Grant Writing
The systematic approach used here mirrors your grant writing methodology:
- Clear analysis framework
- Documented decision-making
- Comprehensive tracking systems
- Professional report generation

### For Novel Series Management
Use this agent to maintain consistency across your Aya Amrani Adventures:
- Central style sheet for the series
- Timeline tracking across multiple books
- Character development arc monitoring
- Setting details preservation

---

## ⚖️ License & Attribution

Based on methodologies from:
- *The Chicago Guide to Copyediting Fiction* © 2023 Amy J. Schneider
- *Developmental Editing: A Handbook* © 2023 Scott Norton
- Both published by University of Chicago Press

This agent implements their methodologies for personal use in manuscript editing.

---

## 🐛 Known Limitations

1. **Context Understanding**: Cannot fully understand narrative context like a human editor
2. **Stylistic Judgment**: Flags potential issues but cannot judge artistic intent
3. **Genre Conventions**: May not recognize all genre-specific conventions
4. **Cultural Nuance**: May miss cultural or linguistic subtleties
5. **Character Arc**: Cannot evaluate character development trajectories

**Recommendation**: Use this agent as a **first-pass analysis tool** and **systematic tracker**, then apply your editorial judgment to the flagged items.

---

## 🎓 Learning Mode

Each command includes educational output explaining **why** something is flagged:

```
GRAMMAR IN FICTION CHECK
========================================
REMEMBER:
  ❗ "It's not my book" - respect author's choices
  ❗ Fragments and comma splices can be intentional for effect
  ❗ First-person narration follows dialogue-like grammar
  ❗ Don't apply grammar hammer to creative choices
  ❗ Query only if something is genuinely confusing
```

This helps you internalize professional editing principles as you work.

---

## 🚦 Getting Started Checklist

- [ ] Read this README completely
- [ ] Review the example workflow
- [ ] Run `dev-analysis` on a sample chapter
- [ ] Review the generated report
- [ ] Run `copyedit` on the same chapter
- [ ] Examine the style sheet created
- [ ] Try `full-report` on a complete manuscript
- [ ] Integrate into your editing workflow

---

## 💬 Support

For questions about the methodologies, consult the original Chicago Guide books.

For questions about using this agent with Claude Code, experiment with different commands and review the generated reports.

---

**Remember:** This agent is a tool to support your editing process, not replace your editorial judgment. The best results come from combining systematic analysis with human understanding of story, character, and craft. 📝✨
