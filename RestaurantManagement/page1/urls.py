from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

"""urlpatterns = [
    path('',views.index,name="index"),
    path('menu',views.menu,name="menu"),
    path('accounts/login/',views.loginpage,name="loginpage"),
    path('accounts/login/signup',views.signup,name="signup"),
    path('chome',views.chome,name="chome"),
    path('staffhome',views.staffhome,name="staffhome"),
    path('accounts/login/logout_user',views.logout_user,name="logout_user"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('customerprofile',views.customerprofile,name="customerprofile"),
    path('a_add_person',views.a_add_person,name="a_add_person"),
    path('a_view_person',views.a_view_person,name="a_view_person"),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]"""

urlpatterns = [
    path('',views.index,name="index"),
    path('menu',views.menu,name="menu"),
    path('accounts/login/',views.loginpage,name="loginpage"),
    path('signup',views.signup,name="signup"),
    path('accounts/profile/',views.chome,name="chome"),
    path('staffhome',views.staffhome,name="staffhome"),
    path('logout_user',views.logout_user,name="logout_user"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('customerprofile',views.customerprofile,name="customerprofile"),
    path('a_add_person',views.a_add_person,name="a_add_person"),
    path('a_view_person',views.a_view_person,name="a_view_person"),
    path('changepassword',views.changepassword,name="changepassword"),
    path('delete_user',views.delete_user,name="delete_user"),
    path('a_add_items',views.a_add_items,name="a_add_items"),
    path('a_view_category',views.a_view_category,name="a_view_category"),
    path('a_view_menu',views.a_view_menu,name="a_view_menu"),
    path('a_add_category',views.a_add_category,name="a_add_category"),
    path('a_edit_menu_item/<int:item_id>/',views.a_edit_menu_item,name="a_edit_menu_item"),
    path('a_view_subcategory/<int:item_id>/',views.a_view_subcategory,name="a_view_subcategory"),
    path('a_edit_subcategory/<int:item_id>/',views.a_edit_subcategory,name="a_edit_subcategory"),
    path('get_category_subcategory_data/', views.get_category_subcategory_data, name='get_category_subcategory_data'),
    path('a_add_subcategory/<int:item_id>/',views.a_add_subcategory,name="a_add_subcategory"),
    path('get_subcategories/', views.get_subcategories, name='get_subcategories'),
    path('a_status_menu/<int:item_id>/',views.a_status_menu,name="a_status_menu"),
    path('a_edit_category/<int:item_id>/',views.a_edit_category,name="a_edit_category"),
    path('a_status_category/<int:item_id>/',views.a_status_category,name="a_status_category"),
    path('a_search_menu/', views.a_search_menu, name='a_search_menu'),





    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]