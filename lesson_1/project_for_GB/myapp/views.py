from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    logger.info('Index page accessed!')
    html = '''
    <center><h1>Главная страница</h1>
    <br>
    <h3>Это мой первый сайт на Django, а это его главная страница!</h3>
    <h5>Нажми ↓ чтобы узнать подробности о авторе проекта</h5>
    <button onclick="window.location.href = 'http://127.0.0.1:8000/about/';">Узнать обо мне</button></center>
    '''
    return HttpResponse(html)

def about(request):
    logger.info('About page accessed!')
    html = '''
        <center><h1>Быков Иван</h1>
        <br>
        <p>Мужчина, 29 лет</p>
        
        <p style="background-color: Yellow; line-height: 2">Не ищет работу</p>
        
        <p><b>Контакты:</b></p>
        <p>8 (800) 555-35-35 лучше позвонить, чем у кого-то занимать!</p>
        <p>ivan@djc-media.ru</p>
        <p>https://github.com/DjonyCooper</p>
        
        <p>Не готов к переезду, готов к редким командировкам</p>
        <button onclick="window.location.href = 'http://127.0.0.1:8000/';">На главную</button></center>
        '''
    return HttpResponse(html)
