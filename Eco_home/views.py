from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Home, HomePicture, TourRequest
from django.contrib import messages
# Create your views here.


def homes(request):
    homes = Home.objects.all().order_by("date_posted")
    context = {
        "homes" : homes
    }
    return render(request, "Eco_home/homes.html", context)

def home_detail (request, home_url, pk):
    home = Home.objects.get(pk=pk)
    homepictures = HomePicture.objects.filter(home=pk).all()

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Please Login to your account first!")

        full_name = request.POST["full_name"]
        date = request.POST["date"]
        phone_number = request.POST["phone_no"]

        try:
            tour_request = TourRequest.objects.create(
                user =request.user,
                home=home,
                full_name=full_name,
                phone_number=phone_number,
                date=date
            )
            tour_request.save()
        except Exception as e:
            print(e)
    


    context = {
        "home" : home,
        "homepictures" : homepictures,
    }
    return render(request, "Eco_home/home_detail.html", context)



def searched_homes(request):

    if request.method == 'GET':
        search = request.GET['searched']
        homes = Home.objects.filter(city_location__icontains = search).all()

    if homes.count() == 0:
       messages.info(request, f"we currently have no availible houses in {search}" )

    context = {
        "homes" : homes
    }
    return render(request, "Eco_home/homes.html", context)


# def post_search(request):
#     form = SearchForm()
#     if 'query' in request.GET:
#     form = SearchForm(request.GET)
#     if form.is_valid():
#         cd = form.cleaned_data
#     results = SearchQuerySet().models(Post).filter(content=cd['query']).load_all()
 
#  # count total results



