from django.shortcuts import render, redirect
from django.conf.global_settings import STATIC_ROOT
from django.shortcuts import render
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from MebukiTechapp.form import CommentForm
from MebukiTech.settings import STATIC_URL
from MebukiTechapp.models import Post, Category,Tag,Comment
from django.core.mail import send_mail
from django.contrib import messages
import os


# class PostDetailView(DetailView):
#     # queryset = Post.objects.all()
#     model = Post
#     template_name = 'post_detail.html'

def PostDetailView(request, pk):
    obj = Post.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST.get('like_count', None):
            obj.like_count += 1
            obj.save()
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.article = obj
                comment.save()
    comments = Comment.objects.filter(article=obj)
    context = {
        'post': obj,
        'comments' : comments,
    }

    return render(request, 'post_detail.html', context)


class IndexView(ListView):
    queryset = Post.objects.all()
    template_name = 'index.html'
    paginate_by = 10


class CategoryListView(ListView):
    queryset = Category.objects.annotate(
        num_posts=Count('post')
    )


class TagListView(ListView):
    queryset = Tag.objects.annotate(
        num_posts=Count('post')
    )


class CategoryPostView(ListView):
    model = Post
    template_name = 'category_post.html'
    paginate_by = 10

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        qs = super().get_queryset().filter(category=self.category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class TagPostView(ListView):
    model = Post
    template_name = 'tag_post.html'
    paginate_by = 10

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        qs = super().get_queryset().filter(tags=self.tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context


class SearchPostView(ListView):
    model = Post
    template_name = 'search_post.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        lookups = (
                Q(title__icontains=query) |
                Q(main__icontains=query) |
                Q(category__name__icontains=query) |
                Q(tags__name__icontains=query)
        )
        if query is not None:
            qs = super().get_queryset().filter(lookups).distinct()
            return qs
        qs = super().get_queryset()
        return qs

    def get_context_date(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

def contact(request):
    context = {}
    if request.method == "POST":
        subject = 'お問い合わせがありました'
        message = """お問い合わせがありました。\n名前:{}\nメールアドレス:{}\n内容:{}""".format(
        request.POST.get('name'),
        request.POST.get('email'),
        request.POST.get('contact'))
        #--- \n　改行コード
        email_from = 'llongjie2@gmail.com'
        email_to = ['llongjie2@gmail.com',]
        # email_from = os.environ['DEFAULT_EMAIL_FROM']
        # email_to = [os.environ['DEFAULT_EMAIL_FROM'],]
        send_mail(
            subject,
            message,
            email_from,
            email_to,
        )
        messages.success(request, 'お問い合わせいただきありがとうございます')

    return render(request, 'contact.html', context)

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

@ensure_csrf_cookie
def like(request, pk):
    d = {"message":"error"}
    if request.method == 'POST':
        obj = Post.objects.get(pk=pk)
        obj.like_count += 1
        obj.save()
        d["message"] = "success"
    return JsonResponse(d)
