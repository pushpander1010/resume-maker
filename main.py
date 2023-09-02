
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, PageBreak, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import helper,css,re
from helper import Experience,Project,Education


doc=SimpleDocTemplate('Hello.pdf',pagesize=letter)
c=canvas.Canvas("Resume.pdf",pagesize=letter,)
h,w=letter
c.translate(10,720)
readData=helper.readCsv('details.csv')
prev=0
story1=[]
story1.append(Paragraph(readData.get('name')[2],css.heading_style))
tmp="";
for key,val in readData.items():
    if re.match(r'subheading.*',key):
        if  re.match(r'.*[.]{1}.*',val[6]):
            tmp+=f'<a href={val[6]}>{val[2]}</a>' +"     "
        else:
            tmp+=f'{val[2]}' +"     "
story1.append(Paragraph(tmp,css.subheading_style))
f1 = Frame(0*inch, 0*inch, 4.2*inch, 1.0*inch, showBoundary=0)
f1.addFromList(story1,c)

story2=[]
tmp="";
for key,val in readData.items():
    if re.match(r'contact.*',key):
        if re.match(r'.*[.]{1}.*',val[6]):
            tmp+=f'<a href={val[6]}>{val[2]}</a><br/>' +"     "
        else:
            tmp+=f'{val[2]}<br/>' +"        "
story2.append(Paragraph(tmp,css.contact_style,))
f2=Frame(4.3*inch,0*inch,4*inch,1.0*inch,showBoundary=0)
prev=1;
f2.addFromList(story2,c)

story3=[]
story3.append(Paragraph("<u>Skills</u>",css.paraheading_style))
story3.append(Paragraph(readData.get('skills')[2],css.normal_style,))
f3=Frame(0*inch,-1*inch,8.2*inch,1.0*inch,showBoundary=0)
prev=1;
f3.addFromList(story3,c)

story4=[]
story4.append(Paragraph("<u>Experiences</u>",css.paraheading_style))
exps=[]
for key,val in readData.items():
    if re.match(r'experience.*',key):
        exp=Experience(val[2])
        exps.append(exp)
        story4.append(Paragraph(f"<h4>{exp.getCompany()}</h4>",css.detHead1_style,))
        story4.append(Paragraph(f"<h4>{exp.getDate()}</h4>",css.detHead2_style,))
        story4.append(Paragraph(f"{exp.getDetails()}",css.detHead3_style,))

f4=Frame(0*inch,-1.6*len(exps)*inch-0.5*inch,8.2*inch,1.6*len(exps)*inch,showBoundary=0)
prev=1.6*len(exps)
f4.addFromList(story4,c)

story5=[]
story5.append(Paragraph("<u>Projects</u>",css.paraheading_style))
exps=[]
for key,val in readData.items():
    if re.match(r'project.*',key):
        exp=Project(val[2])
        exps.append(exp)
        story5.append(Paragraph(f"<h4>{exp.getCompany()}</h4>",css.detHead1_style,))
        story5.append(Paragraph(f"<h4>{exp.getTech()}</h4>",css.detHead2_style,))
        story5.append(Paragraph(f"{exp.getDetails()}",css.detHead3_style,))

f5=Frame(0*inch,-1.1*len(exps)*inch-prev*inch-0.4*inch,8.2*inch,1.1*len(exps)*inch,showBoundary=0)
prev+=1.1*len(exps)
f5.addFromList(story5,c)

story6=[]
story6.append(Paragraph("<u>Education</u>",css.paraheading_style))
exps=[]
for key,val in readData.items():
    if re.match(r'education.*',key):
        exp=Education(val[2])
        exps.append(exp)
        story6.append(Paragraph(f"<h4>{exp.getQualification()}</h4>",css.detHead1_style,))
        story6.append(Paragraph(f"<h4>({exp.getDate()})</h4>",css.detHead2_style,))
        story6.append(Paragraph(f"<b>{exp.getSchool()}</b>",css.detHead3_style,))
        story6.append(Paragraph(f"Percentage/CGPA: {exp.getMarks()}",css.detHead3_style,))

f6=Frame(0*inch,-1.2*len(exps)*inch-prev*inch-0.4*inch,8.2*inch,1.2*len(exps)*inch,showBoundary=0)
prev+=1.2*len(exps)
f6.addFromList(story6,c)


story7=[]
story7.append(Paragraph("<u>Awards and Certifications</u>",css.paraheading_style))
exps=[]
i=1
for key,val in readData.items():
    if re.match(r'certificate.*|awards.*',key):
        exp=val[2]
        exps.append(exp)
        story7.append(Paragraph(f"<u><a color='blue' href='{val[6]}'>{i}. {exp}</a></u>",css.detHead3_style,))
        i+=1
f7=Frame(0*inch,-0.4*len(exps)*inch-prev*inch-0.4*inch,8.2*inch,0.4*len(exps)*inch,showBoundary=0)
prev+=0.4*len(exps)
f7.addFromList(story7,c)


c.line(0,10,600,10)
c.save()