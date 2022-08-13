from django.contrib.auth.models import AnonymousUser
from rest_framework.throttling import SimpleRateThrottle


class BaseRateThrottle(SimpleRateThrottle):
    scope = 'baseThrottle'

    class Meta:
        abstract = True

    def get_cache_key(self, request, view):
        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request)
        }

    def allow_request(self, request, view):
        """
        Implement the check to see if the request should be throttled.
        On success calls `throttle_success`.
        On failure calls `throttle_failure`.
        """
        # Bypass CORS OPTIONS requests
        if request.method == "OPTIONS":
            return True

        if self.rate is None:
            return True

        self.key = self.get_cache_key(request, view)
        if self.key is None:
            return True

        self.history = self.cache.get(self.key, [])
        self.now = self.timer()

        while len(self.history) and self.history[-1] <= self.now - self.duration:
            self.history.pop()

        if len(self.history) >= self.num_requests:
            return self.throttle_failure()

        return self.throttle_success(request)

    def throttle_success(self, request):
        """
        Inserts the current request's timestamp along with the key into the cache.
        """
        # if type(request.user) is not AnonymousUser:
        #   self.history.insert(0, request.user.id)
        self.history.insert(0, self.now)
        self.cache.set(self.key, self.history, self.duration)
        return True


class UserLoginRateThrottle(BaseRateThrottle):
    scope = 'loginAttempts'


class ContactRateThrottle(BaseRateThrottle):
    scope = 'contact'


class EmailValidationRateThrottle(BaseRateThrottle):
    scope = 'emailValidation'


class HealthCheckRateThrottle(BaseRateThrottle):
    scope = 'healthCheck'
