from errors.hlang_error import HlangError

class IllegalCharError(HlangError):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character：非法字符', details)
