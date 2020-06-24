"""
Creates information about SIGO regions.
Must run only after railroad_company is populated.
"""


# RollingStockSigoRegional
def add_rolling_stock_sigo_regional_list(list_of_items):
    from infotrem.models.railroad import RailroadCompany
    from infotrem.models.rolling_stock import RollingStockSigoRegional

    for item in list_of_items:
        company = RailroadCompany.objects.get(abbrev=item[1])
        RollingStockSigoRegional.objects.get_or_create(
            letter=item[0],
            original_company=company,
            abbrev=item[2],
            name=item[3],
        )


add_rolling_stock_sigo_regional_list([
    ('A', 'RFFSA', 'SR-12', "Superintendência Regional São Luiz"),
    ('B', 'RFFSA', 'SR-11', "Superintendência Regional Fortaleza"),
    ('C', 'RFFSA', 'SR-1', "Superintendência Regional Recife"),
    ('D', 'RFFSA', 'SR-7', "Superintendência Regional Salvador"),
    ('E', 'RFFSA', 'SR-2', "Superintendência Regional Belo Horizonte"),
    ('F', 'RFFSA', 'SR-3', "Superintendência Regional Juiz de Fora"),
    ('G', 'RFFSA', 'SR-8', "Superintendência Regional Campos"),
    ('H', 'CBTU', 'STU-RJ', "Superintendência de Trens Urbanos RJ"),
    ('I', 'RFFSA', 'SR-4', "Superintendência Regional São Paulo"),
    ('J', 'RFFSA', 'SR-10', "Superintendência Regional Bauru"),
    ('K', 'CBTU', 'Metrorec', "Metropolitano do Recife"),
    ('L', 'RFFSA', 'SR-5', "Superintendência Regional Curitiba"),
    ('M', 'RFFSA', 'SR-9', "Superintendência Regional Tubarão"),
    ('N', 'RFFSA', 'SR-6', "Superintendência Regional Porto Alegre"),
    ('O', 'CBTU', 'STU-SP', "Superintendência de Trens Urbanos SP"),
    ('P', 'RFFSA', 'Preserfe', "Superintendência de Patrimônio - Preservação"),
    ('Q', 'CBTU', 'Demetrô', "Belo Horizonte"),
    ('R', 'FA', None, "Ferrocarriles Argentinos (Argentina)"),
    ('S', 'CBTU', 'Trensurb', "Porto Alegre"),
    ('U', 'AFE', None, "Administracion de los Ferrocarriles del Estado (Uruguai)"),
    ('V', 'CVRD', 'EFVM', "EF Vitória a Minas"),
    ('W', 'CBTU', None, "Superintendência de Trens Urbanos Fortaleza"),
    ('X', 'ENFE', None, "Empresa Nacional de Ferrocarriles (Bolívia)"),
    ('Y', 'CBTU', None, "Superintendência de Trens Urbanos Recife"),
    ('Z', 'FEPASA', None, "Material oriundo da Ferrovia Paulista S/A"),
])
