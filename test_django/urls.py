from django.urls import path
from . import views #alternativa way if it used then it will be a views.index
from .views import *

urlpatterns = [
    # path("post/<int:id>/",view=dynamicUrl,name="dynamo"),
    path("",view=redirectUrl,name="redirection"),
    path("post/<str:slug>",view=views.details,name="post_detail"),
    path("home/",homePage,name="blog_dash"),
    path("contact/",contactPage,name="contact_details"),
    path("about/",aboutPage,name="about"),\
    path("create-new-post/",createNewPostPage,name="create_new_post"),

]