from django.urls import path

from . import views

app_name = 'olive'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('shop/', views.ShopView.as_view(), name='shop'),
    # path('shop/<category>', views.ShopView.as_view(), name='shop_category'),
    path('<int:olive_id>/', views.DetailView.as_view(), name='detail'),
    path('order/<int:olive_id>/', views.OrderView.as_view(), name='order'),
    path('checkout/<int:olive_id>/', views.CustomerFormView.as_view(), name='checkout'),

]
