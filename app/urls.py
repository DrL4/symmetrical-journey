from django.urls import path
from app.views import home,sport,ticket,orders,category,logout,login, signUp
urlpatterns = [
    path('',home.index,name='home_index' ),
    # Auth Paths
    # ============== login page =============
    path('login', logout.index, name='login_index'),
    path('user', login.loginUser, name="login_user"),
    
    # ============== signUp page =============
    path('signUp', signUp.index, name='signUp_index'),
    path('signUp/user', signUp.save, name='save_user'),
    
    # Category Paths
    path('category/',category.index,name='category_index' ),
    path('category/add/',category.add_index,name='add_category' ),
    path('category/update/<str:pk>',category.update_index,name='update_category'), 
    path('category/delete/<str:pk>',category.delete_index,name='delete_category'),  
    # urls for sport
    path('sports',sport.index,name='sport_index'),
    path('search/',sport.search,name='search'),
    # urls for ticket
    path('tickets',ticket.index,name='ticket_index'),
    # urls for orders
    path('orders',orders.index,name='orders_index'),
]
