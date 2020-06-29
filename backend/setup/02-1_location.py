import os
from typing import List

def batch_create_route_location(route_name: str, sub_route_name: str, locations: List, sub_route_year: int = None):
    from django.contrib.auth.models import User

    from infotrem.models.location_model import Location, LocationTrackGauge
    from infotrem.models.track_gauge_model import TrackGauge
    from infotrem.models.railroad_route_model import RailroadRouteSectionLocation, RailroadRouteSectionLocationKilometer, \
        RailroadRouteSection, RailroadRoute

    railroad_route = RailroadRoute.objects.get_or_create(name=route_name)[0]

    railroad_route_section = RailroadRouteSection.objects.get_or_create(
        railroad_route=railroad_route,
        name=sub_route_name,
        build_year=sub_route_year
    )[0]

    for location in locations:
        user = User.objects.get(username=os.environ['SYSTEM_USER_NAME'])
        location_obj = Location.objects.get_or_create(
            abbrev=location['abbrev'] if 'abbrev' in location else None,
            name=location['name'],
            type=location['type'] if 'type' in location else None,
            center_latitude=location['lat'] if 'lat' in location else None,
            center_longitude=location['lon'] if 'lon' in location else None,
            created_by=user
        )[0]

        for gauge_size in location['gauges']:
            LocationTrackGauge.objects.get_or_create(
                location=location_obj,
                track_gauge=TrackGauge.objects.get(size=gauge_size)
            )

        section_location = RailroadRouteSectionLocation.objects.get_or_create(
            railroad_route=railroad_route,
            location=location_obj,
            railroad_route_section=railroad_route_section,
            location_route_order=location['route_position'] if 'route_position' in location else None,
        )[0]

        if 'kilometer' in location:
            RailroadRouteSectionLocationKilometer.objects.get_or_create(
                railroad_route_section_location=section_location,
                kilometer=location['kilometer'],
                kilometer_year=location['kilometer_year'] if 'kilometer_year' in location else None,
            )


###
# Itararé-Uruguai
# Linha Tronco (1909)
###
batch_create_route_location(
    route_name='Itararé-Uruguai',
    sub_route_name='Linha Tronco',
    sub_route_year=1909,
    locations=[
        {
            'abbrev': 'ZIR',
            'name': 'Itararé',
            'gauges': [1.00],
            'route_position': 1,
            'kilometer': 0.0,
            'kilometer_year': 1908,
        },
        {
            'name': 'Coronel Isaltino',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 9.953,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LSG',
            'name': 'Sengés',
            'gauges': [1.00],
            'route_position': 3,
            'kilometer': 23.691,
            'kilometer_year': 1936,
        },
        {
            'name': 'Tucunduva',
            'gauges': [1.00],
            'route_position': 4,
            'kilometer': 33.203,
            'kilometer_year': 1936,
        },
        {
            'name': 'Rio do Bugre',
            'gauges': [1.00],
            'route_position': 5,
            'kilometer': 42.121,
            'kilometer_year': 1936,
        },
        {
            'name': 'Fábio Rego',
            'gauges': [1.00],
            'route_position': 6,
            'kilometer': 55.966,
            'kilometer_year': 1936,
        },
        {
            'name': 'Engenheiro Schamber',
            'gauges': [1.00],
            'route_position': 7,
            'kilometer': 67.278,
            'kilometer_year': 1936,
        },
        {
            'name': 'Rio das Mortes',
            'gauges': [1.00],
            'route_position': 8,
            'kilometer': 76.635,
            'kilometer_year': 1936,
        },
        {
            'name': 'Samambaia',
            'gauges': [1.00],
            'route_position': 9,
            'kilometer': 88.820,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'L03',
            'name': 'Fábrica Pisa',
            'gauges': [1.00],
            'route_position': 10,
            'kilometer': 91.929,
            'kilometer_year': 1935,
        },
        {
            'abbrev': 'LJR',
            'name': 'Jaguariaíva',
            'gauges': [1.00],
            'route_position': 11,
            'kilometer': 97.929,
            'kilometer_year': 1935,
        },
        {
            'name': 'Cilada',
            'gauges': [1.00],
            'route_position': 12,
            'kilometer': 112.803,
            'kilometer_year': 1936,
        },
        {
            'name': 'Diamante',
            'gauges': [1.00],
            'route_position': 13,
            'kilometer': 121.0,
        },
        {
            'name': 'Presidente Castilhos',
            'gauges': [1.00],
            'route_position': 14,
            'kilometer': 123.031,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LMU',
            'name': 'Raul Mesquita (Joaquim Murtinho)',
            'gauges': [1.00],
            'route_position': 15,
            'kilometer': 133.173,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LPE',
            'name': 'Pedreira',
            'gauges': [1.00],
            'route_position': 16,
            'kilometer': 137,
        },
        {
            'name': 'Espalha Brasas',
            'gauges': [1.00],
            'route_position': 17,
            'kilometer': 145.051,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LPY',
            'name': 'Piraí do Sul',
            'gauges': [1.00],
            'route_position': 18,
            'kilometer': 156.337,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'ZRJ',
            'name': 'Tijuco Preto',
            'gauges': [1.00],
            'route_position': 19,
            'kilometer': 165.888,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LCX',
            'name': 'Caxambu',
            'gauges': [1.00],
            'route_position': 20,
            'kilometer': 179.481,
            'kilometer_year': 1936,
        },
        {
            'name': 'Iapó',
            'gauges': [1.00],
            'route_position': 21,
            'kilometer': 186.317,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LCA',
            'name': 'Castro',
            'gauges': [1.00],
            'route_position': 22,
            'kilometer': 195.143,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LTC',
            'name': 'Tronco',
            'gauges': [1.00],
            'route_position': 23,
            'kilometer': 207.065,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LCB',
            'name': 'Carambeí (Caranbey)',
            'gauges': [1.00],
            'route_position': 24,
            'kilometer': 218.800,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LBQ',
            'name': 'Boqueirão',
            'gauges': [1.00],
            'route_position': 25,
            'kilometer': 227.658,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LRD',
            'name': 'Rio Verde',
            'gauges': [1.00],
            'route_position': 26,
            'kilometer': 236.823,
            'kilometer_year': 1936,
        },
        {
            'name': 'Ponta Grossa',
            'gauges': [1.00],
            'route_position': 27,
            'kilometer': 252.083,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LOF',
            'name': 'Oficinas',
            'gauges': [1.00],
            'route_position': 28,
            'kilometer': 255.602,
            'kilometer_year': 1936,
        },
        {
            'name': 'Rio Tibagi',
            'gauges': [1.00],
            'route_position': 29,
            'kilometer': 267.148,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LRR',
            'name': 'Roxo Roiz',
            'gauges': [1.00],
            'route_position': 30,
            'kilometer': 274.646,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LER',
            'name': 'Guaragi (Entre Rios)',
            'gauges': [1.00],
            'route_position': 30,
            'kilometer': 286.076,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LGU',
            'name': 'Valinhos do Sul (Guaraúna)',
            'gauges': [1.00],
            'route_position': 31,
            'kilometer': 304.896,
            'kilometer_year': 1936,
        },
        {
            'name': 'Rio das Almas',
            'gauges': [1.00],
            'route_position': 32,
            'kilometer': 318.226,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LTS',
            'name': 'Teixeira Soares',
            'gauges': [1.00],
            'route_position': 33,
            'kilometer': 325.379,
            'kilometer_year': 1936,
        },
        {
            'name': 'Diamantina',
            'gauges': [1.00],
            'route_position': 34,
            'kilometer': 332.451,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LFP',
            'name': 'Fernandes Pinheiro',
            'gauges': [1.00],
            'route_position': 35,
            'kilometer': 341.855,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LFL',
            'name': 'Florestal',
            'gauges': [1.00],
            'route_position': 36,
            'kilometer': 349.250,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LIT',
            'name': 'Irati',
            'gauges': [1.00],
            'route_position': 37,
            'kilometer': 358.980,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LGZ',
            'name': 'Eng. Gutierrez (Riozinho)',
            'gauges': [1.00],
            'route_position': 38,
            'kilometer': 385.174,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LRB',
            'name': 'Rebouças',
            'gauges': [1.00],
            'route_position': 39,
            'kilometer': 385.174,
            'kilometer_year': 1936,
        },
        {
            'name': 'Roberto Helling',
            'gauges': [1.00],
            'route_position': 40,
            'kilometer': 397,
            'kilometer_year': 1960,
        },
        {
            'abbrev': 'LRZ',
            'name': 'Rio Azul',
            'gauges': [1.00],
            'route_position': 41,
            'kilometer': 407.102,
            'kilometer_year': 1936,
        },
        {
            'name': 'Minduí (Vera Cruz)',
            'gauges': [1.00],
            'route_position': 42,
            'kilometer': 420,
            'kilometer_year': 1960,
        },
        {
            'abbrev': 'LML',
            'name': 'Mallet',
            'gauges': [1.00],
            'route_position': 43,
            'kilometer': 433.991,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LDZ',
            'name': 'Dorizon',
            'gauges': [1.00],
            'route_position': 44,
            'kilometer': 445.551,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LFN',
            'name': 'Paulo de Frontin',
            'gauges': [1.00],
            'route_position': 45,
            'kilometer': 466.319,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LVD',
            'name': 'Vargem Grande',
            'gauges': [1.00],
            'route_position': 46,
            'kilometer': 480.976,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LFS',
            'name': 'Paula Freitas',
            'gauges': [1.00],
            'route_position': 47,
            'kilometer': 497.562,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LUN',
            'name': 'Porto União da Vitória',
            'gauges': [1.00],
            'route_position': 48,
            'kilometer': 515.960,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LEM',
            'name': 'Eng. Eugênio de Mello (Legru)',
            'gauges': [1.00],
            'route_position': 49,
            'kilometer': 526.971,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LAS',
            'name': 'Achilles Stenghel',
            'gauges': [1.00],
            'route_position': 50,
            'kilometer': 536.040,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LNG',
            'name': 'Nova Galícia',
            'gauges': [1.00],
            'route_position': 51,
            'kilometer': 544.255,
            'kilometer_year': 2000,
        },
        {
            'abbrev': 'LSO',
            'name': 'Cerro Pelado',
            'gauges': [1.00],
            'route_position': 52,
            'kilometer': 563.972,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LMC',
            'name': 'Matos Costa',
            'gauges': [1.00],
            'route_position': 53,
        },
        {
            'name': 'General Dutra',
            'gauges': [1.00],
            'route_position': 54,
            'kilometer': 588,
            'kilometer_year': 1960,
        },
        {
            'abbrev': 'LOM',
            'name': 'Calmon',
            'gauges': [1.00],
            'route_position': 55,
            'kilometer': 594.301,
            'kilometer_year': 1936,
        },
        {
            'name': 'Anhangüera',
            'gauges': [1.00],
            'route_position': 56,
            'kilometer': 606.0,
            'kilometer_year': 465,
        },
        {
            'abbrev': 'LPP',
            'name': 'Presidente Penna',
            'gauges': [1.00],
            'route_position': 57,
            'kilometer': 619.469,
            'kilometer_year': 1935,
        },
        {
            'name': 'Adolfo Konder',
            'gauges': [1.00],
            'route_position': 58,
            'kilometer': 633.659,
            'kilometer_year': 2000,
        },
        {
            'abbrev': 'LRC',
            'name': 'Caçador',
            'gauges': [1.00],
            'route_position': 59,
            'kilometer': 633.659,
            'kilometer_year': 1936,
        },
        {
            'name': 'Engenheiro Leite Ribeiro',
            'gauges': [1.00],
            'route_position': 60,
        },
        {
            'name': 'Coronel Tiburcio Cavalcanti',
            'gauges': [1.00],
            'route_position': 61,
            'kilometer': 670.0,
            'kilometer_year': 1960,
        },
        {
            'abbrev': 'LAN',
            'name': 'Rio das Antas (Campos Novos)',
            'gauges': [1.00],
            'route_position': 62,
            'kilometer': 678.940,
            'kilometer_year': 1935,
        },
        {
            'name': 'Ipoméia (Princesa Isabel)',
            'gauges': [1.00],
            'route_position': 63,
            'kilometer': 692,
            'kilometer_year': 1960,
        },
        {
            'abbrev': 'LGM',
            'name': 'Gramado',
            'gauges': [1.00],
            'route_position': 64,
        },
        {
            'abbrev': 'LVI',
            'name': 'Videira',
            'gauges': [1.00],
            'route_position': 65,
            'kilometer': 708.731,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LPN',
            'name': 'Pinheiro Preto',
            'gauges': [1.00],
            'route_position': 66,
            'kilometer': 728.095,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LBI',
            'name': 'Tangará',
            'gauges': [1.00],
            'route_position': 67,
            'kilometer': 742.998,
            'kilometer_year': 1960,
        },
        {
            'name': 'General Goes',
            'gauges': [1.00],
            'route_position': 68,
            'kilometer': 755,
            'kilometer_year': 1960,
        },
        {
            'abbrev': 'LIU',
            'name': 'Ibicaré',
            'gauges': [1.00],
            'route_position': 69,
            'kilometer': 763.581,
            'kilometer_year': 1935,
        },
        {
            'name': 'Luzerna',
            'gauges': [1.00],
            'route_position': 70,
            'kilometer': 778.495,
            'kilometer_year': 1935,
        },
        {
            'abbrev': 'LHL',
            'name': 'Herval D\'Oeste',
            'gauges': [1.00],
            'route_position': 71,
            'kilometer': 783.480,
            'kilometer_year': 1935,
        },
        {
            'name': 'Itororó',
            'gauges': [1.00],
            'route_position': 72,
            'kilometer': 797.0,
            'kilometer_year': 1960,
        },
        {
            'name': 'Barra Fria',
            'gauges': [1.00],
            'route_position': 73,
            'kilometer': 802.095,
            'kilometer_year': 1936,
        },
        {
            'name': 'Leão',
            'gauges': [1.00],
            'route_position': 74,
            'kilometer': 814.190,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LCZ',
            'name': 'Capinzal',
            'gauges': [1.00],
            'route_position': 75,
            'kilometer': 828.232,
            'kilometer_year': 1936,
        },
        {
            'name': 'Avaí',
            'gauges': [1.00],
            'route_position': 76,
            'kilometer': 844.0,
            'kilometer_year': 1960,
        },
        {
            'name': 'Barra do Pinheiro',
            'gauges': [1.00],
            'route_position': 77,
            'kilometer': 846.985,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LPX',
            'name': 'Piratuba',
            'gauges': [1.00],
            'route_position': 78,
            'kilometer': 858.429,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LUG',
            'name': 'Rio Uruguai',
            'gauges': [1.00],
            'route_position': 79,
            'kilometer': 878.274,
            'kilometer_year': 1935,
        },
        {
            'name': 'Volta Grande',
            'gauges': [1.00],
            'route_position': 80,
            'kilometer': 881.221,
            'kilometer_year': 1935,
        },
        {
            'abbrev': 'NRM',
            'name': 'Marcelino Ramos',
            'gauges': [1.00],
            'route_position': 81,
        },
    ],
)

###
# Itararé-Uruguai
# Variante Jaguariaíva - Fábio Rego (1964)
###
batch_create_route_location(
    route_name='Itararé-Uruguai',
    sub_route_name='Variante Jaguariaíva - Fábio Rego',
    sub_route_year=1909,
    locations=[
        {
            'name': 'Fábio Rego',
            'gauges': [1.00],
            'route_position': 1,
            'kilometer': 55.966,
            'kilometer_year': 1936,
        },
        {
            'name': 'Samambaia (nova)',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 88.820,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LJR',
            'name': 'Jaguariaíva',
            'gauges': [1.00],
            'route_position': 3,
            'kilometer': 97.929,
            'kilometer_year': 1935,
        },
    ],
)

###
# Curitiba - Paranaguá
# Linha Tronco (1885)
###
batch_create_route_location(
    route_name='Curitiba - Paranaguá',
    sub_route_name='Linha Tronco',
    sub_route_year=1885,
    locations=[
        {
            'abbrev': 'LPG',
            'name': 'Paranaguá',
            'gauges': [1.00],
            'route_position': 1,
            'kilometer': 0,
            'kilometer_year': 1935,
        },
        {
            'abbrev': 'LDP',
            'name': 'Porto Dom Pedro II',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 2.300,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LAX',
            'name': 'Alexandra',
            'gauges': [1.00],
            'route_position': 3,
            'kilometer': 16.800,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LSQ',
            'name': 'Saquarema',
            'gauges': [1.00],
            'route_position': 4,
            'kilometer': 24.000,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LMR',
            'name': 'Morretes',
            'gauges': [1.00],
            'route_position': 5,
            'kilometer': 24.000,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LPC',
            'name': 'Porto de Cima',
            'gauges': [1.00],
            'route_position': 6,
            'kilometer': 50.600,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LEL',
            'name': 'Eng. Lange (Volta Grande)',
            'gauges': [1.00],
            'route_position': 7,
            'kilometer': 55.900,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LMY',
            'name': 'Marumbi',
            'gauges': [1.00],
            'route_position': 8,
            'kilometer': 59.643,
            'kilometer_year': 1936,
        },
        {
            'name': 'Cadeado',
            'gauges': [1.00],
            'route_position': 9,
            'kilometer': 63.500,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LVN',
            'name': 'Véu da Noiva (Ypiranga)',
            'gauges': [1.00],
            'route_position': 10,
            'kilometer': 66.800,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LBH',
            'name': 'Banhado',
            'gauges': [1.00],
            'route_position': 11,
            'kilometer': 73.400,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LRN',
            'name': 'Roça Nova',
            'gauges': [1.00],
            'route_position': 12,
            'kilometer': 80.500,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LPQ',
            'name': 'Piraquara',
            'gauges': [1.00],
            'route_position': 13,
            'kilometer': 87.350,
            'kilometer_year': 1936,
        },
        {
            'name': 'Leprosário (São Roque)',
            'gauges': [1.00],
            'route_position': 14,
        },
        {
            'abbrev': 'LNH',
            'name': 'Pinhais',
            'gauges': [1.00],
            'route_position': 15,
            'kilometer': 102.100,
            'kilometer_year': 1936,
        },
        {
            'name': 'Curitiba',
            'gauges': [1.00],
            'route_position': 16,
            'kilometer': 110.390,
            'kilometer_year': 1936,
        },
    ],
)

###
# Curitiba - Paranaguá
# Nova estação de Curitiba (1972)
###
batch_create_route_location(
    route_name='Curitiba - Paranaguá',
    sub_route_name='Nova estação de Curitiba',
    sub_route_year=1972,
    locations=[
        {
            'abbrev': 'LNH',
            'name': 'Pinhais',
            'gauges': [1.00],
            'route_position': 1,
            'kilometer': 102.100,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LCO',
            'name': 'Curitiba (nova)',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 109.436,
            'kilometer_year': 2000,
        },
        {
            'name': 'Curitiba',
            'gauges': [1.00],
            'route_position': 3,
            'kilometer': 110.390,
            'kilometer_year': 1936,
        },
    ],
)

###
# Curitiba - Paranaguá
# Modificações entre Curitiba e Paranaguá (1986)
###
batch_create_route_location(
    route_name='Curitiba - Paranaguá',
    sub_route_name='Modificações entre Curitiba e Paranaguá',
    sub_route_year=1986,
    locations=[
        {
            'abbrev': 'LPG',
            'name': 'Paranaguá',
            'gauges': [1.00],
            'route_position': 1,
            'kilometer': 0,
            'kilometer_year': 1935,
        },
        {
            'abbrev': 'LDP',
            'name': 'Porto Dom Pedro II',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 2.310,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LID',
            'name': 'Quilômetro 5 (KM5)',
            'gauges': [1.00],
            'route_position': 3,
            'kilometer': 6.634,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LAX',
            'name': 'Alexandra',
            'gauges': [1.00],
            'route_position': 4,
            'kilometer': 16.168,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LSQ',
            'name': 'Saquarema',
            'gauges': [1.00],
            'route_position': 5,
            'kilometer': 23.989,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LMR',
            'name': 'Morretes',
            'gauges': [1.00],
            'route_position': 6,
            'kilometer': 40.756,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LOT',
            'name': 'Eng. Roberto Costa',
            'gauges': [1.00],
            'route_position': 7,
            'kilometer': 44.583,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LPC',
            'name': 'Porto de Cima',
            'gauges': [1.00],
            'route_position': 8,
            'kilometer': 50.753,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LEL',
            'name': 'Eng. Lange (Volta Grande)',
            'gauges': [1.00],
            'route_position': 9,
            'kilometer': 56.027,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LMY',
            'name': 'Marumbi (Marumby)',
            'gauges': [1.00],
            'route_position': 10,
            'kilometer': 59.975,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LVN',
            'name': 'Véu da Noiva (Ypiranga)',
            'gauges': [1.00],
            'route_position': 11,
            'kilometer': 66.891,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LKS',
            'name': 'Quilômetro 70 (KM70)',
            'gauges': [1.00],
            'route_position': 12,
            'kilometer': 69.998,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LBH',
            'name': 'Banhado',
            'gauges': [1.00],
            'route_position': 13,
            'kilometer': 74.427,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LRN',
            'name': 'Roça Nova',
            'gauges': [1.00],
            'route_position': 14,
            'kilometer': 80.610,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LPQ',
            'name': 'Piraquara',
            'gauges': [1.00],
            'route_position': 15,
            'kilometer': 87.486,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LUZ',
            'name': 'Eng. Coral',
            'gauges': [1.00],
            'route_position': 16,
            'kilometer': 92.860,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LNH',
            'name': 'Pinhais',
            'gauges': [1.00],
            'route_position': 17,
            'kilometer': 102.235,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LKP',
            'name': 'Quilômetro 103 (KM103)',
            'gauges': [1.00],
            'route_position': 18,
            'kilometer': 103.698,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LTE',
            'name': 'Eng. Theodoro Stresser',
            'gauges': [1.00],
            'route_position': 19,
            'kilometer': 105.160,
            'kilometer_year': 2000,
        },
        {
            'abbrev': 'LCO',
            'name': 'Curitiba (nova)',
            'gauges': [1.00],
            'route_position': 20,
            'kilometer': 109.644,
            'kilometer_year': 2000,
        },
    ],
)

###
# Curitiba - Ponta Grossa
# Linha Tronco (1894)
###
batch_create_route_location(
    route_name='Curitiba - Ponta Grossa',
    sub_route_name='Linha Tronco',
    sub_route_year=1894,
    locations=[
        {
            'name': 'Curitiba',
            'gauges': [1.00],
            'route_position': 1,
            'kilometer': 110.390,
            'kilometer_year': 1936,
        },
        {
            'name': 'Portão',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 118.465,
            'kilometer_year': 1936,
        },
        {
            'name': 'Barigüi',
            'gauges': [1.00],
            'route_position': 3,
            'kilometer': 124.770,
            'kilometer_year': 1936,
        },
        {
            'name': 'Araucária',
            'gauges': [1.00],
            'route_position': 4,
            'kilometer': 134.828,
            'kilometer_year': 1936,
        },
        {
            'name': 'Passaúna',
            'gauges': [1.00],
            'route_position': 5,
            'kilometer': 139.644,
            'kilometer_year': 1935,
        },
        {
            'name': 'Guajuvira',
            'gauges': [1.00],
            'route_position': 6,
            'kilometer': 152.371,
            'kilometer_year': 1935,
        },
        {
            'name': 'Balsa Nova',
            'gauges': [1.00],
            'route_position': 7,
            'kilometer': 168.941,
            'kilometer_year': 1936,
        },
        {
            'name': 'Serrinha',
            'gauges': [1.00],
            'route_position': 8,
            'kilometer': 181.646,
            'kilometer_year': 1935,
        },
        {
            'name': 'Tamandua',
            'gauges': [1.00],
            'route_position': 9,
        },
        {
            'name': 'Restinga Seca',
            'gauges': [1.00],
            'route_position': 10,
            'kilometer': 181.646,
            'kilometer_year': 1935,
        },
        {
            'name': 'Palmeira',
            'gauges': [1.00],
            'route_position': 11,
            'kilometer': 240.618,
            'kilometer_year': 1935,
        },
        {
            'name': 'Lago',
            'gauges': [1.00],
            'route_position': 12,
            'kilometer': 258.775,
            'kilometer_year': 1935,
        },
        {
            'name': 'Desvio Ribas',
            'gauges': [1.00],
            'route_position': 13,
            'kilometer': 271.970,
            'kilometer_year': 1935,
        },
        {
            'name': 'Ponta Grossa',
            'gauges': [1.00],
            'route_position': 14,
        },
    ],
)

###
# Curitiba - Ponta Grossa
# Ramal de Porto Amazonas (1892)
###
batch_create_route_location(
    route_name='Curitiba - Ponta Grossa',
    sub_route_name='Ramal de Porto Amazonas',
    sub_route_year=1892,
    locations=[
        {
            'name': 'Restinga Seca',
            'gauges': [1.00],
            'route_position': 1,
            'kilometer': 181.646,
            'kilometer_year': 1935,
        },
        {
            'name': 'Porto Amazonas',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 212.506,
            'kilometer_year': 1935,
        },
    ],
)

###
# Curitiba - Ponta Grossa
# Ramal de Rio Negro (1895)
###
batch_create_route_location(
    route_name='Curitiba - Ponta Grossa',
    sub_route_name='Ramal de Rio Negro',
    sub_route_year=1895,
    locations=[
        {
            'name': 'Serrinha',
            'gauges': [1.00],
            'route_position': 1,
            'kilometer': 0.0,
            'kilometer_year': 1935,
        },
        {
            'name': 'Lapa',
            'gauges': [1.00],
            'route_position': 2,
        },
        {
            'name': 'Lavrinhas',
            'gauges': [1.00],
            'route_position': 3,
            'kilometer': 41.000,
            'kilometer_year': 1935,
        },
        {
            'name': 'Rio da Varzea',
            'gauges': [1.00],
            'route_position': 4,
            'kilometer': 53.515,
            'kilometer_year': 1935,
        },
        {
            'name': 'Campo do Tenente',
            'gauges': [1.00],
            'route_position': 5,
            'kilometer': 61.498,
            'kilometer_year': 1936,
        },
        {
            'name': 'Roseira',
            'gauges': [1.00],
            'route_position': 6,
            'kilometer': 75,
            'kilometer_year': 1936,
        },
        {
            'name': 'Rio Negro',
            'gauges': [1.00],
            'route_position': 7,
        },
    ],
)

###
# Curitiba - Ponta Grossa
# Modificação entre Serrinha e Palmeira (1914)
###
batch_create_route_location(
    route_name='Curitiba - Ponta Grossa',
    sub_route_name='Modificação entre Serrinha e Palmeira',
    sub_route_year=1914,
    locations=[
        {
            'name': 'Serrinha',
            'gauges': [1.00],
            'route_position': 1,
            'kilometer': 181.646,
            'kilometer_year': 1935,
        },
        {
            'name': 'Nova Capivary',
            'gauges': [1.00],
            'route_position': 2,
        },
        {
            'name': 'Caiacanga',
            'gauges': [1.00],
            'route_position': 3,
            'kilometer': 181.646,
            'kilometer_year': 1935,
        },
        {
            'name': 'Porto Amazonas',
            'gauges': [1.00],
            'route_position': 4,
            'kilometer': 212.506,
            'kilometer_year': 1935,
        },
        {
            'name': 'Nova Restinga',
            'gauges': [1.00],
            'route_position': 4,
            'kilometer': 226.298,
            'kilometer_year': 1935,
        },
        {
            'name': 'Palmeira',
            'gauges': [1.00],
            'route_position': 5,
            'kilometer': 240.618,
            'kilometer_year': 1935,
        },
    ],
)

###
# Curitiba - Ponta Grossa
# Variante de Capivari (1934)
###
batch_create_route_location(
    route_name='Curitiba - Ponta Grossa',
    sub_route_name='Variante de Capivari',
    sub_route_year=1934,
    locations=[
        {
            'abbrev': 'LEB',
            'name': 'Eng. Bley (Nova Capivari)',
            'gauges': [1.00],
            'route_position': 1,
        },
        {
            'name': 'Lapa',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 30.070,
            'kilometer_year': 1935,
        },
    ],
)

###
# Curitiba - Ponta Grossa
# Variante de Rio Negro - 1964
###
batch_create_route_location(
    route_name='Curitiba - Ponta Grossa',
    sub_route_name='Variante de Rio Negro',
    sub_route_year=1964,
    locations=[
        {
            'abbrev': 'LEB',
            'name': 'Eng. Bley (Nova Capivari)',
            'gauges': [1.00],
            'route_position': 1,
            'kilometer': 0.0,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LLA',
            'name': 'Lapa (nova)',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 18.049,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LLV',
            'name': 'Lavrinhas (nova)',
            'gauges': [1.00],
            'route_position': 3,
            'kilometer': 29.049,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LVZ',
            'name': 'Rio da Varzea (nova)',
            'gauges': [1.00],
            'route_position': 4,
            'kilometer': 39.280,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LDR',
            'name': 'Parada Diretor',
            'gauges': [1.00],
            'route_position': 5,
            'kilometer': 50.280,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LRO',
            'name': 'Rio Negro (nova)',
            'gauges': [1.00],
            'route_position': 6,
            'kilometer': 61.350,
            'kilometer_year': 2014,
        },
    ],
)

###
# Curitiba - Ponta Grossa
# Variante Curitiba (nova) - Engenheiro Bley (1977)
###
batch_create_route_location(
    route_name='Curitiba - Ponta Grossa',
    sub_route_name='Variante Curitiba (nova) - Engenheiro Bley',
    sub_route_year=1977,
    locations=[
        {
            'abbrev': 'LCO',
            'name': 'Curitiba (nova)',
            'gauges': [1.00],
            'route_position': 1,
            'kilometer': 109.644,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LTE',
            'name': 'Eng. Theodoro Stresser',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 105.160,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LKP',
            'name': 'Quilômetro 103 (KM103)',
            'gauges': [1.00],
            'route_position': 3,
            'kilometer': 103.698,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LKM',
            'name': 'Quilômetro 108 (KM108)',
            'gauges': [1.00],
            'route_position': 4,
            'kilometer': 107.588,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LIC',
            'name': 'Iguaçu',
            'gauges': [1.00],
            'route_position': 5,
            'kilometer': 114.060,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LAW',
            'name': 'Araucária Terminal',
            'gauges': [1.00],
            'route_position': 6,
            'kilometer': 127.300,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LAR',
            'name': 'Araucária Carga',
            'gauges': [1.00],
            'route_position': 7,
            'kilometer': 132.200,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LAB',
            'name': 'Quilômetro 141 (KM141)',
            'gauges': [1.00],
            'route_position': 8,
            'kilometer': 140.846,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LAB',
            'name': 'General Lúcio',
            'gauges': [1.00],
            'route_position': 9,
            'kilometer': 151.513,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LBN',
            'name': 'Balsa Nova (nova)',
            'gauges': [1.00],
            'route_position': 10,
            'kilometer': 159.346,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LEB',
            'name': 'Eng. Bley (Nova Capivari)',
            'gauges': [1.00],
            'route_position': 11,
            'kilometer': 170.371,
            'kilometer_year': 2014,
        },
    ],
)

###
# Curitiba - Ponta Grossa
# Variante Engenheiro Bley - Ponta Grossa (1969)
###
batch_create_route_location(
    route_name='Curitiba - Ponta Grossa',
    sub_route_name=' Variante Eng. Bley - Ponta Grossa',
    sub_route_year=1969,
    locations=[
        {
            'abbrev': 'LEB',
            'name': 'Eng. Bley (Nova Capivari)',
            'gauges': [1.00],
            'route_position': 1,
            'kilometer': 170.371,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LOZ',
            'name': 'Ozório de Almeida',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 180.150,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LWV',
            'name': 'Walter Scott Veloso',
            'gauges': [1.00],
            'route_position': 3,
            'kilometer': 185.960,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LMO',
            'name': 'Machado da Costa',
            'gauges': [1.00],
            'route_position': 4,
            'kilometer': 196.325,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LLP',
            'name': 'Ângelo Lopes',
            'gauges': [1.00],
            'route_position': 5,
            'kilometer': 209.330,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LLY',
            'name': 'Eng. Lineu do Amaral',
            'gauges': [1.00],
            'route_position': 6,
            'kilometer': 222.742,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LDV',
            'name': 'Desvio Ribas (nova)',
            'gauges': [1.00],
            'route_position': 7,
            'kilometer': 232.457,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LVV',
            'name': 'Vila Velha',
            'gauges': [1.00],
            'route_position': 8,
            'kilometer': 240.100,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LUS',
            'name': 'Uvaranas',
            'gauges': [1.00],
            'route_position': 9,
            'kilometer': 250.050,
            'kilometer_year': 2014,
        },
    ],
)

###
# Curitiba - Rio Branco do Sul
# Ramal de Rio Branco do Sul (1909)
###
batch_create_route_location(
    route_name='Curitiba - Rio Branco do Sul',
    sub_route_name='Ramal de Rio Branco do Sul',
    sub_route_year=1909,
    locations=[
        {
            'name': 'Curitiba',
            'gauges': [1.00],
            'route_position': 1,
            'kilometer': 0,
            'kilometer_year': 1936,
        },
        {
            'name': 'Colônia Argelina',
            'gauges': [1.00],
            'route_position': 2,
        },
        {
            'name': 'Ahu',
            'gauges': [1.00],
            'route_position': 3,
        },
        {
            'abbrev': 'LCH',
            'name': 'Cachoeira',
            'gauges': [1.00],
            'route_position': 4,
        },
        {
            'abbrev': 'LTD',
            'name': 'Almirante Tamandaré',
            'gauges': [1.00],
            'route_position': 5,
            'kilometer': 20.335,
            'kilometer_year': 1936,
        },
        {
            'abbrev': 'LTR',
            'name': 'Tranqueira',
            'gauges': [1.00],
            'route_position': 5,
            'kilometer': 27.680,
            'kilometer_year': 1935,
        },
        {
            'abbrev': 'LIP',
            'name': 'Itaperussu',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 35.535,
            'kilometer_year': 1935,
        },
        {
            'abbrev': 'LBR',
            'name': 'Rio Branco do Sul',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 42.835,
            'kilometer_year': 1935,
        },
    ],
)

###
# Curitiba - Rio Branco do Sul
# Modificações no Ramal de Rio Branco do Sul (1970)
###
batch_create_route_location(
    route_name='Curitiba - Rio Branco do Sul',
    sub_route_name='Modificações no Ramal de Rio Branco do Sul',
    sub_route_year=1970,
    locations=[
        {
            'abbrev': 'LCO',
            'name': 'Curitiba (nova)',
            'gauges': [1.00],
            'route_position': 1,
            'kilometer': 0,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LCH',
            'name': 'Cachoeira',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 12.769,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LTD',
            'name': 'Almirante Tamandaré',
            'gauges': [1.00],
            'route_position': 3,
            'kilometer': 20.268,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LTR',
            'name': 'Tranqueira',
            'gauges': [1.00],
            'route_position': 4,
            'kilometer': 27.649,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LIP',
            'name': 'Itaperussu',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 35.446,
            'kilometer_year': 2014,
        },
        {
            'abbrev': 'LBR',
            'name': 'Rio Branco do Sul',
            'gauges': [1.00],
            'route_position': 2,
            'kilometer': 43.309,
            'kilometer_year': 2014,
        },
    ],
)
