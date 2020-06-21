from infotrem.models.rolling_stock_non_revenue_car import RollingStockNonRevenueCarType


def add_equipment_car_types(list_of_items):
    for item in list_of_items:
        RollingStockNonRevenueCarType.objects.get_or_create(
            letters=item[0],
            description=item[1],
            category=item[2],
        )


def run():
    # RollingStockNonRevenueCarType
    non_revenue_categories = RollingStockNonRevenueCarType.RollingStockNonRevenueCarCategory
    add_equipment_car_types([
        ('AAP', "Alinhadora Automática Plasser", non_revenue_categories.TRACK),
        ('ALI', "Auto de inspeção", non_revenue_categories.OTHER),
        ('ALS', "Auto de serviço até 10 pass. + 2 reboques", non_revenue_categories.OTHER),
        ('ALU', "Auto de Serviço utilitário", non_revenue_categories.OTHER),
        ('ATL', "Auto de Linha", non_revenue_categories.OTHER),
        ('CLS', "Caminhão de Linha", non_revenue_categories.TRACK),
        ('CPP', "Compactadora de Lastro Plasser", non_revenue_categories.TRACK),
        ('DLP', "Desguarnecedora de Lastro Plasser", non_revenue_categories.TRACK),
        ('GBK', "Guindaste Burro Krane", non_revenue_categories.OTHER),
        ('GOR', "Guindaste Orton", non_revenue_categories.RESCUE),
        ('GVP', "Guindaste de Via Permanente", non_revenue_categories.OTHER),
        ('MNP', "Socadora Mínima 2 Plasser", non_revenue_categories.TRACK),
        ('RLK', "Reguladora de Lastro Kershaw", non_revenue_categories.TRACK),
        ('RLP', "Reguladora de Lastro Plasser", non_revenue_categories.TRACK),
        ('RTM', "Reperfiladora de Trilho Plasser", non_revenue_categories.TRACK),
        ('SAP', "Socadora Niveladora Alinhadora Plasser", non_revenue_categories.TRACK),
        ('SAT', "Socadora Niveladora Alinhadora Tamper", non_revenue_categories.TRACK),
        ('SCP', "Socadora Niveladora de AMV Plasser", non_revenue_categories.TRACK),
        ('SNP', "Socadora Niveladora Plasser", non_revenue_categories.TRACK),
        ('SOP', "Soldadora de Trilho Plasser", non_revenue_categories.TRACK),
        ('STK', "Guindaste Takraf", non_revenue_categories.RESCUE),
        ('TBL', "Trem de Barra Longa", non_revenue_categories.TRACK),
        ('TMS', "Trole Motor", non_revenue_categories.OTHER),

    ])
