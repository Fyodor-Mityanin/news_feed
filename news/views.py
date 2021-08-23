from django.shortcuts import render, redirect
from .models import News
from django.core.paginator import Paginator
from .forms import NewsForm, PageForm


def index(request):
    try:
        num_of_news = int(request.GET.get('news_on_page'))
    except (ValueError, TypeError):
        num_of_news = 10
    page_form = PageForm(request.POST or None)
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
