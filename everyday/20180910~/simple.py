class Filter_Text:

    def filter_one(fun):
        def wrapper(self, text=''):
            result_text = fun(self, text)
            return result_text

        return wrapper

    def filter_two(fun):
        def wrapper(self, text=''):
            result_text = fun(self, text)
            return result_text
        return wrapper

    @filter_one
    @filter_two
    def filtet_text(self, text=''):
        return text
