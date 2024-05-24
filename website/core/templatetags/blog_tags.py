from django import template

from core.models import Category


register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.simple_tag()
def is_category_current(request, pk):
    return str(pk) in request.path

@register.simple_tag()
def is_comment_has_like(request, comment):
    return request.user in comment.likes.user.all()
