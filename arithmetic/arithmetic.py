from detect_symbols import detect_symbols
from parser import parse_symbol_list_full


def evaluate_expression(user_input: str):
    if (symbols_list := detect_symbols(user_input)) and (expression_tree := parse_symbol_list_full(symbols_list)):
        return expression_tree.eval()


if __name__ == "__main__":
    text = input("Please insert an arithmetic expression: ")
    if any(x in text for x in " \t"):
        print("Parser does NOT accept whitespace characters!")
        text = "".join(text.split())
        print("Trying the expression with whitespace removed: " + text)
    try:
        result = evaluate_expression(text)
        if result is not None:
            print("=", result)
        else:
            print("Expression is INCORRECT according to the provided grammar!")
    except Exception as e:
        print(e)
        print(
            "There are \"undocumented features\" in the program or expression is INCORRECT.")
