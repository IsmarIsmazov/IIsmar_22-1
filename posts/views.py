from django.shortcuts import render, redirect

from users.utils import get_user_from_request
from posts.models import Post, Comment, Category, Hashtag
from posts.forms import CommentCreateForm, PostCreateForm


# Create your views here.
PAGINATION_LIMIT = 4

def main(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        data = {
            'posts':posts
        }
        return render(request, 'layouts/main.html', context=data)
def posts_view(request):
    if request.method == 'GET':
        category_id = request.GET.get('category_id')
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        if category_id:
            posts = Post.objects.filter(category_id=category_id)
        else:
            posts = Post.objects.all()
        if search_text:
            posts = posts.filter(title__icontains=search_text)

        max_page = round(posts.__len__()/ PAGINATION_LIMIT)
        posts = posts[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]

        data = {
            'posts': posts,
            'user': get_user_from_request(request),
            'category_id': category_id,
            'current_page': page,
            'max_page': range(1, max_page+1)
        }

        return render(request, 'posts/posts.html', context=data)

def hashtags_view(request):
    if request.method == 'GET':
        data = {
            'hashtags': Hashtag.objects.all()
        }
        return render(request, 'posts/hashtags.html', context=data)

def post_detail_view(request, **kwargs):
    if request.method == 'GET':
        post = Post.objects.get(id=kwargs['id'])
        data = {
            'post': post,
            'comments': Comment.objects.filter(post=post),
            'form': CommentCreateForm
        }
        return render(request, 'posts/post_detail.html', context=data)
    if request.method == 'POST':
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                author_id=1,
                text=form.cleaned_data.get('text'),
                post_id=kwargs['id']
            )
            return redirect(f'/posts/{kwargs["id"]}/')
        else:
            post = Post.objects.get(id=kwargs['id'])
            comments = Comment.objects.filter(post=post)

            data = {
                'post': post,
                'comments': comments,
                'form': form
            }

            return render(request, 'posts/post_detail.html', context=data)





def categories_view(request, **kwargs):
    if request.method == 'GET':
        categories = Category.objects.all()

        data = {
            'categories': categories,
            'user': get_user_from_request(request)
        }

        return render(request, 'categories/categories.html', context=data)
def post_create_view(request):
    if request.method == 'GET':
        data = {
            'form': PostCreateForm
        }
        return render(request, 'posts/create.html', context=data)
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST)

        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                category=form.cleaned_data.get('category')
            )
            return redirect('/posts/')
        else:
            data = {
                'form': form
            }
            return render(request, 'posts/create.html', context=data)