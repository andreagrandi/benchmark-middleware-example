from django.views.generic import ListView
from clients.models import Client


class ListClientView(ListView):

    model = Client
    template_name = 'client_list.html'
