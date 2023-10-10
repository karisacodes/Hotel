from django.shortcuts import render

def hotel_home(request):
    return render(request, 'hotel_home/modifidHBS.html')
