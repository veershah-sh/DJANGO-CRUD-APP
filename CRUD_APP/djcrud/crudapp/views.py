from django.shortcuts import render
from .models import Customer
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def index(request):
    customers = Customer.objects.all()
    query = ""
    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            Customer.objects.create(
                name=name,
                email=email
            )
            messages.success(request, "Customer added successfully.")
        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            
            update_customer = Customer.objects.get(id=id)
            update_customer.name = name
            update_customer.email = email
            update_customer.save()

            messages.success(request, "Customer Updated Successfully.")
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Customer.objects.get(id=id).delete()

            messages.success(request, "Customer Deleted Successfully.")
        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            customers = Customer.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))

    context = {"customers": customers, "query": query}
    return render(request, "index.html", context=context)