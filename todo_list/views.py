from django.shortcuts import render,redirect
from django.http import HttpResponse
from todo_list.models import todo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def home_view(request):

    if request.method=='POST':
        user_input=request.POST.get('user_input')
        Date=request.POST.get('Date')
        time1=request.POST.get('time1')

        user=todo.objects.create(
            user=request.user,
            user_input=user_input,
            Date=Date,
            time1=time1,
        )

        user.save()

    tasks=todo.objects.filter(user_id=request.user)
    user_data = User.objects.get(id = request.user.id)

    return render(request=request,template_name='index.html',context={'tasks':tasks,'user_data':user_data})

@login_required(login_url='/login/')
def update_view(request,id):
    res=todo.objects.get(id=id)
    if request.method == 'POST':
        user_input=request.POST.get('user_input')
        Date=request.POST.get('Date')
        time1=request.POST.get('time1')

        res.user_input=user_input
        res.Date=Date
        res.time1=time1
        res.save()
        return redirect('/home/')
    return render(request=request,template_name='update.html',context={'res':res})



@login_required(login_url='/login/')
def delete_view(requset,id):
    todo.objects.get(id=id).delete()
    return redirect('/home/')

