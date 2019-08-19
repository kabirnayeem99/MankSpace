# post/views.py
from django.views.generic import (
    ListView,
    DetailView,
)

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import BlogPost, Category
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class PostListView(ListView):
    model = Category
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'post_create.html'
    fields= '__all__'
    login_url = 'login' # User without login cannot post, rather will redirect to the login page

    def form_valid(self, form):
        """
        Only the logged in user
        can create post.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    template_name = 'post_edit.html'
    fields = [
        'title',
        'body',
    ]
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        """
        Only this certain writer can edit this post
        """
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        """
        Only this certain writer can delete this post
        """
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



