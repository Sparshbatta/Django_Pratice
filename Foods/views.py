# i have created this file- SPARSH
from django.shortcuts import render,reverse
from django.http import HttpResponse

# def index(request):
#     return HttpResponse('''<h1>Hello <a href="https://en.wikipedia.org/wiki/COVID-19_pandemic">Covid-19 Pandemic</a></h1>''')
# def about(request):
#     return HttpResponse('''<h1><a href="https://www.youtube.com/watch?v=IsLyduxZ9sc&list=PLX9Zi6XTqOKQ7TdRz0QynGIKuMV9Q2H8E"> About Us</a></h1>''')

def index(request):
    params={'food':'pizza','chain':'dominos'}
    return  render(request,'index.html',params)

def analyze(request):
    global context
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    punc_list='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    rmnewline=request.POST.get('rmnewline','off')
    spaceremove=request.POST.get('spaceremove','off')
    charcount=request.POST.get('charcount','off')
    result=djtext
    if removepunc=='on':
        result=''
        for char in djtext:
            if char not in punc_list:
                result=result+char
    if fullcaps=='on':
        result=result.upper()
    if spaceremove=='on':
        result=list(result)
        result1=''
        for char in result:
            if char!=' ':
                result1+=char

        result=result1
    if rmnewline=='on':
        result = list(result)
        print(result)
        result1 = ''
        for char in result:
            if char != '\n' and char!='\r':
                result1+=char





        result = result1

       


    context={'purpose':'analyzing text','analyzed_text':result}
    if charcount=='on':
        count=0
        for _ in result:
            count+=1
        context={'purpose':'analyzing text and counting characters','analyzed_text':result,'counter':count}
    if charcount!='on' and rmnewline!='on' and removepunc!='on' and spaceremove!='on' and fullcaps!='on':
        return render(request,'error.html',context)
    return render(request,'analyze.html',context)




