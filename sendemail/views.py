from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from xaqaton.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .forms import RegForm


def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = RegForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = RegForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            secondname = form.cleaned_data['secondname']
            age = form.cleaned_data['age']
            number = form.cleaned_data['number']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            team = form.cleaned_data['team']
            role = form.cleaned_data['role']
            data = form.cleaned_data['data']
            hack = form.cleaned_data['hack']
            a = f'''
            Почта: {email}
            Имя: {name}
            Фамилия: {surname}
            Отчество: {secondname}
            возраст: {age}
            номер: {number}
            Адрес: {address}
            Команда: {team}
            Роль в команде: {role}
            Персональные данных: {data}
            Положение: {hack}
            '''
            try:
                send_mail(f'{team} от {email}', a,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            # return redirect('success')
            messages.success(request, 'Спасибо! Ваша заявка отправлена.')

    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "mail/index.html", {'form': form})
