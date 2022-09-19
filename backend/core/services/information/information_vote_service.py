from core.models import InformationVote, Information, User


class InformationVoteService:
    information: Information

    def __init__(self, information: Information):
        self.information = information

    def has_user_voted(self, user: User) -> bool:
        return InformationVote.objects.filter(information=self.information, created_by=user).exists()
