import copy
import uuid

from datetime import timedelta

from django.utils.datetime_safe import datetime

from api.models import Event
from api.serializers import EventSerializer
from api.tests import dataset
from api.tests.views import generic
from api.views import EventViewSet


base_payload_invalid = {
    'event_type': 1,
    'title': '',
    'description': dataset.get_random_string(100000),
    'notice_text': dataset.get_random_string(100000),
    'published': True,
    'registration_start_date': 2,
    'registration_end_date': '123456',
    'payment_limit_date': '7891011',
    'exam_objective_date': 121314,
    'exam_practical_date': 151617,
    'results_objective_date': '123456',
    'results_practical_date': '7891011',
    'results_final_date': 121314,
    'end_date': 121314,
    'generate_billet': 1,
    'payment_instructions': None,
    'billet_gateway': 0,
    'allow_multiple_vacancy_subscription': 0,
}
base_payload_valid = {
    'event_type': Event.EventType.PUBLIC_TENDER,
    'title': 'Event Test ' + dataset.get_random_string(15),
    'description': dataset.get_random_string(500),
    'notice_text': dataset.get_random_string(30),
    'published': True,
    'registration_start_date': (datetime.now() - timedelta(days=2)).isoformat(),
    'registration_end_date': (datetime.now() + timedelta(days=2)).isoformat(),
    'payment_limit_date': (datetime.now() + timedelta(days=3)).isoformat(),
    'exam_objective_date': (datetime.now() + timedelta(days=20)).isoformat(),
    'exam_practical_date': (datetime.now() + timedelta(days=21)).isoformat(),
    'results_objective_date': (datetime.now() + timedelta(days=30)).isoformat(),
    'results_practical_date': (datetime.now() + timedelta(days=31)).isoformat(),
    'results_final_date': (datetime.now() + timedelta(days=31)).isoformat(),
    'end_date': (datetime.now() + timedelta(days=60)).isoformat(),
    'generate_billet': 0,
    'payment_instructions': dataset.get_random_words(50),
    'billet_gateway': None,
    'allow_multiple_vacancy_subscription': 0,
}


class EventViewSetCreateTest(generic.GenericCreateTestCases.CreateTest):
    endpoint = '/events/'
    serializer = EventSerializer
    model = Event
    requires_admin = True
    view = EventViewSet
    payload_invalid = base_payload_invalid
    user = dataset.get_default_admin()

    def setUp(self) -> None:
        super(EventViewSetCreateTest, self).setUp()
        billet_gateway = dataset.create_billet_gateway()
        self.payload_valid = copy.deepcopy(base_payload_valid)
        self.payload_valid['billet_gateway'] = billet_gateway.id


class EventViewSetDestroyTest(generic.GenericDestroyTestCase.DestroyTest):
    endpoint = '/events/'
    serializer = EventSerializer
    model = Event
    requires_admin = True
    view = EventViewSet
    model_fake_id = uuid.uuid4()
    user = dataset.get_default_admin()

    def setUp(self) -> None:
        super(EventViewSetDestroyTest, self).setUp()
        self.event = dataset.create_event()
        self.model_real_id = self.event.id

    def tearDown(self) -> None:
        if self.event is not None:
            self.event.delete()
        super(EventViewSetDestroyTest, self).tearDown()


class EventViewSetListTest(generic.GenericListTestCase.ListTest):
    endpoint = '/events/'
    serializer = EventSerializer
    model = Event
    requires_login = False
    view = EventViewSet
    expected_items = 20

    def setUp(self) -> None:
        super(EventViewSetListTest, self).setUp()
        self.events = dataset.create_events(total=self.expected_items)

    def tearDown(self) -> None:
        for event in self.events:
            event.delete()
        super(EventViewSetListTest, self).tearDown()


class EventViewSetPartialUpdateTest(generic.GenericPartialUpdateTestCase.PartialUpdateTest):
    endpoint = '/events/'
    serializer = EventSerializer
    model = Event
    requires_admin = True
    view = EventViewSet
    model_fake_id = uuid.uuid4()
    payload_invalid = base_payload_invalid
    user = dataset.get_default_admin()

    def setUp(self) -> None:
        super(EventViewSetPartialUpdateTest, self).setUp()
        billet_gateway = dataset.create_billet_gateway()
        self.payload_valid = copy.deepcopy(base_payload_valid)
        self.payload_valid['billet_gateway'] = billet_gateway.id
        self.event = dataset.create_event()
        self.model_real_id = self.event.id

    def tearDown(self) -> None:
        if self.event is not None:
            self.event.delete()
        super(EventViewSetPartialUpdateTest, self).tearDown()


class EventViewSetRetrieveTest(generic.GenericRetrieveTestCase.RetrieveTest):
    endpoint = '/events/'
    serializer = EventSerializer
    model = Event
    requires_login = False
    view = EventViewSet
    model_fake_id = uuid.uuid4()

    def setUp(self) -> None:
        super(EventViewSetRetrieveTest, self).setUp()
        self.event = dataset.create_event()
        self.model_real_id = self.event.id

    def tearDown(self) -> None:
        if self.event is not None:
            self.event.delete()
        super(EventViewSetRetrieveTest, self).tearDown()
