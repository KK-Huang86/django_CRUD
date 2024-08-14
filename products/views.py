from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from .form import ProductForm

# Create your views here.

def index(req):
  if req.method=="POST":
    form=ProductForm(req.POST)
    if form.is_valid:
      form.save()
      return redirect("product:index")
    else:
      return render(req,"pages/new.html",{"form":form})
  product=Product.objects.all()
  return render(req,"pages/index.html",{"products":product})

def show(req,id):
  product=get_object_or_404(Product,pk=id)
  if req.method=="POST":
    form=ProductForm(req.POST,instance=product)
    if form.is_valid:
      form.save()
      return redirect("product:show", product.id)
  return render(req,"pages/show.html",{"product":product})

def new(req):
  form=ProductForm()
  return render(req,"pages/new.html",{"form":form})

def edit(req,id):
  product=get_object_or_404(Product,pk=id)
  form=ProductForm(instance=product)
  return render(req,"pages/edit.html",{"product":product,"form":form})

def delete(req,id):
  product=get_object_or_404(Product,pk=id)
  product.delete()
  return redirect("product:index")

