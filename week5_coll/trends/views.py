from django.shortcuts import render, redirect
from .forms import KeywordForm
from .models import Keyword, Trend
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64


# Create your views here.
def keyword(request):
    keywords = Keyword.objects.all()
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')
    else:
        form = KeywordForm()
    context = {
        'form' : form,
        'keywords' : keywords,
    }
    return render(request, 'trends/keyword.html', context)


def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')


def crawling(request):
    keywords = Keyword.objects.all()
    trends = Trend.objects.all()
    
    for keyword in keywords:
        to_search = keyword.name
        url = f'https://www.google.com/search?q={to_search}'
        
        # 크롬 브라우저 열림
        driver = webdriver.Chrome()
        driver.get(url)
        
        # 열린 페이지 소스를 받아옴
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        detail = soup.select_one('div#result-stats')
        text = detail.text
        numbers = re.findall(r'\d+', text)
        
        trend = Trend()

        if to_search in trends:
            trend.result = ''.join(numbers)
            trend.search_period = 'all'
        else:
            trend.name = to_search
            trend.result = ''.join(numbers)
            trend.search_period = 'all'
            
        trend.save()

    
    context = {
        'keywords' : keywords,
        'trends' : trends,
    }
    
    return render(request, 'trends/crawling.html', context)


def crawling_histogram(request):
    plt.rcParams['font.family'] ='Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] =False
    trends = Trend.objects.all()
    x = []
    y = []
    for qu in trends:
        x.append(qu.name)
        y.append(qu.result)
        
    plt.clf()
    
    plt.bar(x, y)
    
    plt.title('Technology Trend Analysis')
    plt.ylabel('Result')
    plt.xlabel('Keyword')
    plt.legend(loc='upper right')
    
    plt.grid(True)
    
    buffer = BytesIO()
    
    plt.savefig(buffer, format='png')
    
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    
    buffer.close()
    
    context = {
        'chart_image' : f'data:image/png;base64,{image_base64}'
    }
    
    return render(request, 'trends/crawling_histogram.html', context)



def crawling_advanced():
    pass


