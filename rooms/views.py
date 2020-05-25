from django.utils import timezone
from django.http import Http404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django_countries import countries
from . import models, forms


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


class RoomDetail(DetailView):

    """RoomDetail Definition"""

    model = models.Room


def search(request):

    form = forms.SearchForm()

    return render(request, "rooms/search.html", {"form": form})


# implement by not using django form api

# city = request.GET.get("city", "Anywhere")
# city = str.capitalize(city)
# country = request.GET.get("country", "KR")
# room_type = int(request.GET.get("room_type", 0))
# price = int(request.GET.get("price", 0))
# guests = int(request.GET.get("guests", 0))
# bedrooms = int(request.GET.get("bedrooms", 0))
# beds = int(request.GET.get("beds", 0))
# baths = int(request.GET.get("baths", 0))
# room_types = models.RoomType.objects.all()
# amenities = models.Amenity.objects.all()
# facilities = models.Facility.objects.all()
# instant = bool(request.GET.get("instant", False))
# super_host = bool(request.GET.get("super_host", False))
# s_amenities = request.GET.getlist("amenities")
# s_facilities = request.GET.getlist("facilities")

# form = {
#     "city": city,
#     "s_country": country,
#     "s_room_type": room_type,
#     "price": price,
#     "guests": guests,
#     "bedrooms": bedrooms,
#     "beds": beds,
#     "baths": baths,
#     "s_amenities": s_amenities,
#     "s_facilities": s_facilities,
#     "instant": instant,
#     "super_host": super_host,
# }

# choices = {
#     "countries": countries,
#     "room_types": room_types,
#     "amenities": amenities,
#     "facilities": facilities,
# }

# filter_arg = {}

# if city != "Anywhere":
#     filter_arg["city__startswith"] = city
# if room_type != 0:
#     filter_arg["room_type__pk"] = room_type  # foreign key

# filter_arg["country"] = country

# if price != 0:
#     filter_arg["price__lte"] = price
# if guests != 0:
#     filter_arg["guests__gte"] = guests
# if bedrooms != 0:
#     filter_arg["bedrooms__gte"] = bedrooms
# if beds != 0:
#     filter_arg["beds__gte"] = beds
# if baths != 0:
#     filter_arg["baths__gte"] = baths

# if instant is True:
#     filter_arg["instant_book"] = True
# if super_host is True:
#     filter_arg["host__superhost"] = True

# if len(s_amenities) > 0:
#     for s_amenity in s_amenities:
#         filter_arg["amenities__pk"] = int(s_amenity)

# if len(s_facilities) > 0:
#     for s_facility in s_facilities:
#         filter_arg["facility__pk"] = int(s_facility)

# rooms = models.Room.objects.filter(**filter_arg)

# return render(request, "rooms/search.html", {**form, **choices, "rooms": rooms},)

# room_detail function based view
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404()


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
