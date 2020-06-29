import logging

from infotrem.models.rolling_stock_freight_car import RollingStockFreightCarCategory, \
    RollingStockFreightCarGrossWeightType
from infotrem.models.track_gauge_model import TrackGauge


# Fright cars categories
RollingStockFreightCarCategory.objects.get_or_create(letter='A', name='Gaiola')
RollingStockFreightCarCategory.objects.get_or_create(letter='C', name='Caboose')
RollingStockFreightCarCategory.objects.get_or_create(letter='F', name='Fechado')
RollingStockFreightCarCategory.objects.get_or_create(letter='G', name='Gondola')
RollingStockFreightCarCategory.objects.get_or_create(letter='H', name='Hopper')
RollingStockFreightCarCategory.objects.get_or_create(letter='I', name='Isotérmico')
RollingStockFreightCarCategory.objects.get_or_create(letter='P', name='Plataforma')
RollingStockFreightCarCategory.objects.get_or_create(letter='T', name='Tanque')


def add_freight_car_type(category_letter, types):
    from infotrem.models.rolling_stock_freight_car import RollingStockFreightCarCategory, RollingStockFreightCarType

    category = RollingStockFreightCarCategory.objects.get(letter=category_letter)
    for car_type in types:
        RollingStockFreightCarType.objects.get_or_create(
            category=category,
            letters=car_type[0],
            description=car_type[1],
        )

# Freight cars types
add_freight_car_type('A', [
    ('AC', 'Gaiola com coberta com estrado e estrutura metálica (inclui réguas de madeira)'),
    ('AM', 'Gaiola com cobertura de madeira'),
    ('AR', 'Gaiola para animais de raça'),
    ('AV', 'Gaiola para aves'),
    ('AD', 'Gaiola descoberta'),
    ('AN', 'Gaiola não remunerada'),
    ('AQ', 'Gaiola de outros tipos'),
])
add_freight_car_type('C', [
    ('CC', 'Caboose convencional'),
    ('CB', 'Caboose com compartimento para bagagem'),
    ('CN', 'Caboose não remunerado'),
    ('CQ', 'Caboose de outros tipos'),
])
add_freight_car_type('F', [
    ('FR', 'Fechado convencional, caixa metálica com revestimento'),
    ('FS', 'Fechado convencional, caixa metálica sem revestimento'),
    ('FM', 'Fechado convencional, caixa de madeira ou mista'),
    ('FE', 'Fechado com escotilhas'),
    ('FH', 'Fechado com escotilhas e tremonhas'),
    ('FL', 'Fechado com laterais corrediças (all door)'),
    ('FP', 'Fechado com escotilhas, portas basculantes, fundo em lombo de camelo e proteção anti-corrosiva'),
    ('FV', 'Fechado ventilado'),
    ('FN', 'Fechado não remunerado'),
    ('FQ', 'Fechado de outros tipos'),
])
add_freight_car_type('G', [
    ('GD', 'Gôndola para descarga em car-dumper'),
    ('GP', 'Gôndola com bordas fixas e portas laterais'),
    ('GF', 'Gôndola com bordas fixas e fundo móvel (drop-bottom)'),
    ('GM', 'Gôndola com bordas fixas e cobertura móvel'),
    ('GT', 'Gôndola com bordas tombantes'),
    ('GS', 'Gôndola com bordas semi-tombantes'),
    ('GH', 'Gôndola com bordas basculantes ou semi-tombantes com fundo em lombo de camelo'),
    ('GC', 'Gôndola com bordas basculantes ou semi-tombantes com fundo em lombo de camelo e cobertura móvel'),
    ('GB', 'Gôndola basculante'),
    ('GN', 'Gôndola não remunerado'),
    ('GQ', 'Gôndola outros tipos'),
])
add_freight_car_type('H', [
    ('HF', 'Hooper fechado convencional'),
    ('HP', 'Hooper fechado com proteção anti-corrosiva'),
    ('HE', 'Hooper tanque (center-flow) com proteção anti-corrosiva'),
    ('HT', 'Hooper tanque (center-flow) convencional'),
    ('HA', 'Hooper aberto'),
    ('HN', 'Hooper não remunerado'),
    ('HQ', 'Hooper de outros tipos'),
])
add_freight_car_type('I', [
    ('IC', 'Isotérmico convencional'),
    ('IF', 'Isotérmico frigorífico'),
    ('IN', 'Isotérmico não remunerado'),
    ('IQ', 'Isotérmico de outros tipos'),
])
add_freight_car_type('P', [
    ('PM', 'Plataforma convencional com piso de madeira'),
    ('PE', 'Plataforma convencional com piso metálico'),
    ('PD', 'Plataforma convencional com disposito p/ containers'),
    ('PC', 'Plataforma para containers'),
    ('PR', 'Plataforma com estrado rebaixado'),
    ('PT', 'Plataforma para auto-trem'),
    ('PG', 'Plataforma para piggy-back'),
    ('PP', 'Plataforma com cabeceira (bulkhead)'),
    ('PB', 'Plataforma para bobinas'),
    ('PA', 'Plataforma com 2 pavimentos, para automóveis'),
    ('PN', 'Plataforma não remunerada'),
    ('PQ', 'Plataforma de outros tipos'),
])
add_freight_car_type('T', [
    ('TC', 'Tanque convencional'),
    ('TS', 'Tanque com serpentinas para aquecimento'),
    ('TP', 'Tanque para produtos pulverulentos'),
    ('TF', 'Tanque para fertilizantes'),
    ('TA', 'Tanque para ácidos ou outros corrosivos líquidos'),
    ('TG', 'para gás liquifeito de petróleo'),
    ('TN', 'Tanque não remunerado'),
    ('TQ', 'Tanque de outros tipos'),
])

# Freight cars gross weight type
metric_gauge = TrackGauge.objects.get(tag='NARROW')
RollingStockFreightCarGrossWeightType.objects.get_or_create(letter='A', max_gross_tons=30.0, gauge=metric_gauge)
RollingStockFreightCarGrossWeightType.objects.get_or_create(letter='B', max_gross_tons=47.0, gauge=metric_gauge)
RollingStockFreightCarGrossWeightType.objects.get_or_create(letter='C', max_gross_tons=64.0, gauge=metric_gauge)
RollingStockFreightCarGrossWeightType.objects.get_or_create(letter='D', max_gross_tons=80.0, gauge=metric_gauge)
RollingStockFreightCarGrossWeightType.objects.get_or_create(letter='E', max_gross_tons=100.0, gauge=metric_gauge)
RollingStockFreightCarGrossWeightType.objects.get_or_create(letter='F', max_gross_tons=119.0, gauge=metric_gauge)
RollingStockFreightCarGrossWeightType.objects.get_or_create(letter='G', max_gross_tons=143.0, gauge=metric_gauge)

large_gauge = TrackGauge.objects.get(tag='BROAD')
RollingStockFreightCarGrossWeightType.objects.get_or_create(letter='P', max_gross_tons=47.0, gauge=large_gauge)
RollingStockFreightCarGrossWeightType.objects.get_or_create(letter='Q', max_gross_tons=64.0, gauge=large_gauge)
RollingStockFreightCarGrossWeightType.objects.get_or_create(letter='R', max_gross_tons=80.0, gauge=large_gauge)
RollingStockFreightCarGrossWeightType.objects.get_or_create(letter='S', max_gross_tons=100.0, gauge=large_gauge)
RollingStockFreightCarGrossWeightType.objects.get_or_create(letter='T', max_gross_tons=119.0, gauge=large_gauge)
RollingStockFreightCarGrossWeightType.objects.get_or_create(letter='U', max_gross_tons=143.0, gauge=large_gauge)

print("Freight car types created")
