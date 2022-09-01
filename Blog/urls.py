from django.urls import path
from .views import post_list , post_detail , new_post ,edit_post ,delete_post #,Post_view,Post_Detail,Post_Delete

app_name = 'post'

urlpatterns = [
    path('' , post_list ,name='post_list'),
    path('<int:id>', post_detail , name='post_detail'),
    path('<int:id>/edit',edit_post, name = 'edit_post'),
    path('<int:id>/delete',delete_post , name='delete_post'),
    path('new' , new_post , name='new_post'),




    # path('cbv' , Post_view.as_view() , name = 'cbv_Post_list'),
    # path('cbv/<int:pk>',Post_Detail.as_view(), name='cbv_Post_detail'),
    # path('cbv/<int:pk>/delete>',Post_Delete.as_view(), name='cbv_Post_delete')
]