from django.shortcuts import render

# Create your views here.
def all_rooms(request):
    hungry = True
    return render(request, "all_rooms.html", context={"hungry": hungry})
