from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    if request.method == "POST":
        listing_title = request.POST["listing_title"]
        listing_id = request.POST["listing_id"]
        contact_name = request.POST["name"]
        contact_phone = request.POST["phone"]
        contact_email = request.POST["email"]
        contact_message = request.POST["message"]
        user_id = request.POST["user_id"]
        realtor_email = request.POST["realtor_email"]

        contact = Contact(
            listing=listing_title,
            listing_id=listing_id,
            name=contact_name,
            phone=contact_phone,
            email=contact_email,
            message=contact_message,
            user_id=user_id,
        )  # creates contact object

        # check if user has already contacted for the listing
        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(
                user_id=user_id, listing_id=listing_id
            )
            if has_contacted:
                messages.error(
                    request,
                    "You already made inquiry for " + listing_title + " listing",
                )
                return redirect(to="/listings/" + listing_id)
        else:
            messages.error(
                request,
                "You cannot make request for listing unless login, Please Login First!",
            )
            return redirect(to="/listings/" + listing_id)

        contact.save()  # this will store data to database

        # let's send mail to the realtor
        send_mail(
            subject="Property Listing Inquiry",
            message=f"""
            There has been inquiry for {listing_title} from {contact_name}

            Here's the information about {contact_name}

            name            : {contact_name}
            phone           : {contact_phone}
            email           : {contact_email}
            interested in   : {listing_title}
            message         : {contact_message}

            Sign in to btre admin area to more info
            """,
            from_email="tonystark62499@gmail.com",
            recipient_list=[realtor_email, "jerrico62499@gmail.com"],
            fail_silently=False,
        )
        messages.success(
            request,
            "Your request has been submited. a realtor will get back to you soon.",
        )
        return redirect("/listings/" + listing_id)
