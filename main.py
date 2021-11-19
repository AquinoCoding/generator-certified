from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import time
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

global can, packet, nameCertificateUser, listaNomesThree



packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)

def moreThree(nameCertificateUser):
    can.setFontSize(size=40)
    can.drawString(220, 273, nameCertificateUser, )
    can.showPage()
    can.save()
    creatFile(nameCertificateUser)
    

def moreTwo(nameCertificateUser):
    can.setFontSize(size=40)
    can.drawString(287, 273, nameCertificateUser, )
    can.showPage()
    can.save()
    creatFile(nameCertificateUser)


def manualAutomation():

    nameCertificateUser = input('Informe o nome: ')

    validation = int(input('3 NOMES = [1]\n2 NOMES = [2]\nInforme: '))

    if validation == 1:
        moreThree(nameCertificateUser)

    elif validation == 2:
        moreTwo(nameCertificateUser)

    else:
        manualAutomation()


def Automatic():

    listaNomesThree = ['Lucas Eduardo Aquino', 'Eduardo Fernando Silva', 'Gabriel Oliveira Silva']
    for i in range(len(listaNomesThree)):
        moreThree(listaNomesThree[i])

    listaNomesTwo = ['Lucas Eduardo', 'Eduardo Fernando', 'Gabriel Oliveira']
    for i in range(len(listaNomesTwo)):
        moreTwo(listaNomesTwo[i])
    
    exit()

def creatFile(nameFile):
    
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    origin_pdf = PdfFileReader(open("Original.pdf", "rb"))
    insertPDF = PdfFileWriter()

    page = origin_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    insertPDF.addPage(page)

    with open("Certificado"+nameFile+".pdf", "wb") as validation_PDF:
        insertPDF.write(validation_PDF)

def controladora():
    validation = input('Automatic [1]\nManual    [2]\nInforme: ')

    if validation == '1':
        Automatic()
    
    if validation == '2':
        manualAutomation()
    
    else:
        controladora()

try:
    controladora()
except:
    del listaNomesThree[0]
    controladora()
    
