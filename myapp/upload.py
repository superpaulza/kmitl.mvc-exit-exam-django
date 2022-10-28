from django import forms
from .models import Meme
from django.core.validators import RegexValidator


# the model of upload form
class MemeUpload(forms.ModelForm):
    # validate input
    path = forms.CharField(min_length=5, max_length=500,
                           validators=[RegexValidator('^.*\.(jpg|JPG|jpeg|JPEG|gif|GIF|png|PNG)$', message='error')])

    # form model
    class Meta:
        model = Meme
        exclude = ['name', 'reach', 'like', 'share', 'comment', 'engagement']

    # validator exception
    def __init__(self, *args, **kwargs):
        super(MemeUpload, self).__init__(*args, **kwargs)
        self.fields['path'].error_messages = {
            'required': 'Please enter file path',
            'invalid': 'Invalid file type only accept .jpg,.jpeg,.gif,.png types'
        }
