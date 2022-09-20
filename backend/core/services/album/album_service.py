from core.models import AlbumComment, Album


class AlbumService:
    @staticmethod
    def delete_album(album: Album):
        album_comments = AlbumComment.objects.filter(album=album)
        for album_comment in album_comments:
            album_comment.comment.delete()
            album_comment.delete()

        album.delete()
