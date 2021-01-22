from .models import Chat

def menu_links(request):
    links =Chat.objects.all()
    return dict(links=links)
