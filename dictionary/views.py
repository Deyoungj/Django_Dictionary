from django.shortcuts import render, redirect
from PyDictionary import PyDictionary


def home(request):

    searched = None
    if "searched" in request.GET:
        searched = request.GET.get('searched')
        print(searched)
        return redirect(f"searched/{searched}")
        
    return render(request, 'dictionary/index.html')


def searched(request):
    searched = None
    
    if "searched" in request.GET:    
        searched = request.GET.get('searched')
        search = PyDictionary()
        meanings = search.meaning(searched)
        return render(request, 'dictionary/searched.html',{'meanings': meanings.items()})


    return render(request, 'dictionary/searched.html')

    


    

    
