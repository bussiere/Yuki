<<<<<<< HEAD
# Create your views here.
from django_quicky import view
from django_quicky import routing
 

urls, urlpatterns = routing()

urlpatterns.add_admin('/admin/')

@url(r'^$')
@view(render_to='index.html')
def index(request):
    truc = 'toto'
    return {'truc': truc}


@view(render_to='index.html')
def index(request):
    truc = 'titi'
    return {'truc': truc}
=======
>>>>>>> ad3df59ba1c150421d00ab334f44874069194291
