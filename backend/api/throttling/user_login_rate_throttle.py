from api.throttling.base_rate_throttle import BaseRateThrottle


class UserLoginRateThrottle(BaseRateThrottle):
    scope = 'loginAttempts'
