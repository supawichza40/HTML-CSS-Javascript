from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = "posts"
urlpatterns = [
    
    path("",views.PostList.as_view(),name = "all"),
    path("new/",views.CreatePost.as_view(),name = "create"),
    path("by/<username>",views.UserPosts.as_view(),name = "for_user"),
    path("by/<username>/<int:pk>/",views.PostDetail.as_view(),name = "single"),
    path("delete/<int:pk>/",views.DeletePost.as_view(),name = "delete"),
    path("upload/",views.upload_file,name = "upload")
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
