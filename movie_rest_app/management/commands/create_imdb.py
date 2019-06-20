import json
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from ...models import Genre, MovieDetail

class Command(BaseCommand):
    def handle(self, *args, **options):
        ##### insert movies details from given jeson ####
        filepath = settings.BASE_DIR + '/imdb_data.json'
        with open(filepath, 'r') as file:
            cl = {}
            raw = file.read()
            raw_data = json.loads(raw)

            for m_details in raw_data:
                cl['name'] = m_details.get('name')
                cl['popularity'] = m_details.get('99popularity')
                cl['director'] = m_details.get('director')
                cl['imdb_score'] = m_details.get('imdb_score')

                ##### Movie details object ####
                mv, created = MovieDetail.objects.get_or_create(**cl)
                genre_list = m_details.get('genre')

                for name in genre_list:
                    name = name.strip()
                    genre, created = Genre.objects.get_or_create(name=name)
                    mv.genre.add(genre)
                mv.save()
            print "#####################################################"
            print "### Ok. All Movies Details Created In PostgreSQL. ###"
            print "#####################################################"


