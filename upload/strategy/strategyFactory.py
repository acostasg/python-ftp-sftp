from injectionContainer import Container


class Strategy:
    """
    Factory with responsibility to instance strategy
    """
    CONST_SECURE = 1
    CONST_UNSECURE = 2

    __strategy_class = None

    def __init__(self, type_class):
        """

        :param type_class: int
        :return: void
        """
        from strategy \
            import secure as str_secure, unsecure as str_unsecure

        if type_class == Strategy.CONST_UNSECURE:
            self.__strategy_class = str_unsecure.Unsecure(Container.dependency('logger'))
        if type_class == Strategy.CONST_SECURE:
            self.__strategy_class = str_secure.Secure(Container.dependency('logger'))

    def upload(self, request):
        """

        :param request:
        :return: boolean
        """
        return self.__strategy_class.upload(request)
