from django.contrib import admin
from django.urls import include,path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from blogs import views as BlogsViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('category/', include('blogs.urls')),
    path('blogs/<slug:slug>/', BlogsViews.blogs, name='blogs'),
    # Search endpoint for blogs
    path('blogs/search/', BlogsViews.search, name='search'),
    
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
    
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
