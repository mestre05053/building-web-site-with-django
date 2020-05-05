from django.shortcuts import render, redirect

# Create your views here.

from blog.models import BlogPost
from blog.forms import CreateBlogPostForm
from account.models import Account

def create_blog_view(request):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect ('must_authenticate')

	form = CreateBlogPostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		obj = form.save(commit=False) #*(commit=false) guarda el formulario despues que los campos ya fueron validados 
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		form = CreateBlogPostForm()

	context['form'] = form


	return render (request, "blog/create_blog.html", context)