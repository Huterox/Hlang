from errors.hlang_error import HlangError


class InvalidSyntaxError(HlangError):
    def __init__(self, pos_start, pos_end, details=''):
        super().__init__(pos_start, pos_end, 'Invalid Syntax：错误语法', details)