from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('banter_like/<int:pk>', views.banter_like, name='banter_like'),
    path('banter_show/<int:pk>', views.banter_show, name='banter_show'),
    path('unfollow/<int:pk>', views.unfollow, name='unfollow'),
    path('follow/<int:pk>', views.follow, name='follow'),
    path('delete_banter/<int:pk>', views.delete_banter, name='delete_banter'),
    path('edit_banter/<int:pk>', views.edit_banter, name='edit_banter'),
    path('search/', views.search, name='search'),
    path('search_user/', views.search_user, name='search_user'),
    path('followers/<int:pk>/', views.followers, name='followers'),
    path('follows/<int:pk>/', views.follows, name='follows'),
    
]