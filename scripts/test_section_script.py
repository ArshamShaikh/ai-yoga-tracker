import docx
from docx.shared import Inches, Pt
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()
# Section 1
s1 = doc.sections[0]
s1.top_margin = Inches(1.0)
s1.bottom_margin = Inches(1.0)
s1.left_margin = Inches(1.25)
s1.right_margin = Inches(1.0)

doc.add_paragraph("Front matter 1")
doc.add_page_break()
doc.add_paragraph("Front matter 2")

# Section 2
s2 = doc.add_section()
s2.top_margin = Inches(1.0)
s2.bottom_margin = Inches(1.0)
s2.left_margin = Inches(1.25)
s2.right_margin = Inches(1.0)

sectPr2 = s2._sectPr
pgNumType = parse_xml(f'<w:pgNumType {nsdecls("w")} w:start="1"/>')
sectPr2.append(pgNumType)

s2.footer.is_linked_to_previous = False
p_foot = s2.footer.paragraphs[0]
p_foot.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
fld = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
p_foot._p.append(fld)

doc.add_paragraph("Chapter 1 page 1")
doc.add_page_break()
doc.add_paragraph("Chapter 1 page 2")

doc.save(r'c:\arsham\TY\MP\ai-yoga-tracker\test_section.docx')
print("Saved test_section.docx successfully!")
