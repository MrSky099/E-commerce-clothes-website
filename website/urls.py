"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('product_list/',views.product_list,name='product_list'),
    path('cart/',views.cart,name='cart'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('single-blog/',views.single_blog,name='single-blog'),
    path('blog/',views.blog,name='blog'),
    path('single-product/<int:id>',views.single_product,name='single-product'),
    path('Catagory/',views.Catagory,name='Catagory'),
    path('checkout/',views.checkout,name='checkout'),
    path('elements/',views.elements,name='elements'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('confirmation/',views.confirmation,name='confirmation'),
    path('cat/<int:id>',views.cat,name='cat'),
    path('add_to_cart/<int:id>',views.add_to_cart,name='add_to_cart'),
    path('minus/<int:id>',views.minus,name='minus'),
    path('plus/<int:id>',views.plus,name='plus'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('order/',views.order,name='order'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
