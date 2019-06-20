from rest_framework import routers
from movie_rest_app import views as m_views

########## To routing urls ###########
router = routers.DefaultRouter()
router.register(r'movie_details', m_views.MovieDetailViewset)
