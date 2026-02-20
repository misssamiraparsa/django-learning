from django.shortcuts import render
from datetime import date

all_posts = [
    {
        'slug': 'learn-django',
        'title': 'my first django project',
        'author': 'Samira Parsa',
        'image': 'django.png',
        'data': date(2026, 3, 11),
        'short_description': 'this is my first project:D',
        'content': """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe teneturLorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe teneturLorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
        """
    },

    {
        'slug': 'learn-kotlin',
        'title': 'my first django project',
        'author': 'zahra Parsa',
        'image': 'ml.png',
        'data': date(2026, 3, 12),
        'short_description': 'this is my first project:D',
        'content': """
     Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
         perspiciatis quod soluta veritatis?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe teneturLorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe teneturLorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe tenetur Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
         deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
     """
    },

    {
        'slug': 'learn-python',
        'title': 'my first django project',
        'author': 'Sima Parsa',
        'image': 'python.png',
        'data': date(2026, 3, 4),
        'short_description': 'this is my first project:D',
        'content': """
     Lorem ipsum dolor sit amet, consectetur adiLorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe teneturLorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe teneturLorem ipsum dolor sit amet, consectetur adipisicing elit. Ad aliquid dicta, eius eos eum eveniet
            perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
            deleniti est fugit officiis porro quia saepe teneturpisicing elit. Ad aliquid dicta, eius eos eum eveniet
         perspiciatis quod soluta veritatis? Alias atque ducimus facere odit pariatur! Alias, aspernatur consequuntur
         deleniti est fugit officiis porro quia saepe tenetur, veniam veritatis voluptatem voluptatum?
     """
    }
]

def get_date(post):
    return post['data']

def index(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-2:]
    return render(request, 'blog/index.html', {
        'latest_posts': latest_posts
    })

def posts(request):
    context = {
        'all_posts' : all_posts
    }
    return render(request, 'blog/all-posts.html', context)

def single_post(request,slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post' : post
    })
