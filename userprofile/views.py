from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.contrib.auth import logout

from .forms import UserForm, UserProfileForm
from .models import *
from django.contrib.auth import authenticate, login
from .forms import LoginForm


# Create your views here.


def inform(request):
    return render(request, template_name='userprofile/index.html')


#@login_required
def prof_list(request):
    paginator = Paginator(User.objects.all(), 5)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        users = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        users = paginator.page(paginator.num_pages)

    return render(request, template_name='userprofile/index_profile.html', context={'users': users})


def profile_detail(request, user_id):
    if request.user.is_staff:
        user = get_object_or_404(User, id=user_id)
        return render(request, 'userprofile/profile_detail.html', {'user_profile': user})
    else:
        return render(request, 'userprofile/profile_detail.html')


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
    places = Place.objects.all()
    return render(request, template_name='userprofile/places.html', context={'places': places})


def teach_list(request):
    teachers = TeacherProfile.objects.all()
    return render(request, template_name='userprofile/teacherprofile.html', context={'teachers': teachers})


def teach_detail(request, id_teacher):
    teacher = get_object_or_404(TeacherProfile, id_teacher=id_teacher)
    return render(request, 'userprofile/teacher_detail.html', {'teacher': teacher})


def lessons_list(request):
    lessons = Lesson.objects.all()
    return render(request, template_name='userprofile/lessons.html', context={'lessons': lessons})


def statement_pay(request):
    statements = Statement.objects.all()
    return render(request, template_name='userprofile/statement_pay.html', context={'statements': statements})


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
        print(request.POST)
        print(user_form.errors)
        print(profile_form.errors)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile_form.save()
            return redirect(reverse('profile_detail_url', args=[user.pk]))
        else:
            return render(request, template_name='userprofile/registration.html',
                          context={'user_form': user_form, 'profile_form': profile_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request=request, **form.cleaned_data)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('profile_detail_url', args=[user.pk]))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    elif request.method == 'GET':
        form = LoginForm()
        return render(request, 'userprofile/login.html', {'form': form})

    return HttpResponse(content='Error during login', status=404)


def logout_user(request):
    logout(request)
    return redirect('info_url')

