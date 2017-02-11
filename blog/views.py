from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Comment
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import Http404
from django.core.mail import EmailMessage
from .forms import PostForm, CommentForm
from django.shortcuts import render,redirect

# for post
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


# for post detail of a post checked by post title
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# for new post
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


# post edit
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


#post save as draft
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


# from draft to publish
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


# delete post
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


#comment view
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


# comment approve
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


# comment remove
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


def contact(request):
    return render(request, 'blog/contact.html')

def about(request):
    return render(request,'blog/about.html')


def email_one(request):
    subject = "I am a text email"
    to = ['buddy@buddylindsey.com']
    from_email = 'test@example.com'

    ctx = {
        'user': 'buddy',
        'purchase': 'Books'
    }

    message = render_to_string('/email.txt', ctx)

    EmailMessage(subject, message, to=to, from_email=from_email).send()

    return HttpResponse('email_one')


def signUp(request):
    try:
        form=SignupForm()
        #student_form=StudentForm()
        if request.method=="POST":
            form=SignupForm(request.POST or None, request.FILES or None)
            #std_form=StudentForm(request.POST or None)
            if form.is_valid():
                username=request.POST.get('username',None)
                #usertype=request.POST.get('user_type',None)
                if username is not None and username != '':
                    user_list=USER.objects.all()
                    for i in user_list:
                        user=username==i.username
                        if user:
                            u_list = USER.objects.filter(username=username)
                            return HttpResponse('<script> alert("Already Exists"); </script>')
                    signUp_save = form.save(commit=False)
                    signUp_save.save()
                    #std=Student(id=signUp_save.id)
                    u = USER.objects.filter(username=username)
                    #std=Student(user_id=u.id)
                    #if std_form.is_valid():
                        #std_save.user_id=signUp_save
                        #std_save = std_form.save(commit=False)
                        #std_save.save()
                        #std_form.save()''
                    #if usertype=='1':

                return redirect("login")
            else:
                form=SignupForm()
                return  render(request,'registration/signUp.html')
        return  render(request,'registration/signUp.html')

    except:
        raise Http404

def mailshow(request):
    userr = User.objects.get(username=request.user)
    return render(request, 'blog/mail.html',{{ userr.email }})
