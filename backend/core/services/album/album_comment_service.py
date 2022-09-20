from typing import Dict

from core.models import AlbumComment
from core.services.comment.comment_service import CommentService


class AlbumCommentService:
    @staticmethod
    def create_album_comment_from_data(input_data: Dict) -> AlbumComment:
        comment_data = input_data.pop('comment')
        comment_data['created_by'] = input_data['created_by']
        comment = CommentService.create_comment_from_data(input_data=comment_data)

        album_comment = AlbumComment()
        album_comment.album = input_data['album_id']
        album_comment.comment = comment
        album_comment.created_by = input_data['created_by']
        album_comment.save()

        return album_comment

    @staticmethod
    def update_album_comment_from_data(input_data: Dict, album_comment: AlbumComment) -> AlbumComment:
        comment_data = input_data.pop('comment')
        comment_data['updated_by'] = input_data['updated_by']
        comment = CommentService.update_comment_from_data(input_data=comment_data, comment=album_comment.comment)

        album_comment.album = input_data['album_id']
        album_comment.comment = comment
        album_comment.updated_by = input_data['updated_by']
        album_comment.save()

        return album_comment
