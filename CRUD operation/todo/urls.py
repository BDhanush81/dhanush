from django.contrib import admin
from django.urls import path,include
from todo import views

urlpatterns = [
    path('',views.admin),
    path('storedata',views.storedata),
    path('table',views.table),
    path('modifystd/<int:d>',views.update),
    path('changetodo',views.changetodo),
    path('deletestd/<int:d>',views.delete),
    path('search-result/',views.productserach,name='product-search'),

]
