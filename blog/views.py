from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from tags.models import Tag
from .models import Bloog

def show_bloog(request):

    if request.method == "POST":
        bloog = Bloog.objects.create(name=request.POST.get("bloog_name"),
                            description=request.POST.get("description_name"),
                            owner=request.user)

        bloog.tags.add(*request.POST.getlist("tag_names"))


    return render(request, "my_blog.html", {"bloogs": Bloog.objects.filter(owner=request.user.id),
                                             "tags":Tag.objects.all()})


def get_bloog(request, bloog_id):
    try:
        bloog = Bloog.objects.get(id=bloog_id)
        if request.user.id != bloog.owner.id:
            raise PermissionDenied
        return render(request, "detailed_blog.html", {"bloog": bloog})
    except Bloog.DoesNotExist:
        raise Http404("We don't have any.")
