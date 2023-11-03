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
    path('addperson',views.addperson,name="addperson"),
    path('viewperson',views.viewperson,name="viewperson"),
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
    path('addperson',views.addperson,name="addperson"),
    path('viewperson',views.viewperson,name="viewperson"),
    path('changepassword',views.changepassword,name="changepassword"),
    path('delete_user',views.delete_user,name="delete_user"),
    path('additems',views.additems,name="additems"),
    path('a_view_category',views.a_view_category,name="a_view_category"),
    path('a_view_menu',views.a_view_menu,name="a_view_menu"),
    path('a_add_category',views.a_add_category,name="a_add_category"),
    #path('new',views.new,name="new"),


    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]