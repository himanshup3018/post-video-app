from django.shortcuts import render,redirect
from .models import Tweet ,Video
from .forms import TweetForm, VideoForm , User_RegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request,'index.html')


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('create_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

def video_list(request):
    videos = Video.objects.all().order_by('date_posted')
    return render(request,'video_list.html',{'videos':videos})

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
        return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request,'tweet_form.html',{'form':form})
@login_required
def Video_create(request):
    if request.method == "POST":
        form = VideoForm(request.POST,request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
        return redirect('video_list')
    else:
        form = VideoForm()
    return render(request,'video_form.html',{'form':form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
        return redirect('tweet_list')

    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweet_form.html', {'form': form})
@login_required
def video_edit(request, video_id):
    video = get_object_or_404(Video,pk=video_id,user = request.user)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES,instance=video)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
        return redirect('video_list')

    else:
        form = VideoForm(instance=video)

    return render(request, 'video_form.html', {'form': form})


@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_conform.html',{'tweet':tweet})

@login_required

def video_delete(request,video_id):
    videos = get_object_or_404(Video,pk=video_id,user=request.user)
    if request.method == 'POST':
        videos.delete()
        return redirect('video_list')
    return render(request,'video_conform.html',{'videos':videos})

def register(request):
    if request.method == 'POST':
        form = User_RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('index')
    else:
        form = User_RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})









