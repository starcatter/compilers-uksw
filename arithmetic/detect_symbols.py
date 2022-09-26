printable_terminal_symbols = "()+-/*"
digits = "0123456789"


class Symbol:
    def __init__(self, sym_type: str, as_str: str):
        self.type = sym_type
        self.str = as_str

    def __str__(self):
        return self.str


def detect_symbols(text: str) -> list:
    symbol_list = [Symbol("^", "")]
    for c in text:
        if c in digits:
            if symbol_list[-1].type == 'n':
                symbol_list[-1].str += c
            else:
                symbol_list.append(Symbol('n', c))
        elif c in printable_terminal_symbols:
            symbol_list.append(Symbol(c, c))
        else:
            return []
    symbol_list.append(Symbol("$", ""))
    return symbol_list
