from django.views.generic import ListView
from . models import Post, Category


class HomeView(ListView):
    template_name = "index.html"
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related("post_category")
    