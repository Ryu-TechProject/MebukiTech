from django.db.models import Count

from MebukiTechapp.models import Category, Tag


def common(request):
    context = {
        'categories': Category.objects.annotate(
            num_posts=Count('post')),

        'tags': Tag.objects.annotate(
            num_posts=Count('post')),
    }
    return context