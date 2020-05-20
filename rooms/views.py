from django.shortcuts import render
from . import models

# Create your views here.
def all_rooms(request):
    hungry = True
    all_rooms = models.Room.objects.all()

    return render(
        request, "rooms/home.html", context={"hungry": hungry, "rooms": all_rooms}
    )
