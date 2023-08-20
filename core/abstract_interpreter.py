from abc import ABC, abstractmethod

class AbstractInterpreter(ABC):

    @abstractmethod
    def visit(self, node, context):
       pass

    @abstractmethod
    def no_visit_method(self, node, context):
        pass

    @abstractmethod
    def visit_NumberNode(self, node, context):
        pass

    @abstractmethod
    def visit_StringNode(self, node, context):
        pass

    @abstractmethod
    def visit_ListNode(self, node, context):
        pass

    @abstractmethod
    def visit_VarAccessNode(self, node, context):
        pass

    @abstractmethod
    def visit_VarAssignNode(self, node, context):
        pass

    @abstractmethod
    def visit_BinOpNode(self, node, context):
      pass

    @abstractmethod
    def visit_UnaryOpNode(self, node, context):
        pass

    @abstractmethod
    def visit_IfNode(self, node, context):
        pass

    @abstractmethod
    def visit_ForNode(self, node, context):
        pass

    @abstractmethod
    def visit_WhileNode(self, node, context):
        pass

    @abstractmethod
    def visit_FuncDefNode(self, node, context):
       pass

    @abstractmethod
    def visit_CallNode(self, node, context):
       pass

    @abstractmethod
    def visit_ReturnNode(self, node, context):
       pass

    @abstractmethod
    def visit_ContinueNode(self, node, context):
        pass

    @abstractmethod
    def visit_BreakNode(self, node, context):
        pass

