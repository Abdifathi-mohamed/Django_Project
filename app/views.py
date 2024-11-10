from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')
def base(request):
    return render(request, 'base.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def service(request):
    
    return render(request, 'service.html')
def blog(request):
    return render(request, 'blog.html')
def blog_details(request):
    return render(request, 'blog_details.html')
def team(request):
    return render(request, 'team.html')
def testimonial(request):
    return render(request, 'testimonial.html')
def project(request):
    return render(request, 'project.html')