from django.urls import path,include
from users import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('register/',views.registerationPage,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view, name= 'logout'),
    path('reserchers/',views.reserchers, name='reserchers'),
    path('createpannel/',views.User_pannel_creation,name='createpannel'),
    path('myprofiles/',views.myprofiles,name='myprofiles'),
    path('editprofile/<int:p_id>',views.editprofile,name='editprofile'),
    path('search/',views.searchfunction,name='search'),
    path('delete/<int:d_id>',views.delete,name='delete'),
]

