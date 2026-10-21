# Contribuindo

## Organização

```text
skills/<nome-da-skill>/
  SKILL.md             # Quando usar, resultado e instruções essenciais
  agents/openai.yaml   # Nome, descrição curta e exemplo de invocação
  references/          # Detalhes consultados conforme a necessidade
  assets/              # Templates destinados ao projeto consumidor
.claude-plugin/        # Manifesto do plugin e do marketplace do Claude Code
scripts/               # Validação do catálogo
```

Crie somente as pastas necessárias. Use nomes em minúsculas com hífens e mantenha o nome da pasta igual ao campo `name` do frontmatter. Escreva as instruções em português; respeite o idioma do projeto ao gerar artefatos.

Cada skill deve funcionar sozinha. Não use caminhos absolutos da máquina, nomes de clientes, IDs reais, tokens ou dependências implícitas de outras skills deste catálogo. Exemplos devem ser fictícios. Use referências relativas internas para permitir copiar uma pasta isoladamente. Quando duas skills precisarem do mesmo material, como `references/clickup-access.md`, mantenha uma cópia em cada uma e atualize as duas juntas.

Mantenha o procedimento compartilhado compatível com Claude Code e Codex: considere `AGENTS.md` e `CLAUDE.md` aplicáveis ao projeto e evite depender de nomes fixos de ferramentas de um único ambiente. Documente os caminhos de instalação e as formas de invocação de cada host no README. Os metadados específicos do Codex ficam em `agents/openai.yaml`. No frontmatter, use apenas `name`, `description`, `license`, `allowed-tools`, `metadata` e `compatibility`: campos exclusivos do Claude Code, como `argument-hint`, quebram o upload no claude.ai e o validador do skill-creator.

## Alterações

Descreva no frontmatter a capacidade e o gatilho de uso. Coloque no corpo as decisões que o agente precisa tomar e em `references/` os detalhes condicionais. Coloque templates em `assets/`, deixando claro que devem ser adaptados ao projeto, não copiados sobre convenções existentes.

Evite transformar preferências de um projeto em exigências universais. Diferencie fatos encontrados no código, comportamento desejado, premissas e decisões confirmadas. Não inclua comandos ou endpoints de ferramentas como se fossem disponíveis em todo ambiente.

Ao corrigir uma falha observada, registre um cenário de validação relevante e faça a menor mudança suficiente. Atualize o catálogo quando mudar o propósito de uma skill e incremente `version` em `.claude-plugin/plugin.json` ao publicar mudanças, para que quem instalou o plugin receba a atualização.

## Validação

Execute a partir da raiz do repositório:

```sh
python3 scripts/validate_skills.py                       # todas as skills
python3 scripts/validate_skills.py skills/sdd-setup      # uma skill
```

O script não tem dependências externas e retorna código diferente de zero quando encontra problemas, o que permite usá-lo em CI. Com o Claude Code instalado, valide também o manifesto com `claude plugin validate .`.

O validador verifica estrutura, nomes e frontmatter; ele não valida as decisões do agente. Revise também links relativos, consistência dos metadados e ausência de instruções dependentes do ambiente do autor.

Exercite os cenários abaixo em um projeto temporário, usando tasks fictícias ou uma exportação local. Operações reais no ClickUp só entram no teste quando fizerem parte do pedido autorizado.

| Cenário | Comportamento esperado |
| --- | --- |
| Revisar task com critério conflitante com o código | Registrar a divergência com evidência; não decidir automaticamente que o código é o requisito correto |
| Revisar hierarquia com subtask já existente e repetir o pedido | Reutilizar a subtask e preservar seu ID; não duplicar entregas |
| Atualizar ClickUp com erro após criar uma subtask | Consultar o estado antes de repetir; separar alterações confirmadas, falhas e resultado desconhecido |
| Atualizar descrições e criar comentários na task | Mostrar prévia de todas as escritas e aguardar confirmação, salvo pedido para aplicar diretamente |
| Repetir a revisão de uma task já comentada | Atualizar os comentários anteriores e publicar só o que mudou, sem duplicar |
| Revisar task com pendência e divergência | Registrar ambas em comentário na task afetada, atribuído a quem decide ou perguntando ao usuário quando não houver indicação; manter na descrição apenas escopo, aceite e decisões |
| Revisar sem acesso ao ClickUp ou ao repositório | Produzir somente o que as fontes disponíveis permitem e informar a cobertura ausente |
| Encontrar regra em resposta encadeada ou checklist e anexo sem permissão | Considerar a regra acessível e registrar o anexo não lido com seu impacto, sem alegar cobertura completa |
| Encontrar sugestão recente que contraria decisão confirmada | Manter a sugestão como pendência, sem substituir a decisão automaticamente |
| Analisar código com mudanças locais ainda não commitadas | Registrar branch, commit e mudanças relevantes incluídas na consulta; não atribuir a análise somente ao commit |
| Usar projeto com instruções aplicáveis em CLAUDE.md | Considerar essas instruções e referenciar a documentação canônica sem duplicar regras |
| Configurar SDD em projeto sem convenções | Criar base adaptada ao projeto e explicar como produzir e validar uma entrega |
| Configurar SDD em projeto que usa Spec Kit sem `plan.md` | Preservar fluxo, idioma, localização e divisão dos artefatos; não introduzir um fluxo paralelo |
| Criar specs de task e subtasks que atravessam dois serviços | Separar responsabilidades, explicitar dependências e rastrear cada requisito à fonte |
| Criar specs com regra de negócio em aberto | Registrar pergunta e impacto; não inventar requisito nem apresentar a parte bloqueada como pronta |
| Criar specs de task com descrição insuficiente e revisão anterior não aplicada | Usar somente a task no ClickUp, apontar o que falta e recomendar revisar e atualizar a task antes |
| Criar specs com alterações locais no repositório | Registrar branch, commit e alterações locais no resumo da entrega, não nos artefatos |
| Gerar specs novamente com trabalho concluído em `tasks.md` | Atualizar a entrega existente preservando IDs, checkboxes e histórico relevante |

Informe na entrega quais cenários foram realmente executados e quais passaram apenas por revisão das instruções.

Os exemplos completos em `references/example.md` de cada skill são material de orientação com dados fictícios, não registros de testes aprovados.
