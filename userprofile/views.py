from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from .forms import UserForm, UserProfileForm
from .models import *


# Create your views here.


def inform(request):
    return render(request, template_name='userprofile/index.html')


def prof_list(request):
    profiles = UserProfile.objects.all()
    return render(request, template_name='userprofile/index_profile.html', context={'profiles': profiles})


def profile_detail(request, id_profile):
    profile = get_object_or_404(UserProfile, id_profile=id_profile)
    return render(request, 'userprofile/profile_detail.html', {'profile': profile})


def group_list(request):
    groups = Group.objects.all()
    return render(request, template_name='userprofile/group.html', context={'groups': groups})


def group_detail(request, id_group):
    group = get_object_or_404(Group, id_group=id_group)
    return render(request, 'userprofile/group_detail.html', {'group': group})


def compclass_list(request):
    compclass = CompClass.objects.all()
    return render(request, template_name='userprofile/compclass.html', context={'compclass': compclass})


def places_list(request):
    places = Places.objects.all()
    return render(request, template_name='userprofile/places.html', context={'places': places})


def teach_list(request):
    teachers = TeacherProfile.objects.all()
    return render(request, template_name='userprofile/teacherprofile.html', context={'teachers': teachers})


def teach_detail(request, id_teacher):
    teacher = get_object_or_404(TeacherProfile, id_teacher=id_teacher)
    return render(request, 'userprofile/teacher_detail.html', {'teacher': teacher})


def lessons_list(request):
    lessons = Lessons.objects.all()
    return render(request, template_name='userprofile/lessons.html', context={'lessons': lessons})


def registration(request):
    if request.method == 'GET':
        user_form = UserForm()
        profile_form = UserProfileForm()
        return render(request, template_name='userprofile/registration.html',
                      context={'user_form': user_form, 'profile_form': profile_form})

    elif request.method == 'POST':
        # Сохранение в модели и валидация
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile_form.save()
            return redirect(reverse('profile_detail_url', args=[user.pk]))
        else:
            return HttpResponse(status=505)
