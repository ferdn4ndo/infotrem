import os

from django.contrib.auth.models import User

from infotrem.models.rolling_stock import RollingStock


def add_information(author: User, item_type, name: str, information_text: str, references: str):
    from infotrem.models.information import Information
    from infotrem.models.rolling_stock import RollingStockInformation
    from infotrem.serializers.rolling_stock import RollingStockSerializer, RollingStockInformationSerializer

    rolling_stock = RollingStockSerializer.get_or_create_from_name_and_type(
        name, item_type
    )

    if RollingStockInformationSerializer.check_if_info_exists(rolling_stock, information_text):
        print("Information already registered!")
        return

    information, created = Information.objects.get_or_create(
        author=author,
        content=information_text,
        status=Information.InformationStatus.DISCUSSION,
        references=references
    )
    print("Information # {} {}!".format(information.id, 'created' if created else 'updated'))

    rolling_stock_information, created = RollingStockInformation.objects.get_or_create(
        rolling_stock=rolling_stock,
        information=information
    )
    print("RollingStockInformation # {} {}!".format(rolling_stock_information.id, 'created' if created else 'updated'))


rstype = RollingStock.RollingStockType
user = User.objects.get(username=os.environ['SYSTEM_USER_NAME'])

add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904323",
    information_text="Locomotiva transformada em Slug M-2",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904409",
    information_text="Locomotiva transferida para a Ferrovia Teresa Cristina",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904316",
    information_text="Locomotiva com tanque de combustível ampliado para 4900L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904340",
    information_text="Locomotiva com tanque de combustível ampliado para 4900L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904385",
    information_text="Locomotiva com tanque de combustível ampliado para 4900L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904391",
    information_text="Locomotiva com tanque de combustível ampliado para 4900L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904395",
    information_text="Locomotiva com tanque de combustível ampliado para 4900L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904396",
    information_text="Locomotiva com tanque de combustível ampliado para 4900L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904400",
    information_text="Locomotiva com tanque de combustível ampliado para 4900L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904404",
    information_text="Locomotiva com tanque de combustível ampliado para 4900L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904305",
    information_text="Locomotiva com tanque de combustível ampliado para 5200L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904329",
    information_text="Locomotiva com tanque de combustível ampliado para 5200L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904338",
    information_text="Locomotiva com tanque de combustível ampliado para 5200L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904377",
    information_text="Locomotiva com tanque de combustível ampliado para 5200L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904386",
    information_text="Locomotiva com tanque de combustível ampliado para 5200L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904387",
    information_text="Locomotiva com tanque de combustível ampliado para 5200L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904392",
    information_text="Locomotiva com tanque de combustível ampliado para 5200L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904381",
    information_text="Locomotiva com tanque de combustível ampliado para 6000L",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904380",
    information_text="Locomotiva já utilizou o bio-diesel como combustível (fez testes), e retornou a utilizar diesel comum",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904386",
    information_text="Locomotiva já utilizou o bio-diesel como combustível (fez testes), e retornou a utilizar diesel comum",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904334",
    information_text="Locomotiva com passadiço traseiro",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904309",
    information_text="Locomotiva com passadiço traseiro",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904409",
    information_text="Locomotiva com passadiço traseiro",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904332",
    information_text="Locomotiva com passadiço traseiro",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904310",
    information_text="Locomotiva com passadiço traseiro",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904389",
    information_text="Locomotiva com passadiço traseiro",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904304",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904305",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904321",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904329",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904331",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904332",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904333",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904338",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904341",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904349",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904352",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904356",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904359",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904363",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904368",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904377",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904380",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904381",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904383",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904385",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904386",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904387",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904391",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904392",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904395",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904396",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904397",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904399",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904403",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904404",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904405",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904412",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904413",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904420",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904423",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904426",
    information_text="Locomotiva adaptada para M1 (com plug)",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904301",
    information_text="Locomotiva acidentada e recuperada c/ peças de outras G22U",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904302",
    information_text="Locomotiva baixada",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904309",
    information_text="Locomotiva baixada no acidente da serra de São Francisco em 2012",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904317",
    information_text="Locomotiva baixada",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904324",
    information_text="Locomotiva baixada",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904324",
    information_text="Locomotiva baixada",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904327",
    information_text="Locomotiva baixada",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904328",
    information_text="Foi batizada com o nome de União na época da RFFSA",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904336",
    information_text="Locomotiva baixada",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904337",
    information_text="Locomotiva baixada",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904341",
    information_text="Locomotiva acidentada e recuperada c/ peças de outras G22U",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904347",
    information_text="Locomotiva baixada",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904348",
    information_text="Locomotiva baixada no acidente da serra de São Francisco em 2012",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904350",
    information_text="Locomotiva baixada no acidente da serra de São Francisco em 2012",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904352",
    information_text="Locomotiva baixada no acidente da serra de São Francisco em 2012",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904353",
    information_text="Locomotiva baixada",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904362",
    information_text="Foi batizada com o nome de Corupá na época da RFFSA",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904367",
    information_text="Locomotiva baixada",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904370",
    information_text="Locomotiva baixada no acidente da serra de São Francisco em 2012",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904392",
    information_text="Foi batizada com o nome de São Francisco do Sul na época da RFFSA",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904392",
    information_text="Foi usada como referência pela Frateschi na criação da sua miniatura",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904393",
    information_text="Locomotiva baixada",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904408",
    information_text="Locomotiva baixada no acidente da serra de São Francisco em 2012",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904415",
    information_text="Locomotiva microprocessada",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904428",
    information_text="Locomotiva baixada",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904301",
    information_text="Numeração original RFFSA pré-SIGO: 1501",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904302",
    information_text="Numeração original RFFSA pré-SIGO: 1502",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904303",
    information_text="Numeração original RFFSA pré-SIGO: 1503",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904304",
    information_text="Numeração original RFFSA pré-SIGO: 1504",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904305",
    information_text="Numeração original RFFSA pré-SIGO: 1505",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904306",
    information_text="Numeração original RFFSA pré-SIGO: 1506",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904307",
    information_text="Numeração original RFFSA pré-SIGO: 1507",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904308",
    information_text="Numeração original RFFSA pré-SIGO: 1508",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904309",
    information_text="Numeração original RFFSA pré-SIGO: 1509",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904310",
    information_text="Numeração original RFFSA pré-SIGO: 1510",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904311",
    information_text="Numeração original RFFSA pré-SIGO: 1511",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904312",
    information_text="Numeração original RFFSA pré-SIGO: 1512",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904313",
    information_text="Numeração original RFFSA pré-SIGO: 1513",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904314",
    information_text="Numeração original RFFSA pré-SIGO: 1514",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904315",
    information_text="Numeração original RFFSA pré-SIGO: 1515",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904316",
    information_text="Numeração original RFFSA pré-SIGO: 1516",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904317",
    information_text="Numeração original RFFSA pré-SIGO: 1517",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904318",
    information_text="Numeração original RFFSA pré-SIGO: 1518",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904319",
    information_text="Numeração original RFFSA pré-SIGO: 1519",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904320",
    information_text="Numeração original RFFSA pré-SIGO: 1520",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904321",
    information_text="Numeração original RFFSA pré-SIGO: 1521",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904322",
    information_text="Numeração original RFFSA pré-SIGO: 1522",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904323",
    information_text="Numeração original RFFSA pré-SIGO: 1523",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904324",
    information_text="Numeração original RFFSA pré-SIGO: 1524",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904325",
    information_text="Numeração original RFFSA pré-SIGO: 1525",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904326",
    information_text="Numeração original RFFSA pré-SIGO: 1526",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904327",
    information_text="Numeração original RFFSA pré-SIGO: 1527",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904328",
    information_text="Numeração original RFFSA pré-SIGO: 1528",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904329",
    information_text="Numeração original RFFSA pré-SIGO: 1529",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904330",
    information_text="Numeração original RFFSA pré-SIGO: 1530",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904331",
    information_text="Numeração original RFFSA pré-SIGO: 1531",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904332",
    information_text="Numeração original RFFSA pré-SIGO: 1532",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904333",
    information_text="Numeração original RFFSA pré-SIGO: 1533",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904334",
    information_text="Numeração original RFFSA pré-SIGO: 1534",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904335",
    information_text="Numeração original RFFSA pré-SIGO: 1535",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904336",
    information_text="Numeração original RFFSA pré-SIGO: 1536",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904337",
    information_text="Numeração original RFFSA pré-SIGO: 1537",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904338",
    information_text="Numeração original RFFSA pré-SIGO: 1538",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904339",
    information_text="Numeração original RFFSA pré-SIGO: 1539",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904340",
    information_text="Numeração original RFFSA pré-SIGO: 1540",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904341",
    information_text="Numeração original RFFSA pré-SIGO: 1541",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904342",
    information_text="Numeração original RFFSA pré-SIGO: 1542",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904343",
    information_text="Numeração original RFFSA pré-SIGO: 1543",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904344",
    information_text="Numeração original RFFSA pré-SIGO: 1544",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904345",
    information_text="Numeração original RFFSA pré-SIGO: 1545",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904346",
    information_text="Numeração original RFFSA pré-SIGO: 1546",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904347",
    information_text="Numeração original RFFSA pré-SIGO: 1547",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904348",
    information_text="Numeração original RFFSA pré-SIGO: 1548",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904349",
    information_text="Numeração original RFFSA pré-SIGO: 1549",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904350",
    information_text="Numeração original RFFSA pré-SIGO: 1550",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904351",
    information_text="Numeração original RFFSA pré-SIGO: 1551",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904352",
    information_text="Numeração original RFFSA pré-SIGO: 1552",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904353",
    information_text="Numeração original RFFSA pré-SIGO: 1553",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904354",
    information_text="Numeração original RFFSA pré-SIGO: 1554",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904355",
    information_text="Numeração original RFFSA pré-SIGO: 1555",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904356",
    information_text="Numeração original RFFSA pré-SIGO: 1556",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904357",
    information_text="Numeração original RFFSA pré-SIGO: 1557",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904358",
    information_text="Numeração original RFFSA pré-SIGO: 1558",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904359",
    information_text="Numeração original RFFSA pré-SIGO: 1559",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904360",
    information_text="Numeração original RFFSA pré-SIGO: 1560",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904361",
    information_text="Numeração original RFFSA pré-SIGO: 1561",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904362",
    information_text="Numeração original RFFSA pré-SIGO: 1562",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904363",
    information_text="Numeração original RFFSA pré-SIGO: 1563",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904364",
    information_text="Numeração original RFFSA pré-SIGO: 1564",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904365",
    information_text="Numeração original RFFSA pré-SIGO: 1565",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904366",
    information_text="Numeração original RFFSA pré-SIGO: 1566",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904367",
    information_text="Numeração original RFFSA pré-SIGO: 1567",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904368",
    information_text="Numeração original RFFSA pré-SIGO: 1568",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904369",
    information_text="Numeração original RFFSA pré-SIGO: 1569",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904370",
    information_text="Numeração original RFFSA pré-SIGO: 1570",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904371",
    information_text="Numeração original RFFSA pré-SIGO: 1571",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904372",
    information_text="Numeração original RFFSA pré-SIGO: 1572",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904373",
    information_text="Numeração original RFFSA pré-SIGO: 1573",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904374",
    information_text="Numeração original RFFSA pré-SIGO: 1574",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904375",
    information_text="Numeração original RFFSA pré-SIGO: 1575",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904376",
    information_text="Numeração original RFFSA pré-SIGO: 1576",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904377",
    information_text="Numeração original RFFSA pré-SIGO: 1577",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904378",
    information_text="Numeração original RFFSA pré-SIGO: 1578",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904379",
    information_text="Numeração original RFFSA pré-SIGO: 1579",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904380",
    information_text="Numeração original RFFSA pré-SIGO: 1580",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904381",
    information_text="Numeração original RFFSA pré-SIGO: 1581",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904382",
    information_text="Numeração original RFFSA pré-SIGO: 1582",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904383",
    information_text="Numeração original RFFSA pré-SIGO: 1583",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904384",
    information_text="Numeração original RFFSA pré-SIGO: 1584",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904385",
    information_text="Numeração original RFFSA pré-SIGO: 1585",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904386",
    information_text="Numeração original RFFSA pré-SIGO: 1586",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904387",
    information_text="Numeração original RFFSA pré-SIGO: 1587",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904388",
    information_text="Numeração original RFFSA pré-SIGO: 1588",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904389",
    information_text="Numeração original RFFSA pré-SIGO: 1589",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904390",
    information_text="Numeração original RFFSA pré-SIGO: 1590",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904391",
    information_text="Numeração original RFFSA pré-SIGO: 1591",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904392",
    information_text="Numeração original RFFSA pré-SIGO: 1592",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904393",
    information_text="Numeração original RFFSA pré-SIGO: 1593",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904394",
    information_text="Numeração original RFFSA pré-SIGO: 1594",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904395",
    information_text="Numeração original RFFSA pré-SIGO: 1595",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904396",
    information_text="Numeração original RFFSA pré-SIGO: 1596",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904397",
    information_text="Numeração original RFFSA pré-SIGO: 1597",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904398",
    information_text="Numeração original RFFSA pré-SIGO: 1598",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904399",
    information_text="Numeração original RFFSA pré-SIGO: 1599",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904400",
    information_text="Numeração original RFFSA pré-SIGO: 1600",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904401",
    information_text="Numeração original RFFSA pré-SIGO: 1601",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904402",
    information_text="Numeração original RFFSA pré-SIGO: 1602",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904403",
    information_text="Numeração original RFFSA pré-SIGO: 1603",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904404",
    information_text="Numeração original RFFSA pré-SIGO: 1604",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904405",
    information_text="Numeração original RFFSA pré-SIGO: 1605",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904406",
    information_text="Numeração original RFFSA pré-SIGO: 1606",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904407",
    information_text="Numeração original RFFSA pré-SIGO: 1607",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904408",
    information_text="Numeração original RFFSA pré-SIGO: 1608",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904409",
    information_text="Numeração original RFFSA pré-SIGO: 1609",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904410",
    information_text="Numeração original RFFSA pré-SIGO: 1610",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904411",
    information_text="Numeração original RFFSA pré-SIGO: 1611",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904412",
    information_text="Numeração original RFFSA pré-SIGO: 1612",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904413",
    information_text="Numeração original RFFSA pré-SIGO: 1613",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904414",
    information_text="Numeração original RFFSA pré-SIGO: 1614",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904415",
    information_text="Numeração original RFFSA pré-SIGO: 1615",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904416",
    information_text="Numeração original RFFSA pré-SIGO: 1616",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904417",
    information_text="Numeração original RFFSA pré-SIGO: 1617",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904418",
    information_text="Numeração original RFFSA pré-SIGO: 1618",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904419",
    information_text="Numeração original RFFSA pré-SIGO: 1619",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904420",
    information_text="Numeração original RFFSA pré-SIGO: 1620",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904421",
    information_text="Numeração original RFFSA pré-SIGO: 1621",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904422",
    information_text="Numeração original RFFSA pré-SIGO: 1622",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904423",
    information_text="Numeração original RFFSA pré-SIGO: 1623",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904424",
    information_text="Numeração original RFFSA pré-SIGO: 1624",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904425",
    information_text="Numeração original RFFSA pré-SIGO: 1625",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904426",
    information_text="Numeração original RFFSA pré-SIGO: 1626",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904427",
    information_text="Numeração original RFFSA pré-SIGO: 1627",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904428",
    information_text="Numeração original RFFSA pré-SIGO: 1628",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)
add_information(
    author=user,
    item_type=rstype.LOCOMOTIVE,
    name="G22U 904429",
    information_text="Numeração original RFFSA pré-SIGO: 1629",
    references="https://pt.wikipedia.org/wiki/EMD_G22U"
)


