from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import state_choices, bedroom_choices, price_choices


def index(request):
    listings = Listing.objects.order_by("-list_date")
    print(listings)
    paginator = Paginator(listings, 3)
    page_number = request.GET.get("page")
    paged_listings_object = paginator.get_page(page_number)

    context = {"listings": paged_listings_object}
    return render(request, "listings/listings.html", context=context)


def listing(request, listing_id):
    """this method is by me but it doesn't handle 404 page"""
    # listing_obj = Listing.objects.filter(id=listing_id)
    # print(listing_id)
    # print(listing_obj)
    # print(listing_obj[0])
    # context = {"listing": listing_obj.first()}

    """new Method"""
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {"listing": listing}
    return render(request, "listings/listing.html", context=context)


def search(request):
    queryset_list = Listing.objects.order_by("-list_date")

    # Keywords
    # State
    if "state" in request.GET:
        state = request.GET["state"]
        fullname_of_state = state_choices[state]

        if state:  # first check if there is a object with key value
            queryset_list = queryset_list.filter(state__iexact=state)
            if (
                not queryset_list
            ):  # if not with key value then check with full name[value] object.
                if fullname_of_state:
                    queryset_list = Listing.objects.order_by("-list_date").filter(
                        state__iexact=fullname_of_state
                    )
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Bedrooms
    if "bedrooms" in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Max Price
    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        "listings": queryset_list,
        "state_choices": state_choices,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "values": request.GET,
    }
    return render(request, "listings/search.html", context=context)
