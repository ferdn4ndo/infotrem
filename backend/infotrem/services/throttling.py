from rest_framework.throttling import UserRateThrottle


class MediaDefaultUserThrottle(UserRateThrottle):
    rate = '10/day'


class MediaModeratorUserThrottle(UserRateThrottle):
    rate = '100/day'

