import random
import string
import uuid
import pytz
from datetime import timedelta

import os

from typing import Dict, List

from django.utils import timezone
from django.utils.datetime_safe import datetime

from api.models import Billet, BilletGateway, Event
from core.models.location.location_city_model import LocationCity
from core.models.location.location_state_model import LocationState
from core.models.user.user_model import User


def create_request_url(endpoint: str = ''):
    protocol = 'https' if 'LETSENCRYPT_HOST' in os.environ else 'http'

    url = "{}://{}/{}".format(protocol, os.environ['VIRTUAL_HOST'], endpoint)
    return url


def get_random_string(length: int = 10) -> str:
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def get_random_words(words: int = 5) -> str:
    return ' '.join([get_random_string(random.randint(5, 15)) for x in range(words)])


def get_random_email() -> str:
    return get_random_string(random.randint(5, 20)) + '@' + get_random_string(random.randint(5, 10)) + '.com'


def get_random_datetime() -> datetime:
    return datetime(
        year=random.randint(1900, 2099),
        month=random.randint(1, 12),
        day=random.randint(1, 28),
        hour=random.randint(0, 23),
        minute=random.randint(0, 59),
        second=random.randint(0, 59),
        tzinfo=pytz.UTC
    )


def create_user(email: str = None, is_admin=False) -> User:
    if email is None:
        email = get_random_email()
    user = User(
        email=email,
        email_validated=1,
        email_validation_sent=1,
        email_validation_hash=get_random_string(64),
        name=get_random_words(3).capitalize(),
        cpf=random.randint(9999999999, 99999999999),
        birth_date=get_random_datetime(),
        address=get_random_words(5),
        number=random.randint(1, 15000),
        complement=get_random_string() + ' ' + str(random.randint(1, 20)),
        city=LocationCity.objects.filter(ibge_id=353530905).first(),
        state=LocationState.objects.filter(abbrev="SP").first(),
        zipcode=random.randint(10000000, 99999999),
        phone=random.randint(11000000000, 99999999999),
        is_admin=is_admin,
        is_staff=is_admin,
        is_active=True,
    )
    user.save()
    return user


def get_default_admin() -> User:
    admin, created = User.objects.get_or_create(
        email="test_admin@cscconsultoria.com.br",
        is_admin=True,
    )
    admin.save()
    return admin


def get_default_creation_args() -> Dict:
    return {
        'created_by': get_default_admin(),
        'created_at': timezone.now(),
        'updated_by': None,
        'updated_at': None,
    }


def create_billet_gateway(
        billet_type: str = BilletGateway.GatewayType.BANCO_DO_BRASIL,
        metadata: Dict = None
) -> BilletGateway:
    if metadata is None:
        metadata = {'foo': 'bar'}

    admin = get_default_admin()
    billet_gateway = BilletGateway(
        type=billet_type,
        metadata=metadata,
        **get_default_creation_args()
    )
    billet_gateway.save()
    return billet_gateway


def create_billet() -> Billet:
    gateway = create_billet_gateway()
    billet = Billet(
        gateway=gateway,
        status=Billet.BilletStatus.GENERATED,
        ref_number=random.randint(10, 10000),
        filemgr_uuid=uuid.uuid4(),
        store_message=get_random_words(10),
        original_value=random.randint(100, 99900) / 100,
        due_date=timezone.now() - timedelta(days=5),
        payment_date=timezone.now(),
        bar_code=str(random.randint(0, 99999)) * 10,
        **get_default_creation_args()
    )
    billet.save()
    return billet


def create_billets(total: 2) -> List:
    return [create_billet() for x in range(total)]


def create_event() -> Event:
    billet_gateway = create_billet_gateway()
    event = Event(
        event_type=Event.EventType.PUBLIC_TENDER,
        title='Event Test ' + get_random_string(15),
        description=get_random_string(500),
        notice_text=get_random_string(30),
        published=True,
        registration_start_date=timezone.now() - timedelta(days=2),
        registration_end_date=timezone.now() + timedelta(days=2),
        payment_limit_date=timezone.now() + timedelta(days=3),
        exam_objective_date=timezone.now() + timedelta(days=20),
        exam_practical_date=timezone.now() + timedelta(days=21),
        results_objective_date=timezone.now() + timedelta(days=30),
        results_practical_date=timezone.now() + timedelta(days=31),
        results_final_date=timezone.now() + timedelta(days=31),
        end_date=timezone.now() + timedelta(days=60),
        generate_billet=1,
        payment_instructions=None,
        billet_gateway=billet_gateway,
        allow_multiple_vacancy_subscription=0,
        **get_default_creation_args()
    )
    event.save()
    return event


def create_events(total: 2) -> List:
    return [create_event() for x in range(total)]
