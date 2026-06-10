from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic.list import ListView
from article_module.models import Article
from jalali_date import datetime2jalali, date2jalali


# class ArticleView(View):
#    def get(self, request):
#        articles = Article.objects.filter(is_active=True)
#        context = {
#            'articles': articles
#        }
#        return render(request, 'article_module/articles_page.html', context)

class ArticleListView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'article_module/articles_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        context['date'] = date2jalali(self.request.user.date_joined)
        return context
