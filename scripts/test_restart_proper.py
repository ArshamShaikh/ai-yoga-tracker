import docx
from docx.shared import Inches, Pt
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()
# Section 1
s1 = doc.sections[0]
doc.add_paragraph("Front matter 1")
doc.add_page_break()
doc.add_paragraph("Front matter 2")

# Section 2
s2 = doc.add_section()
sectPr = s2._sectPr
# Proper placement of pgNumType
cols = sectPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}cols')
pgNumType = parse_xml(f'<w:pgNumType {nsdecls("w")} w:start="1"/>')
if cols is not None:
    cols.addprevious(pgNumType)
else:
    sectPr.append(pgNumType)

s2.footer.is_linked_to_previous = False
p_foot = s2.footer.paragraphs[0]
p_foot.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
fld = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
p_foot._p.append(fld)

doc.add_paragraph("Chapter 1 page 1")
doc.add_page_break()
doc.add_paragraph("Chapter 1 page 2")

test_out = r'c:\arsham\TY\MP\ai-yoga-tracker\scripts\test_restart_proper.docx'
doc.save(test_out)
print("Saved proper restart test docx!")
