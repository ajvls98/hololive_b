from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import Hello_world

# Create your views here.

html_cond = '''
<div style="display:flex; justify-content: center; align-items: center">
<img src = "https://i.pinimg.com/564x/b8/60/70/b860700206194b5a6dcf62da391a54f5.jpg" alt = "이나니스" >
</div>
'''


def hello_world(request):

    if request.method == 'POST':

        temp = request.POST.get('hello_world_text_input')

        new_hello_world = Hello_world()
        new_hello_world.text = temp
        new_hello_world.save()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world.text})

    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'get 요청입니다.'})
