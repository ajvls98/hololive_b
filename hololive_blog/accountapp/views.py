from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

html_cond = '''
<div style="display:flex; justify-content: center; align-items: center">
<img src = "https://i.pinimg.com/564x/b8/60/70/b860700206194b5a6dcf62da391a54f5.jpg" alt = "이나니스" >
</div>
'''


def hello_world(request):
    return render(request, 'base.html')
