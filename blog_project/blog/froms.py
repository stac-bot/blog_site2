from django import forms
from .models import Post, Comment

#create the form for the Post model
class PostForm(forms.ModelForm):

    class Meta():
        model =Post
        fields =('author','title','text',)

        #this is how we give the css styling to the widgets
        widgets ={
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea' 'postcontent'}),
            }
#create the model for the comments
class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields ={'author', 'text',}

        widgets ={
                'author': forms.TextInput(attrs={'class': 'textinputclass'}),
                'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
