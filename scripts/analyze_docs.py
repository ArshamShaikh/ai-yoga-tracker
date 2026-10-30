import pypdf
import re

def check_pdf(path, name):
    r = pypdf.PdfReader(path)
    print(f"=== {name} ({len(r.pages)} pages) ===")
    for i, p in enumerate(r.pages):
        txt = p.extract_text()
        lines = [l.strip() for l in txt.splitlines() if l.strip()]
        # find single numbers that might be page numbers
        nums = [l for l in lines if l.isdigit() and len(l) <= 3]
        # find chapter headings
        chaps = [l for l in lines if any(k in l.upper() for k in [
            'CHAPTER', 'TABLE OF CONTENTS', 'CERTIFICATE', 'ACKNOWLEDGEMENT', 
            'DECLARATION', 'ABSTRACT', 'PLAGIARISM'
        ])]
        if chaps:
            print(f"Physical P{i+1}: PageNum={nums} | Headings={chaps}")

print("ANALYSIS OF PETCARE REFERENCE PDF:")
check_pdf(r"c:\arsham\TY\MP\AI-Powered PetCare Smart Pet Health and Care Management System.pdf", "PetCare PDF")
