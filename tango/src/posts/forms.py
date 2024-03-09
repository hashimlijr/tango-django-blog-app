from django import forms
from tinymce.widgets import TinyMCE
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from markdownx.models import MarkdownxField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Post, Comment

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail',
        'categories', 'featured', 'previous_post', 'next_post')
        widgets = {
            'content': CKEditorWidget(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': "Type your comment",
        'id': "usercomment",
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('content', )