# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:33:18 2023

@author: Utente
"""

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import cm


from classes import pdf_template


def AllPageSetup(canvas, doc):
    canvas.saveState()
    canvas.drawImage('cern2.jpg', x=0, y=0)
    canvas.restoreState()
    
pdf_template.import_font_ttf(
    font_name='times-roman', font_file='times.ttf',
    font_name_italic='times-romanI', font_file_italic= 'timesi.ttf',
    font_name_bold='times-romanB', font_file_bold='timesbd.ttf',
    font_name_bolditalic='times-romanBI', font_file_bolditalic='timesbi.ttf')


full_name = "Marie Curie"
degree = "MSc"

doc = SimpleDocTemplate("CV_{}_CERN.pdf".format(full_name),
                        pagesize=A4,
                        rightMargin=2*cm,
                        leftMargin=2*cm,
                        topMargin=2.5*cm,
                        bottomMargin=2.5*cm)

styles = pdf_template.set_doc_style(font_name='times-roman',
                                    font_name_bold='times-romanB')


Story=[]


title = '<font color=#0030a0>{}, {}</font>'.format(full_name, degree)
job_title = "Physicist"

Story.append(Paragraph(title, styles["Title_2"]))
Story.append(Spacer(1, 0.3*cm))
Story.append(Paragraph(job_title, styles["HeadingCenter"]))
Story.append(Spacer(1, 1*cm))

table_style=[
 ('ALIGN',(0,0),(-1,-1),'CENTER'),
 ('FONT', (0,0), (-1,0), 'times-romanB'),
 ('FONT', (0,1), (-1,1), 'times-roman')
]

dob = "07/11/1867"
ctz = "Polish"
res = 'France'
tel = "0123456789"
mail = "marie.curie@gmail.com"
linkedin = "www.linkedin.com/in/mariecurie/"
oth = "https://www.kaggle.com/mariecurie"

data= [['Date of Birth:', 'Citizenship:', "Address:", 'Mobile:'],
        [dob, ctz, res, tel]]
t=Table(data)
t.setStyle(TableStyle(table_style))

Story.append(t)

data= [['Mail:', "LinkedIn:", "Kaggle:"],
        [mail, linkedin, oth]]

t=Table(data)
t.setStyle(TableStyle(table_style))

Story.append(t)
Story.append(Spacer(1, 0.5*cm))


professional_summary = """I am the first woman ever to teach at Sorbonne. 
Double Nobel prize winner."""
Story.append(Paragraph(professional_summary, styles["Justify"]))
Story.append(Spacer(1, 1*cm))

last_experience_dates = """General Physics teacher at Sorbonne <br/>
1908 - current"""
last_experience_descr_point1 = """<bullet>&bull;</bullet> First woman to teach
at Sorbonne."""
last_experience_descr_point2 = """<bullet>&bull;</bullet> Lorem ipsum dolor sit 
amet, consectetur adipiscing elit."""
last_experience_descr_point3 = """<bullet>&bull;</bullet> Quisque at laoreet
 metus, eget rhoncus massa. Nam tempor odio eu mi malesuada laoreet. 
 Nam mollis nisi eu turpis mollis, ac ullamcorper sem convallis."""
last_experience_descr_point4 = """<bullet>&bull;</bullet>Ut aliquam erat et 
interdum tristique.  Sed a augue bibendum, vehicula odio nec, tempor ligula. """
last_experience_descr_point5 = """<bullet>&bull;</bullet>Duis pharetra feugiat 
ornare. Donec tincidunt sapien vel augue lobortis rutrum. Ut dictum sapien
quis mi facilisis lacinia."""
last_experience_descr_point6 = """<bullet>&bull;</bullet> Sed congue sapien 
vel magna aliquam, quis varius lacus ultrices. Mauris eget lacinia justo, ac 
fermentum orci. Cras accumsan mollis neque, at tincidunt nunc viverra non."""

Story.append(Paragraph("<font color=#0030a0>PROFESSIONAL EXPERIENCE</font>", styles["HeadingLeft"]))
Story.append(Spacer(1, 0.5*cm))
Story.append(Paragraph(last_experience_dates, styles["HeadingLeft2"]))
Story.append(Spacer(1, 0.3*cm))
Story.append(Paragraph(last_experience_descr_point1, styles["Justify"]))
Story.append(Paragraph(last_experience_descr_point2, styles["Justify"]))
Story.append(Paragraph(last_experience_descr_point3, styles["Justify"]))
Story.append(Paragraph(last_experience_descr_point4, styles["Justify"]))
Story.append(Paragraph(last_experience_descr_point5, styles["Justify"]))
Story.append(Paragraph(last_experience_descr_point6, styles["Justify"]))

prev_experience_dates = """Radioactive substances Researcher <br/>
1897 - current"""
prev_experience_descr_point1 = """<bullet>&bull;</bullet> Pellentesque
 imperdiet tincidunt quam, ut ultricies mi. Curabitur vitae ultricies nisi. 
 Proin pharetra convallis nisl et fermentum. Fusce at ultrices lacus."""
prev_experience_descr_point2 = """<bullet>&bull;</bullet> Ut nec quam venenatis,
 tincidunt tortor ut, sodales nulla. Morbi quis enim lacus. In venenatis
 tellus nibh, vitae sollicitudin nisl dapibus ut."""
prev_experience_descr_point3 = """<bullet>&bull;</bullet> Sed pharetra velit 
vitae felis elementum tincidunt. Cras vehicula finibus tellus in lobortis.
 Nulla quis mauris mi. Cras consequat sit amet nisl ac malesuada. Ut eget
 pellentesque massa."""
prev_experience_descr_point4 = """<bullet>&bull;</bullet>Mauris consectetur 
turpis ac enim scelerisque, ut dignissim arcu ultrices. Cras vehicula elit et
 arcu accumsan consectetur. Sed lobortis sollicitudin cursus. """

Story.append(Spacer(1, 0.5*cm))
Story.append(Paragraph(prev_experience_dates, styles["HeadingLeft2"]))
Story.append(Spacer(1, 0.3*cm))
Story.append(Paragraph(prev_experience_descr_point1, styles["Justify"]))
Story.append(Paragraph(prev_experience_descr_point2, styles["Justify"]))
Story.append(Paragraph(prev_experience_descr_point3, styles["Justify"]))
Story.append(Paragraph(prev_experience_descr_point4, styles["Justify"]))

Story.append(Spacer(1, 1*cm))
Story.append(Paragraph("<font color=#0030a0>EDUCATION AND TRAINING</font>", styles["HeadingLeft"]))
Story.append(Spacer(1, 0.5*cm))

edu_last = """Physics <br/>
1891"""
uni = """Sorbonne"""

Story.append(Paragraph(edu_last, styles["HeadingLeft2"]))
Story.append(Paragraph(uni, styles["Justify"]))
Story.append(Spacer(1, 0.3*cm))


certification = """Certifications:"""
cert_1 = """<bullet>&bull;</bullet>Nobel Prize 1903, Physics"""
cert_2 = """<bullet>&bull;</bullet>Nobel Prize 1911, Chemistry"""


Story.append(Spacer(1, 0.5*cm))
Story.append(Paragraph(certification, styles["HeadingLeft2"]))
Story.append(Spacer(1, 0.3*cm))
Story.append(Paragraph(cert_1, styles["Justify"]))
Story.append(Paragraph(cert_2, styles["Justify"]))


Story.append(Spacer(1, 1*cm))
Story.append(Paragraph("<font color=#0030a0>PROGRAMMING & DIGITAL SKILLS</font>", styles["HeadingLeft"]))
Story.append(Spacer(1, 0.5*cm))

prog_1 = """<bullet>&bull;</bullet>Python (Numpy, Matplotlib, seaborn, Scipy,
Pandas, Scikit-learn, Tensorflow, PySpark)"""
prog_2 = """<bullet>&bull;</bullet>SQL"""
prog_4 = """<bullet>&bull;</bullet>Amazon Redshift"""
prog_5 = """<bullet>&bull;</bullet>Git, BitBucket"""
prog_5 = """<bullet>&bull;</bullet>Microsoft Office"""

Story.append(Paragraph(prog_1, styles["Justify"]))
Story.append(Paragraph(prog_2, styles["Justify"]))
Story.append(Paragraph(prog_4, styles["Justify"]))
Story.append(Paragraph(prog_5, styles["Justify"]))


Story.append(Spacer(1, 1*cm))
Story.append(Paragraph("<font color=#0030a0>LANGUAGE SKILLS</font>", styles["HeadingLeft"]))
Story.append(Spacer(1, 0.5*cm))

lang_1 = "Polish"
lev_lang_1 = "Mothertongue"

lang_2 = "French"
lev_lang_2 = "Highly Proficient"


Story.append(Paragraph("{}: {}".format(lang_1, lev_lang_1), styles["HeadingLeft2"]))
Story.append(Paragraph("{}: {}".format(lang_2, lev_lang_2), styles["HeadingLeft2"]))

Story.append(Spacer(1, 1*cm))
Story.append(Paragraph("<font color=#0030a0>COMMUNICATION & INTERPERSONAL SKILLS</font>", styles["HeadingLeft"]))
Story.append(Spacer(1, 0.5*cm))

skill_1 = """<bullet>&bull;</bullet>Workaholic"""
skill_2 = """<bullet>&bull;</bullet>Active listener"""
skill_3 = """<bullet>&bull;</bullet>Diplomatic"""
skill_4 = """<bullet>&bull;</bullet>Logical and analytical approach to problem-solving"""
skill_5 = """<bullet>&bull;</bullet>Cooperative"""
skill_6 = """<bullet>&bull;</bullet>Continuous learner"""
skill_7 = """<bullet>&bull;</bullet>Committed"""

Story.append(Paragraph(skill_1, styles["Justify"]))
Story.append(Paragraph(skill_2, styles["Justify"]))
Story.append(Paragraph(skill_3, styles["Justify"]))
Story.append(Paragraph(skill_4, styles["Justify"]))
Story.append(Paragraph(skill_5, styles["Justify"]))
Story.append(Paragraph(skill_6, styles["Justify"]))
Story.append(Paragraph(skill_7, styles["Justify"]))

doc.build(Story, onFirstPage=AllPageSetup, 
          onLaterPages=AllPageSetup)