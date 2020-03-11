from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))
    theme = forms.ChoiceField(choices=Video.THEME_CHOICES, widget=forms.Select(attrs={'class': 'browser-default'}))

    def __init__(self, *args, **kargs):
        super(VideoForm, self).__init__(*args, **kargs)

    class Meta:
        model = Video
        exclude = ('thumbs_up', 'thumbs_down', 'publish_date')
    