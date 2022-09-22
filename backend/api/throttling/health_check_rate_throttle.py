from api.throttling.base_rate_throttle import BaseRateThrottle


class HealthCheckRateThrottle(BaseRateThrottle):
    scope = 'healthCheck'
