import re

# C keywords
keywords = {
    "auto", "break", "case", "char", "const",
    "continue", "default", "do", "double", "else",
    "enum", "extern", "float", "for", "goto",
    "if", "int", "long", "register", "return",
    "short", "signed", "sizeof", "static", "struct",
    "switch", "typedef", "union", "unsigned",
    "void", "volatile", "while"
}

# Token counters
keyword_count = 0
identifier_count = 0
operator_count = 0
constant_count = 0
string_count = 0
separator_count = 0
comment_count = 0
special_count = 0

print("\nLEXICAL ANALYZER AND TOKEN COUNTER")
print("===================================\n")

print(f"{'TOKEN':25} TOKEN TYPE")
print("-" * 50)

# Open input.c
try:
    with open("input.c", "r") as file:
        source = file.read()

except FileNotFoundError:
    print("Error: input.c not found.")
    print("Make sure input.c is in the same folder.")
    exit()


# Token pattern
token_pattern = r'''
    //.*                              # Single-line comment
    |/\*[\s\S]*?\*/                  # Multi-line comment
    |"(?:\\.|[^"\\])*"               # String literal
    |'(?:\\.|[^'\\])*'               # Character literal
    |[A-Za-z_][A-Za-z0-9_]*          # Identifier / keyword
    |\d+(?:\.\d+)?                   # Number constant
    |==|!=|>=|<=|\+\+|--|&&|\|\|     # Two-character operators
    |[+\-*/%=<>!]                    # Single-character operators
    |[(){}\[\];,]                    # Separators
    |[#@?$]                           # Special symbols
'''

tokens = re.findall(token_pattern, source, re.VERBOSE)


for token in tokens:

    # Comments
    if token.startswith("//") or token.startswith("/*"):
        print(f"{token[:25]:25} Comment")
        comment_count += 1

    # String literal
    elif token.startswith('"'):
        print(f"{token:25} String Literal")
        string_count += 1

    # Character literal
    elif token.startswith("'"):
        print(f"{token:25} Constant")
        constant_count += 1

    # Keywords
    elif token in keywords:
        print(f"{token:25} Keyword")
        keyword_count += 1

    # Identifiers
    elif re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', token):
        print(f"{token:25} Identifier")
        identifier_count += 1

    # Numeric constants
    elif re.fullmatch(r'\d+(?:\.\d+)?', token):
        print(f"{token:25} Constant")
        constant_count += 1

    # Operators
    elif re.fullmatch(r'==|!=|>=|<=|\+\+|--|&&|\|\||[+\-*/%=<>!]', token):
        print(f"{token:25} Operator")
        operator_count += 1

    # Separators
    elif token in "(){}[];,":
        print(f"{token:25} Separator")
        separator_count += 1

    # Special symbols
    else:
        print(f"{token:25} Special Symbol")
        special_count += 1


# Display token counts
print("\n" + "-" * 50)
print("TOKEN COUNT")
print("-" * 50)

print(f"Keywords        : {keyword_count}")
print(f"Identifiers     : {identifier_count}")
print(f"Operators       : {operator_count}")
print(f"Constants       : {constant_count}")
print(f"String Literals : {string_count}")
print(f"Separators      : {separator_count}")
print(f"Comments        : {comment_count}")
print(f"Special Symbols : {special_count}")
