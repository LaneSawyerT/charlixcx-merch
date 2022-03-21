from django.shortcuts import render
from django.views import generic
from .models import NewsPost

# Create your views here.
class NewsPostList(generic.ListView):
    model = NewsPost
    queryset = NewsPost.objects.filter(status=1).order_by('created_on')
    template_name = "news.html"
    paginate_by = 4