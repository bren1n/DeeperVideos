from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from django.http import HttpResponseRedirect


def list_videos(request):
    all_videos = Video.objects.all()
    form = VideoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'home.html', {'all_videos': all_videos, 'form': form})

def delete_video(request, video_id):
    video = Video.objects.get(id=video_id)
    video.delete()
    return HttpResponseRedirect('/')

def thumbs_video(request, video_id, thumb_type):
    video = Video.objects.get(id=video_id)
    if thumb_type == 1:
        video.thumbs_up += 1
    else:
        video.thumbs_down += 1
    video.save()
    return HttpResponseRedirect('/')

def rank_themes(request):
    themes = Video.THEME_CHOICES
    themes_dict = []
    themes_list = []
    for theme in themes:
        themes_objects = {}
        thumbs_up = 0
        thumbs_down = 0
        score = 0
        all_theme_videos = Video.objects.filter(theme=theme[1])
        for video in all_theme_videos:
            thumbs_up += video.thumbs_up
            thumbs_down += video.thumbs_down
            score += (video.thumbs_up - (video.thumbs_down/2)) 
            print(thumbs_up - (thumbs_down/2), video.title)
            print(score)
        themes_objects.update({'theme': {'name': theme[1], 'thumbs_up': thumbs_up, 'thumbs_down': thumbs_down, 'score': score}})
        themes_dict.append(themes_objects)
    
    
    themes_dict = sorted(themes_dict, key=lambda k: k['theme']['score'], reverse=True)
    for x in themes_dict:
        obj = []
        obj.append(x['theme']['name'])
        obj.append(x['theme']['thumbs_up'])
        obj.append(x['theme']['thumbs_down'])
        obj.append(x['theme']['score'])
        themes_list.append(obj)
    return render(request, 'rank.html', {'themes': themes_list})


