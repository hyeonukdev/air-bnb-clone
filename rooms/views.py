from django.http import Http404
from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView, DetailView
from . import models


def all_rooms(request):
    # page = request.GET.get("page", 1)
    # page = int(page or 1)
    # page_size = 10
    # limit = page_size * page
    # offset = limit - page_size
    # all_rooms = models.Room.objects.all()[offset:limit]
    # page_count = ceil(models.Room.objects.count() / page_size)
    # return render(
    #     request,
    #     "rooms/home.html",
    #     {
    #         "potato": all_rooms,
    #         "page": page,
    #         "page_count": page_count,
    #         "page_range": range(1, page_count),
    #     },
    # )
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")

class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    # template_name = "rooms/room_list.html"
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
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
        raise Http404()


class RoomDetail(DetailView):
    """ RoomDetail Definition """

    model = models.Room


def search(request):
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city": city})
