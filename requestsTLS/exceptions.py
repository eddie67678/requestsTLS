class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidURL(Error):
    """Raised When URL Supplied Is Invalid"""
    def __init__(self) -> None:
        super().__init__("Invalid URL Passed. Must Start with http:// OR https://")

