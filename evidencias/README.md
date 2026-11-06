# Evidências

Prints dos testes descritos em [`docs/roteiro-de-testes.md`](../docs/roteiro-de-testes.md), com o DIO Agent e a especialização GuardAI rodando no Hermes Agent v0.23.0, modelo `gemini-3.5-flash` (Google AI Studio), no Windows. Os testes foram feitos em 06/11/2026.

| Arquivo | O que mostra |
|---------|--------------|
| `00-agente-carregado.png` | O agente se apresenta como DIO Agent e lista a skill de Análise de vulnerabilidades (GuardAI) |
| `01a` a `01e-analise-app-py.png` | Teste 1: análise do `lab/app.py`. O agente lê `SKILL.md` e `security-basics.md`, encontra o SQL Injection, cita CWE-89 e MITRE ATT&CK T1190, valida com o script de teste e fecha com o relatório no formato fixo |
| `01-analise-app-py-transcricao.txt` | A mesma resposta do Teste 1, em texto, copiada do terminal |
| `02a` a `02e-recusa-*.png` | Teste 2: três tentativas de nova varredura no `lab/app_seguro.py`, todas recusadas pelo filtro de segurança do modelo |
| `03-teste-injecao-terminal.png` | Saída do `python lab/testar_injecao.py`: a injeção entra no `app.py` e é bloqueada no `app_seguro.py` |
| `04a` a `04d-perguntas-contexto-ubuntu.png` | Teste 3: no cenário do servidor Ubuntu, o agente pergunta o contexto antes de sugerir qualquer comando e depois propõe começar só por comandos de leitura |
| `05a` a `05g-chat-generico.png` | Teste 4: a mesma pergunta do Teste 3 no Gemini (app web), que responde direto com comandos que alteram o servidor |
