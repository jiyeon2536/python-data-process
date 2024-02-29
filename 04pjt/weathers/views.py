from django.shortcuts import render
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64
# Create your views here.
csv_path = 'weathers/data/austin_weather.csv'


def problem1(request):
    df = pd.read_csv(csv_path)
    # 데이터(.csv)를 pandas dataframe 형식으로 저장
    context = {
        'df' : df,
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    df = pd.read_csv(csv_path)

    # 일 별 온도 비교를 위한 라인 그래프 생성
    df['Date'] = pd.to_datetime(df['Date'])

    x = df['Date']
    y = df['TempHighF']
    y1 = df['TempAvgF']
    y2 = df['TempLowF']

    plt.clf()

    plt.plot(x, y, label='High Temperature')
    plt.plot(x, y1, label='Average Temparature')
    plt.plot(x, y2, label='Low Temperature')

    plt.title('Temperature Variation')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.xlabel('Date')
    plt.legend(loc='lower center')

    plt.grid(True)    
    # 비어있는 버퍼 생성
    buffer = BytesIO()

    plt.savefig(buffer, format='png', dpi=200)

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}'
    }
    return render(request, 'weathers/problem2.html', context)
    

def problem3(request):
    # 월별 온도 비교를 위한 라인 그래프 생성
    df = pd.read_csv(csv_path)

    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    grouped_by_month = df.groupby(['Year', 'Month'])

    grouped_count = pd.DataFrame(grouped_by_month)

    # 전체 월 리스트
    month_list = []

    for i in range(len(grouped_count[0])):
        month = '-'.join(map(str, grouped_count[0][i]))
        month_list.append(month)
    
    high_m = grouped_by_month['TempHighF'].mean()
    aver_m = grouped_by_month['TempAvgF'].mean()
    low_m = grouped_by_month['TempLowF'].mean()

    plt.clf()

    plt.plot(month_list, high_m, label='High Temperature')
    plt.plot(month_list, aver_m, label='Average Temparature')
    plt.plot(month_list, low_m, label='Low Temperature')

    plt.title('Temperature Variation')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.xlabel('Date')
    plt.xticks(ticks=month_list)
    plt.locator_params(axis='x', nbins=len(month_list)/6)
    plt.legend(loc='lower right')

    plt.grid(True)    
    # 비어있는 버퍼 생성
    buffer = BytesIO()

    plt.savefig(buffer, format='png', dpi=200)

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}'
    }
    return render(request, 'weathers/problem3.html', context)


def problem4(request):
    # 기상 현상 발생 횟수 히스토그램 생성
    df = pd.read_csv(csv_path)
    eventdict = {
        'No Events':0
    }
    for event in df['Events']:
        event = event.split(',')
        for i in event:
            i = i.strip()
            if i:
                if i in eventdict:
                    eventdict[i] += 1
                else:
                    eventdict[i] = 1
            else:
                eventdict['No Events'] += 1


    x = list(eventdict.keys())
    y = list(eventdict.values())

    plt.clf()

    plt.bar(x, y)

    plt.title('Event Counts')
    plt.ylabel('Count')
    plt.xlabel('Events')

    plt.grid(True)    
    # 비어있는 버퍼 생성
    buffer = BytesIO()

    plt.savefig(buffer, format='png', dpi=200)

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}'
    }
    return render(request, 'weathers/problem4.html', context)



