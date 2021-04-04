from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from apps.message_form.models import Message
# Create your views here.


def message_form(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        memo = request.POST.get("message", "")
        message = Message()
        message.name = name
        message.email = email
        message.message = memo
        message.save()
        return render(request, "index.html", {
            "Message": message
        })

    if request.method == "GET":
        template = loader.get_template('index.html')
        var_dict = {}
        all_message = Message.objects.all()
        if all_message:
            message = all_message[0]
            var_dict = {
                "Message": message
            }
        # return render(request, "index.html", var_dict)
        return HttpResponse(template.render(var_dict))
