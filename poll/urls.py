from django.urls import path
from . import views
from  .views import *
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload-posts'),
    path('update/<int:post_id>', views.update_post),
    path('delete/<int:post_id>', views.delete_post),
    path('post/<slug:post_slug>',views.show_post,name = 'post'),
    path('addpage/', addpage,name = 'add_page'),
    path('mail/',send_message)



]