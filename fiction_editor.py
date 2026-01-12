#!/usr/bin/env python3
"""
FICTION EDITOR AGENT - Claude Code
Based on "The Chicago Guide to Copyediting Fiction" and "Developmental Editing: A Handbook"

This agent implements professional editing methodologies from the University of Chicago Press
guides to provide comprehensive developmental and copyediting support for fiction manuscripts.

USAGE:
    python fiction_editor.py <command> [options]

For detailed help on any command:
    python fiction_editor.py <command> --help

Author: Based on methodologies by Amy J. Schneider and Scott Norton
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Tuple, Optional, Set

class StyleSheet:
    """Manages the fiction style sheet for tracking consistency."""
    
    def __init__(self, manuscript_path: str):
        self.manuscript_path = manuscript_path
        self.manuscript_name = Path(manuscript_path).stem
        self.sheet_path = f"{self.manuscript_name}_style_sheet.json"
        self.data = self._load_or_create()
    
    def _load_or_create(self) -> Dict:
        """Load existing style sheet or create new one."""
        if os.path.exists(self.sheet_path):
            with open(self.sheet_path, 'r') as f:
                return json.load(f)
        
        return {
            'manuscript': self.manuscript_name,
            'created': datetime.now().isoformat(),
            'last_updated': datetime.now().isoformat(),
            'general_style': {
                'punctuation': {},
                'spelling': {},
                'capitalization': {},
                'numbers': {},
                'italics': {},
                'special_terms': {}
            },
            'characters': {},
            'places': {},
            'timeline': [],
            'dialogue_patterns': {},
            'consistency_notes': [],
            'queries': []
        }
    
    def save(self):
        """Save style sheet to disk."""
        self.data['last_updated'] = datetime.now().isoformat()
        with open(self.sheet_path, 'w') as f:
            json.dump(self.data, f, indent=2)
        print(f"Style sheet saved: {self.sheet_path}")
    
    def add_character(self, name: str, details: Dict):
        """Add or update character information."""
        self.data['characters'][name] = details
        self.save()
    
    def add_place(self, name: str, details: Dict):
        """Add or update place information."""
        self.data['places'][name] = details
        self.save()
    
    def add_timeline_event(self, event: Dict):
        """Add timeline event."""
        self.data['timeline'].append(event)
        self.save()
    
    def add_query(self, query: Dict):
        """Add editor query."""
        self.data['queries'].append(query)
        self.save()
    
    def get_report(self) -> str:
        """Generate a comprehensive style sheet report."""
        report = []
        report.append("=" * 80)
        report.append(f"STYLE SHEET: {self.manuscript_name}")
        report.append("=" * 80)
        report.append(f"Created: {self.data['created']}")
        report.append(f"Last Updated: {self.data['last_updated']}")
        report.append("")
        
        # Characters
        if self.data['characters']:
            report.append("\nCHARACTERS")
            report.append("-" * 40)
            for name, details in sorted(self.data['characters'].items()):
                report.append(f"\n{name}:")
                for key, value in details.items():
                    report.append(f"  • {key}: {value}")
        
        # Places
        if self.data['places']:
            report.append("\n\nPLACES")
            report.append("-" * 40)
            for name, details in sorted(self.data['places'].items()):
                report.append(f"\n{name}:")
                for key, value in details.items():
                    report.append(f"  • {key}: {value}")
        
        # Timeline
        if self.data['timeline']:
            report.append("\n\nTIMELINE")
            report.append("-" * 40)
            for event in sorted(self.data['timeline'], key=lambda x: x.get('order', 0)):
                report.append(f"\n{event.get('timestamp', 'N/A')}: {event.get('description', '')}")
        
        # Queries
        if self.data['queries']:
            report.append("\n\nEDITOR QUERIES")
            report.append("-" * 40)
            for i, query in enumerate(self.data['queries'], 1):
                report.append(f"\n[Q{i}] Location: {query.get('location', 'N/A')}")
                report.append(f"     {query.get('question', '')}")
        
        return "\n".join(report)


class DevelopmentalEditor:
    """Implements developmental editing techniques from Norton's handbook."""
    
    def __init__(self, manuscript_path: str):
        self.manuscript_path = manuscript_path
        self.text = self._load_manuscript()
        self.analysis = {}
    
    def _load_manuscript(self) -> str:
        """Load manuscript text."""
        with open(self.manuscript_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def analyze_concept(self) -> Dict:
        """
        CONCEPT ANALYSIS - Norton Ch.1
        - Locate the central concept
        - Profile the audience
        - Evaluate market potential
        - Bring vision into focus
        """
        print("CONCEPT ANALYSIS")
        print("=" * 40)
        print("\nAnalyzing manuscript concept...")
        
        # Word count and basic stats
        words = len(self.text.split())
        paragraphs = len([p for p in self.text.split('\n\n') if p.strip()])
        
        # Try to identify opening concept
        first_500_words = ' '.join(self.text.split()[:500])
        
        analysis = {
            'word_count': words,
            'paragraph_count': paragraphs,
            'opening_concept': first_500_words,
            'questions': [
                "What is the central concept or premise of this story?",
                "Who is the target audience?",
                "What makes this story unique in its genre?",
                "What is the emotional core that will resonate with readers?"
            ]
        }
        
        self.analysis['concept'] = analysis
        return analysis
    
    def analyze_thesis(self) -> Dict:
        """
        THESIS ANALYSIS - Norton Ch.3
        - Cull theses from topics
        - Choose the main thesis
        - Create working title
        """
        print("\nTHESIS ANALYSIS")
        print("=" * 40)
        print("\nIdentifying central theme/thesis...")
        
        # Look for repeated themes or words
        words = self.text.lower().split()
        word_freq = defaultdict(int)
        
        # Focus on meaningful words (simple approach)
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'is', 'was', 'are', 'been', 'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'them', 'their', 'my', 'your', 'his', 'her', 'its', 'our'}
        
        for word in words:
            clean_word = re.sub(r'[^\w]', '', word)
            if len(clean_word) > 4 and clean_word not in stop_words:
                word_freq[clean_word] += 1
        
        # Get top 20 most frequent meaningful words
        top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:20]
        
        analysis = {
            'frequent_themes': top_words,
            'questions': [
                "What is the central argument or theme?",
                "What does this story say about the human condition?",
                "How do the recurring elements support the thesis?",
                "What's the 'so what?' factor - why does this story matter?"
            ]
        }
        
        self.analysis['thesis'] = analysis
        return analysis
    
    def analyze_narrative(self) -> Dict:
        """
        NARRATIVE ANALYSIS - Norton Ch.4
        - Untangle timelines from arguments
        - Find main timelines
        - Brainstorm timeline strategies
        - Compose new timeline
        """
        print("\nNARRATIVE ANALYSIS")
        print("=" * 40)
        print("\nAnalyzing narrative structure and timeline...")
        
        # Try to identify chapter breaks
        chapters = re.findall(r'(Chapter \d+|CHAPTER \d+|Part \d+|PART \d+)', self.text, re.IGNORECASE)
        
        # Look for time markers
        time_markers = re.findall(r'(yesterday|today|tomorrow|last year|next month|morning|evening|night|dawn|dusk|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)', self.text, re.IGNORECASE)
        
        analysis = {
            'chapter_count': len(chapters),
            'chapters_found': chapters[:10],  # First 10
            'time_markers_found': len(time_markers),
            'time_marker_samples': list(set(time_markers))[:20],
            'questions': [
                "Is the timeline linear or non-linear?",
                "Are there multiple timelines that need to be tracked separately?",
                "Do flashbacks serve the story or confuse the reader?",
                "Is the pacing appropriate for the genre?",
                "Does each scene advance the plot or develop character?"
            ]
        }
        
        self.analysis['narrative'] = analysis
        return analysis
    
    def analyze_rhythm(self) -> Dict:
        """
        RHYTHM ANALYSIS - Norton Ch.7
        - Rearrange furniture
        - Balance chapter weights
        - Edit for pace
        """
        print("\nRHYTHM & PACING ANALYSIS")
        print("=" * 40)
        print("\nAnalyzing narrative rhythm and pacing...")
        
        # Sentence length analysis (proxy for pacing)
        sentences = re.split(r'[.!?]+', self.text)
        sentence_lengths = [len(s.split()) for s in sentences if s.strip()]
        
        avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
        
        # Look for dialogue vs narration ratio
        dialogue_markers = len(re.findall(r'"[^"]+"', self.text))
        
        analysis = {
            'average_sentence_length': round(avg_sentence_length, 2),
            'total_sentences': len(sentence_lengths),
            'dialogue_instances': dialogue_markers,
            'questions': [
                "Do long expository sections need breaking up?",
                "Are action sequences paced with short, punchy sentences?",
                "Does dialogue move at a natural rhythm?",
                "Are there passages that drag - too much description, too little action?",
                "Are chapter endings compelling (hooks for next chapter)?"
            ]
        }
        
        self.analysis['rhythm'] = analysis
        return analysis
    
    def generate_dev_report(self, output_path: Optional[str] = None) -> str:
        """Generate comprehensive developmental editing report."""
        report = []
        report.append("=" * 80)
        report.append("DEVELOPMENTAL EDITING REPORT")
        report.append("=" * 80)
        report.append(f"Manuscript: {self.manuscript_path}")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        for section, data in self.analysis.items():
            report.append(f"\n{section.upper()} ANALYSIS")
            report.append("-" * 40)
            
            for key, value in data.items():
                if key == 'questions':
                    report.append("\nKEY QUESTIONS:")
                    for q in value:
                        report.append(f"  ❓ {q}")
                elif isinstance(value, list) and value:
                    report.append(f"\n{key.replace('_', ' ').title()}:")
                    for item in value[:10]:  # Limit output
                        report.append(f"  • {item}")
                elif not isinstance(value, (dict, list)):
                    report.append(f"\n{key.replace('_', ' ').title()}: {value}")
        
        report_text = "\n".join(report)
        
        if output_path:
            with open(output_path, 'w') as f:
                f.write(report_text)
            print(f"\nReport saved: {output_path}")
        
        return report_text


class CopyEditor:
    """Implements copyediting techniques from Schneider's guide."""
    
    def __init__(self, manuscript_path: str):
        self.manuscript_path = manuscript_path
        self.text = self._load_manuscript()
        self.style_sheet = StyleSheet(manuscript_path)
        self.issues = defaultdict(list)
    
    def _load_manuscript(self) -> str:
        """Load manuscript text."""
        with open(self.manuscript_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def check_internal_consistency(self) -> Dict:
        """
        CHECK INTERNAL CONSISTENCY - Schneider Ch.1
        Fiction must be internally consistent even if not factually accurate.
        """
        print("INTERNAL CONSISTENCY CHECK")
        print("=" * 40)
        
        # Extract character names (capitalized words)
        potential_names = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', self.text)
        name_frequency = defaultdict(int)
        for name in potential_names:
            name_frequency[name] += 1
        
        # Filter to likely character names (appear multiple times)
        character_names = {name: count for name, count in name_frequency.items() if count > 5}
        
        # Check for variant spellings
        variants = {}
        for name1 in character_names:
            for name2 in character_names:
                if name1 != name2 and name1.lower() == name2.lower():
                    variants[name1] = name2
        
        # Extract place names (look for common patterns)
        places = set(re.findall(r'(?:in|at|from|to)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)', self.text))
        
        return {
            'character_names': dict(sorted(character_names.items(), key=lambda x: x[1], reverse=True)[:20]),
            'potential_variants': variants,
            'places_mentioned': sorted(places)[:20],
            'checks_needed': [
                "Verify consistent character name spelling throughout",
                "Check character descriptions don't contradict",
                "Verify place descriptions remain consistent",
                "Check timeline for impossible sequences"
            ]
        }
    
    def analyze_dialogue(self) -> Dict:
        """
        DIALOGUE ANALYSIS - Schneider Ch.8
        "Is this how people talk?" - Preserve authentic voice.
        """
        print("\nDIALOGUE ANALYSIS")
        print("=" * 40)
        
        # Extract dialogue
        dialogue_lines = re.findall(r'"([^"]+)"', self.text)
        
        # Check for dialogue tags
        said_variants = re.findall(r'(said|asked|replied|shouted|whispered|muttered|exclaimed|cried|yelled|screamed)', self.text, re.IGNORECASE)
        tag_frequency = defaultdict(int)
        for tag in said_variants:
            tag_frequency[tag.lower()] += 1
        
        # Check for action beats vs tags
        action_beats = len(re.findall(r'"\s*\n\s*[A-Z][^"]*?\.', self.text))
        
        return {
            'dialogue_instances': len(dialogue_lines),
            'dialogue_tag_frequency': dict(sorted(tag_frequency.items(), key=lambda x: x[1], reverse=True)),
            'action_beats_found': action_beats,
            'checks_needed': [
                "Ensure dialogue sounds natural, not stilted",
                "Check that characters have distinct voices",
                "Verify dialect/accent consistency for each character",
                "Confirm dialogue punctuation follows chosen style",
                "Watch for over-use of dialogue tags beyond 'said'",
                "Ensure informal speech isn't 'corrected' to formal grammar"
            ]
        }
    
    def check_grammar_fiction(self) -> Dict:
        """
        GRAMMAR IN FICTION - Schneider Ch.7
        Different rules apply - intentional fragments, comma splices okay in context.
        """
        print("\nGRAMMAR IN FICTION CHECK")
        print("=" * 40)
        
        # Look for intentional fragments (common in fiction)
        potential_fragments = re.findall(r'(?<=[.!?])\s+([A-Z][^.!?]{3,30}[.!?])', self.text)
        
        # Look for comma splices in dialogue (often intentional)
        comma_splices_in_dialogue = re.findall(r'"[^"]*,[^"]*,"[^"]*"', self.text)
        
        # Sentence starters
        sentence_starters = re.findall(r'(?:^|[.!?]\s+)([A-Z][a-z]+)', self.text)
        starter_freq = defaultdict(int)
        for starter in sentence_starters:
            starter_freq[starter] += 1
        
        return {
            'potential_fragments': len(potential_fragments),
            'comma_splices_in_dialogue': len(comma_splices_in_dialogue),
            'common_sentence_starters': dict(sorted(starter_freq.items(), key=lambda x: x[1], reverse=True)[:10]),
            'remember': [
                "\"It's not my book\" - respect author's choices",
                "Fragments and comma splices can be intentional for effect",
                "First-person narration follows dialogue-like grammar",
                "Don't apply grammar hammer to creative choices",
                "Query only if something is genuinely confusing"
            ]
        }
    
    def fact_check_fiction(self) -> Dict:
        """
        FACT-CHECKING IN FICTION - Schneider Ch.9
        Balance real-world facts with fictional license.
        """
        print("\nFACT-CHECKING IN FICTION")
        print("=" * 40)
        
        # Look for years/dates
        years = set(re.findall(r'\b(19\d{2}|20\d{2})\b', self.text))
        
        # Look for brand names
        potential_brands = set(re.findall(r'\b([A-Z][a-z]+(?:[A-Z][a-z]+)?)\b', self.text))
        
        # Look for place names that might need verification
        locations = set(re.findall(r'(?:in|at|from|to|near)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)', self.text))
        
        return {
            'years_mentioned': sorted(years),
            'locations_to_verify': sorted(locations)[:20],
            'checks_needed': [
                "Verify historical events match stated years",
                "Check that technology references match time period",
                "Confirm real locations are accurately described",
                "Verify brand names and trademarks are used correctly",
                "Check that fictionalized places are consistently described",
                "Respect author's deliberate anachronisms if intentional"
            ]
        }
    
    def generate_copyedit_report(self, output_path: Optional[str] = None) -> str:
        """Generate comprehensive copyediting report."""
        report = []
        report.append("=" * 80)
        report.append("COPYEDITING REPORT")
        report.append("=" * 80)
        report.append(f"Manuscript: {self.manuscript_path}")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Run all checks
        consistency = self.check_internal_consistency()
        dialogue = self.analyze_dialogue()
        grammar = self.check_grammar_fiction()
        facts = self.fact_check_fiction()
        
        sections = [
            ("INTERNAL CONSISTENCY", consistency),
            ("DIALOGUE", dialogue),
            ("GRAMMAR IN FICTION", grammar),
            ("FACT-CHECKING", facts)
        ]
        
        for title, data in sections:
            report.append(f"\n{title}")
            report.append("-" * 40)
            
            for key, value in data.items():
                if key in ['checks_needed', 'remember']:
                    report.append(f"\n{key.replace('_', ' ').title().upper()}:")
                    for item in value:
                        report.append(f"  ❗ {item}")
                elif isinstance(value, dict):
                    report.append(f"\n{key.replace('_', ' ').title()}:")
                    for k, v in list(value.items())[:10]:
                        report.append(f"  • {k}: {v}")
                elif isinstance(value, (list, set)):
                    report.append(f"\n{key.replace('_', ' ').title()}: {len(value)} found")
                    if len(value) <= 10:
                        for item in value:
                            report.append(f"  • {item}")
                else:
                    report.append(f"\n{key.replace('_', ' ').title()}: {value}")
        
        # Add style sheet info
        report.append("\n\n" + self.style_sheet.get_report())
        
        report_text = "\n".join(report)
        
        if output_path:
            with open(output_path, 'w') as f:
                f.write(report_text)
            print(f"\nReport saved: {output_path}")
        
        return report_text


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(
        description="Fiction Editor Agent - Professional editing based on Chicago Guides",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
AVAILABLE COMMANDS:
  dev-analysis        Run full developmental editing analysis
  concept            Analyze story concept and premise
  thesis             Identify central theme/thesis
  narrative          Analyze narrative structure and timeline
  rhythm             Analyze pacing and rhythm
  
  copyedit           Run full copyediting analysis
  consistency        Check internal consistency
  dialogue           Analyze dialogue
  grammar            Check grammar (fiction-appropriate)
  facts              Fact-check fiction elements
  
  style-sheet        Generate or update style sheet
  full-report        Run both developmental and copyediting analyses

EXAMPLES:
  python fiction_editor.py dev-analysis manuscript.txt
  python fiction_editor.py copyedit manuscript.txt -o report.txt
  python fiction_editor.py style-sheet manuscript.txt
  python fiction_editor.py full-report manuscript.txt
        """
    )
    
    parser.add_argument('command', help='Command to execute')
    parser.add_argument('manuscript', help='Path to manuscript file')
    parser.add_argument('-o', '--output', help='Output file for report')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.manuscript):
        print(f"Error: Manuscript file not found: {args.manuscript}")
        sys.exit(1)
    
    # Route to appropriate handler
    if args.command in ['dev-analysis', 'concept', 'thesis', 'narrative', 'rhythm']:
        editor = DevelopmentalEditor(args.manuscript)
        
        if args.command == 'dev-analysis':
            editor.analyze_concept()
            editor.analyze_thesis()
            editor.analyze_narrative()
            editor.analyze_rhythm()
            report = editor.generate_dev_report(args.output)
            if not args.output:
                print("\n" + report)
        
        elif args.command == 'concept':
            analysis = editor.analyze_concept()
            print(json.dumps(analysis, indent=2))
        
        elif args.command == 'thesis':
            analysis = editor.analyze_thesis()
            print(json.dumps(analysis, indent=2))
        
        elif args.command == 'narrative':
            analysis = editor.analyze_narrative()
            print(json.dumps(analysis, indent=2))
        
        elif args.command == 'rhythm':
            analysis = editor.analyze_rhythm()
            print(json.dumps(analysis, indent=2))
    
    elif args.command in ['copyedit', 'consistency', 'dialogue', 'grammar', 'facts', 'style-sheet']:
        editor = CopyEditor(args.manuscript)
        
        if args.command == 'copyedit':
            report = editor.generate_copyedit_report(args.output)
            if not args.output:
                print("\n" + report)
        
        elif args.command == 'consistency':
            result = editor.check_internal_consistency()
            print(json.dumps(result, indent=2))
        
        elif args.command == 'dialogue':
            result = editor.analyze_dialogue()
            print(json.dumps(result, indent=2))
        
        elif args.command == 'grammar':
            result = editor.check_grammar_fiction()
            print(json.dumps(result, indent=2))
        
        elif args.command == 'facts':
            result = editor.fact_check_fiction()
            print(json.dumps(result, indent=2))
        
        elif args.command == 'style-sheet':
            print(editor.style_sheet.get_report())
    
    elif args.command == 'full-report':
        print("Running comprehensive editing analysis...\n")
        
        # Developmental analysis
        dev_editor = DevelopmentalEditor(args.manuscript)
        dev_editor.analyze_concept()
        dev_editor.analyze_thesis()
        dev_editor.analyze_narrative()
        dev_editor.analyze_rhythm()
        dev_report = dev_editor.generate_dev_report()
        
        # Copyediting analysis
        copy_editor = CopyEditor(args.manuscript)
        copy_report = copy_editor.generate_copyedit_report()
        
        # Combine reports
        full_report = f"{dev_report}\n\n{'='*80}\n\n{copy_report}"
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(full_report)
            print(f"\nFull report saved: {args.output}")
        else:
            print(full_report)
    
    else:
        print(f"Unknown command: {args.command}")
        print("Run with --help for usage information")
        sys.exit(1)


if __name__ == '__main__':
    main()
