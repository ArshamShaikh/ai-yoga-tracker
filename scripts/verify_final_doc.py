import docx
from docx.oxml import parse_xml

doc_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Master_Thesis_Final.docx'
doc = docx.Document(doc_path)

print(f"Total Paragraphs: {len(doc.paragraphs)}")
print(f"Total Tables: {len(doc.tables)}")

images_count = 0
for rel in doc.part.rels.values():
    if "image" in rel.target_ref:
        images_count += 1
print(f"Total Embedded Images: {images_count}")

hyperlinks_count = 0
for p in doc.paragraphs:
    hyperlinks = p._p.xpath('.//w:hyperlink')
    if hyperlinks:
        hyperlinks_count += len(hyperlinks)
print(f"Total Clickable Hyperlinks: {hyperlinks_count}")

# Check key headings
print("\n--- Document Heading Check ---")
for p in doc.paragraphs:
    if p.text.startswith("CHAPTER") or p.text in ["CERTIFICATE", "ACKNOWLEDGEMENT", "PLAGIARISM REPORT", "DECLARATION", "ABSTRACT", "TABLE OF CONTENTS"]:
        print(f"Found: {p.text}")

print("\n--- Checking Figure Captions in Chapter 7 (Results) ---")
for p in doc.paragraphs:
    if "Figure 7." in p.text:
        print(f"Found: {p.text}")

print("\nVerification check complete!")
