from typing import Dict

from core.models import CompanyPaintSchemeInformation
from core.services.information.information_service import InformationService


class CompanyPaintSchemeInformationService:
    @staticmethod
    def create_company_paint_scheme_information_from_data(validated_data: Dict) -> CompanyPaintSchemeInformation:
        information_data = validated_data['information']
        information_data['created_by'] = validated_data['information']
        information = InformationService.create_information_from_data(
            information_data=information_data,
            created_by=validated_data['created_by']
        )

        company_paint_scheme_information = CompanyPaintSchemeInformation()
        company_paint_scheme_information.paint_scheme = validated_data['paint_scheme_id']
        company_paint_scheme_information.information = information
        company_paint_scheme_information.created_by = validated_data['created_by']
        company_paint_scheme_information.save()

        return company_paint_scheme_information


    @staticmethod
    def update_company_paint_scheme_information_from_data(
            validated_data: Dict,
            company_paint_scheme_information: CompanyPaintSchemeInformation
    ) -> CompanyPaintSchemeInformation:
        information = InformationService.update_information_from_data(
            information_data=validated_data['information'],
            information=company_paint_scheme_information.information,
            updated_by=validated_data['updated_by']
        )

        company_paint_scheme_information.updated_by = validated_data['updated_by']
        company_paint_scheme_information.information = information
        company_paint_scheme_information.save()

        return company_paint_scheme_information
