from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2306244892',
        'name': 'Laurentius Arlana Farel Mahardika',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
# Create your views here.
