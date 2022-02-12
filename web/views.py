from urllib.request import Request
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import User, Token, Expense, Income
# Create your views here.

@csrf_exempt
def submit_expense(request):
    """ user submits an expense """

    # TODO: validate data. user might be. token might be fake, amount might be fake...
    this_token = request.GET.get('token')
    this_user = User.objects.filter(token__token=this_token).get()
    date = request.GET.get('date') if 'date' in request.GET else timezone.now()
    Expense.objects.create(
        text=request.GET.get('text'),
        amount=request.GET.get('amount'),
        date=date,
        user=this_user
    )

    return JsonResponse(
        {'status': 'ok'}, 
        encoder=DjangoJSONEncoder
    )

@csrf_exempt
def submit_income(request):
    """ user submits an income """

    # TODO: validate data. user might be. token might be fake, amount might be fake...
    this_token = request.GET.get('token')
    this_user = User.objects.filter(token__token=this_token).get()
    date = request.GET.get('date') if 'date' in request.GET else timezone.now()
    Income.objects.create(
        text=request.GET.get('text'),
        amount=request.GET.get('amount'),
        date=date,
        user=this_user
    )

    return JsonResponse(
        {'status': 'ok'}, 
        encoder=DjangoJSONEncoder
    )
