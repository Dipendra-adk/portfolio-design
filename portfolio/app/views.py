from django.shortcuts import redirect, render
from  django.contrib import messages
from app.models import Contact,Blogs

# Create your views here.
def home(request):
    return render(request, 'home.html')

def handleblog(request):
    posts=Blogs.objects.all() #get all blogs in the database
    context={"posts":posts} # passing as a dictionary
    return render(request,'handleblog.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    #getting the data from user and storing it in the admin interface or db.
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdescription=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdescription)
        query.save()
        messages.success(request, "Your message has been sent successfully")
       # messages.info(request,f"the name is {fname} & email is {femail} & your number is {fphoneno} & query is {fdescription}")
        return redirect('/contact')
        
    return render(request, 'contact.html')