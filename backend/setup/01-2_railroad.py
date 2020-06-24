from infotrem.models.railroad import RailroadCompany, RailroadRoute

# RailroadCompany
RailroadCompany.objects.get_or_create(name="Ferrovias Paulistas S/A", abbrev="FEPASA")
RailroadCompany.objects.get_or_create(name="Rede Ferroviária Federal S/A", abbrev="RFFSA")
RailroadCompany.objects.get_or_create(name="Estrada de Ferro Sorocabana", abbrev="EFS")
RailroadCompany.objects.get_or_create(name="Companhia Brasileira de Trens Urbanos", abbrev="CBTU")
RailroadCompany.objects.get_or_create(name="Companhia Vale do Rio Doce", abbrev="CVRD")
RailroadCompany.objects.get_or_create(name="Ferrocarriles Argentinos (Argentina)", abbrev="FA")
RailroadCompany.objects.get_or_create(name="Administracion de los Ferrocarriles del Estado (Uruguai)", abbrev="AFE")
RailroadCompany.objects.get_or_create(name="Empresa Nacional de Ferrocarriles", abbrev="ENFE")
