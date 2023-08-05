from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from reportlab.pdfgen import canvas
# Create your views here.
def add_product(request):
    global add_prod_lat
    msg=""
    dta={'msg':msg}
    if request.method=="POST":
        pname=request.POST.get('pname').title()
        qty=request.POST.get('quantity')
        rate=request.POST.get('Rate')
        amt=request.POST.get('hid_amount')
        print("Amount is ",amt)
        gs=request.POST.get('GST')
        tot=request.POST.get('hide_tot_amt')
        print("Total amount is",tot)
        product_name_check=addproduct.objects.filter(product_name=pname) 
        if product_name_check.exists():
            msg="Prduct is already  available try to add new product"
            dta['msg']=msg
        else:
            add_p=addproduct(product_name=pname,quantity=qty,rate=rate,amount=amt,total_amount=tot,gst=gs)
            add_p.save()
            msg="Save successfully" 
            print("Save successfully")
            dta['msg']=msg
            
            add_prod_lat=addproduct.objects.latest("id")               
    return render(request,'add_product.html',context=dta)

def show_product(request):
    add_pr=addproduct.objects.all()
    return render(request,'show_product.html',{'add_pr':add_pr})

def bill_page(request):  #print page
    ad_prod=addproduct.objects.all()# this all product name display in dropdown button
    invoice_all=invoice.objects.all()
    bill_no=None
    if addproduct.objects.exists():
        if invoice.objects.exists():
            inv_lat=invoice.objects.latest("id")
            bill_no=inv_lat.bill_number+1
        else:
            bill_no=1
    else:
        return redirect('add_product')
    
    msg=""
    fail_bill_msg=""
    dta={'invoice_all':invoice_all,'msg':msg,'ad_prod':ad_prod,'bill_no':bill_no,'fail_bill_msg':fail_bill_msg,}
    if request.method=="POST":
        inv=None
        billno=request.POST.get('billno')
        pname=request.POST.get('prod_name')
        ad_pr_for_ky=addproduct.objects.get(product_name=pname)
        qty=request.POST.get('quantity')
        rate=request.POST.get('Rate')
        amt=request.POST.get('hid_amount')
        print("Amount is ",amt)
        gs=request.POST.get('GST')
        tot=request.POST.get('hide_tot_amt')
        print("Total amount is",tot)
        bill_num=invoice.objects.filter(bill_number=billno)
        inv=None
        if bill_num.exists():
            dta['fail_bill_msg']='Already this bill number is exists try again'
        else:
            inv=invoice(bill_number=billno,product_name=pname,quantity=qty,rate=rate,amount=amt,total_amount=tot,gst=gs,add_prod_id=ad_pr_for_ky)
            inv.save()
        msg="Save successfully"
        dta['msg']=msg
        print("Save successfully")
        pdf = canvas.Canvas('invoice.pdf')
        pdf.drawString(100, 450, f"Bill details from SS Mall")
        pdf.line(100,400,100,400 )
        pdf.drawString(100,400, "Bill Number" )
        pdf.drawString(280,400,  billno)

        pdf.drawString(100,350, "Product Name")
        pdf.drawString(280,350, pname)

        pdf.drawString(100,300, "Quantity" )
        pdf.drawString(280,300, qty)


        pdf.drawString(100, 250, "Rate")
        pdf.drawString(280,250, rate)


        pdf.drawString(100, 200, "Amount" )
        pdf.drawString(280,200, amt)

        pdf.drawString(100, 150, "Total Amount")
        pdf.drawString(280,150, tot)
        pdf.save()
        with open('invoice.pdf', 'rb') as f:
            response = HttpResponse(f, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
        return response
    return render(request,'bill.html',context=dta)

def edit_sale(request,pk):
    inv=invoice.objects.get(id=pk)
    if request.method=="POST":
        pname=request.POST.get('pname')

        qty=request.POST.get('quantity')
        rate=request.POST.get('Rate')
        amt=request.POST.get('hid_amount')
        print("Amount is ",amt)
        gs=request.POST.get('GST')
        tot=request.POST.get('hide_tot_amt')
        print("Total amount is",tot)
        inv=invoice(product_name=pname,quantity=qty,rate=rate,amount=amt,total_amount=tot,gst=gs,)
        inv.save() 
        print("Update successfully")
        return redirect('index')
    return render(request,'edit_sale.html',{'inv':inv})

def delete_sale(request,pk):
    inv=invoice.objects.get(id=pk)
    inv.delete()
    return redirect('index')


# def get_product(request):
#    prod_name=request.GET.get('pro_name')
#    prod=addproduct.objects.filter(product_name=prod_name)
#    serializer = prod(queryset, many=True)
#    data={'prod':prod}
#    return JsonResponse(data)

def get_product_data(request):
  productName = request.GET.get('product_name')
  product = addproduct.objects.filter(product_name=productName).first()
  data = {
    'quantity': product.quantity,
    'rate': product.rate,
    'amount': product.amount,
    'gst': product.gst,
    'total_amount': product.total_amount
  }
  return JsonResponse(data)

