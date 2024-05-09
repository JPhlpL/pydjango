from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

    
blog_posts = [
    {
        'employee': 'Philip',
        'salary': 'Php 20.00',
    },
    {
        'employee': 'John',
        'salary': 'Php 30.00',
    }
]

def home(request):
    data = {
        'info': blog_posts
    }
    return render(request, 'welcome/home.html', data)

    # return HttpResponse('<h1> Blog Home </h1>')
    # data = {
    #     'title': 'Python',
    #     'content': 'Very very'
    # }
    # return render(request, 'welcome/home.html', data)
    # return HttpResponse('<h1> Blog Home </h1>')
