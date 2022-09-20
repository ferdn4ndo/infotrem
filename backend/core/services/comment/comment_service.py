from typing import Dict

from core.models import Comment


class CommentService:
    @staticmethod
    def create_comment_from_data(input_data: Dict) -> Comment:
        comment = Comment()

        comment.created_by = input_data['created_by']
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
