

"""
定义语法解释器的节点
NumberNode：表示数字节点，用于存储数字的令牌（token）信息。

BinOpNode：表示二元操作符节点。其中：
            left_node（左节点），
            op_tok（操作符令牌），
            right_node（右节点）

UnaryOpNode：表示一元操作符节点。
            op_tok（操作符令牌）
            node（子节点）

这段代码定义了两个类，分别为 `VarAccessNode` 和 `VarAssignNode`。

VarAccessNode 类表示一个设的访问节点。它具有以下属性和方法：
    - var_name_tok：表示设名的令牌（token）对象。
    - pos_start：表示节点在源代码中的起始位置，通过 `var_name_tok.pos_start` 获取。
    - pos_end：表示节点在源代码中的结束位置，通过 `var_name_tok.pos_end` 获取。

VarAssignNode 类表示一个设的赋值节点。它具有以下属性和方法：
    - var_name_tok：表示设名的令牌（token）对象。
    - value_node：表示赋给设的值的节点对象。
    - pos_start：表示节点在源代码中的起始位置，通过 `var_name_tok.pos_start` 获取。
    - pos_end：表示节点在源代码中的结束位置，通过 `value_node.pos_end` 获取。

IfNode 类表示 if 语句的节点。它具有以下属性和方法：

    cases：表示 if 语句的条件和对应的代码块的列表。
    else_case：表示 if 语句的 else 分支的代码块（可选）。
    pos_start：表示节点在源代码中的起始位置，为第一个条件的起始位置。
    pos_end：表示节点在源代码中的结束位置，为 else 分支的结束位置（如果存在），否则为最后一个条件的结束位置。

ForNode 类表示 for 循环的节点。它具有以下属性和方法：

    var_name_tok：表示循环变量的令牌（token）对象。
    start_value_node：表示循环变量的起始值的节点对象。
    end_value_node：表示循环变量的结束值的节点对象。
    step_value_node：表示循环变量的步长值的节点对象。
    body_node：表示循环体的节点对象。
    pos_start：表示节点在源代码中的起始位置，为变量名的起始位置。
    pos_end：表示节点在源代码中的结束位置，为循环体的结束位置。

WhileNode 类表示 while 循环的节点。它具有以下属性和方法：

    condition_node：表示循环条件的节点对象。
    body_node：表示循环体的节点对象。
    pos_start：表示节点在源代码中的起始位置，为条件的起始位置。
    pos_end：表示节点在源代码中的结束位置，为循环体的结束位置。


FuncDefNode 类表示函数定义的节点。它具有以下属性：

    var_name_tok：函数名称的记号（Token）。
    arg_name_toks：参数名称的记号列表。
    body_node：函数体的节点。
    pos_start：节点在源代码中的起始位置。如果存在函数名记号，
    则起始位置为该记号的起始位置；如果不存在函数名记号但存在参数名记号，
    则起始位置为第一个参数名记号的起始位置；否则起始位置为函数体节点的起始位置。
    pos_end：节点在源代码中的结束位置，等于函数体节点的结束位置。

CallNode 类表示函数调用的节点。它具有以下属性：

    node_to_call：被调用的函数节点。
    arg_nodes：参数节点列表。
    pos_start：节点在源代码中的起始位置，等于被调用函数节点的起始位置。
    pos_end：节点在源代码中的结束位置。如果存在参数节点，
    则结束位置为最后一个参数节点的结束位置；否则结束位置为被调用函数节点的结束位置。
"""


class NumberNode:
    def __init__(self, tok):
        self.tok = tok

        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end

    def __repr__(self):
        return f'{self.tok}'


class StringNode:
    def __init__(self, tok):
        self.tok = tok

        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end

    def __repr__(self):
        return f'{self.tok}'


class ListNode:
    def __init__(self, element_nodes, pos_start, pos_end):
        self.element_nodes = element_nodes

        self.pos_start = pos_start
        self.pos_end = pos_end


class VarAccessNode:
    def __init__(self, var_name_tok):
        self.var_name_tok = var_name_tok

        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.var_name_tok.pos_end


class VarAssignNode:
    def __init__(self, var_name_tok, value_node):
        self.var_name_tok = var_name_tok
        self.value_node = value_node

        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.value_node.pos_end


class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

        self.pos_start = self.left_node.pos_start
        self.pos_end = self.right_node.pos_end

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'


class UnaryOpNode:
    def __init__(self, op_tok, node):
        self.op_tok = op_tok
        self.node = node

        self.pos_start = self.op_tok.pos_start
        self.pos_end = node.pos_end

    def __repr__(self):
        return f'({self.op_tok}, {self.node})'


class IfNode:
    def __init__(self, cases, else_case):
        self.cases = cases
        self.else_case = else_case

        self.pos_start = self.cases[0][0].pos_start
        self.pos_end = (self.else_case or self.cases[len(self.cases) - 1])[0].pos_end


class ForNode:
    def __init__(self, var_name_tok, start_value_node, end_value_node, step_value_node, body_node, should_return_null):
        self.var_name_tok = var_name_tok
        self.start_value_node = start_value_node
        self.end_value_node = end_value_node
        self.step_value_node = step_value_node
        self.body_node = body_node
        self.should_return_null = should_return_null

        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.body_node.pos_end


class WhileNode:
    def __init__(self, condition_node, body_node, should_return_null):
        self.condition_node = condition_node
        self.body_node = body_node
        self.should_return_null = should_return_null

        self.pos_start = self.condition_node.pos_start
        self.pos_end = self.body_node.pos_end


class FuncDefNode:
    def __init__(self, var_name_tok, arg_name_toks, body_node, should_auto_return):
        self.var_name_tok = var_name_tok
        self.arg_name_toks = arg_name_toks
        self.body_node = body_node
        self.should_auto_return = should_auto_return

        if self.var_name_tok:
            self.pos_start = self.var_name_tok.pos_start
        elif len(self.arg_name_toks) > 0:
            self.pos_start = self.arg_name_toks[0].pos_start
        else:
            self.pos_start = self.body_node.pos_start

        self.pos_end = self.body_node.pos_end


class CallNode:
    def __init__(self, node_to_call, arg_nodes):
        self.node_to_call = node_to_call
        self.arg_nodes = arg_nodes

        self.pos_start = self.node_to_call.pos_start

        if len(self.arg_nodes) > 0:
            self.pos_end = self.arg_nodes[len(self.arg_nodes) - 1].pos_end
        else:
            self.pos_end = self.node_to_call.pos_end


class ReturnNode:
    def __init__(self, node_to_return, pos_start, pos_end):
        self.node_to_return = node_to_return

        self.pos_start = pos_start
        self.pos_end = pos_end


class ContinueNode:
    def __init__(self, pos_start, pos_end):
        self.pos_start = pos_start
        self.pos_end = pos_end


class BreakNode:
    def __init__(self, pos_start, pos_end):
        self.pos_start = pos_start
        self.pos_end = pos_end



class ParseResult:
  def __init__(self):
    self.error = None
    self.node = None
    self.last_registered_advance_count = 0
    self.advance_count = 0
    self.to_reverse_count = 0

  def register_advancement(self):
    self.last_registered_advance_count = 1
    self.advance_count += 1

  def register(self, res):
    self.last_registered_advance_count = res.advance_count
    self.advance_count += res.advance_count
    if res.error: self.error = res.error
    return res.node

  def try_register(self, res):
    if res.error:
      self.to_reverse_count = res.advance_count
      return None
    return self.register(res)

  def success(self, node):
    self.node = node
    return self

  def failure(self, error):
    if not self.error or self.last_registered_advance_count == 0:
      self.error = error
    return self