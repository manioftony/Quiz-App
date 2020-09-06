# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from masterdata.models import Question, Answer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


def index(request):
    try:
        if request.user.is_authenticated:
            if request.method == 'GET':
                page = 1
                q_obj = Question.objects.filter(active=2)
                return render(request, 'index.html', locals())
            else:
                count = 0
                q_obj = Question.objects.filter(active=2)
                result_obj = request.POST
                for i in result_obj:
                    a_obj = Answer.objects.filter(
                        question__id__icontains=i, active=2)
                    if a_obj.exists():
                        a_obj = a_obj[0]
                        if str(a_obj.anwer_text) == str(result_obj.get(i)):
                            count = count+1
                page = 2
                return render(request, 'index.html', locals())
        else:
            return redirect('/')
    except Exception as e:
        return HttpResponse(e)


def login_data(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/index')
            else:
                pass
        else:
            return render(request, 'login.html', locals())
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/index')
        else:
            form = AuthenticationForm()
            return render(request=request,
                          template_name="login.html",
                          context={"form": form})


class QuestionAnswerView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        q_obj = Answer.objects.filter(active=2)
        obj = [{'question':i.question.question,'answer':i.anwer_text} for i in q_obj] 
        content = {"data":obj,'status':200}
        return Response(content)
