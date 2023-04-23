from django.shortcuts import redirect , get_object_or_404
from django.views.generic import View , TemplateView , ListView , DeleteView , CreateView , UpdateView ,DetailView , FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.db import transaction
from . import models,forms

class HomePageView(TemplateView):
    template_name = 'home_page/home_page.html'

# =======================================================

class PostListView(ListView):
    template_name = 'blog_pages/post_list_page.html'
    context_object_name = 'posts'
    # paginate_by = 9
    
    def get_queryset(self):
        published_post = models.Post.objects.filter(post_status='published')
        return published_post.order_by('-publish_date')
         
# =======================================================

class PostDetailView(DetailView):
    model = models.Post
    context_object_name = 'post'
    template_name = 'blog_pages/post_detail_page.html'
    
    def get_context_data(self, **kwargs): 
        context         = super().get_context_data(**kwargs)
        post_comments   = models.PostComment.objects.filter(post_id__exact = context['post'].id,active=True,)
        context['post_comments'] = post_comments
        context['comment_form']  = forms.PostCommentForm()
        return context

# =======================================================

class PostCommentCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = models.PostComment
    form_class = forms.PostCommentForm
    template_name = 'blog_pages/post_detail_page.html'
    context_object_name = 'post'
    success_message = 'Comment is Posted Success fully , it will be shown when admins confirm it'
    
    def form_valid(self, form):
        post = models.Post.objects.get(pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blog:post-detail', kwargs={'pk': self.kwargs['pk'], 'slug': self.kwargs['slug']})


# =======================================================

class PostCombine_detail_comment_View(View):
    
    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostCommentCreateView.as_view()
        return view(request, *args, **kwargs)

# =======================================================

class PostCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = models.Post
    template_name = 'blog_forms/post_create_form.html'
    success_url = reverse_lazy('authentication_app:user-panel')
    login_url = '/auth/login/'
    fields = ['title', 'post_header_image']
    success_message = 'post created successfully'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['paragraphs'] = forms.PostParagraphFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            # Create a new instance of the Post model
            post = models.Post()
            post.post_author = self.request.user
            data['paragraphs'] = forms.PostParagraphFormSet(instance=post)
        return data

    def form_valid(self, form):
        form.instance.post_author = self.request.user
        with transaction.atomic():
            self.object = form.save()
            formset = forms.PostParagraphFormSet(self.request.POST, self.request.FILES, instance=self.object)
            if formset.is_valid():
                formset.save()
        return super().form_valid(form)
    
# =======================================================
  
class PostUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = models.Post
    template_name = 'blog_forms/post_update_form.html'
    success_url = reverse_lazy('authentication_app:user-panel')
    login_url = '/auth/login/'
    fields = ['title', 'post_header_image']
    success_message = 'post updated successfully'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['paragraphs'] = forms.PostParagraphFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['paragraphs'] = forms.PostParagraphFormSet(instance=self.object)
        return data
    
    def form_valid(self, form):
        form.instance.post_author = self.request.user
        form.instance.post_slug = slugify(form.instance.title)
        with transaction.atomic():
            self.object = form.save()
            formset = forms.PostParagraphFormSet(self.request.POST, self.request.FILES, instance=self.object)
            if formset.is_valid():
                formset.save()
        return super().form_valid(form)


# =======================================================

class PostStatusUpdateView(LoginRequiredMixin,View):
    model = models.Post
    form_class = forms.PostStatusForm
    success_url = reverse_lazy('authentication_app:user-panel')
    login_url = '/auth/login/'
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            post = get_object_or_404(self.model, pk=self.kwargs.get('pk'))
            post.post_status = form.cleaned_data['post_status']
            post.save()
            data = {'success': True}
        else:
            data = {'success': False, 'errors': form.errors}
        return JsonResponse(data)

# =======================================================

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Post
    success_url = reverse_lazy('authentication_app:user-panel')
    login_url = '/auth/login/'
       
# =======================================================