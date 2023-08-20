

"""
在解析token的时候，记录当前字符的位置
"""
import string


class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char=None):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)


DIGITS = '0123456789'
CHINESE_WORD = "设且或否如果再者不然遍历到步长循环函数就结束返回继续终止"
LETTERS = string.ascii_letters + CHINESE_WORD
LETTERS_DIGITS = LETTERS + DIGITS



"""
定义的Token类型，和关键字
"""

TT_INT = "整数"
TT_FLOAT = "浮点数"
TT_STRING = '字符串'
TT_PLUS = "加号"
TT_DIV = "除号"
TT_MINUS = "减号"
TT_LPAREN = "左括号"
TT_RPAREN = "右括号"
TT_POW	= '次幂'
TT_MUL = "乘"
TT_EOF = 'EOF'
TT_IDENTIFIER = '设变量'
TT_KEYWORD = '关键字'
TT_EQ = '赋值'
TT_EE = '等于'
TT_NE = '不等于'
TT_LT = '小于'
TT_GT = '大于'
TT_LTE = '小于等于'
TT_GTE = '大于等于'
TT_LSQUARE = '[括号'
TT_RSQUARE = ']括号'
TT_COMMA = '，号'
TT_ARROW = '-> 符号'
TT_NEWLINE = '换行'
TT_ANNO = "注释#开头#结束"

class KeyWord:

    def __init__(self,ek,ck):
        self.ex = ek
        self.ck = ck

    def __contains__(self, value):
        # 如果value等于ex或ck中的任意一个，返回True；否则返回False
        return value == self.ex or value == self.ck

    def __eq__(self, other):
        # 如果ex或ck有一个相等，则两个对象相等
        return self.ex == other.ex or self.ck == other.ck

    def __ne__(self, other):
        # 如果ex和ck都不相等，则两个对象不相等
        return not (self.ex == other.ex or self.ck == other.ck)


class Punctuation:
    def __init__(self,ep,cp):
        self.ep = ep
        self.cp = cp

    def __contains__(self, value):
        return value == self.ep or value == self.cp

    def __eq__(self, other):
        return self.ep == other.ep or self.cp == other.cp

    def __ne__(self, other):
        return not (self.ep == other.ep or self.cp == other.cp)

PUNCTUATIONS = {
    ',':Punctuation(',','，'),
    '(':Punctuation('(','（'),
    ')':Punctuation(')','）'),
    '[':Punctuation('[','【'),
    ']':Punctuation(']','】'),
    ';':Punctuation(';','；'),
}


KEYWORDSEC = {

    'var':KeyWord('var','设'),
    '设':KeyWord('var','设'),
    'and':KeyWord('and','且'),
    '且':KeyWord('and','且'),
    'or':KeyWord('or','或'),
    '或':KeyWord('or','或'),
    'not':KeyWord('not','否'),
    '否':KeyWord('not','否'),
    'if':KeyWord('if','如果'),
    '如果':KeyWord('if','如果'),
    'elif':KeyWord('elif','再者'),
    '再者':KeyWord('elif','再者'),
    'else':KeyWord('else','不然'),
    '不然':KeyWord('else','不然'),
    'for':KeyWord('for','遍历'),
    '遍历':KeyWord('for','遍历'),
    'to':KeyWord('to','到'),
    '到':KeyWord('to','到'),
    'step':KeyWord('step','步长'),
    '步长':KeyWord('step','步长'),
    'while':KeyWord('while','循环'),
    '循环':KeyWord('while','循环'),
    'fun':KeyWord('fun','函数'),
    '函数':KeyWord('fun','函数'),
    'then':KeyWord('then','就'),
    '就':KeyWord('then','就'),
    'end':KeyWord('end','结束'),
    '结束':KeyWord('end','结束'),
    'return':KeyWord('return','返回'),
    '返回':KeyWord('return','返回'),
    'continue':KeyWord('continue','继续'),
    '继续':KeyWord('continue','继续'),
    'break':KeyWord('break','终止'),
    '终止':KeyWord('break','终止'),
}



KEYWORDS = [
    'var',
    '设',
    'and',
    '且',
    'or',
    '或',
    'not',
    '否',
    'if',
    '如果',
    'elif',
    '再者',
    'else',
    '不然',
    'for',
    '遍历',
    'to',
    '到',
    'step',
    '步长',
    'while',
    '循环',
    'fun',
    '函数',
    'then',
    '就',
    'end',
    '结束',
    'return',
    '返回',
    'continue',
    '继续',
    'break',
    '终止'
]



class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end.copy()

    def matches(self, type_, value):
        # return self.type == type_ and self.value == value
        return self.type == type_ and self.value in KEYWORDSEC.get(value)

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'