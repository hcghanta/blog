from django.urls import path
# from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path(r'', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path(r'<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path(r'<int:post_id>/share/',
         views.post_share, name='post_share'),
    path(r'tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
]
