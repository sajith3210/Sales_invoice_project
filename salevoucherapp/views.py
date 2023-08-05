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
        # inv=None
  
        inv=invoice(bill_number=billno,product_name=pname,quantity=qty,rate=rate,amount=amt,total_amount=tot,gst=gs,add_prod_id=ad_pr_for_ky)
        inv.save()
        msg="Save successfully"
        dta['msg']=msg
        print("Save successfully")
  
    return render(request,'bill.html',context=dta)



def print_pdf(request):
        bill_lat=invoice.objects.latest('id')
        billno=bill_lat.bill_number
        bill_num=invoice.objects.filter(bill_number=bill_lat.bill_number)
        pdf = canvas.Canvas('invoice.pdf')
        # pdf.drawString(100, 450, f"Bill details from SS Mall")
        pdf.line(100,400,100,400 )
        pdf.drawString(70,400, "Bill Number" )
        pdf.drawString(150,400,  str(billno))

        pdf.drawString(70,350, "Product")
        pdf.drawString(140,350, "Quantity" )
        pdf.drawString(210, 350, "Rate")
        pdf.drawString(280, 350, "Amount" )
        pdf.drawString(350, 350, "GST" )
        pdf.drawString(420, 350, "Total Amount")

        
        inv_get_bill_no=invoice.objects.filter(bill_number=billno)
        first_lp=0
        x_axis_numb=70
        y_axis_numb=350
        for inv in inv_get_bill_no: 
                first_lp =first_lp+1
                if first_lp==1:
                    pdf.drawString(x_axis_numb,y_axis_numb-50, inv.product_name)

                x_axis_numb=x_axis_numb+70  
                pdf.drawString(x_axis_numb,y_axis_numb-50, str(inv.quantity))
                x_axis_numb=x_axis_numb+70 
                pdf.drawString(x_axis_numb,y_axis_numb-50, str(inv.rate))
                x_axis_numb=x_axis_numb+70 
                pdf.drawString(x_axis_numb,y_axis_numb-50, str(inv.amount))
                x_axis_numb=x_axis_numb+70 
                pdf.drawString(x_axis_numb,y_axis_numb-50, str(inv.gst))
                x_axis_numb=x_axis_numb+70 
                pdf.drawString(x_axis_numb,y_axis_numb-50, str(inv.total_amount))

                y_axis_numb=y_axis_numb - 50
                first_lp=0
                x_axis_numb=70

        pdf.save()
        with open('invoice.pdf', 'rb') as f:
            response = HttpResponse(f, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
        return response
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

