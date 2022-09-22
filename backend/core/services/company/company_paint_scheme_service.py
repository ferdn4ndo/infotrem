from typing import Dict

from core.models import CompanyPaintScheme


class CompanyPaintSchemeService:
    @staticmethod
    def create_company_paint_scheme_from_data(validated_data: Dict) -> CompanyPaintScheme:
        company_paint_scheme = CompanyPaintScheme()
        company_paint_scheme.company = validated_data['company_id']
        company_paint_scheme.name = validated_data['name']
        company_paint_scheme.start_date = validated_data['start_date']
        company_paint_scheme.end_date = validated_data['end_date']
        company_paint_scheme.created_by = validated_data['created_by']
        company_paint_scheme.save()

        return company_paint_scheme


    @staticmethod
    def update_company_paint_scheme_from_data(
            validated_data: Dict,
            company_paint_scheme: CompanyPaintScheme
    ) -> CompanyPaintScheme:
        company_paint_scheme.company = validated_data['company_id']
        company_paint_scheme.name = validated_data['name']
        company_paint_scheme.start_date = validated_data['start_date']
        company_paint_scheme.end_date = validated_data['end_date']
        company_paint_scheme.updated_by = validated_data['updated_by']
        company_paint_scheme.save()

        return company_paint_scheme
