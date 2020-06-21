import logging
import os

from django.contrib.auth.models import User

from infotrem.models.information import Information
from infotrem.models.rolling_stock import RollingStockSigoSeriesInformation


def add_sigo_numeric_range_info(list_of_numeric_ranges, user: User):
    for item in list_of_numeric_ranges:
        information = Information.objects.get_or_create(
            author=user,
            content=item[2],
            status=Information.InformationStatus.APPROVED,
        )

        RollingStockSigoSeriesInformation.objects.get_or_create(
            start_number=item[0],
            end_number=item[1],
            information=information
        )


def run():
    user = User.objects.get(username=os.environ['SYSTEM_USER_NAME'])

    add_sigo_numeric_range_info([
        (0, 99999, "Vagões Particulares"),
        (100000, 299999, "Vagões originários da CVRD"),
        (300000, 599999, "Vagões originários da Fepasa"),
        (600000, 799999, "Vagões originários da RFFSA"),
        (800000, 839999, "Vagões originários da ENFE"),
        (900000, 909999, "Locomotivas originárias da RFFSA"),
        (910000, 911999, "Locomotivas originárias da CVRD"),
        (912000, 917999, "Locomotivas originárias da Fepasa"),
        (918000, 918099, "Locomotivas originárias da ENFE"),
        (918100, 919999, "Locomotivas Particulares"),
        (920000, 929999, "Carros originários da RFFSA"),
        (930000, 930999, "Carros originários da CVRD"),
        (931000, 931999, "Carros originários da ENFE"),
        (933000, 937999, "Carros originários da Fepasa"),
        (946000, 946199, "Automotrizes de bitola larga originárias da RFFSA"),
        (946200, 946299, "TUDH (carro motor) de bitola larga originários da RFFSA"),
        (946300, 946399, "TUDH (carro reboque) de bitola larga originários da RFFSA"),
        (946400, 946599, "TUE (carro motor) de bitola larga originados da RFFSA"),
        (946600, 946699, "TUE (carro reboque) de bitola larga originados RFFSA"),
        (947000, 947199, "Automotrizes bitola métrica RFFSA"),
        (947200, 947299, "TUDH (carro motor) bitola métrica RFFSA"),
        (947300, 947399, "TUDH (carro reboque) bitola métrica RFFSA"),
        (947400, 947599, "TUE (carro motor) bitola métrica RFFSA"),
        (947600, 947699, "TUE (carro reboque) bitola métrica RFFSA"),
        (950000, 959999, "Equipamento de Via Permanente RFFSA"),
        (960000, 969999, "Equipamento de Eletrotécnica RFFSA"),
        (970000, 970499, "Guindastes RFFSA"),
        (970500, 974999, "Equipamento de Socorro RFFSA"),
        (975000, 979999, "Autos de Linha RFFSA"),
        (900001, 900100, "Locomotivas a vapor originárias da RFFSA com bitola de 0,76m"),
        (900101, 900400, "Locomotivas a vapor originárias da RFFSA com bitola de 1,00m"),
        (900401, 900500, "Locomotivas a vapor originárias da RFFSA com bitola de 1,60m"),
        (900501, 900750, "Locomotivas a diesel originárias da RFFSA de fabricantes diversos com bitola de 1,00m"),
        (900751, 900100, "Locomotivas a diesel originárias da RFFSA de fabricantes diversos com bitola de 1,60m"),
        (902001, 903000, "Locomotivas a diesel originárias da RFFSA fabricados pela GE com bitola de 1,00m"),
        (903001, 904000, "Locomotivas a diesel originárias da RFFSA fabricadas pela GE com bitola de 1,60m"),
        (904001, 905000, "Locomotivas a diesel originárias da RFFSA fabricados pela GM com bitola de 1,00m"),
        (905001, 906000, "Locomotivas a diesel originárias da RFFSA fabricadas pela GM com bitola de 1,60m"),
        (906001, 907000, "Locomotivas a diesel originárias da RFFSA fabricados pela ALCO com bitola de 1,00m"),
        (907001, 908000, "Locomotivas a diesel originárias da RFFSA fabricadas pela ALCO com bitola de 1,60m"),
        (900801, 909000, "Locomotivas elétricas originárias da RFFSA de fabricantes diversos com bitola de 1,00m"),
        (900901, 909999, "Locomotivas elétricas originárias da RFFSA de fabricantes diversos com bitola de 1,60m"),
    ], user)

    logging.info("Sigo numeric ranges information created")
