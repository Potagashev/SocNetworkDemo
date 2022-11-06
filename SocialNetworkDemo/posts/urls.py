from django.urls import path

from .views import home, get_post, add_post, add_comment

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:post_id>/', get_post, name='post_details'),
    path('add_post/', add_post, name='add_post'),
    path('add_comment/<int:post_id>', add_comment, name='add_comment'),

]
