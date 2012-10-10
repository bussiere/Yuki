# Create your views here.
from django_quicky import view


@view(render_to='index.html')
def index(request):
    truc = 'toto'
    return {'truc': truc}