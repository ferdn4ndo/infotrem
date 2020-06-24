import os

from django.contrib.auth.models import User

from infotrem.models.rolling_stock import RollingStock


def add_information(author: User, item_type, name: str, information_text: str, references: str):
    from infotrem.models.information import Information
    from infotrem.models.rolling_stock import RollingStockInformation
    from infotrem.serializers.information import InformationSerializer
    from infotrem.serializers.rolling_stock import RollingStockSerializer, RollingStockInformationSerializer
    from django.contrib.auth.models import User

    user = User.objects.get(username=os.environ['SYSTEM_USER_NAME'])

    rolling_stock = RollingStockSerializer.get_or_create_from_name_and_type(
        name, item_type
    )

    if RollingStockInformationSerializer.check_if_info_exists(rolling_stock, information_text):
        print("Information already registered!")
        return

    information = InformationSerializer(data={
        "author": author,
        "content": information_text,
        "status": Information.InformationStatus.DISCUSSION,
        "references": references,
    })
    print("Information # {} created!".format(information.id))

    rolling_stock_information, created = RollingStockInformation.objects.get_or_create(
        rolling_stock=rolling_stock,
        information=information
    )
    print("RollingStockInformation # {} {}!".format(rolling_stock_information.id, 'created' if created else 'updated'))

rstype = RollingStock.RollingStockType
user = User.objects.get(username=os.environ['SYSTEM_USER_NAME'])

informations = [
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "ACR 609585",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 610035",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FLR 610067",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610597",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611004",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611057",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621024",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621590",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621963",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PCS 616091",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PMR 617342",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 623221",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623756",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FSR 610080",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610499",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610646",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610678",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610877",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610957",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610993",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611000",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611024",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614303",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PMR 617277",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNP 620511",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 624273",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNP 609758",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611030",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PDQ 616242",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 623828",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 623834",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 623837",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 623841",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 623843",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 623854",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 623987",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 623988",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 623993",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 623999",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 624003",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 624004",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 624008",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 624012",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 624013",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 646155",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 646157",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 646162",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 646164",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 646171",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 646175",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 646177",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 646178",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622721",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622908",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623485",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GFS 613748",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HNR 624020",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610574",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610854",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611175",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614316",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 623858",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNP 609777",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610616",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610619",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610823",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610862",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610938",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610948",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610960",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611184",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611189",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 613926",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614183",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GNR 614415",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PMR 617312",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617356",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617374",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617507",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620528",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620872",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620974",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621185",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621602",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622100",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622744",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDR 622787",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDR 622832",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDR 622860",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622981",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623441",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623464",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623506",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623515",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623562",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623602",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623697",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623713",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623766",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623801",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HES 623818",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HTS 623875",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HNR 624041",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HNR 624047",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 609659",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 610034",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610503",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610560",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610785",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610794",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610800",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610818",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610834",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610901",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610929",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610930",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610935",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610994",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611055",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614069",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614073",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614228",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614236",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614277",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614284",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HNS 615930",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 616346",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 620109",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620658",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620861",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621087",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621545",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621734",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621804",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621901",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622006",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622015",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622051",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622072",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622073",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622117",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622158",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622231",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622278",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622286",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622291",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621081",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621083",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622718",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622768",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622810",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622821",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622823",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622839",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622861",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622896",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622921",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622925",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622941",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622942",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622973",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622984",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622996",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 623011",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 623018",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 623022",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 623056",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 623057",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 623104",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623362",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HNR 624023",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610462",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610470",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610474",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610599",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610713",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610731",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610762",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610832",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610843",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611083",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611145",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611192",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 613984",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 613989",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 613990",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614003",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614084",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614102",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614213",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614262",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614305",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614323",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614337",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GNR 614367",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 616124",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617256",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TCR 617567",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TCS 617590",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621350",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621599",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621601",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621632",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621641",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621738",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621868",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621881",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621958",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621966",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621996",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622048",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622160",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622166",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622211",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622695",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TCS 646946",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623331",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNR 646494",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNR 646502",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 613935",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 613953",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 613955",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614052",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614089",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614092",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614186",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614194",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614232",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GNR 614433",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GNR 614444",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TCR 617572",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 624415",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 624474",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611198",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 619685",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 619699",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 619899",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 620007",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 620010",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 620025",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 620161",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 620204",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 620351",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 620413",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621512",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621514",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621518",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621521",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621538",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621561",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621563",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621564",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621592",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621605",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621613",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621614",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621622",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621634",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621644",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621646",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621657",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621663",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621685",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621692",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621693",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621695",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621697",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621699",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621700",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621709",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621717",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621736",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621752",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621753",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621760",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621765",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621768",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621769",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621770",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621777",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621783",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621803",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621805",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621809",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621820",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621834",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621838",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621859",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621862",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621877",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621887",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621890",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621895",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621896",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621909",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621916",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621928",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621933",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621940",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621953",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621954",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621970",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621971",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621985",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621986",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622003",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622008",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622019",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622027",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622040",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622041",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622050",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622056",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622059",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622087",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622090",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622092",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622103",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622116",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622119",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622126",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622156",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622171",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622178",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622181",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622182",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622188",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622205",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622212",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622217",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622219",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622224",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622229",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622240",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622241",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622246",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622250",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622271",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622272",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622274",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622289",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622297",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622785",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 609665",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNP 609707",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNP 609760",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNP 609774",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNP 609789",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 609975",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNR 610419",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610479",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610498",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610520",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610526",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610598",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610804",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610889",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610907",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610924",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610985",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611013",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614339",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GNR 614365",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GNR 614372",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 616100",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PER 616121",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 616126",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 616132",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 616154",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 616164",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 616174",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 616234",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 616755",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 617068",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617278",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617371",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617375",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617470",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617482",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617500",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620604",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620607",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620613",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620654",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620659",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620664",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620684",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620697",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620726",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620773",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620807",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620843",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620922",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620923",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620941",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620961",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620972",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620978",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621066",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621088",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621122",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621125",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621129",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621135",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621137",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621145",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621168",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621252",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621299",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621309",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621318",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621375",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621404",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621413",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621434",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621465",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621485",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621491",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621497",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621524",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621567",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621606",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621673",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621723",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621724",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621832",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621866",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621891",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622066",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622075",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622280",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622865",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDR 623152",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623316",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623324",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623337",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 623341",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PDS 623384",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623408",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623431",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623450",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623475",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623484",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623547",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GNS 623580",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623643",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623646",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623669",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623700",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623702",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623736",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623743",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623753",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623783",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNP 642216",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRR 642219",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 642343",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 642361",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNR 644939",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 645665",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNP 609721",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNP 609769",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611040",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 614931",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PAR 616080",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 616222",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621661",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621993",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623556",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 624411",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610504",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610716",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610744",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611186",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 613924",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TCR 617540",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TCR 617563",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TCR 617564",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TCR 617569",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TCR 617570",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TNR 617576",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TCR 617577",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621750",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621844",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622033",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622228",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TNS 641940",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TNS 641946",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TNS 641948",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TNS 641955",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TNS 641956",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TNS 641957",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TNS 641963",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TNS 641965",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TNS 641970",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TNS 641973",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TNS 641974",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TNS 641981",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNP 644902",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TCR 646945",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PAR 616002",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PCR 616004",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PAR 616014",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PAR 616038",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PAR 616041",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PAR 616051",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PAR 616064",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PAR 616066",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PAR 616070",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PAR 616079",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PCS 616092",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PCS 616097",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PCS 616098",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620575",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620831",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620855",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621014",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621057",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621098",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621214",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621287",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622707",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622725",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622736",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622740",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622745",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622842",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622866",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622867",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622907",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622936",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622951",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622986",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 623068",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 623154",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 623213",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 623231",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 623289",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GNS 623318",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623343",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623430",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623453",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623483",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623523",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623529",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623532",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623538",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623544",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623560",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623569",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623589",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623590",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623593",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623605",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623619",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623651",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623674",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623685",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623692",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623711",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623733",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623744",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623759",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623784",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HNR 624044",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HNR 624045",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HNR 624054",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "TCR 624759",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNQ 642293",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 616130",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622203",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNR 646497",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "QNR 646942",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617323",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 610092",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 610125",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 610146",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 610298",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610548",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610586",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610682",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610775",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610888",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611177",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614181",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GNR 614446",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617324",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617350",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 617403",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PMS 617407",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617472",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 619721",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 619740",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 619742",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 619746",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 619775",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 619819",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620526",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620649",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620662",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620782",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620796",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620870",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620964",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620984",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621071",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621652",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621823",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621857",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621886",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621918",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621946",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622109",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622197",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622242",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622260",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622690",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622738",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622757",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622770",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDR 622888",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDR 622890",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623354",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623510",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623748",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610900",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614094",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614158",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614190",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 619758",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FHS 620101",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622055",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 622202",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617387",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617454",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617468",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622716",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDR 622850",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623534",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623549",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623636",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GNS 623655",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623677",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623745",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623769",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623797",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PCS 616093",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GFS 622584",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622848",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 623350",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 623648",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623687",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PBS 624066",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PBS 624099",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PBS 624109",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PBS 624122",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PBS 624133",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PBS 624143",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PBS 624161",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PBS 624221",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 624299",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621589",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 621766",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 623138",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GNS 623414",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623536",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623617",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623649",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GTS 623799",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PPS 623806",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 623168",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620657",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620661",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620875",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620912",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621119",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622680",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 623089",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 623255",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614205",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 609930",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 609970",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 610079",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 610111",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 610142",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 610174",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 610208",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 610231",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 610287",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRR 610292",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 610321",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNR 610436",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 610946",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611090",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FRS 611160",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 614153",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GNR 614393",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "HNS 615870",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PES 616248",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617221",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617341",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617343",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617383",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PMS 617401",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "PNR 617512",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620698",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620755",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 620784",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GQR 621080",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622720",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622727",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622830",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622892",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 622935",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 623058",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 623078",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 623134",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPR 623158",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNP 609804",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "FNP 642215",
        "information_text": "Vagão arrendado inservível, substituído da malha inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo I)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 614505",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 614687",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 614740",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 614760",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 614766",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 614806",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 614848",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 614857",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 614858",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 614893",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 614900",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GPS 614937",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728359",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728360",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728361",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728362",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728363",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728364",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728365",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728366",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728367",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728368",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728369",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728370",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728371",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728372",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728373",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728374",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728375",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728376",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728377",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728378",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728379",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728380",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728383",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728384",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728387",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728388",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728389",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728390",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728391",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728392",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728394",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728395",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728396",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728397",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728398",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728399",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728400",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728401",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728402",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728403",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728404",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728405",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728406",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728407",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728408",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728409",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728410",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728411",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728412",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728413",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728414",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728415",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728416",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728417",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728418",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728419",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728420",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728421",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728422",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728423",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728424",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728425",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728426",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728427",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728428",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728429",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728430",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728431",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728432",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728433",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728434",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728435",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728437",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728438",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728439",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728440",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728441",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728442",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728443",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728444",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728445",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728446",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728447",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728448",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728449",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728450",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728451",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728452",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728453",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728454",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728455",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728456",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728457",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728458",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728459",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728460",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728463",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728464",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728467",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728468",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728469",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728470",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728471",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728472",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728473",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728474",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728475",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728476",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728477",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728478",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728479",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728480",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728483",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728484",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728485",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728486",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728487",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728488",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728490",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728491",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728492",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728493",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728494",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728495",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728496",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728497",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728498",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728499",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728500",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728501",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728502",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728503",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728504",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728505",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728507",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728508",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728509",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728510",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728511",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728512",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728513",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728514",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728515",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728516",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728517",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728521",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728523",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728524",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728527",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728532",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728537",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728538",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728555",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728556",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728557",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728558",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728561",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728562",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728563",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728564",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728577",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728578",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728579",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728580",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728581",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728582",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728583",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728584",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728587",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728588",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728589",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728590",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728593",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728594",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728597",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728598",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728599",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728600",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728601",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728602",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728603",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728604",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728605",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728606",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728607",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728608",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728609",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728610",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728611",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728612",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728613",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728614",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728615",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728616",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728617",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728618",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728619",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728620",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728621",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728622",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728625",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728626",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728629",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728630",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728631",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728632",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728635",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728636",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728637",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728638",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728639",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728640",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728641",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728642",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728643",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728644",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728645",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728646",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728647",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728648",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728649",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728650",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728651",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728652",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728653",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728654",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728655",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728656",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728659",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728660",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728661",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728662",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728663",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728664",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728665",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728666",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728667",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728668",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728669",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728670",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728671",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728672",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728673",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728674",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728675",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728676",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728677",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728678",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728679",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728680",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728681",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728682",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728683",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728684",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728685",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728686",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728687",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728688",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728689",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728690",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728691",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728692",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728694",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728703",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728704",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728705",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728706",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728707",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728708",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728709",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728710",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728711",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728712",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728713",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728714",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728715",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728716",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728717",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728718",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728719",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728720",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728721",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728722",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728723",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728724",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728725",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728726",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728727",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728728",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728729",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728730",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728731",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728732",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728733",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728734",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728735",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728736",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728737",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728738",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728739",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728740",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728741",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728742",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728743",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728744",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728749",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728750",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728751",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728752",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728753",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728754",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728755",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728756",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728757",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728758",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728759",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728760",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728761",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728762",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728763",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728764",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728767",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728768",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728769",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728770",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728771",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728772",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728773",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728774",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728775",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728776",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728777",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728778",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728779",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728780",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728781",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728782",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728785",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728786",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728787",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728788",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728789",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728790",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728791",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728792",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728793",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728794",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728795",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728796",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728799",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728800",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728801",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728802",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728805",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728806",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728807",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 728808",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737481",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737482",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737483",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737484",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737485",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737486",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737487",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737488",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737491",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737492",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737493",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737494",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737495",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737496",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737497",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737498",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737499",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737500",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737501",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737502",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737505",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737506",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737509",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737510",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737511",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737512",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737513",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737514",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737515",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737516",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737517",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737518",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737519",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737520",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737525",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737526",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737527",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737528",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737531",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737532",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737533",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737534",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737535",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737536",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737537",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737538",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737539",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737540",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737541",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737542",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737545",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737546",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737547",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737548",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737549",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737550",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737551",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737552",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737553",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737554",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737555",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737556",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737559",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737560",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737561",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737562",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737563",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737564",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737565",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737566",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737567",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737568",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737569",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737570",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737571",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737572",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737573",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737574",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737575",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737576",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737577",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737578",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737579",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737580",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737581",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737582",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737585",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737586",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737589",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737590",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737591",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737592",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737593",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737594",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737595",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737596",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737597",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737598",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737599",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737600",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737601",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737602",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737603",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737604",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737605",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737606",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737607",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737608",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737609",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737610",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737611",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737612",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737613",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737614",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737615",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737616",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737617",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737618",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737619",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737620",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737621",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737622",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737623",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737624",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737625",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737626",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737627",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737628",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737629",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDT 737630",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737853",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737854",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737855",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737856",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737857",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737858",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737859",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737860",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737861",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737862",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737863",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737864",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737865",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737866",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737867",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737868",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737869",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737870",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737871",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737872",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737873",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737874",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737875",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737876",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737877",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GDS 737878",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737928",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737929",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737930",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737931",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737932",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737933",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737934",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737935",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737936",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737937",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737938",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737939",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737940",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737941",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737942",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737943",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737944",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737945",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737946",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737947",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737948",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737949",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737950",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737951",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.FREIGHT_CAR,
        "name": "GHS 737952",
        "information_text": "Vagão operacional utilizado como troca (substituto) da malha arrendada inativa da MRS (ANTT - portaria nº89 de 5 de Abril de 2011 - Anexo II)",
        "references": "http://vfco.brazilia.jor.br/ferrovias/estrada.de.ferro.central.do.brasil/2011-04-05-portaria-089-ANTT.shtml"
    },
    {
        "author": user,
        "item_type": rstype.NON_REVENUE_CAR,
        "name": "CNQ 609609",
        "information_text": "Ex NCC 031000 que circulou na década de 90 em trens de containers entre Rio e São Paulo",
        "references": "http://vfco.brazilia.jor.br/vag/caboose/vagao-caboose-CNQ-trem-containers-SR3-RFFSA.shtml"
    },
    {
        "author": user,
        "item_type": rstype.NON_REVENUE_CAR,
        "name": "CNQ 609613",
        "information_text": "Ex NCC 031004 que circulou na década de 90 em trens de containers entre Rio e São Paulo",
        "references": "http://vfco.brazilia.jor.br/vag/caboose/vagao-caboose-CNQ-trem-containers-SR3-RFFSA.shtml"
    }
]
