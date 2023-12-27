from django.shortcuts import render, redirect
from django.http import HttpResponse
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
from django.contrib.auth.decorators import login_required
from user.models import InvestorProfile

@login_required
def your_form_view(request):
    investor_name = None  
    if InvestorProfile.objects.filter(user=request.user).exists():
        investor_profile = InvestorProfile.objects.get(user=request.user)
        investor_name = investor_profile.user.get_full_name() 

    context = {'investor_name': investor_name}
    return render(request, 'contract/deal_form.html', context)





@login_required
def create_deal_pdf(request):
    if request.method == 'POST':
        investor_name = request.POST.get('investor_name', '').strip() or 'Unknown Investor'
        company_name = request.POST.get('company_name', '__________')
        investment_percentage = request.POST.get('investment_percentage', '___')
        investment_amount = request.POST.get('investment_amount', '__________')
        agreement_date = request.POST.get('agreement_date') or datetime.now().strftime('%Y-%m-%d')


        investor_name = request.POST.get('investor_name', None)
        if not investor_name:  
            try:
                investor_profile = InvestorProfile.objects.get(user=request.user)
                investor_name = investor_profile.user.get_full_name()
            except InvestorProfile.DoesNotExist:
                investor_name = 'Unknown Investor'

        buffer = io.BytesIO()

        doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=inch, leftMargin=inch, topMargin=inch, bottomMargin=inch)
        styles = getSampleStyleSheet()

        contract_title = ParagraphStyle(name='ContractTitle', fontSize=18, spaceAfter=20, alignment=TA_CENTER)
        contract_clause = ParagraphStyle(name='ContractClause', fontSize=10, leading=12)
        contract_clause_bold = ParagraphStyle(name='ContractClauseBold', fontSize=10, leading=12, spaceAfter=6, fontName='Helvetica-Bold')

        logo = "media/images/default.jpg"  
        logo_img = Image(logo, 2*inch, 1*inch)  
        logo_img.hAlign = 'CENTER'

        elements = [logo_img]
        elements.append(Paragraph("Investment Agreement", contract_title))

        clauses = [
            "This Agreement is made and entered into by and between:",
            f"INVESTOR: <u>{investor_name}</u>",
            f"COMPANY: <u>{company_name}</u>",
            f"Date: <u>{agreement_date}</u>",
            "Hereinafter referred to as the 'Parties'.",
            "WHEREAS, the Investor wishes to invest capital in the Company, and the Company wishes to accept the investment under the following terms:",
            f"1. Investment Amount: The Investor agrees to invest an amount of <u>${investment_amount}</u> into the Company.",
            f"2. Investment Percentage: For the investment amount, the Investor will receive an equity stake of <u>{investment_percentage}%</u> in the Company.",
            "IN WITNESS WHEREOF, the Parties have executed this Agreement as of the date first above written."
        ]

        for clause in clauses:
            style = contract_clause_bold if 'WHEREAS' in clause or clause.startswith("IN WITNESS WHEREOF") else contract_clause
            elements.append(Paragraph(clause, style))
            elements.append(Spacer(1, 12))

        elements.append(Spacer(1, 24))

        signature_data = [
            [Paragraph(f"Investor Signature: <br/><br/><br/><u>{investor_name}</u>", contract_clause),
            Paragraph(f"Company Representative Signature: <br/><br/><br/><u>{company_name}</u>", contract_clause)]
        ]

        signature_table = Table(signature_data, colWidths=[3*inch, 3*inch], rowHeights=[0.75*inch])

        signature_table.setStyle(TableStyle([
            ('LINEBEFORE', (1, 0), (1, 0), 0.5, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),  # قد تحتاج لضبط هذه القيمة
            ('LINEBELOW', (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(signature_table)

        doc.build(elements)

        pdf = buffer.getvalue()
        buffer.close()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="investment_agreement.pdf"'

        return response
    else:
        return redirect('contract/deal_form.html')

def deal_form(request):
    if request.method == 'POST':
        return create_deal_pdf(request)
    return render(request, 'contract/deal_form.html')
