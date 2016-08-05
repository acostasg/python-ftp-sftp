class Strategy:
    CONST_SECURE = 1
    CONST_UNSECURE = 2

    def __init__(self, type, logging):
        """

        :param type: int
        :param logging: logging
        :return: void
        """
        from strategy \
            import secure as str_secure, unsecure as str_unsecure

        if type == Strategy.CONST_UNSECURE:
            self.__strategyClass = str_unsecure.Unsecure(logging)
        if type == Strategy.CONST_SECURE:
            self.__strategyClass = str_secure.Secure(logging)

    def upload(self, request):
        """

        :param request:
        :return: boolean
        """
        return self.__strategyClass.upload(request)
