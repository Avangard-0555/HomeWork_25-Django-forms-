from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def private_news(request):
    # Логика для страницы, доступной только авторизованным пользователям
    return render(request, 'news/private_news.html')

def public_news(request):
    # Логика для страницы, доступной всем пользователям
    return render(request, 'news/public_news.html')


#Шаг 8: Проверка доступа к страницам новостей

#Чтобы контролировать доступ к определенным страницам, используйте декоратор @login_required в представлениях. Например:

#from django.contrib.auth.decorators import login_required

#@login_required
#def private_news(request):
    # Логика для доступа к приватным новостям
    #return render(request, 'news/private_news.html')



















      
