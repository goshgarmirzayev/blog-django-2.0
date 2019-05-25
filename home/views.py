from django.shortcuts import render, HttpResponse


# Create your views here.
def home_view(request):
    context = {
        'name':'user'}
    context2 = {
        'name': 'Guest'}
    if request.user.is_authenticated:
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html', context2)
