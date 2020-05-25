from django.utils import timezone
from django.urls import reverse
from django.views.generic import ListView
from django.shortcuts import render, redirect
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))


# # Create your views here.
# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.page(int(page))
#         return render(request, "rooms/home.html", {"page": rooms})
#     except EmptyPage:
#         return redirect("/")
#     #   print(vars(rooms))
