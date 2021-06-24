import uuid

from api.models import Billet
from api.serializers import BilletSerializer
from api.tests import dataset
from api.tests.views import generic
from api.views import BilletViewSet


class BilletViewSetListTest(generic.GenericListTestCase.ListTest):
    endpoint = '/billets/'
    serializer = BilletSerializer
    model = Billet
    requires_admin = True
    view = BilletViewSet
    expected_items = 20

    def setUp(self) -> None:
        super(BilletViewSetListTest, self).setUp()
        self.billets = dataset.create_billets(total=self.expected_items)

    def tearDown(self) -> None:
        for billet in self.billets:
            billet.delete()
        super(BilletViewSetListTest, self).tearDown()


class BilletViewSetRetrieveTest(generic.GenericRetrieveTestCase.RetrieveTest):
    endpoint = '/billets/'
    serializer = BilletSerializer
    model = Billet
    requires_admin = True
    view = BilletViewSet
    model_fake_id = uuid.uuid4()

    def setUp(self) -> None:
        super(BilletViewSetRetrieveTest, self).setUp()
        self.billet = dataset.create_billet()
        self.model_real_id = self.billet.id

    def tearDown(self) -> None:
        if self.billet is not None:
            self.billet.delete()
        super(BilletViewSetRetrieveTest, self).tearDown()
