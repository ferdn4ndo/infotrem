

class GenericError(Exception):
    pass


class PreConditionFailed(GenericError):
    pass


class FileOversizeLimit(GenericError):
    pass


class InvalidFileMimeType(GenericError):
    pass


class MissingLocalTempFile(GenericError):
    pass


class S3BucketError(GenericError):
    pass


class InvalidArgumentClass(GenericError):
    pass


class UnreachableURL(GenericError):
    pass
