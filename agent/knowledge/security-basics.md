# Fundamentos de segurança

Base de conhecimento usada pela skill `vulnerability-analysis`. Define os termos, a matriz de severidade e as referências que o agente usa para classificar uma falha.

## Conceitos essenciais

| Termo | O que é | Exemplo |
|-------|---------|---------|
| **Ativo** | Tudo que tem valor e precisa de proteção | Banco de clientes, servidor, código-fonte |
| **Vulnerabilidade** | Uma fraqueza que pode ser explorada | Login que monta SQL concatenando a entrada do usuário |
| **Ameaça** | Algo ou alguém que pode explorar a fraqueza | Um atacante na internet, um script automatizado |
| **Exploit** | A forma concreta de explorar a vulnerabilidade | Digitar `' OR '1'='1` no campo de usuário |
| **Risco** | A chance de a ameaça explorar a vulnerabilidade, combinada com o dano que isso causaria | Alto, se o sistema está exposto e guarda dados sensíveis |
| **Controle** | Medida que reduz o risco | Consulta parametrizada, firewall, MFA, backup |
| **Risco residual** | O que sobra de risco depois dos controles | Senhas fracas continuam um problema mesmo sem SQL Injection |

Resumo para lembrar: **sem vulnerabilidade, a ameaça não tem por onde entrar; sem ameaça, a vulnerabilidade não é explorada; o risco existe quando as duas se encontram num ativo que importa.**

## A tríade CIA

Toda avaliação de impacto responde: o que a falha afeta?

- **Confidencialidade:** só quem tem permissão acessa a informação. Quebrada quando dados vazam.
- **Integridade:** a informação não é alterada indevidamente. Quebrada quando alguém modifica ou apaga dados, ou se passa por outra pessoa.
- **Disponibilidade:** o sistema funciona quando é preciso. Quebrada quando o serviço cai ou os dados ficam inacessíveis.

## Matriz de severidade

**Impacto**

- **Baixo:** afeta pouca informação, de baixa sensibilidade, sem efeito relevante no serviço.
- **Médio:** afeta dados internos ou parte do serviço; o dano é recuperável.
- **Alto:** expõe ou altera dados sensíveis, permite tomar contas ou o controle do sistema, ou derruba o serviço.

**Probabilidade**

- **Baixa:** exige acesso interno, credencial privilegiada ou condições raras.
- **Média:** exige algum conhecimento ou acesso, mas é viável.
- **Alta:** sistema exposto, exploração simples e conhecida, sem controles que impeçam.

**Severidade = cruzamento das duas**

| Impacto \ Probabilidade | Baixa | Média | Alta |
|-------------------------|-------|-------|------|
| **Alto** | Média | Alta | Crítica |
| **Médio** | Baixa | Média | Alta |
| **Baixo** | Baixa | Baixa | Média |

Esta matriz é uma simplificação didática. Em ambientes profissionais, a referência mais usada para pontuar vulnerabilidades é o CVSS (Common Vulnerability Scoring System), que considera mais fatores.

## Referências para classificar

- **CWE (Common Weakness Enumeration):** catálogo de tipos de fraqueza. Ex.: CWE-89 é SQL Injection, CWE-798 é credencial fixa no código. https://cwe.mitre.org
- **OWASP Top 10:** as categorias de risco mais comuns em aplicações web, como Injection e Broken Access Control. https://owasp.org/www-project-top-ten/
- **MITRE ATT&CK:** catálogo das técnicas que atacantes usam. Ex.: T1190 (Exploit Public-Facing Application) é a exploração de uma aplicação exposta, como um login vulnerável a SQL Injection; T1110 (Brute Force) é a tentativa de adivinhar senhas. https://attack.mitre.org
- **CVE:** identificador de uma vulnerabilidade específica, já publicada, num produto. Só cite um CVE quando tiver certeza de que ele existe e se aplica.

## Boas práticas

**Desenvolvimento**

- Trate toda entrada do usuário como não confiável: valide e use consultas parametrizadas, nunca concatenação.
- Guarde senhas com hash forte e salt (bcrypt, scrypt, Argon2), nunca em texto puro.
- Não deixe segredos no código: use variáveis de ambiente ou um cofre de segredos.
- Mensagens de erro genéricas para o usuário; detalhes só nos logs.
- Mantenha dependências atualizadas e revise o código antes de ir para produção.

**Infraestrutura**

- Menor privilégio: cada usuário e serviço só com o acesso de que precisa.
- Superfície mínima: desligue serviços e feche portas que não usa.
- Atualizações de segurança frequentes.
- SSH com chave, sem login de root e, se possível, sem senha.
- Firewall com política de negar por padrão, liberando só o necessário.
- Logs ativos e revisados; backups testados.

**Princípios gerais**

- **Defesa em profundidade:** várias camadas de controle, para que a falha de uma não comprometa tudo.
- **Segurança por padrão:** a configuração inicial deve ser a segura.
- **Mude com cuidado:** diagnostique antes de alterar e tenha um caminho para desfazer.

## Ética e escopo

Testes de segurança só em sistemas próprios ou com autorização por escrito. Para praticar, use laboratórios: máquinas virtuais, containers, aplicações propositalmente vulneráveis (como DVWA ou OWASP Juice Shop) e plataformas de treino.
