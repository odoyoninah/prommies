from django.conf import settings
from django.urls import path,include
from django.contrib import admin
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('account/', include('django.contrib.auth.urls')), 
    path('uploadproject/', views.uploadproject, name='uploadproject'),
    path('api/prommies/',views.PrommiesView.as_view()),
    path('apikey/',views.apikey,name='apikey'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)