from antlr4 import *
from antlr4.tree.Trees import Trees
from PogLangLexer import PogLangLexer
from PogLangParser import PogLangParser
from ErrorListener import PogLangErrorListener
import sys
import subprocess
import os

def escape(text):
    return text.replace('"', '\\"')

def walk_tree(tree, rule_names, output, count, parent_id=None):
    node_id = count[0]
    count[0] += 1

    label = escape(Trees.getNodeText(tree, rule_names))
    output.append(f'  node{node_id} [label="{label}"];')

    if parent_id is not None:
        output.append(f'  node{parent_id} -> node{node_id};')

    for i in range(tree.getChildCount()):
        walk_tree(tree.getChild(i), rule_names, output, count, node_id)

def generate_ast(file_path, dot_output_path, png_output_path):
    # Processa o arquivo de entrada com ANTLR
    input_stream = FileStream(file_path, encoding="utf-8")
    lexer = PogLangLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(PogLangErrorListener())

    tokens = CommonTokenStream(lexer)
    parser = PogLangParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(PogLangErrorListener())

    tree = parser.program()

    # Gera o conteúdo do arquivo DOT
    output = ['digraph AST {']
    walk_tree(tree, parser.ruleNames, output, [0])
    output.append('}')

    with open(dot_output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))
    print(f"AST DOT gerada em: {dot_output_path}")

    # Chama o Graphviz para converter o .dot em .png
    try:
        subprocess.run(["dot", "-Tpng", dot_output_path, "-o", png_output_path], check=True)
        print(f"AST PNG gerada em: {png_output_path}")
    except Exception as e:
        print("Falha ao gerar PNG via Graphviz. Verifique se 'dot' está instalado e no PATH.")
        print(e)

if __name__ == "__main__":
    # Obtém os argumentos de linha de comando:
    # 1º argumento: arquivo de entrada (default: "input.pog")
    # 2º argumento: arquivo .dot de saída (default: "ast.dot")
    # 3º argumento: arquivo .png de saída (default: "ast.png")
    file = sys.argv[1] if len(sys.argv) > 1 else "input.pog"
    dot_file = sys.argv[2] if len(sys.argv) > 2 else "ast.dot"
    png_file = sys.argv[3] if len(sys.argv) > 3 else "ast.png"
    generate_ast(file, dot_file, png_file)
