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
            import Secure as StrSecure, Unsecure as StrUnsecure

        if type == Strategy.CONST_UNSECURE:
            self.__strategyClass = StrUnsecure.Unsecure(logging)
        if type == Strategy.CONST_SECURE:
            self.__strategyClass = StrSecure.Secure(logging)

    def upload(self, request):
        """

        :param request:
        :return: void
        """
        self.__strategyClass.upload(request)
