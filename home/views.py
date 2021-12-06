from fpdf import FPDF
from home.models import BillDetails
from django.http.response import FileResponse
from django.shortcuts import render



def index(request):
    context = {}
    return render(request,"index.html",context)

def get_Bill(request):
        # verifying the request method 
        if request.method == "POST":
            client_name = request.POST['client_name']
            client_email = request.POST['client_email']
            client_address = request.POST['client_address']
            client_gst = request.POST['client_gst']
            biller_name = request.POST['biller_name']
            biller_email = request.POST['biller_email']
            biller_address = request.POST['biller_address']
            biller_gst = request.POST['biller_gst']
            cost_service = request.POST['cost_service']
            tax_rate = request.POST['tax_rate']
            bank_accounts = request.POST['bank_accounts']
            tax_cost = (int(cost_service) * int(tax_rate))/100
            total_amount = int(cost_service) + int(tax_cost)
            post_query = BillDetails(client_name = client_name, client_email=client_email,client_address=client_address,client_gst=client_gst,biller_name=biller_name,biller_email=biller_email,biller_address=biller_address,biller_gst=biller_gst,cost_service=cost_service,tax_rate=tax_rate,bank_accounts=bank_accounts,total_amount=total_amount)
            # storing customer details into database
            post_query.save()

            #creating a dictionary with the given data
            context = {
                'Client name': client_name,
                'Client email':client_email,
                'Client address': client_address,
                'Client GST No': client_gst,
                'Biller name': biller_name,
                'Biller email': biller_email,
                'Biller address': biller_address,
                'Biller GST': biller_gst,
                'Cost Service':str(cost_service)+' /-',
                'Tax Rate': str(tax_rate)+'%',
                'Total Amount':str(total_amount)+' /-',
                'Bank Details':bank_accounts
            }

            # Now converting the dictionary to text file
            with open("convert.txt", 'w') as f: 
                for key, value in context.items(): 
                    f.write('%s : %s\n' % (key, value))
            # Now converting text file into pdf file
            val = text_to_pdf("convert.txt")

            # Creating a file response for the final output
            pdf = open('invoice.pdf', 'rb')
            response = FileResponse(pdf)

            #return the final response
            return response

#creating a function for converting text into pdf
# This entire function is only for converting text file into pdf file
def text_to_pdf(file):
    f = open(file,"r")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 20)
    pdf.cell(200, 10, txt = "Generated Invoice", ln = 1, align = 'C')
    pdf.set_font("Arial", size = 10)
    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
    pdf.set_font("Arial", size = 20)
    pdf.cell(200, 10, txt = "-----------------------------------------", ln = 1, align = 'C')
    pdf.output("invoice.pdf")

