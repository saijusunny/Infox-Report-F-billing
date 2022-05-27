from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
elements = []
data = [['00', '01', '02', '03', '04'],
    ['10', '11', '12', '13', '14'],
    ['20', '21', '22', '23', '24'],
    ['30', '31', '32', '33', '34']]
t = Table(data,5*[0.8*inch], 4*[0.4*inch])
# t.setStyle(TableStyle([
#     ('TEXTCOLOR',(0,0),(-1,-1),colors.green),
#     ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
#     ('BOX', (0,0), (-1,-1), 0.25, colors.black),
#     ]))
elements.append(t)
doc = SimpleDocTemplate('TabDemo3.pdf')
doc.build(elements)