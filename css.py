from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, PageBreak, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

heading_style = ParagraphStyle(
    name='CustomStyle',
    fontName='Helvetica-bold',
    fontSize=25,
    textColor=colors.black,
    leading=14,
    alignment=0,  # Center alignment
    spaceAfter=20,
)

subheading_style = ParagraphStyle(
    name='CustomStyle',
    fontName='Helvetica',
    fontSize=10,
    textColor=colors.blue,
    leading=14,
    alignment=0,  # Center alignment
    spaceAfter=10,
)

contact_style = ParagraphStyle(
    name='CustomStyle',
    fontName='Helvetica',
    fontSize=10,
    textColor=colors.black,
    leading=14,
    alignment=2,  # Center alignment
    spaceAfter=5,
)

paraheading_style = ParagraphStyle(
    name='CustomStyle',
    fontName='Helvetica-bold',
    fontSize=14,
    textColor=colors.black,
    leading=14,
    alignment=0,  # Center alignment
    spaceAfter=5,
)

normal_style = ParagraphStyle(
    name='CustomStyle',
    fontName='Helvetica',
    fontSize=10,
    textColor=colors.black,
    leading=10,
    alignment=0,  # Center alignment
    spaceAfter=10,
)

detHead1_style = ParagraphStyle(
    name='CustomStyle',
    fontName='Helvetica-bold',
    fontSize=12,
    textColor=colors.black,
    leading=10,
    alignment=0,  # Center alignment
    spaceAfter=5,
)

detHead2_style = ParagraphStyle(
    name='CustomStyle',
    fontName='Helvetica',
    fontSize=8,
    textColor=colors.black,
    leading=0,
    alignment=0,  # Center alignment
    spaceAfter=10,
)

detHead3_style = ParagraphStyle(
    name='CustomStyle',
    fontName='Helvetica',
    fontSize=10,
    textColor=colors.black,
    leading=10,
    alignment=0,  # Center alignment
    spaceAfter=10,
)






