from django.shortcuts import render
from .models import Count
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def like_button(request):
    count, created = Count.objects.get_or_create(pk=1)
    count.like_count += 1
    count.save()
    return JsonResponse({'like_count': count.like_count, 'dislike_count': count.dislike_count})


@csrf_exempt
def dislike_button(request):
    count, created = Count.objects.get_or_create(pk=1)
    count.dislike_count += 1
    count.save()
    return JsonResponse({'like_count': count.like_count, 'dislike_count': count.dislike_count})


def index(request):
    count, created = Count.objects.get_or_create(pk=1)
    return render(request, 'index.html', {'count': count})
