# Script de processamento de logs:
A principal finalidade do projeto é de facilitar na validação das logs de um sistema,
captando o horário que foi efeituado o acesso, o usuário que acessou, e o a ação executado pelo usuário.
Também há uma detecção de erros e formação de um relatório estatístico.

# Principais conceitos abordados:
- **Fundamentos Python**: class, if/else/elif, for, split e open/read/write.
- **Programação Orientada a objetos**: encapsulamento, estado do objeto e comportamento.
- **Manipulação de arquivo**: arquivo de entrada, arquivo de saida, leitura linha a linha e escrita estruturada.
- **Processamento e validação de dados**: parsing, validação de formato e classificação de eventos(LOGIN/LOGOUT/ERROR).
- **Controle de estado**: sessões, autenticação e workflows.
- **Contadores e estatísticas**: contadores de eventos, diferenciação de válido e inválido e geração de resumo final.
- **separação de funções**: parsing, validação e relatório.

# Log utilizada está localizada em "Logs.txt" e segue o formato:
- **DATA;USUÁRIO;AÇÃO**

# Exemplo das logs utilizadas
2025-01-21 08:15:10;user123;LOGIN
2025-01-21 08:16:44;user123;ERROR
2025-01-21 08:20:01;user123;LOGOUT
2025-01-21 09:01:55;user999;LOGIN
2025-01-21 09:05:12;user999;ERROR
2025-01-21 09:07:44;user999;LOGOUT
2025-01-21 10:15:33;user777;LOGIN
2025-01-21 10:20:18;user777;LOGIN 
2025-01-21 10:23:55;user777;LOGOUT
2025-01-21 11:05:33;user888;LOGIN
2025-01-21 11:06:05;user888;LOGOUT
2025-01-21 11:06:15;user888;LOGOUT
2025-01-21 12:00:01;user555;LOGIN
2025-01-21 12:05:10;user555;ERROR
2025-01-21 12:06:42;user555;LOGIN 
2025-01-21 12:08:33;user555;LOGOUT
2025-01-21 12:10:10;user555;LOGOUT 
2025-01-21 12:15:21;user999;LOGIN
2025-01-21 12:20:10;user999;LOGOUT
2025-01-21 12:21:50;user111;ERROR
2025-01-21 12:22:20;user111;LOGIN
2025-01-21 12:25:55;user111;LOGOUT
INVALID_LINE_SHOULD_BE_IGNORED
2025-01-21 13:10:10;user200;LOGIN
2025-01-21 13:20:44;user200;LOGOUT
2025-01-21 14:00:05;user123;LOGIN
2025-01-21 14:05:33;user123;ERROR
2025-01-21 14:07:55;user123;LOGOUT
2025-01-21 14:20:10;user888;LOGIN
2025-01-21 14:30:12;user888;LOGIN   
2025-01-21 14:33:05;user888;ERROR
2025-01-21 14:40:01;user888;LOGOUT
2025-01-21 15:00:00;user555;LOGIN
2025-01-21 15:10:12;user555;LOGOUT

# Resultado esperado

Ao final da execução, o sistema gera um relatório com as seguintes informações:

- **O detalhamento das ações processadas**
- **A identificação de erros inconsistências**
- **Um resumo estístico com os totais de eventos processados**

Este projeto foi criado partindo do propósito de praticar Python, POO e processamento de dados estruturados.

# Erros captados dentro do código

Comando igual seguido -- ERRO 
Logout sem login -- ERRO
Linhas inválidas -- Ignoradas 
Error -- Não quera o código

# Melhorias para o futuro

- **Caminho do arquivo configurável**
- **Contadores exibindo comandos válidos por usuário**
- **Exportar relatório em outros formatos**
- **Tornar o projeto automático, verificando as logs no mesmo instante**

