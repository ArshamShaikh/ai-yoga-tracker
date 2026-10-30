import os
import sys
import docx

# Ensure current directory is in python path
sys.path.append(os.path.dirname(__file__))

from builder_core import create_base_document, start_chapter_section
from builder_front_matter import build_front_matter
from builder_chapters_1_to_3 import build_chapters_1_to_3
from builder_chapter_4_survey import build_chapter_4_survey
from builder_chapter_5_design import build_chapter_5_design
from builder_chapter_6_implementation import build_chapter_6_implementation
from builder_chapters_7_to_9 import build_chapters_7_to_9

def generate_document(toc_data=None, output_path=None):
    print("Initializing document with official 3pt thick black borders and margins...")
    doc = create_base_document()

    print("Generating Front Matter (strictly matching PetCare template)...")
    build_front_matter(doc, toc_data=toc_data)

    print("Creating Section 2 for Chapters (Restarting page number at 1)...")
    start_chapter_section(doc)

    print("Generating Chapters 1 to 3 (Introduction, Requirements, Analysis)...")
    build_chapters_1_to_3(doc)

    print("Generating Chapter 4 (Survey of Technology)...")
    build_chapter_4_survey(doc)

    print("Generating Chapter 5 (System Design with Persistence Schema & UML)...")
    build_chapter_5_design(doc)

    print("Generating Chapter 6 (System Implementation with clean boxed code & QA)...")
    build_chapter_6_implementation(doc)

    print("Generating Chapters 7 to 9 (Results, Conclusion, IEEE References)...")
    build_chapters_7_to_9(doc)

    if not output_path:
        output_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Master_Thesis_Final.docx'

    doc.save(output_path)
    print(f"Successfully generated document at: {output_path}")
    return output_path

if __name__ == "__main__":
    generate_document()
