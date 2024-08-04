from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:pk>/comments/', views.load_comments, name='load_comments'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/toggle_favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('post/<int:pk>/translate/<str:lang>/', views.translate_post, name='translate_post'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', next_page='private_area'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('private/', views.private_area, name='private_area'),
    path('upload_profile_picture/', views.upload_profile_picture, name='upload_profile_picture'),
    path('upload_post_picture/<int:pk>/', views.upload_post_picture, name='upload_post_picture'),
]
