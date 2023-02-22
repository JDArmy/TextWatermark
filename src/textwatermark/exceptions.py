'''Exception'''


class WMError(Exception):
    '''Watermark Error'''
    # pass


class WMInvalidArgumentError(WMError):
    '''Invalid Argument Error'''

    def __init__(self, namespace: str, name: str):
        super().__init__()
        self._namespace = namespace
        self._name = name

    def __repr__(self):
        return f'Can not found "{self._name}" in {self._namespace}'

    def __str__(self):
        return self.__repr__()
