from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
import json
from .models import Product, Contact, Orders, OrderUpdate

def index(request):
    # products=Product.objects.all()

    # print(products)

    # params={
    #     'products':products,
    #     'numberOfSlides':nSlides,
    #     'range':range(1,nSlides),
    #  }

    # allProducts=[
    #     [products,range(1,nSlides),nSlides],
    #     [products,range(1,nSlides),nSlides],
    # ]
    # params={
    #     'allProducts':allProducts
    # }

    allProducts=[]
    categorProduct=Product.objects.values('category')
    categories={item['category'] for item in categorProduct}
    for catgry in categories:
        prod=Product.objects.filter(category=catgry)
        slidesCount=len(prod)
        nSlides=slidesCount//4+ceil((slidesCount/4)-(slidesCount//4))
        allProducts.append([prod,range(1,nSlides),nSlides])

    params={'allProducts':allProducts}

    return render(request,'shop/index.html',params)


def searchMatch(query,item):
    # return true only if the query matches the item in any sort
    if(query in item.product_name.lower() or query in item.product_name.upper()
     or query in item.product_description.lower() or query in item.product_name.upper()
      or query in item.subcategory or query in item.category):
        return True
    else:
        return False


def search(request):
    query=request.GET.get('search')
    allProducts=[]
    categorProduct=Product.objects.values('category')
    categories={item['category'] for item in categorProduct}
    for catgry in categories:
        prodtemp=Product.objects.filter(category=catgry)
        prod=[item for item in prodtemp if searchMatch(query,item)]


        slidesCount=len(prod)
        nSlides=slidesCount//4+ceil((slidesCount/4)-(slidesCount//4))
        if len(prod)!=0:
            allProducts.append([prod,range(1,nSlides),nSlides])

    params={'allProducts':allProducts,'msg':""}
    if(len(allProducts)==0):
        params={'msg':'Please enter valid product'}

    return render(request,'shop/search.html',params)




def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=='POST':
        # in get instring word represent name in html tag that we given
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phoneNumber=request.POST.get('phone','')
        desc=request.POST.get('desc','')

        contact=Contact(name=name,email=email,phoneNumber=phoneNumber,desc=desc)
        contact.save()

    return render(request,'shop/contact.html')

def tracker(request):
    if request.method=='POST':
        order_id=request.POST.get('order_id','')
        email=request.POST.get('email','')

        try:
            order=Orders.objects.filter(order_id=order_id,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=order_id)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps([updates,order[0].item_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request,'shop/tracker.html')





def product(request ,myid):
    # Fetching id based on the product
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/product.html',{'product':product[0]},)



def checkout(request):
    if request.method =='POST':
        item_json=request.POST.get('item_json','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phoneNumber=request.POST.get('phoneNumber','')
        address_line_1=request.POST.get('address_line_1','')
        address_line_2=request.POST.get('address_line_2','')
        state=request.POST.get('state','')
        city=request.POST.get('city','')
        zip_code=request.POST.get('zip_code','')

        order=Orders(item_json=item_json,name=name,email=email,phoneNumber=phoneNumber
        ,address_line_1=address_line_1,address_line_2=address_line_2
        ,state=state,city=city,zip_code=zip_code)

        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc='The order has been placed')
        update.save()
        order_placed=True
        id=order.order_id
        return render(request,'shop/checkout.html',{'order_placed':order_placed, 'id':id})
    return render(request,'shop/checkout.html')