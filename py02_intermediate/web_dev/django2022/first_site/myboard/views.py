from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Answer, Post
from .forms import PostForm

# Create your views here.
def index(request):
    # Post 목록 리스트
    post_list = Post.objects.order_by('-date')
    context = {'post_list': post_list}
    return render(request, 'myboard/post_list.html', context)

def detail(request, post_id):
    # Post 내용 출력
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'myboard/post_detail.html', context)

# Post 내용 생성
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            return redirect('myboard:index')
    else:
        form = PostForm()
        
    context = {'form':form}
    return render(request, 'myboard/post_form.html', context)

# 답글 저장 
def answer_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    answer = Answer(post=post, content=request.POST.get('content'), writer='Someone', date=timezone.now())
    answer.save()
    return redirect('myboard:detail', post_id=post.id)