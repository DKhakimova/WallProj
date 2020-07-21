from django.shortcuts import render, redirect
from log_reg_app.models import User
from .models import Message, Comment
from django.contrib import messages

# Create your views here.

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'post_messages': Message.objects.all(),
        'comments': Comment.objects.all(),
    }
    return render(request, 'dashboard.html', context)

def create_message(request):
    if request.method == "POST":
        errors = Message.objects.validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='create_message')
            return redirect('/wall')
        
    if request.method == "POST":
        message = request.POST['message']
        Message.objects.create(message=message, author_id = request.session['user_id'] )
    return redirect('/wall')

def delete_message(request):
    if request.method == "POST":
        message_to_delete = Message.objects.get(id=request.POST['message_id'])
        if message_to_delete.author.id == request.session['user_id']:
            message_to_delete.delete()
    return redirect('/wall')

def create_comment(request):
    if request.method == "POST":
        comment = request.POST['comment']
        Comment.objects.create(comment=comment, author_id = request.session['user_id'], message_id = request.POST['message_id'])
    return redirect('/wall')

def delete_comment(request):
    if request.method == "POST":
        comment_to_delete = Comment.objects.get(id=request.POST['comment_id'])
        if comment_to_delete.author.id == request.session['user_id']:
            comment_to_delete.delete()
    return redirect('/wall')