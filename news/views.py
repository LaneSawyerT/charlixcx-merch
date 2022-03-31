from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import NewsPost

# Create your views here.
class NewsPostList(generic.ListView):
    model = NewsPost
    queryset = NewsPost.objects.filter(status=1).order_by('created_on')
    template_name = "news.html"
    paginate_by = 4


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = NewsPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_details.html",
            {
                "post": post,
                "liked": liked,
            },
        )