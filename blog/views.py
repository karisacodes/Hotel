from django.shortcuts import render

posts = [
    {
    'author': 'CoreyMs',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'April 2 , 2023'
}
,
{
        
    'author': 'Jane Doe',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'April 12 , 2023'

}
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
def me(request):
    return render(request, 'blog/about.html', {'title': 'About'})
def start(request):
    return render(request,'blog/quavo.html')
