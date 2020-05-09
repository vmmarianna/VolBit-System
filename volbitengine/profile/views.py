from .models import *
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import View


# Create your views here.

def prof_list(request):
    profiles = Profile.objects.all()
    return render(request, template_name='profile/index.html', context={'profiles': profiles})


def profile_detail(request, id_profile):
    profile = get_object_or_404(Profile, id_profile=id_profile)
    return render(request, 'profile/profile_detail.html', {'profile': profile})


def group_list(request):
    groups = Group.objects.all()
    return render(request, template_name='profile/group.html', context={'groups': groups})


def group_detail(request, id_group):
    group = get_object_or_404(Group, id_group=id_group)
    return render(request, 'profile/group_detail.html', {'group': group})


def compclass_list(request):
    compclass = CompClass.objects.all()
    return render(request, template_name='profile/compclass.html', context={'compclass': compclass})


def compclass_detail(request, id_comp):
    compclas = get_object_or_404(CompClass, id_comp=id_comp)
    return render(request, 'profile/compcl_detail.html', {'compclas': compclas})
