from django.shortcuts import render
from django.http import HttpResponse
from makeup.models import Shop
from makeup.models import Makeup,Skincare,Digitalstuff, Comment
from django.views import generic
# Create your views here.

#def Shops(request):
#    shops=Shop.objects.all()
#    context={
#        "shoplist":shops
#    }
#
#    return render(request,"makeup/shoplist.html",context)

class Shops(generic.ListView):
    queryset = Shop.objects.all()
    template_name = 'makeup/shoplist.html'
    context_object_name =  'shoplist'


#def shop_details(request , shop_id):
#    shop = Shop.objects.get( pk = shop_id)
#    context = {
#        "shopha": shop,
#        }
#    return render(request,"makeup/shop_details.html",context)  

class Shop_details(generic.shop_details):
    model = Shop
    template_name = 'makeup/shop_details.html'
#    context_object_name =  'shopha'

#    def get_queryset(self):
#        return Shop.objects.get( pk=self.request.Shop['shop_id'])

    

def comments(request):
    comments = Comment.objects.all() 
    context = {
        "comments" : comments,
    }
    return render(request,"makeup/shop_details.html",context)

def skincareposts(request):
    skincare_post = Skincare.objects.all()
    context = {
        "skinposts":skincare_post,    
    }
    return render(request, "makeup/skincareposts.html",context)



def makeupposts(request): 
    makeup_post = Makeup.objects.all()
    context = {
        "makeupposts":makeup_post,
    }
    return render(request, "makeup/makeuppost.html",context)


def allposts(request): 
    makeup_posts = Makeup.objects.all()
    skincare_posts = Skincare.objects.all()
    digitalstuff_posts = Digitalstuff.objects.all()
    context = {
        "makeupposts":makeup_posts,
        "skincareposts":skincare_posts,
        "digitalstufposts":digitalstuff_posts,
    }
    return render(request, "makeup/allposts.html",context)

##


