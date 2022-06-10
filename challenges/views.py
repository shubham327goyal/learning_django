from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

monthly_challenges = {   #dictionary
    "january" : "eat nothing",
    "february" : "walk for 1 hour",
    "march" : "learn something new",
    "april" : "dont go outside",
    "may" : "dont use phone",
    "june" : "leanr new skills",
    "july" : "open laptop",
    "august" : "hwo are you",
    "september" : "kaise ho",
    "october" : "diwali time",
    "november" : "how are you guys",
    "december" : "compter screen on krlo"
}

def monthwiseno(request , monthwise):
    months = list(monthly_challenges.keys())

    if monthwise > len(months):
        return HttpResponseNotFound("error not found")

    forward_month = months[monthwise-1]

    return HttpResponseRedirect("/challenges/" + forward_month)

def monthwise(request , monthwise):
    try:
        text = monthly_challenges[monthwise]
    except:
        return HttpResponseNotFound("this is not supported")
    return HttpResponse(text)