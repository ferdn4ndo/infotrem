from typing import Dict

from core.models import Comment, Company


class CompanyService:
    @staticmethod
    def create_company_from_data(validated_data: Dict) -> Comment:
        company = Company()

        company.abbrev = validated_data['abbrev']
        company.name = validated_data['name']
        company.created_by = validated_data['created_by']

        if 'company_information' in validated_data:
            for information_data in validated_data['company_information']:
                information = InformationService


        comment.text = input_data['text']

        if 'replies_to' in input_data:
            comment.replies_to = input_data['replies_to']

        comment.save()

        return comment

    @staticmethod
    def update_comment_from_data(input_data: Dict, comment: Comment) -> Comment:
        comment.updated_by = input_data['updated_by']
        comment.text = input_data['text']

        if 'replies_to' in input_data:
            comment.replies_to = input_data['replies_to']

        comment.save()

        return comment
