from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post,AboutPage
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm,PostForm

blog_title = "David post"


# posts = [
#         {
#             "id": "1",
#             "title": "Olympics",
#             "description":"paris olympics starts in 2024",
#             "content": "post 1 content",
#             "category": "sport",
#         },
#         {
#             "id": "2",
#             "title": "Toy story 4",
#             "description":"disney realesed a poster",
#             "content": "post 2 content",
#             "category": "kids",
#         },
#         {"id": "3", "title": "Briyani", "content": "post 3 content", "category": "food"},
#         {
#             "id": "4",
#             "title": "Election result",
#             "description":"the election realesd a new announcement",
#             "content": "post 4 content",
#             "category": "politics",
#         },
#         {
#             "id": "5",
#             "title": "No more fee",
#             "description":"there is free education offered by seemaan",
#             "content": "post 5 content",
#             "category": "Educations",
#         },
#         {
#             "id": "6" ,
#             "title": "Libra goes to peak",
#             "description":"there is no more worry for libra sign",
#             "content": "post 6 content",
#             "category": "Astrology",
#         },
#     ]
# Create your views here.
def homePage(request):

    posts = Post.objects.all()
    pages = Paginator(posts, 6)
    pg_no = request.GET.get("page")
    page_obj = pages.get_page(pg_no)
    return render(
        request=request,
        template_name="html/jobs.html",
        context={"blog_title": blog_title, "page_obj": page_obj},
    )


def details(req, slug):
    # post = next((item for item in posts if item['id'] == post_id),None)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post is {post}')
    try:
        post = Post.objects.get(slug=slug)
        related_post = Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("post does not exist")
    return render(
        request=req,
        template_name="html/details.html",
        context={"post": post, "related_post": related_post},
    )


# def dynamicUrl(req, id):
#     return HttpResponse(f"ID is {id}")


def contactPage(req):
    if req.method == "POST":
        form_obj = ContactForm(req.POST)
        # form_obj.cleaned_data['name']
        logger = logging.getLogger("TESTING")
        if form_obj.is_valid():
            form_obj.save()
            logger.debug(
                f"submited data is {form_obj.cleaned_data['name']} {form_obj.cleaned_data['email']} {form_obj.cleaned_data['message']}"
            )
        else:
            logger.debug("form validation is failed ")

    return render(
        request=req,
        template_name="html/contact.html",
    )

def createNewPostPage(req):
    if req.method == "POST":
        new_post_form = PostForm(req.POST)
        logger = logging.getLogger("TESTING")
        if new_post_form.is_valid():
            title = new_post_form.cleaned_data['title']
            content = new_post_form.cleaned_data['content']
            img = new_post_form.cleaned_data['img']
            category = new_post_form.cleaned_data['category']
            Post.objects.create(
                title=title,
                content=content,
                img=img,
                category=category
            )
            logger.debug(f"new post created with title {title} ")
        else :
            logger.debug("new post form validation is failed ")
            
    return render(
        request=req,
        template_name="html/create_post.html",
        context={"form":PostForm()}
    )

def aboutPage(req):
    about = AboutPage.objects.first()
    about_content = about.content if about is not None else ""
    return render(
        request=req,
        template_name="html/about.html",
        context={"about_content":about_content}
    )


def redirectUrl(req):
    return redirect(reverse("blog_dash"))
