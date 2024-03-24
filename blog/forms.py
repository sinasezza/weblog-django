from django import forms
from django.forms.models import inlineformset_factory
from . import models

    
PostParagraphFormSet = inlineformset_factory(
    models.Post,models.PostParagraph, 
    fields=('topic', 'content', 'order','header_image'),
    extra=0,
    can_delete=True,
    widgets={
        'topic': forms.TextInput(attrs={'maxlength': 45, 'required': True}),
        'order': forms.NumberInput(attrs={'max': 100}),
        'content':forms.Textarea(attrs={'maxlength':1000}),
    }
)

# ===============================================

class PostStatusForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('status',)

# ===============================================

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = models.PostComment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'cols':50,'rows':4,'maxlength':300,'style':'font-size:25px;font-style:italic;'})
        }