import logging

from infotrem.models.location import TrackGaugeConfiguration


def run():
    TrackGaugeConfiguration.objects.get_or_create(tag='NARROW', name='Métrica', gauges=[1.00])
    TrackGaugeConfiguration.objects.get_or_create(tag='BROAD', name='Larga', gauges=[1.60])
    TrackGaugeConfiguration.objects.get_or_create(tag='MIXED', name='Mista (Métrica & Larga)', gauges=[1.00, 1.60])

    logging.info("Track gauge configurations created")
