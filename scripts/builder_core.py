import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def apply_section_border(section, sz="24"):
    """
    Applies a thick, professional single-line black border around the page,
    matching the PetCare university project standard.
    sz="24" corresponds to 3.0pt width (w:sz in eighths of a point).
    """
    sectPr = section._sectPr
    # Remove existing borders if any
    for existing in sectPr.xpath('.//w:pgBorders'):
        sectPr.remove(existing)
    
    pgBorders = parse_xml(
        f'<w:pgBorders {nsdecls("w")} w:offsetFrom="page">'
        f'<w:top w:val="single" w:sz="{sz}" w:space="24" w:color="000000"/>'
        f'<w:left w:val="single" w:sz="{sz}" w:space="24" w:color="000000"/>'
        f'<w:bottom w:val="single" w:sz="{sz}" w:space="24" w:color="000000"/>'
        f'<w:right w:val="single" w:sz="{sz}" w:space="24" w:color="000000"/>'
        f'</w:pgBorders>'
    )
    sectPr.append(pgBorders)

def create_base_document():
    doc = docx.Document()
    # Section 1: Front matter (no page numbers in footer)
    s1 = doc.sections[0]
    s1.top_margin = Inches(1.0)
    s1.bottom_margin = Inches(1.0)
    s1.left_margin = Inches(1.25)
    s1.right_margin = Inches(1.0)
    s1.page_width = Inches(8.27)
    s1.page_height = Inches(11.69)
    apply_section_border(s1, sz="24")
    return doc

def start_chapter_section(doc):
    """
    Creates Section 2 for Chapter 1 onwards.
    Restarts page numbering at 1, unlinks footer from Section 1,
    and inserts a centered page number field in the footer.
    """
    s2 = doc.add_section()
    s2.top_margin = Inches(1.0)
    s2.bottom_margin = Inches(1.0)
    s2.left_margin = Inches(1.25)
    s2.right_margin = Inches(1.0)
    s2.page_width = Inches(8.27)
    s2.page_height = Inches(11.69)
    apply_section_border(s2, sz="24")

    # Set page number starting at 1 (proper OpenXML schema sequence before w:cols)
    sectPr2 = s2._sectPr
    for existing in sectPr2.xpath('.//w:pgNumType'):
        sectPr2.remove(existing)
    cols = sectPr2.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}cols')
    pgNumType = parse_xml(f'<w:pgNumType {nsdecls("w")} w:start="1"/>')
    if cols is not None:
        cols.addprevious(pgNumType)
    else:
        sectPr2.append(pgNumType)

    # Unlink footer
    s2.footer.is_linked_to_previous = False
    p_foot = s2.footer.paragraphs[0]
    p_foot.text = ""
    p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_foot.paragraph_format.space_before = Pt(8)
    p_foot.paragraph_format.space_after = Pt(0)
    
    # Page field run
    fld = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
    p_foot._p.append(fld)
    return s2

def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_table_borders(table, sz="8", color="000000"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
        f'<w:insideV w:val="none"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def add_title_header(doc, text, size=18):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(size)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(15)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(11)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.italic = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_body(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.4
    p.paragraph_format.space_after = Pt(6)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_bullet(doc, bold_prefix, text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.space_after = Pt(4)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_bold = p.add_run(bold_prefix + ': ')
    r_bold.font.name = 'Times New Roman'
    r_bold.font.bold = True
    r_bold.font.color.rgb = RGBColor(0, 0, 0)
    r_text = p.add_run(text)
    r_text.font.name = 'Times New Roman'
    r_text.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_code_box(doc, file_name, code_text):
    """
    Renders source code inside a single-cell bordered table box,
    matching PetCare's clean boxed code layout.
    """
    p_fn = doc.add_paragraph()
    p_fn.paragraph_format.space_before = Pt(10)
    p_fn.paragraph_format.space_after = Pt(4)
    p_fn.paragraph_format.keep_with_next = True
    r_fn = p_fn.add_run(file_name)
    r_fn.font.name = 'Consolas'
    r_fn.font.size = Pt(11)
    r_fn.font.bold = True
    r_fn.font.color.rgb = RGBColor(0, 0, 0)

    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="8" w:space="0" w:color="222222"/>'
        f'<w:bottom w:val="single" w:sz="8" w:space="0" w:color="222222"/>'
        f'<w:left w:val="single" w:sz="8" w:space="0" w:color="222222"/>'
        f'<w:right w:val="single" w:sz="8" w:space="0" w:color="222222"/>'
        f'<w:insideH w:val="none"/>'
        f'<w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

    cell = table.rows[0].cells[0]
    cell.width = Inches(6.02)
    set_cell_shading(cell, "FAFAFC")

    p = cell.paragraphs[0]
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = p.add_run(code_text)
    run.font.name = 'Consolas'
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)

    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_after = Pt(4)
    return table

def add_figure(doc, img_path, caption, width_in=5.6):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(10)
        p_img.paragraph_format.space_after = Pt(4)
        p_img.paragraph_format.keep_with_next = True
        doc.add_picture(img_path, width=Inches(width_in))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(10)
        r_cap = p_cap.add_run(caption)
        r_cap.font.name = 'Times New Roman'
        r_cap.font.size = Pt(10.5)
        r_cap.font.bold = True
        r_cap.font.color.rgb = RGBColor(0, 0, 0)

def add_toc_item(doc, title, page_no, level=1):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(2)
    if level == 1:
        p.paragraph_format.left_indent = Inches(0.0)
        p.paragraph_format.space_before = Pt(5)
    elif level == 2:
        p.paragraph_format.left_indent = Inches(0.22)
    elif level == 3:
        p.paragraph_format.left_indent = Inches(0.44)
    pPr = p._p.get_or_add_pPr()
    tabs = parse_xml(f'<w:tabs {nsdecls("w")}><w:tab w:val="right" w:leader="dot" w:pos="8640"/></w:tabs>')
    pPr.append(tabs)
    r_t = p.add_run(title)
    r_t.font.name = 'Times New Roman'
    r_t.font.size = Pt(11 if level == 1 else 10.5)
    if level == 1:
        r_t.font.bold = True
    r_t.font.color.rgb = RGBColor(0, 0, 0)
    
    # Format page number with leading zero if single digit (like 01, 07)
    page_str = str(page_no).zfill(2) if isinstance(page_no, int) or (isinstance(page_no, str) and page_no.isdigit() and len(page_no) == 1) else str(page_no)
    r_p = p.add_run(f'\t{page_str}')
    r_p.font.name = 'Times New Roman'
    r_p.font.size = Pt(11 if level == 1 else 10.5)
    if level == 1:
        r_p.font.bold = True
    r_p.font.color.rgb = RGBColor(0, 0, 0)

def add_hyperlink(paragraph, url, text, color="0044CC", underline=True):
    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    hyperlink = parse_xml(f'<w:hyperlink {nsdecls("w")} r:id="{r_id}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>')
    new_run = parse_xml(f'<w:r {nsdecls("w")}/>')
    rPr = parse_xml(f'<w:rPr {nsdecls("w")}/>')
    if color:
        c = parse_xml(f'<w:color {nsdecls("w")} w:val="{color}"/>')
        rPr.append(c)
    if underline:
        u = parse_xml(f'<w:u {nsdecls("w")} w:val="single"/>')
        rPr.append(u)
    font = parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>')
    rPr.append(font)
    sz = parse_xml(f'<w:sz {nsdecls("w")} w:val="22"/>')
    rPr.append(sz)
    new_run.append(rPr)
    new_run.append(parse_xml(f'<w:t {nsdecls("w")}>{text}</w:t>'))
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)
