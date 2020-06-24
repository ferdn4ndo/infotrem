import os

from infotrem.models.location import TrackGauge
from infotrem.models.railroad import Manufacturer


def create_locomotive(model_name: str, sigo_number: int, **metadata):
    from django.contrib.auth.models import User

    from infotrem.models.rolling_stock import RollingStock
    from infotrem.models.rolling_stock_locomotive import RollingStockLocomotive, RollingStockLocomotiveModel

    rolling_stock_item, created = RollingStock.objects.get_or_create(
        type=RollingStock.RollingStockType.LOCOMOTIVE,
        gauge=metadata['gauge'] if 'gauge' in metadata else None,
        is_sigo=True,
        sigo_number=sigo_number,
        manufacturer=metadata['manufacturer'] if 'manufacturer' in metadata else None,
    )
    print("RollingStockItem SIGO # {} {}!".format(sigo_number, 'created' if created else 'updated'))

    model = RollingStockLocomotiveModel.objects.get(name=model_name)

    if 'gauge' in metadata:
        del metadata['gauge']

    if 'manufacturer' in metadata:
        del metadata['manufacturer']

    rolling_stock_locomotive, created = RollingStockLocomotive.objects.get_or_create(
        rolling_stock=rolling_stock_item,
        model=model,
    )
    print("RollingStockLocomotive SIGO #{} {}!".format(sigo_number, 'created' if created else 'updated'))

    metadata['created_by'] = User.objects.get(username=os.environ['SYSTEM_USER_NAME'])

    for attr, value in metadata.items():
        setattr(rolling_stock_locomotive, attr, value)

    rolling_stock_locomotive.save()


metric = TrackGauge.objects.get(tag='NARROW')
gm = Manufacturer.objects.get(short_name='EMD')

create_locomotive("G22U", 904301, gauge=metric, manufacturer=gm, serial_number='1292', build_year=1972)
create_locomotive("G22U", 904302, gauge=metric, manufacturer=gm, serial_number='1293', build_year=1972)
create_locomotive("G22U", 904303, gauge=metric, manufacturer=gm, serial_number='1294', build_year=1972)
create_locomotive("G22U", 904304, gauge=metric, manufacturer=gm, serial_number='1295', build_year=1972)
create_locomotive("G22U", 904305, gauge=metric, manufacturer=gm, serial_number='1296', build_year=1972)
create_locomotive("G22U", 904306, gauge=metric, manufacturer=gm, serial_number='1297', build_year=1972)
create_locomotive("G22U", 904307, gauge=metric, manufacturer=gm, serial_number='1298', build_year=1972)
create_locomotive("G22U", 904308, gauge=metric, manufacturer=gm, serial_number='1299', build_year=1972)
create_locomotive("G22U", 904309, gauge=metric, manufacturer=gm, serial_number='1300', build_year=1972)
create_locomotive("G22U", 904310, gauge=metric, manufacturer=gm, serial_number='1301', build_year=1972)
create_locomotive("G22U", 904311, gauge=metric, manufacturer=gm, serial_number='1302', build_year=1972)
create_locomotive("G22U", 904312, gauge=metric, manufacturer=gm, serial_number='1303', build_year=1972)
create_locomotive("G22U", 904313, gauge=metric, manufacturer=gm, serial_number='1304', build_year=1972)
create_locomotive("G22U", 904314, gauge=metric, manufacturer=gm, serial_number='1305', build_year=1972)
create_locomotive("G22U", 904315, gauge=metric, manufacturer=gm, serial_number='1306', build_year=1972)
create_locomotive("G22U", 904316, gauge=metric, manufacturer=gm, serial_number='1307', build_year=1972)
create_locomotive("G22U", 904317, gauge=metric, manufacturer=gm, serial_number='1308', build_year=1972)
create_locomotive("G22U", 904318, gauge=metric, manufacturer=gm, serial_number='1309', build_year=1972)
create_locomotive("G22U", 904319, gauge=metric, manufacturer=gm, serial_number='1310', build_year=1972)
create_locomotive("G22U", 904320, gauge=metric, manufacturer=gm, serial_number='1311', build_year=1972)
create_locomotive("G22U", 904321, gauge=metric, manufacturer=gm, serial_number='1312', build_year=1972)
create_locomotive("G22U", 904322, gauge=metric, manufacturer=gm, serial_number='1313', build_year=1972)
create_locomotive("G22U", 904323, gauge=metric, manufacturer=gm, serial_number='1314', build_year=1972)
create_locomotive("G22U", 904324, gauge=metric, manufacturer=gm, serial_number='1315', build_year=1972)
create_locomotive("G22U", 904325, gauge=metric, manufacturer=gm, serial_number='1316', build_year=1972)
create_locomotive("G22U", 904326, gauge=metric, manufacturer=gm, serial_number='1317', build_year=1972)
create_locomotive("G22U", 904327, gauge=metric, manufacturer=gm, serial_number='1318', build_year=1972)
create_locomotive("G22U", 904328, gauge=metric, manufacturer=gm, serial_number='1319', build_year=1972)
create_locomotive("G22U", 904329, gauge=metric, manufacturer=gm, serial_number='1320', build_year=1972)
create_locomotive("G22U", 904330, gauge=metric, manufacturer=gm, serial_number='1321', build_year=1972)
create_locomotive("G22U", 904331, gauge=metric, manufacturer=gm, serial_number='1322', build_year=1972)
create_locomotive("G22U", 904332, gauge=metric, manufacturer=gm, serial_number='1323', build_year=1972)
create_locomotive("G22U", 904333, gauge=metric, manufacturer=gm, serial_number='1324', build_year=1972)
create_locomotive("G22U", 904334, gauge=metric, manufacturer=gm, serial_number='1325', build_year=1972)
create_locomotive("G22U", 904335, gauge=metric, manufacturer=gm, serial_number='1326', build_year=1972)
create_locomotive("G22U", 904336, gauge=metric, manufacturer=gm, serial_number='1327', build_year=1972)
create_locomotive("G22U", 904337, gauge=metric, manufacturer=gm, serial_number='1328', build_year=1972)
create_locomotive("G22U", 904338, gauge=metric, manufacturer=gm, serial_number='1329', build_year=1972)
create_locomotive("G22U", 904339, gauge=metric, manufacturer=gm, serial_number='1330', build_year=1972)
create_locomotive("G22U", 904340, gauge=metric, manufacturer=gm, serial_number='1331', build_year=1972)
create_locomotive("G22U", 904341, gauge=metric, manufacturer=gm, serial_number='1332', build_year=1972)
create_locomotive("G22U", 904342, gauge=metric, manufacturer=gm, serial_number='1333', build_year=1972)
create_locomotive("G22U", 904343, gauge=metric, manufacturer=gm, serial_number='1334', build_year=1972)
create_locomotive("G22U", 904344, gauge=metric, manufacturer=gm, serial_number='1335', build_year=1972)
create_locomotive("G22U", 904345, gauge=metric, manufacturer=gm, serial_number='1336', build_year=1972)
create_locomotive("G22U", 904346, gauge=metric, manufacturer=gm, serial_number='1337', build_year=1972)
create_locomotive("G22U", 904347, gauge=metric, manufacturer=gm, serial_number='1338', build_year=1972)
create_locomotive("G22U", 904348, gauge=metric, manufacturer=gm, serial_number='1339', build_year=1972)
create_locomotive("G22U", 904349, gauge=metric, manufacturer=gm, serial_number='1340', build_year=1972)
create_locomotive("G22U", 904350, gauge=metric, manufacturer=gm, serial_number='1341', build_year=1972)
create_locomotive("G22U", 904351, gauge=metric, manufacturer=gm, serial_number='1342', build_year=1972)
create_locomotive("G22U", 904352, gauge=metric, manufacturer=gm, serial_number='1343', build_year=1972)
create_locomotive("G22U", 904353, gauge=metric, manufacturer=gm, serial_number='1344', build_year=1972)
create_locomotive("G22U", 904354, gauge=metric, manufacturer=gm, serial_number='1345', build_year=1972)
create_locomotive("G22U", 904355, gauge=metric, manufacturer=gm, serial_number='1346', build_year=1972)
create_locomotive("G22U", 904356, gauge=metric, manufacturer=gm, serial_number='1347', build_year=1972)
create_locomotive("G22U", 904357, gauge=metric, manufacturer=gm, serial_number='1348', build_year=1972)
create_locomotive("G22U", 904358, gauge=metric, manufacturer=gm, serial_number='1349', build_year=1972)
create_locomotive("G22U", 904359, gauge=metric, manufacturer=gm, serial_number='1350', build_year=1972)
create_locomotive("G22U", 904360, gauge=metric, manufacturer=gm, serial_number='1351', build_year=1972)
create_locomotive("G22U", 904361, gauge=metric, manufacturer=gm, serial_number='1352', build_year=1972)
create_locomotive("G22U", 904362, gauge=metric, manufacturer=gm, serial_number='1353', build_year=1972)
create_locomotive("G22U", 904363, gauge=metric, manufacturer=gm, serial_number='1354', build_year=1972)
create_locomotive("G22U", 904364, gauge=metric, manufacturer=gm, serial_number='1355', build_year=1972)
create_locomotive("G22U", 904365, gauge=metric, manufacturer=gm, serial_number='1356', build_year=1972)
create_locomotive("G22U", 904366, gauge=metric, manufacturer=gm, serial_number='1357', build_year=1972)
create_locomotive("G22U", 904367, gauge=metric, manufacturer=gm, serial_number='1358', build_year=1972)
create_locomotive("G22U", 904368, gauge=metric, manufacturer=gm, serial_number='1359', build_year=1972)
create_locomotive("G22U", 904369, gauge=metric, manufacturer=gm, serial_number='1360', build_year=1972)
create_locomotive("G22U", 904370, gauge=metric, manufacturer=gm, serial_number='1361', build_year=1972)
create_locomotive("G22U", 904371, gauge=metric, manufacturer=gm, serial_number='1362', build_year=1972)
create_locomotive("G22U", 904372, gauge=metric, manufacturer=gm, serial_number='1363', build_year=1972)
create_locomotive("G22U", 904373, gauge=metric, manufacturer=gm, serial_number='1364', build_year=1972)
create_locomotive("G22U", 904374, gauge=metric, manufacturer=gm, serial_number='1365', build_year=1972)
create_locomotive("G22U", 904375, gauge=metric, manufacturer=gm, serial_number='1366', build_year=1972)
create_locomotive("G22U", 904376, gauge=metric, manufacturer=gm, serial_number='1390', build_year=1973)
create_locomotive("G22U", 904377, gauge=metric, manufacturer=gm, serial_number='1391', build_year=1973)
create_locomotive("G22U", 904378, gauge=metric, manufacturer=gm, serial_number='1392', build_year=1973)
create_locomotive("G22U", 904379, gauge=metric, manufacturer=gm, serial_number='1393', build_year=1973)
create_locomotive("G22U", 904380, gauge=metric, manufacturer=gm, serial_number='1394', build_year=1973)
create_locomotive("G22U", 904381, gauge=metric, manufacturer=gm, serial_number='1395', build_year=1973)
create_locomotive("G22U", 904382, gauge=metric, manufacturer=gm, serial_number='1396', build_year=1973)
create_locomotive("G22U", 904383, gauge=metric, manufacturer=gm, serial_number='1397', build_year=1973)
create_locomotive("G22U", 904384, gauge=metric, manufacturer=gm, serial_number='1398', build_year=1973)
create_locomotive("G22U", 904385, gauge=metric, manufacturer=gm, serial_number='1399', build_year=1973)
create_locomotive("G22U", 904386, gauge=metric, manufacturer=gm, serial_number='1400', build_year=1973)
create_locomotive("G22U", 904387, gauge=metric, manufacturer=gm, serial_number='1401', build_year=1973)
create_locomotive("G22U", 904388, gauge=metric, manufacturer=gm, serial_number='1402', build_year=1973)
create_locomotive("G22U", 904389, gauge=metric, manufacturer=gm, serial_number='1403', build_year=1973)
create_locomotive("G22U", 904390, gauge=metric, manufacturer=gm, serial_number='1404', build_year=1973)
create_locomotive("G22U", 904391, gauge=metric, manufacturer=gm, serial_number='1405', build_year=1973)
create_locomotive("G22U", 904392, gauge=metric, manufacturer=gm, serial_number='1406', build_year=1973)
create_locomotive("G22U", 904393, gauge=metric, manufacturer=gm, serial_number='1407', build_year=1973)
create_locomotive("G22U", 904394, gauge=metric, manufacturer=gm, serial_number='1408', build_year=1973)
create_locomotive("G22U", 904395, gauge=metric, manufacturer=gm, serial_number='1409', build_year=1973)
create_locomotive("G22U", 904396, gauge=metric, manufacturer=gm, serial_number='1410', build_year=1973)
create_locomotive("G22U", 904397, gauge=metric, manufacturer=gm, serial_number='1411', build_year=1973)
create_locomotive("G22U", 904398, gauge=metric, manufacturer=gm, serial_number='1412', build_year=1973)
create_locomotive("G22U", 904399, gauge=metric, manufacturer=gm, serial_number='1413', build_year=1973)
create_locomotive("G22U", 904400, gauge=metric, manufacturer=gm, serial_number='1414', build_year=1973)
create_locomotive("G22U", 904401, gauge=metric, manufacturer=gm, serial_number='1415', build_year=1973)
create_locomotive("G22U", 904402, gauge=metric, manufacturer=gm, serial_number='1416', build_year=1973)
create_locomotive("G22U", 904403, gauge=metric, manufacturer=gm, serial_number='1417', build_year=1973)
create_locomotive("G22U", 904404, gauge=metric, manufacturer=gm, serial_number='1418', build_year=1973)
create_locomotive("G22U", 904405, gauge=metric, manufacturer=gm, serial_number='1419', build_year=1973)
create_locomotive("G22U", 904406, gauge=metric, manufacturer=gm, serial_number='1420', build_year=1973)
create_locomotive("G22U", 904407, gauge=metric, manufacturer=gm, serial_number='1421', build_year=1973)
create_locomotive("G22U", 904408, gauge=metric, manufacturer=gm, serial_number='1422', build_year=1973)
create_locomotive("G22U", 904409, gauge=metric, manufacturer=gm, serial_number='1423', build_year=1973)
create_locomotive("G22U", 904410, gauge=metric, manufacturer=gm, serial_number='1424', build_year=1973)
create_locomotive("G22U", 904411, gauge=metric, manufacturer=gm, serial_number='1425', build_year=1973)
create_locomotive("G22U", 904412, gauge=metric, manufacturer=gm, serial_number='1426', build_year=1973)
create_locomotive("G22U", 904413, gauge=metric, manufacturer=gm, serial_number='1427', build_year=1973)
create_locomotive("G22U", 904414, gauge=metric, manufacturer=gm, serial_number='1428', build_year=1973)
create_locomotive("G22U", 904415, gauge=metric, manufacturer=gm, serial_number='1429', build_year=1973)
create_locomotive("G22U", 904416, gauge=metric, manufacturer=gm, serial_number='1430', build_year=1973)
create_locomotive("G22U", 904417, gauge=metric, manufacturer=gm, serial_number='1431', build_year=1973)
create_locomotive("G22U", 904418, gauge=metric, manufacturer=gm, serial_number='1432', build_year=1973)
create_locomotive("G22U", 904419, gauge=metric, manufacturer=gm, serial_number='1433', build_year=1973)
create_locomotive("G22U", 904420, gauge=metric, manufacturer=gm, serial_number='1434', build_year=1973)
create_locomotive("G22U", 904421, gauge=metric, manufacturer=gm, serial_number='1435', build_year=1973)
create_locomotive("G22U", 904422, gauge=metric, manufacturer=gm, serial_number='1436', build_year=1973)
create_locomotive("G22U", 904423, gauge=metric, manufacturer=gm, serial_number='1437', build_year=1973)
create_locomotive("G22U", 904424, gauge=metric, manufacturer=gm, serial_number='1438', build_year=1973)
create_locomotive("G22U", 904425, gauge=metric, manufacturer=gm, serial_number='1439', build_year=1973)
create_locomotive("G22U", 904426, gauge=metric, manufacturer=gm, serial_number='1440', build_year=1973)
create_locomotive("G22U", 904427, gauge=metric, manufacturer=gm, serial_number='1441', build_year=1973)
create_locomotive("G22U", 904428, gauge=metric, manufacturer=gm, serial_number='1442', build_year=1973)
create_locomotive("G22U", 904429, gauge=metric, manufacturer=gm, serial_number='1443', build_year=1973)
