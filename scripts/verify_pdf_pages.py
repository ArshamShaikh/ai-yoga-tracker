import pypdf

pdf_path = r'c:\arsham\TY\MP\ai-yoga-tracker\Documents\AI-Based-Yoga-Trainer-Project-Report.pdf'
reader = pypdf.PdfReader(pdf_path)
print(f"Total Pages in Exported PDF: {len(reader.pages)}")

print("\n--- PRELIMINARY PAGES PREVIEW ---")
for i in range(min(10, len(reader.pages))):
    text = reader.pages[i].extract_text()
    first_line = text.split("\n")[0] if text else "[Empty]"
    last_line = text.split("\n")[-1] if text else "[Empty]"
    print(f"Page {i+1}: First line: '{first_line[:60]}' | Last line: '{last_line[-40:]}'")

print("\n--- CERTIFICATE CHECK (Page 2) ---")
print(reader.pages[1].extract_text())

print("\n--- DECLARATION CHECK (Page 5) ---")
print(reader.pages[4].extract_text())

print("\n--- CHAPTER 1 START CHECK (Page 9) ---")
print(reader.pages[8].extract_text()[:400])
