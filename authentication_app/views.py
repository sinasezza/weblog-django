from django.shortcuts import render , redirect
from django.views.generic import View , DeleteView , DetailView , UpdateView
from django.contrib.auth.views import LoginView , LogoutView 
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages 
from django.urls import reverse_lazy
from . import models,forms
import blog.models as blog_models

class UserSignupView(View):
    
    def get(self,request):
        if request.user.is_authenticated:
            messages.warning(request,'you are already loged in , please log out and try again')
            return redirect('authentication_app:user-panel')
        step_one_form   = forms.UserSignupForm_Step01()
        step_two_form   = forms.UserSignupForm_Step02()
        step_three_form = forms.UserSignupForm_Step03()
        
        context = {'form1':step_one_form,'form2':step_two_form,'form3':step_three_form}
        
        return render(request,'authentication_app/signup_form.html',context=context)
    
    # ===========================================
    
    def post(self,request):
        step_one_form   = forms.UserSignupForm_Step01(request.POST)
        step_two_form   = forms.UserSignupForm_Step02(request.POST)
        step_three_form = forms.UserSignupForm_Step03(request.POST,request.FILES)
        if step_one_form.is_valid() and step_two_form.is_valid() and step_three_form.is_valid():
            user = models.AuthUser.objects.create_user(
                username    = step_one_form.cleaned_data['username'],
                phone_number= step_one_form.cleaned_data['phone_number'],
                password    = step_one_form.cleaned_data['password1'],
                 
                first_name  = step_two_form.cleaned_data['first_name'],
                last_name   = step_two_form.cleaned_data['last_name'],
                email       = step_two_form.cleaned_data['email'],
                age         = step_two_form.cleaned_data['age'],
                bio         = step_two_form.cleaned_data['bio'],
                
                profile_photo=step_three_form.cleaned_data['profile_photo']
            )
            login(request, user)
            return redirect('authentication_app:user-panel')
        else:
            context = {'form1':step_one_form,'form2':step_two_form,'form3':step_three_form}
            return render(request, 'authentication_app/signup_form.html',context=context)
    
# ================================================

class UserLoginView(LoginView):
    template_name = 'authentication_app/login_form.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('authentication_app:user-panel')

# ================================================

class UserLogoutView(LoginRequiredMixin,LogoutView):
    template_name = 'authentication_app/logout_form.html'
    next_page = reverse_lazy('blog:post-list')
    login_url = 'authentication_app:login'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
# ================================================

class UserDeleteView(LoginRequiredMixin,DeleteView):
    model = models.AuthUser
    template_name = 'authentication_app/delete_account_form.html'
    success_url = reverse_lazy('blog:post-list')
    login_url = 'authentication_app:login'

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        logout(request)
        return response
    
# ================================================

class UserProfileView(DetailView):
    model = models.AuthUser
    template_name = 'authentication_app/user_profile.html'
    context_object_name = 'user'
    
# ================================================

class UserPanelView(LoginRequiredMixin,DetailView):
    model = models.AuthUser
    template_name = 'authentication_app/user_panel.html'
    context_object_name = 'user'
    login_url = 'authentication_app:login'
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context     = super().get_context_data(**kwargs)
        user_posts  = blog_models.Post.objects.filter(author_id=self.request.user.id)
        context['posts'] = user_posts.order_by('-publish_date')
        return context
    
# ================================================

class UserChangeProfileView(LoginRequiredMixin, UpdateView):
    model = models.AuthUser
    form_class = forms.UserChangeProfileForm
    template_name = 'authentication_app/change_profile_form.html'
    login_url = 'authentication_app:login'
    success_url =  reverse_lazy('authentication_app:user-panel')
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        # Save the updated user object
        response = super().form_valid(form)

        # Authenticate the user with their new password
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['new_password'],
        )

        # Log the user in
        login(self.request, user)

        return response
    
# ================================================

