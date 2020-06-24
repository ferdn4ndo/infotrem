import logging
import os




def add_sigo_numeric_range_info(list_of_numeric_ranges):
    from django.contrib.auth.models import User

    from infotrem.models.information import Information
    from infotrem.models.rolling_stock import RollingStockSigoSeriesInformation

    user = User.objects.get(username=os.environ['SYSTEM_USER_NAME'])

    for item in list_of_numeric_ranges:
        information = Information.objects.get_or_create(
            author=user,
            content=item[2],
            status=Information.InformationStatus.APPROVED,
            references=item[3],
            created_by=user,
        )[0]

        RollingStockSigoSeriesInformation.objects.get_or_create(
            sigo_start_number=item[0],
            sigo_end_number=item[1],
            information=information
        )



add_sigo_numeric_range_info([
    (0, 99999, "Vagões Particulares", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (100000, 299999, "Vagões originários da CVRD", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (300000, 599999, "Vagões originários da Fepasa", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (600000, 799999, "Vagões originários da RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (800000, 839999, "Vagões originários da ENFE", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (900000, 909999, "Locomotivas originárias da RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (910000, 911999, "Locomotivas originárias da CVRD", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (912000, 917999, "Locomotivas originárias da Fepasa", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (918000, 918099, "Locomotivas originárias da ENFE", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (918100, 919999, "Locomotivas Particulares", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (920000, 929999, "Carros originários da RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (930000, 930999, "Carros originários da CVRD", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (931000, 931999, "Carros originários da ENFE", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (933000, 937999, "Carros originários da Fepasa", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (946000, 946199, "Automotrizes de bitola larga originárias da RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (946200, 946299, "TUDH (carro motor) de bitola larga originários da RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (946300, 946399, "TUDH (carro reboque) de bitola larga originários da RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (946400, 946599, "TUE (carro motor) de bitola larga originados da RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (946600, 946699, "TUE (carro reboque) de bitola larga originados RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (947000, 947199, "Automotrizes bitola métrica RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (947200, 947299, "TUDH (carro motor) bitola métrica RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (947300, 947399, "TUDH (carro reboque) bitola métrica RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (947400, 947599, "TUE (carro motor) bitola métrica RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (947600, 947699, "TUE (carro reboque) bitola métrica RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (950000, 959999, "Equipamento de Via Permanente RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (960000, 969999, "Equipamento de Eletrotécnica RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (970000, 970499, "Guindastes RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (970500, 974999, "Equipamento de Socorro RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (975000, 979999, "Autos de Linha RFFSA", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (900001, 900100, "Locomotivas a vapor originárias da RFFSA com bitola de 0,76m", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (900101, 900400, "Locomotivas a vapor originárias da RFFSA com bitola de 1,00m", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (900401, 900500, "Locomotivas a vapor originárias da RFFSA com bitola de 1,60m", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (900501, 900750, "Locomotivas a diesel originárias da RFFSA de fabricantes diversos com bitola de 1,00m", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (900751, 900100, "Locomotivas a diesel originárias da RFFSA de fabricantes diversos com bitola de 1,60m", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (902001, 903000, "Locomotivas a diesel originárias da RFFSA fabricados pela GE com bitola de 1,00m", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (903001, 904000, "Locomotivas a diesel originárias da RFFSA fabricadas pela GE com bitola de 1,60m", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (904001, 905000, "Locomotivas a diesel originárias da RFFSA fabricados pela GM com bitola de 1,00m", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (905001, 906000, "Locomotivas a diesel originárias da RFFSA fabricadas pela GM com bitola de 1,60m", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (906001, 907000, "Locomotivas a diesel originárias da RFFSA fabricados pela ALCO com bitola de 1,00m", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (907001, 908000, "Locomotivas a diesel originárias da RFFSA fabricadas pela ALCO com bitola de 1,60m", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (900801, 909000, "Locomotivas elétricas originárias da RFFSA de fabricantes diversos com bitola de 1,00m", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
    (900901, 909999, "Locomotivas elétricas originárias da RFFSA de fabricantes diversos com bitola de 1,60m", "http://vfco.brazilia.jor.br/ferrovias/ef/codVeiculos.shtml"),
])

print("Sigo numeric ranges information created")
