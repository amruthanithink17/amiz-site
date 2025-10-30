from django.urls import path
from . import views

urlpatterns = [
    # Main Pages
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('mens/', views.mens, name='mens'),
    path('womens/', views.womens, name='womens'),
    path('kids/', views.kids, name='kids'),
    path('accessories/', views.accessories, name='accessories'),
    path('sales/', views.sales, name='sales'),
    path('contact/', views.contact, name='contact'),
    path('shipping/', views.shipping, name='shipping'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('cart/', views.cart, name='cart'),
     # 👇 add these
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove-from-wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),

    path('orders/', views.orders, name='orders'),
    path('proceed_order/', views.proceed_order, name='proceed_order'),

    # Authentication Pages
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('account/', views.account, name='account'),
    path('profile/', views.profile, name='profile'),  # 👈 Add this
    #path('orders/', views.orders, name='orders'),  # 👈 add this
]
