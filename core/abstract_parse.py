from abc import ABC, abstractmethod
"""
语法解析器
"""
class AbstractParser(ABC):


    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def statements(self):
      pass

    @abstractmethod
    def statement(self):
       pass

    @abstractmethod
    def expr(self):
        pass

    @abstractmethod
    def comp_expr(self):
        pass

    @abstractmethod
    def arith_expr(self):
        pass

    @abstractmethod
    def term(self):
        pass

    @abstractmethod
    def factor(self):
        pass

    @abstractmethod
    def power(self):
        pass

    @abstractmethod
    def call(self):
        pass

    @abstractmethod
    def atom(self):
        pass

    @abstractmethod
    def list_expr(self):
       pass

    @abstractmethod
    def if_expr(self):
       pass

    @abstractmethod
    def if_expr_b(self):
        pass

    @abstractmethod
    def if_expr_c(self):
       pass

    @abstractmethod
    def if_expr_b_or_c(self):
      pass

    @abstractmethod
    def if_expr_cases(self, case_keyword):
        pass

    @abstractmethod
    def for_expr(self):
       pass

    @abstractmethod
    def while_expr(self):
      pass

    @abstractmethod
    def func_def(self):
       pass

    @abstractmethod
    def bin_op(self, func_a, ops, func_b=None):
        pass

