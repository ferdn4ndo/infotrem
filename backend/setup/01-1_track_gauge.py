from infotrem.models.track_gauge import TrackGauge


TrackGauge.objects.get_or_create(tag='NARROW', name='Métrica', size=1.00)
TrackGauge.objects.get_or_create(tag='BROAD', name='Larga', size=1.60)

print("Track gauges created")
