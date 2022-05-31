import os
import pandas as pd
import numpy as np
from datetime import datetime as dt
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Frame, Table, TableStyle, Image, Spacer, SimpleDocTemplate
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Pull in Student Names
student_names = pd.read_csv("test_names.csv")

# Define table style
tblstyle = TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.white),
                       ('BOX', (0, 0), (-1, -1), 0.25, colors.white),
                       ('FONTSIZE', (0, 0), (-1, 0), 6),
                       ('FONTSIZE', (0, 1), (-1, -1), 6),
                       ('TEXTFONT', (0, 0), (-1, 0), 'Calibri-Bold'),
                       ('TEXTFONT', (0, 1), (0, -1), 'Calibri-Bold'),
                       ('TEXTFONT', (0, 1), (-1, -1), 'Calibri'),
                       ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                       ('TEXTCOLOR', (1, 1), (0, -1), colors.black),
                       ('LEFTPADDING', (0, 0), (-1, -1), 1),
                       ('RIGHTPADDING', (0, 0), (-1, -1), 1),
                       ('TOPPADDING', (0, 0), (-1, -1), 0),
                       ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                       ('ROWBACKGROUNDS', (0, 0), (-1, -1), (colors.HexColor('#e8e9ec'), colors.HexColor('#CED1D6'))),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3A5675')),
                       ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                       ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                       ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
                       ])



# Create a document
c = canvas.Canvas("student_list.pdf")

# turn datatable the table into a list of lists which is the format reportlab wants
data_summary = [pd.DataFrame(student_names).columns.values.tolist()] + pd.DataFrame(student_names).values.tolist()

# config the widths and heights of this specific table
colwidths_2 = [300] * len(data_summary)
rowheights_2 = [15] * len(data_summary)

# create table using the platypus Table object & set the style
tbl_summary = Table(data_summary, colwidths_2, rowheights_2, hAlign='LEFT', repeatRows=1)
tbl_summary.setStyle(tblstyle)


# Build Story - Add a spacer at the beginning for your heading
story = [
    Spacer(1, 1 * inch)
]

story.append(tbl_summary)

# Create Page 1 Formatting
def myFirstPage(canvas: canvas.Canvas, doc):
    canvas.saveState()

    dtstring = dt.date.today().strftime("%B %d, %Y")

    # create header on first page
    canvas.drawString(55, 750, "Student Report: " + dtstring)
    canvas.line(50, 740, 530, 740)


# Use a Document Template so the flowable can flow to the next page.  
doc = SimpleDocTemplate(
    "student_list.pdf",
    pageSize=letter,
    rightMargin=0.5 * inch, leftMargin=0.5 * inch, topMargin=0.5 * inch, bottomMargin=0.5 * inch,
)

# Build and save
doc.build(story, onFirstPage=myFirstPage)