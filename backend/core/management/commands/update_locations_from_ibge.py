from typing import Dict

from django.core.management.base import BaseCommand

from core.services.web_request.web_request_service import WebRequestService
from core.models.location.location_city_model import LocationCity
from core.models.location.location_state_model import LocationState


class Command(BaseCommand):
    help = 'Update the list of states and cities'
    indexes = {}

    def __init__(self, *args, **kwargs):
        self.options = {}
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument('--verbose', type=bool, default=False, help="Increase text output. Useful for debugging.")

    def handle(self, *args, **options):
        self.options = options
        states_dicts = self.get_ibge_states_dicts()
        states = [self.update_state_from_ibge_dict(state_dict) for state_dict in states_dicts]

        for state in states:
            self.update_cities_for_state(state)

        self.stdout.write("Finished updating locations!")

    def get_ibge_states_dicts(self):
        self.stdout.write("Retrieving list of states...")
        url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
        req = WebRequestService(url=url, stream=True)
        data = req.get_json_response()
        self.stdout.write("Retrieved {} states from IBGE".format(len(data)))
        return data

    def update_state_from_ibge_dict(self, state_dict: Dict) -> LocationState:
        if len(LocationState.objects.filter(ibge_id=state_dict['id'])) > 0:
            state = LocationState.objects.filter(ibge_id=state_dict['id']).first()
            created = False
        else:
            state, created = LocationState.objects.get_or_create(abbrev=state_dict['sigla'])
        state.abbrev = state_dict['sigla']
        state.name = state_dict['nome']
        state.ibge_id = state_dict['id']
        state.save()
        self.stdout.write("State {} [{}] {} [IBGE ID: {} | CSC ID: {}]".format(
            state.name,
            state.abbrev,
            "created" if created else "updated",
            state.ibge_id,
            state.id
        ))
        return state

    def update_cities_for_state(self, state: LocationState):
        self.stdout.write("Updating cities for {} state [{}]...".format(state.name, state.abbrev))
        url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/{}/distritos".format(state.abbrev.upper())
        req = WebRequestService(url=url, stream=True)
        cities_data = req.get_json_response()
        self.stdout.write("Retrieved {} cities from state {} from IBGE".format(len(cities_data), state.abbrev))

        for city_dict in cities_data:
            self.update_city_from_ibge_dict(city_dict, state)

    def update_city_from_ibge_dict(self, city_dict: Dict, state: LocationState) -> LocationCity:
        if len(LocationCity.objects.filter(ibge_id=city_dict['id'])) > 0:
            city = LocationCity.objects.filter(ibge_id=city_dict['id']).first()
            created = False
        else:
            city, created = LocationCity.objects.get_or_create(name=city_dict['nome'], state=state)
        
        city.state = state
        city.name = city_dict['nome']
        city.ibge_id = city_dict['id']
        city.save()

        if self.options['verbose']:
            self.stdout.write("City {} - {} {} [IBGE ID: {} | CSC ID: {}]".format(
                city.name,
                city.state.abbrev,
                "created" if created else "updated",
                city.ibge_id,
                city.id
            ))
        
        return city
