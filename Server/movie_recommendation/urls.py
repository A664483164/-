from django.contrib import admin
from django.urls import path
from webApp.views import user_List,to_user_home,login,go_movie
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'login/',login),
    path(r'movies/<int:page>',go_movie,name='movies'),
    path('user_List/<int:page>',user_List,name='user_List'),
    path('to_user_home/<int:u_id>',to_user_home),
]
