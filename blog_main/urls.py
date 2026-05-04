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
    path('<slug:slug>/', BlogsViews.blogs, name='blogs'),
    
    path('blogs/search/', BlogsViews.search, name='search')
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
