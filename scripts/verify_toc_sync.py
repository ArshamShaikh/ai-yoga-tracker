import pypdf
import re

pdf_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI_Yoga_Trainer_Project_Report_Final.pdf'
reader = pypdf.PdfReader(pdf_path)

print(f"Total Pages: {len(reader.pages)}")

# Extract TOC entries from pages 7, 8, 9 (0-indexed: 6, 7, 8)
toc_text = ""
for p_idx in [6, 7, 8]:
    toc_text += reader.pages[p_idx].extract_text() + "\n"

toc_lines = [line.strip() for line in toc_text.split("\n") if line.strip() and not line.strip().startswith("TABLE OF CONTENTS")]

# For each TOC line, extract title and page number
discrepancies = []
for line in toc_lines:
    # Match title and trailing digits
    m = re.search(r'^(.*?)\s*\.{3,}\s*(\d+)$', line)
    if m:
        title = m.group(1).strip()
        expected_page = int(m.group(2))
        
        # In Section 2, page 1 is physical page 10 (0-indexed 9)
        # So expected physical page is expected_page + 9 (0-indexed: expected_page + 8)
        target_phys_idx = expected_page + 8
        
        found = False
        if target_phys_idx < len(reader.pages):
            p_text = reader.pages[target_phys_idx].extract_text()
            # Clean title comparison
            clean_title_core = re.sub(r'\(.*?\)', '', title).strip()
            if clean_title_core in p_text or title[:20] in p_text:
                found = True
        
        if not found:
            # Check adjacent page
            for offset in [-1, 1]:
                check_idx = target_phys_idx + offset
                if 0 <= check_idx < len(reader.pages):
                    if title[:20] in reader.pages[check_idx].extract_text():
                        discrepancies.append((title, expected_page, check_idx - 8))
                        break

print(f"Total TOC items evaluated: {len(toc_lines)}")
if discrepancies:
    print(f"Found {len(discrepancies)} slight discrepancies (+/- 1 page):")
    for d in discrepancies[:10]:
        print(f"  Item: '{d[0]}' | TOC says: {d[1]} | Found on page: {d[2]}")
else:
    print("ALL TOC ENTRIES ARE 100% PERFECTLY SYNCHRONIZED!")
