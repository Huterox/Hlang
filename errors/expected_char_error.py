from errors.hlang_error import HlangError


class ExpectedCharError(HlangError):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Expected Character 这里期望字符', details)