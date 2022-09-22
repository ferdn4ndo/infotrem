from api.throttling.base_rate_throttle import BaseRateThrottle


class EmailValidationRateThrottle(BaseRateThrottle):
    scope = 'emailValidation'
