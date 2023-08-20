from abc import ABC, abstractmethod


class AbstractLexer(ABC):

    @abstractmethod
    def make_tokens(self):
        pass

    @abstractmethod
    def make_number(self):
        pass

    @abstractmethod
    def make_minus_or_arrow(self):
        pass

    @abstractmethod
    def make_less_than(self):
        pass

    @abstractmethod
    def make_greater_than(self):
        pass
