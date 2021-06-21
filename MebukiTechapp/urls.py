from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from MebukiTechapp import views

from MebukiTechapp.views import IndexView, PostDetailView, CategoryPostView, TagPostView, \
    SearchPostView

app_name = 'MebukiTechapp'
urlpatterns = [
                  path('', IndexView.as_view(), name='index'),
                  path('post/<int:pk>/', views.PostDetailView, name='post_detail'),
                  path('category/<str:category_slug>/', CategoryPostView.as_view(), name='category_post'),
                  path('tag/<str:tag_slug>/', TagPostView.as_view(), name='tag_post'),
                  path('search/', SearchPostView.as_view(), name='search_post'),
                  path('contact/', views.contact),
                  path('post/<int:pk>/like/', views.like),
              ]