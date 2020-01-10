from django.db import models


# be aware that this is not a db model
class Result:
    def __init__(self, result):
        self.result = result
