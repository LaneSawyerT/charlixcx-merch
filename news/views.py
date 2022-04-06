from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View

from django.http import HttpResponseRedirect
from .models import NewsPost, Category
from profiles.models import UserProfile

# Create your views here.
class NewsPostList(generic.ListView):
    
    model = NewsPost

    queryset = None

    template_name = "news.html"
    paginate_by = 4

    def get_queryset(self, **kwargs):
        if self.request.GET.get('filter'):
            category = get_object_or_404(Category, tag_name=self.request.GET.get('filter'))
            self.queryset = NewsPost.objects.filter(status=1, category=category.id).order_by("-created_on")
        else:
            self.queryset = NewsPost.objects.filter(status=1).order_by("-created_on")
        return self.queryset


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = NewsPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        user = get_object_or_404(UserProfile, user=request.user)
        liked = False
        if post.likes.filter(id=user.id).exists():
            liked = True

        return render(
            request,
            "post_details.html",
            {
                "post": post,
                "liked": liked,
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(NewsPost, slug=slug)
        user = get_object_or_404(UserProfile, user=request.user)

        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
        else:
            post.likes.add(user)
        
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))