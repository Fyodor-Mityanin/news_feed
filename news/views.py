from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .forms import NewsForm, PageForm
from .models import News

from .forms import NEWS_ON_PAGE_CHOICES

posible_news_on_page = [int(x[0]) for x in NEWS_ON_PAGE_CHOICES]


def index(request):
    try:
        num_of_news = int(request.GET.get('news_on_page'))
    except (ValueError, TypeError):
        num_of_news = 10
    if num_of_news not in posible_news_on_page:
        num_of_news = 10
    page_form = PageForm(initial={'news_on_page': num_of_news})
    news_list = News.objects.all()
    paginator = Paginator(news_list, num_of_news)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page, 'paginator': paginator, 'page_form': page_form}
    )


def add_news(request):
    form = NewsForm(request.POST or None, files=request.FILES or None,)
    if form.is_valid():
        form.save()
        return redirect('news:index')
    return render(
        request,
        'new.html',
        {'form': form, }
    )
