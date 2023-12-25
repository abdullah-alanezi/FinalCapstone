from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime
import io
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

def create_deal_pdf(request):
    # Extracting form data
    investor_name = request.POST.get('investor_name', '__________')
    company_name = request.POST.get('company_name', '__________')
    investment_percentage = request.POST.get('investment_percentage', '___')
    investment_amount = request.POST.get('investment_amount', '__________')
    agreement_date = request.POST.get('agreement_date') or datetime.now().strftime('%Y-%m-%d')

    # Setting up a buffer for the PDF
    buffer = io.BytesIO()

    # Document setup
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=inch, leftMargin=inch, topMargin=inch, bottomMargin=inch)
    styles = getSampleStyleSheet()

    # Styles for the PDF
    contract_title = ParagraphStyle(name='ContractTitle', fontSize=18, spaceAfter=20, alignment=TA_CENTER)
    contract_clause = ParagraphStyle(name='ContractClause', fontSize=10, leading=12)
    contract_clause_bold = ParagraphStyle(name='ContractClauseBold', fontSize=10, leading=12, spaceAfter=6, fontName='Helvetica-Bold')

    # Logo addition
    logo = "media/images/default.jpg"  # Replace with the path to your logo
    logo_img = Image(logo, 2*inch, 1*inch)  # Adjust the size as needed
    logo_img.hAlign = 'CENTER'

    # Elements of the PDF
    elements = [logo_img]  # Start with the logo
    elements.append(Paragraph("Investment Agreement", contract_title))

    # Agreement clauses
    clauses = [
        "This Agreement is made and entered into by and between:",
        f"INVESTOR: <u>{investor_name}</u>",
        f"COMPANY: <u>{company_name}</u>",
        f"Date: <u>{agreement_date}</u>",
        "Hereinafter referred to as the 'Parties'.",
        "WHEREAS, the Investor wishes to invest capital in the Company, and the Company wishes to accept the investment under the following terms:",
        f"1. Investment Amount: The Investor agrees to invest an amount of <u>${investment_amount}</u> into the Company.",
        f"2. Investment Percentage: For the investment amount, the Investor will receive an equity stake of <u>{investment_percentage}%</u> in the Company.",
        "3. Use of Funds: The Company shall utilize the invested funds for business development and growth initiatives as previously agreed upon.",
        "4. Governing Law: This Agreement shall be governed by the laws of the jurisdiction in which the Company is registered.",
        "5. Entire Agreement: This document and any exhibits attached constitute the entire agreement between the Parties.",
        "6. Amendment: Any amendments to this Agreement must be in writing and signed by both Parties.",
        "IN WITNESS WHEREOF, the Parties have executed this Agreement as of the date first above written."
    ]

    # Adding clauses to the PDF
    for clause in clauses:
        style = contract_clause_bold if 'WHEREAS' in clause or clause.startswith("IN WITNESS WHEREOF") else contract_clause
        elements.append(Paragraph(clause, style))
        elements.append(Spacer(1, 12))

    # Signatures
    elements.append(Spacer(1, 24))
    elements.append(Paragraph(f"Investor Signature: {investor_name}", contract_clause))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Company Representative Signature: {company_name}", contract_clause))
    elements.append(Spacer(1, 48))
    # Building the PDF
    doc.build(elements)

    pdf = buffer.getvalue()
    buffer.close()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="investment_agreement.pdf"'

    return response


def deal_form(request):
    if request.method == 'POST':
        return create_deal_pdf(request)
    return render(request, 'contract/deal_form.html')
