from typing import Optional

from parse_tree import ParseTree

parse_table = {'E': {'(': ['T', 'K'], '-': ['-', 'F', 'R'], 'n': ['T', 'K']},
               'F': {'(': ['G'], '-': ['-', 'F'], 'n': ['G']}, 'G': {'(': ['(', 'E', ')'], 'n': ['n']},
               'K': {'$': ['e'], ')': ['e'], '+': ['+', 'T', 'K'], '-': ['-', 'T', 'K']},
               'L': {'$': ['e'], ')': ['e'], '*': ['*', 'G', 'L'], '+': ['e'], '-': ['e'], '/': ['/', 'G', 'L']},
               'R': {'$': ['$'], ')': ['e']}, 'T': {'(': ['G', 'L'], 'n': ['G', 'L']}}

terminal_symbols = list("+-/*()ne$")


def parse_symbol_list_full(symbol_list: list) -> Optional[ParseTree]:
    if len(symbol_list) < 2:
        return
    if symbol_list.pop(0).type != "^":
        return
    if symbol_list[-1].type != "$":
        return

    symbol_list = list(reversed(symbol_list))
    head = ParseTree('E', None)
    stack = [head]
    while stack and symbol_list:
        symbol = symbol_list.pop()
        while stack and stack[-1].str not in terminal_symbols:
            if symbol.type not in parse_table[stack[-1].str]:
                return
            else:
                last_type = stack[-1].str
                new_symbols = parse_table[last_type][symbol.type]
                if new_symbols != ['e']:
                    last_expr = stack.pop()
                    last_expr.tail = [ParseTree(x, last_expr) for x in new_symbols]
                    stack.extend(last_expr.tail[::-1])
                else:
                    stack.pop()

        if stack and stack[-1].str == symbol.type:
            last_on_stack = stack.pop()
            if symbol.type == "n":
                last_on_stack.tail.append(symbol.str)
            if symbol.type == '$':
                last_on_stack.parent.tail.remove(last_on_stack)

    if stack or symbol_list:
        return

    return head
