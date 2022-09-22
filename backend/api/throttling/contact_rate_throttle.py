from api.throttling.base_rate_throttle import BaseRateThrottle


class ContactRateThrottle(BaseRateThrottle):
    scope = 'contact'
