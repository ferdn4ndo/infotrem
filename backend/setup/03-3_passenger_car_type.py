from infotrem.models.rolling_stock_passenger_car import RollingStockPassengerCarType, RollingStockPassengerCarMaterial


# RollingStockPassengerCarType
RollingStockPassengerCarType.objects.get_or_create(letter='A', name="Administração")
RollingStockPassengerCarType.objects.get_or_create(letter='B', name="Bagagem e/ou Correio")
RollingStockPassengerCarType.objects.get_or_create(letter='D', name="Dormitório com cabines")
RollingStockPassengerCarType.objects.get_or_create(letter='E', name="Pulmann(com poltronas especiais)")
RollingStockPassengerCarType.objects.get_or_create(letter='F', name="Buffet (com poltronas e bar)")
RollingStockPassengerCarType.objects.get_or_create(letter='L', name="Poltronas - leito")
RollingStockPassengerCarType.objects.get_or_create(letter='P', name="Poltronas de primeira classe")
RollingStockPassengerCarType.objects.get_or_create(letter='Q', name="Qualquer / outros")
RollingStockPassengerCarType.objects.get_or_create(letter='R', name="Restaurante")
RollingStockPassengerCarType.objects.get_or_create(letter='S', name="Segunda classe")
RollingStockPassengerCarType.objects.get_or_create(letter='T', name="Classe turística")
RollingStockPassengerCarType.objects.get_or_create(letter='U', name="Suburbano")

# RollingStockPassengerCarMaterial
RollingStockPassengerCarMaterial.objects.get_or_create(letter='A', name="Alumínio")
RollingStockPassengerCarMaterial.objects.get_or_create(letter='C', name="Aço carbono")
RollingStockPassengerCarMaterial.objects.get_or_create(letter='D', name="Aço carbono e Madeira")
RollingStockPassengerCarMaterial.objects.get_or_create(letter='E', name="Aço carbono e Inoxidável")
RollingStockPassengerCarMaterial.objects.get_or_create(letter='I', name="Aço Inoxidável")
RollingStockPassengerCarMaterial.objects.get_or_create(letter='L', name="Aço carbono e Alumínio")
RollingStockPassengerCarMaterial.objects.get_or_create(letter='M', name="Madeira")
RollingStockPassengerCarMaterial.objects.get_or_create(letter='Q', name="Qualquer / outros")