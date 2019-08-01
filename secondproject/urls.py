
from django.contrib import admin
from django.urls import path
import blog.views
import portfolio.views
from django.conf import settings                #file
from django.conf.urls.static import static      

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('test/', blog.views.test, name="test"),
    path('blog/<int:blog_id>', blog.views.detail, name="detail"),
    path('blog/newpost/', blog.views.newpost, name="newpost"),
    path('blog/create/', blog.views.create, name="create"),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)