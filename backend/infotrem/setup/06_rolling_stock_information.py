import os

from django.contrib.auth.models import User

from infotrem.models.information import Information
from infotrem.models.rolling_stock import RollingStock, RollingStockInformation
from infotrem.serializers.rolling_stock import RollingStockSerializer


def add_information(user: User, item_type, name: str, information_text: str):
    rolling_stock = RollingStockSerializer.get_or_create_from_name_and_type(
        name, item_type
    )

    information = Information.objects.create(
        author=user,
        content=information_text,
        status=Information.InformationStatus.DISCUSSION,
    )
    information.save()

    rolling_stock_information = RollingStockInformation.objects.create(
        rolling_stock=rolling_stock,
        information=information
    )
    rolling_stock_information.save()


def run():
    rstype = RollingStock.RollingStockType
    user = User.objects.get(username=os.environ['SYSTEM_USER_NAME'])

    add_information(user, rstype.LOCOMOTIVE, "G22U 904323", "Locomotiva transformada em Slug M-2")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904409", "Locomotiva transferida para a Ferrovia Teresa Cristina")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904316", "Locomotiva com tanque de combustível ampliado para 4900L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904340", "Locomotiva com tanque de combustível ampliado para 4900L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904385", "Locomotiva com tanque de combustível ampliado para 4900L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904391", "Locomotiva com tanque de combustível ampliado para 4900L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904395", "Locomotiva com tanque de combustível ampliado para 4900L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904396", "Locomotiva com tanque de combustível ampliado para 4900L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904400", "Locomotiva com tanque de combustível ampliado para 4900L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904404", "Locomotiva com tanque de combustível ampliado para 4900L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904305", "Locomotiva com tanque de combustível ampliado para 5200L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904329", "Locomotiva com tanque de combustível ampliado para 5200L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904338", "Locomotiva com tanque de combustível ampliado para 5200L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904377", "Locomotiva com tanque de combustível ampliado para 5200L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904386", "Locomotiva com tanque de combustível ampliado para 5200L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904387", "Locomotiva com tanque de combustível ampliado para 5200L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904392", "Locomotiva com tanque de combustível ampliado para 5200L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904381", "Locomotiva com tanque de combustível ampliado para 6000L")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904380", "Locomotiva já utilizou o bio-diesel como combustível (fez testes), e retornou a utilizar diesel comum")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904386", "Locomotiva já utilizou o bio-diesel como combustível (fez testes), e retornou a utilizar diesel comum")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904334", "Locomotiva com passadiço traseiro")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904309", "Locomotiva com passadiço traseiro")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904409", "Locomotiva com passadiço traseiro")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904332", "Locomotiva com passadiço traseiro")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904310", "Locomotiva com passadiço traseiro")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904389", "Locomotiva com passadiço traseiro")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904304", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904305", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904321", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904329", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904331", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904332", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904333", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904338", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904341", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904349", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904352", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904356", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904359", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904363", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904368", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904377", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904380", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904381", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904383", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904385", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904386", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904387", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904391", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904392", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904395", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904396", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904397", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904399", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904403", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904404", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904405", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904412", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904413", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904420", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904423", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904426", "Locomotiva adaptada para M1 (com plug)")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904301", "Locomotiva acidentada e recuperada c/ peças de outras G22U")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904302", "Locomotiva baixada")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904309", "Locomotiva baixada no acidente da serra de São Francisco em 2012")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904317", "Locomotiva baixada")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904324", "Locomotiva baixada")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904324", "Locomotiva baixada")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904327", "Locomotiva baixada")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904328", "Foi batizada com o nome de União na época da RFFSA")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904336", "Locomotiva baixada")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904337", "Locomotiva baixada")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904341", "Locomotiva acidentada e recuperada c/ peças de outras G22U")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904347", "Locomotiva baixada")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904348", "Locomotiva baixada no acidente da serra de São Francisco em 2012")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904350", "Locomotiva baixada no acidente da serra de São Francisco em 2012")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904352", "Locomotiva baixada no acidente da serra de São Francisco em 2012")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904353", "Locomotiva baixada")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904362", "Foi batizada com o nome de Corupá na época da RFFSA")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904367", "Locomotiva baixada")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904370", "Locomotiva baixada no acidente da serra de São Francisco em 2012")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904392", "Foi batizada com o nome de São Francisco do Sul na época da RFFSA")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904392", "Foi usada como referência pela Frateschi na criação da sua miniatura")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904393", "Locomotiva baixada")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904408", "Locomotiva baixada no acidente da serra de São Francisco em 2012")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904415", "Locomotiva microprocessada")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904428", "Locomotiva baixada")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904301", "Numeração original RFFSA pré-SIGO: 1501")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904302", "Numeração original RFFSA pré-SIGO: 1502")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904303", "Numeração original RFFSA pré-SIGO: 1503")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904304", "Numeração original RFFSA pré-SIGO: 1504")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904305", "Numeração original RFFSA pré-SIGO: 1505")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904306", "Numeração original RFFSA pré-SIGO: 1506")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904307", "Numeração original RFFSA pré-SIGO: 1507")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904308", "Numeração original RFFSA pré-SIGO: 1508")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904309", "Numeração original RFFSA pré-SIGO: 1509")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904310", "Numeração original RFFSA pré-SIGO: 1510")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904311", "Numeração original RFFSA pré-SIGO: 1511")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904312", "Numeração original RFFSA pré-SIGO: 1512")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904313", "Numeração original RFFSA pré-SIGO: 1513")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904314", "Numeração original RFFSA pré-SIGO: 1514")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904315", "Numeração original RFFSA pré-SIGO: 1515")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904316", "Numeração original RFFSA pré-SIGO: 1516")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904317", "Numeração original RFFSA pré-SIGO: 1517")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904318", "Numeração original RFFSA pré-SIGO: 1518")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904319", "Numeração original RFFSA pré-SIGO: 1519")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904320", "Numeração original RFFSA pré-SIGO: 1520")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904321", "Numeração original RFFSA pré-SIGO: 1521")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904322", "Numeração original RFFSA pré-SIGO: 1522")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904323", "Numeração original RFFSA pré-SIGO: 1523")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904324", "Numeração original RFFSA pré-SIGO: 1524")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904325", "Numeração original RFFSA pré-SIGO: 1525")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904326", "Numeração original RFFSA pré-SIGO: 1526")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904327", "Numeração original RFFSA pré-SIGO: 1527")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904328", "Numeração original RFFSA pré-SIGO: 1528")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904329", "Numeração original RFFSA pré-SIGO: 1529")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904330", "Numeração original RFFSA pré-SIGO: 1530")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904331", "Numeração original RFFSA pré-SIGO: 1531")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904332", "Numeração original RFFSA pré-SIGO: 1532")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904333", "Numeração original RFFSA pré-SIGO: 1533")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904334", "Numeração original RFFSA pré-SIGO: 1534")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904335", "Numeração original RFFSA pré-SIGO: 1535")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904336", "Numeração original RFFSA pré-SIGO: 1536")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904337", "Numeração original RFFSA pré-SIGO: 1537")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904338", "Numeração original RFFSA pré-SIGO: 1538")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904339", "Numeração original RFFSA pré-SIGO: 1539")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904340", "Numeração original RFFSA pré-SIGO: 1540")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904341", "Numeração original RFFSA pré-SIGO: 1541")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904342", "Numeração original RFFSA pré-SIGO: 1542")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904343", "Numeração original RFFSA pré-SIGO: 1543")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904344", "Numeração original RFFSA pré-SIGO: 1544")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904345", "Numeração original RFFSA pré-SIGO: 1545")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904346", "Numeração original RFFSA pré-SIGO: 1546")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904347", "Numeração original RFFSA pré-SIGO: 1547")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904348", "Numeração original RFFSA pré-SIGO: 1548")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904349", "Numeração original RFFSA pré-SIGO: 1549")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904350", "Numeração original RFFSA pré-SIGO: 1550")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904351", "Numeração original RFFSA pré-SIGO: 1551")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904352", "Numeração original RFFSA pré-SIGO: 1552")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904353", "Numeração original RFFSA pré-SIGO: 1553")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904354", "Numeração original RFFSA pré-SIGO: 1554")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904355", "Numeração original RFFSA pré-SIGO: 1555")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904356", "Numeração original RFFSA pré-SIGO: 1556")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904357", "Numeração original RFFSA pré-SIGO: 1557")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904358", "Numeração original RFFSA pré-SIGO: 1558")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904359", "Numeração original RFFSA pré-SIGO: 1559")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904360", "Numeração original RFFSA pré-SIGO: 1560")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904361", "Numeração original RFFSA pré-SIGO: 1561")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904362", "Numeração original RFFSA pré-SIGO: 1562")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904363", "Numeração original RFFSA pré-SIGO: 1563")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904364", "Numeração original RFFSA pré-SIGO: 1564")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904365", "Numeração original RFFSA pré-SIGO: 1565")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904366", "Numeração original RFFSA pré-SIGO: 1566")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904367", "Numeração original RFFSA pré-SIGO: 1567")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904368", "Numeração original RFFSA pré-SIGO: 1568")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904369", "Numeração original RFFSA pré-SIGO: 1569")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904370", "Numeração original RFFSA pré-SIGO: 1570")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904371", "Numeração original RFFSA pré-SIGO: 1571")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904372", "Numeração original RFFSA pré-SIGO: 1572")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904373", "Numeração original RFFSA pré-SIGO: 1573")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904374", "Numeração original RFFSA pré-SIGO: 1574")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904375", "Numeração original RFFSA pré-SIGO: 1575")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904376", "Numeração original RFFSA pré-SIGO: 1576")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904377", "Numeração original RFFSA pré-SIGO: 1577")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904378", "Numeração original RFFSA pré-SIGO: 1578")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904379", "Numeração original RFFSA pré-SIGO: 1579")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904380", "Numeração original RFFSA pré-SIGO: 1580")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904381", "Numeração original RFFSA pré-SIGO: 1581")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904382", "Numeração original RFFSA pré-SIGO: 1582")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904383", "Numeração original RFFSA pré-SIGO: 1583")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904384", "Numeração original RFFSA pré-SIGO: 1584")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904385", "Numeração original RFFSA pré-SIGO: 1585")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904386", "Numeração original RFFSA pré-SIGO: 1586")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904387", "Numeração original RFFSA pré-SIGO: 1587")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904388", "Numeração original RFFSA pré-SIGO: 1588")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904389", "Numeração original RFFSA pré-SIGO: 1589")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904390", "Numeração original RFFSA pré-SIGO: 1590")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904391", "Numeração original RFFSA pré-SIGO: 1591")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904392", "Numeração original RFFSA pré-SIGO: 1592")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904393", "Numeração original RFFSA pré-SIGO: 1593")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904394", "Numeração original RFFSA pré-SIGO: 1594")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904395", "Numeração original RFFSA pré-SIGO: 1595")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904396", "Numeração original RFFSA pré-SIGO: 1596")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904397", "Numeração original RFFSA pré-SIGO: 1597")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904398", "Numeração original RFFSA pré-SIGO: 1598")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904399", "Numeração original RFFSA pré-SIGO: 1599")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904400", "Numeração original RFFSA pré-SIGO: 1600")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904401", "Numeração original RFFSA pré-SIGO: 1601")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904402", "Numeração original RFFSA pré-SIGO: 1602")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904403", "Numeração original RFFSA pré-SIGO: 1603")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904404", "Numeração original RFFSA pré-SIGO: 1604")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904405", "Numeração original RFFSA pré-SIGO: 1605")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904406", "Numeração original RFFSA pré-SIGO: 1606")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904407", "Numeração original RFFSA pré-SIGO: 1607")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904408", "Numeração original RFFSA pré-SIGO: 1608")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904409", "Numeração original RFFSA pré-SIGO: 1609")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904410", "Numeração original RFFSA pré-SIGO: 1610")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904411", "Numeração original RFFSA pré-SIGO: 1611")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904412", "Numeração original RFFSA pré-SIGO: 1612")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904413", "Numeração original RFFSA pré-SIGO: 1613")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904414", "Numeração original RFFSA pré-SIGO: 1614")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904415", "Numeração original RFFSA pré-SIGO: 1615")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904416", "Numeração original RFFSA pré-SIGO: 1616")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904417", "Numeração original RFFSA pré-SIGO: 1617")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904418", "Numeração original RFFSA pré-SIGO: 1618")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904419", "Numeração original RFFSA pré-SIGO: 1619")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904420", "Numeração original RFFSA pré-SIGO: 1620")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904421", "Numeração original RFFSA pré-SIGO: 1621")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904422", "Numeração original RFFSA pré-SIGO: 1622")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904423", "Numeração original RFFSA pré-SIGO: 1623")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904424", "Numeração original RFFSA pré-SIGO: 1624")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904425", "Numeração original RFFSA pré-SIGO: 1625")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904426", "Numeração original RFFSA pré-SIGO: 1626")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904427", "Numeração original RFFSA pré-SIGO: 1627")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904428", "Numeração original RFFSA pré-SIGO: 1628")
    add_information(user, rstype.LOCOMOTIVE, "G22U 904429", "Numeração original RFFSA pré-SIGO: 1629")


