from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.CartView.as_view(), name="user_cart"),
    path("update/<int:item_id>", views.update_cart_item, name="update_item"),
    path("remove/<int:item_id>", views.remove_cart_item, name="remove_item"),
]
