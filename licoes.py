LICOES = [
    {
        "titulo": "Variáveis",
        "paginas": [
            (
                "Em programação, uma **variável** é como uma \"caixa\" onde guardamos informações.\n\n"
                "Por exemplo, podemos criar uma variável chamada `nome` para guardar o nome de uma pessoa."
            ),
            (
                "Em Python, atribuímos um valor a uma variável usando o sinal `=`.\n\n"
                "Exemplo:\n"
                "```python\n"
                "nome = \"Ana\"  # Aqui, guardamos o texto \"Ana\" na variável chamada nome\n"
                "idade = 25      # Aqui, guardamos o número 25 na variável chamada idade\n"
                "```\n"
            ),
            (
                "Agora, pratique:\n"
                "1. Crie uma variável chamada `meu_nome` e atribua o seu nome a ela (como texto).\n"
                "2. Crie outra variável chamada `minha_idade` e atribua a sua idade a ela (como número inteiro)."
            ),
        ],
        "teste": "'meu_nome' in locals() and 'minha_idade' in locals() and isinstance(meu_nome, str) and isinstance(minha_idade, int)",
        "dica": "Lembre-se de usar aspas ao definir variáveis de texto. Exemplo: nome = 'SeuNome'"
    },
    {
        "titulo": "Tipos de Dados",
        "paginas": [
            (
                "Em Python, uma variável pode guardar diferentes tipos de dados.\n\n"
                "Os principais tipos são:\n"
                "- **Texto (str)**: Exemplo: `nome = \"João\"`\n"
                "- **Números inteiros (int)**: Exemplo: `idade = 30`\n"
                "- **Números decimais (float)**: Exemplo: `peso = 75.5`\n"
                "- **Valores lógicos (bool)**: Exemplo: `esta_estudando = True`"
            ),
            (
                "Podemos verificar o tipo de um dado usando a função `type()`.\n\n"
                "Exemplo:\n"
                "```python\n"
                "nome = \"Ana\"\n"
                "print(type(nome))  # Saída: <class 'str'>\n"
                "idade = 25\n"
                "print(type(idade))  # Saída: <class 'int'>\n"
                "```"
            ),
            (
                "Pratique:\n"
                "1. Crie uma variável chamada `meu_numero` e atribua o valor 42.\n"
                "2. Use a função `type()` para verificar o tipo da variável."
            ),
        ],
        "teste": "'meu_numero' in locals() and isinstance(meu_numero, int)",
        "dica": "Para verificar o tipo de dado, use a função type(nome_da_variavel)."
    }
]
