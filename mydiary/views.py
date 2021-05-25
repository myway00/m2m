from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Content,Comment
from .forms import ContentForm,CommentForm
# Create your views here.
def home(request):
    posts = Content.objects.all()
    return render(request, 'home.html', {'posts_list':posts})

def new(request):
    if request.method == 'POST':#댓글을 달면 post가 실행이 되고 아래것들이 실행
        form = ContentForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else: #빈상태로 돌려주는게 얘, 댓글을 다는 순간 얘가 수행되고 redirect가 다시 이 함수를
        #불러와서 지금 상태는 post가 아니니깐 아래의 else를 수행하며
        #빈칸 만들어나오져
        form = ContentForm()
    return render(request, 'new.html',{'form':form})

def detail(request, index):
	post = get_object_or_404(Content, pk=index)
	comment_list = Comment.objects.filter(post=post)
	if request.method =="POST":
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			comment = comment_form.save(commit=False)
			comment.published_date = timezone.now()
			comment.post = post #index-pk-pk-index 
			comment.save()
			return redirect('detail', index = index)#이 인덱스도 같이 넘겨줘야함
	else:
		comment_form = CommentForm()
            #렌더는 탬플릿을 리턴은 url을 
	return render(request, 'detail.html', {'post':post, 'comment_list':comment_list,'comment_form': comment_form})
    #html로 가서 알려줄 것들을 나열해준 것 - 이 나열한 것들을 담은 html페이지를 리턴해, 그리고 리턴은 디테일을 호출
    #이때는 인덱스가 필요, 어떤 인덱스인지 알아야 페이지를 보여줄지 알아야하니깐
    #
def edit(request, index):
    post = get_object_or_404(Content, pk = index)
    if request.method=='POST':
        form = ContentForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now
            post.save()
            return redirect('detail', index=post.pk)
    else:
        form = ContentForm(instance=post)
    return render(request, 'edit.html',{'form':form})

def delete(request,pk):
    post = get_object_or_404(Content, pk=pk)
    post.delete()
    return redirect('home')

#pk가 있어야 동작
def delete_comment(request, index, comment_pk):
	comment = get_object_or_404(Comment, pk=comment_pk)
    #오브젝트는 객체, 코멘트는 클래스
    #코멘트라는 클래스에서 어떤 객체 뽑아올라면 반드시꼭 pk가 필요하다
    #따라서 클래스랑 pk가 들어가서 특정 객체를 지정해주는 것
    #만약 있으면 객체 데리고와
	comment.delete()
	return redirect('detail', index=index)

    #삭제를 하고 원래있던 detail 페이지로 넘어갈 것이야
