from django.forms import ModelForm
from django.forms.widgets import TextInput,Textarea
from products.models import Product

class ProductForm (ModelForm):
  class Meta:
    model=Product
    fields=["title","price","des"]

    widgets={

      "title":TextInput(),
      "price":TextInput(),
      "des":Textarea()
    } 

    labels={
       "title":"產品名稱","price":"產品價格","des":"產品敘述"

    }
