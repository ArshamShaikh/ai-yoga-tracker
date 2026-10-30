import os
import sys

# Ensure current directory is in python path
sys.path.append(os.path.dirname(__file__))

from builder_core import create_base_document
from builder_front_matter import build_front_matter
from builder_chapters_1_to_3 import build_chapters_1_to_3
from builder_chapter_4_survey import build_chapter_4_survey
from builder_chapter_5_design import build_chapter_5_design
from builder_chapter_6_implementation import build_chapter_6_implementation
from builder_chapters_7_to_9 import build_chapters_7_to_9

def main():
    print("=" * 60)
    print("STARTING BUILD OF 87+ PAGE MASTER ACADEMIC THESIS REPORT")
    print("=" * 60)
    
    print("\n[1/7] Initializing document with official Mumbai University borders and margins...")
    doc = create_base_document()

    print("[2/7] Generating Front Matter (Cover, Certificate, Acknowledgement, Plagiarism Card, Declaration, Abstract, TOC)...")
    build_front_matter(doc)

    print("[3/7] Generating Chapters 1 to 3 (Introduction, Requirements, Analysis)...")
    build_chapters_1_to_3(doc)

    print("[4/7] Generating Chapter 4: Survey of Technology (Detailed deep dives into 8 frameworks)...")
    build_chapter_4_survey(doc)

    print("[5/7] Generating Chapter 5: System Design (UML, DFD 0 & 1, Activity, Schemas, FSM, Vector Math)...")
    build_chapter_5_design(doc)

    print("[6/7] Generating Chapter 6: System Implementation (Extensive Frontend & Backend source code + QA)...")
    build_chapter_6_implementation(doc)

    print("[7/7] Generating Chapters 7 to 9 (Results with 5 rounded screenshots, Benchmarks, Conclusion, Clickable References)...")
    build_chapters_7_to_9(doc)

    out_paths = [
        r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Master_Thesis_Final.docx',
        r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Master_Thesis_Complete.docx'
    ]
    saved_path = None
    for p in out_paths:
        try:
            doc.save(p)
            print(f"\nSUCCESS: Master Academic Thesis successfully compiled and saved to:\n--> {p}")
            saved_path = p
            break
        except PermissionError:
            print(f"Notice: Path {p} is currently locked by Word. Trying next fallback path...")
    
    if not saved_path:
        alt_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Master_Thesis_Complete_Expanded.docx'
        doc.save(alt_path)
        print(f"\nSUCCESS: Saved to alternative file:\n--> {alt_path}")

if __name__ == "__main__":
    main()
