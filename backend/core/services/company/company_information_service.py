from typing import Dict

from core.models import CompanyInformation
from core.services.information.information_service import InformationService


class CompanyInformationService:
    @staticmethod
    def create_company_information_from_data(validated_data: Dict) -> CompanyInformation:
        information_data = validated_data['information']
        information_data['created_by'] = validated_data['information']
        information = InformationService.create_information_from_data(
            information_data=information_data,
            created_by=validated_data['created_by']
        )

        company_information = CompanyInformation()
        company_information.company = validated_data['company_id']
        company_information.information = information
        company_information.created_by = validated_data['created_by']
        company_information.save()

        return company_information


    @staticmethod
    def update_company_information_from_data(
            validated_data: Dict,
            company_information: CompanyInformation
    ) -> CompanyInformation:
        information = InformationService.update_information_from_data(
            information_data=validated_data['information'],
            information=company_information.information,
            updated_by=validated_data['updated_by']
        )

        company_information.updated_by = validated_data['updated_by']
        company_information.information = information
        company_information.save()

        return company_information
