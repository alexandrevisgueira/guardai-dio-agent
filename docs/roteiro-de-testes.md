# Roteiro de testes do GuardAI

Os prompts usados para testar a especialização, na ordem do desafio. Rode o Hermes num terminal aberto **na pasta do projeto** e salve um print de cada etapa em `evidencias/`.

Todos os testes usam só código e máquinas de laboratório do próprio autor.

## Teste 1: encontrar a falha no app.py

```
Atue como especialista em AppSec. Analise o arquivo lab/app.py:
encontre a falha, explique como ela seria explorada, cite a técnica
do MITRE ATT&CK e me ajude a reescrever o código.
```

**O que conferir:** o agente aponta a linha que concatena o SQL, classifica como SQL Injection (CWE-89, OWASP Injection, MITRE ATT&CK T1190), avalia impacto, probabilidade e severidade e entrega o relatório no formato fixo da skill.

Para ver a falha acontecendo, rode `python lab/app.py`, digite `admin' --` no usuário e qualquer coisa na senha.

## Teste 2: corrigir e validar

```
Apliquei a correção com consulta parametrizada em lab/app_seguro.py.
Faça uma nova varredura e confirme se o SQL Injection foi mitigado.
Existe algum risco residual?
```

**O que conferir:** o agente confirma a mitigação, aponta o que ainda pode ser melhorado (por exemplo, limite de tentativas de login) e atualiza o relatório.

Validação automática: `python lab/testar_injecao.py`. A injeção deve entrar no `app.py` e ser bloqueada no `app_seguro.py`.

## Teste 3: perguntas de contexto num cenário de infraestrutura

```
Tenho um servidor Ubuntu de laboratório exposto na internet.
Quero saber se ele está seguro. Por onde começo?
```

**O que conferir:** antes de qualquer comando, o agente pergunta o contexto (para que serve o servidor, quais serviços e portas estão abertos, como é o acesso remoto, se há dados reais). Quando chegar aos comandos, começa pelos que só leem.

## Teste 4 (comparação): a mesma pergunta num chat genérico

Envie o prompt do Teste 3 num chat de IA comum, sem o DIO Agent, e compare: o chat genérico tende a responder direto com uma lista de comandos, sem perguntar nada.

## Teste 5 (extra): outro cenário com o mesmo formato

```
Analise esta configuração de SSH do meu servidor de laboratório:
PermitRootLogin yes
PasswordAuthentication yes
Port 22
```

**O que conferir:** o relatório sai na mesma tabela do Teste 1, o que permite comparar a severidade dos dois casos.

## Revisão da skill pelo próprio agente

```
Estou evoluindo o DIO Agent com uma skill de análise de vulnerabilidades.
Já criei a pasta da skill e o SKILL.md, mas não sei se o processo que escrevi
está claro para um agente.
Leia o meu SKILL.md e me pergunte, etapa por etapa, o que ficou ambíguo.
```
