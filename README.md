# AI Skills

Skills compartilháveis para esclarecer demandas e criar especificações nos projetos. Cada pasta em `skills/` é uma unidade independente, com um `SKILL.md` como ponto de entrada.

## Catálogo

| Skill | Quando usar | Resultado |
| --- | --- | --- |
| [clickup-review-task](skills/clickup-review-task/SKILL.md) | Revisar uma task e suas subtasks a partir de uma URL do ClickUp, comparando com o código | Descrições claras, subtasks sem sobreposição, decisões nas descrições e pendências e divergências em comentários |
| [sdd-setup](skills/sdd-setup/SKILL.md) | Adotar ou completar Spec-Driven Development em um projeto | Convenções, templates e fluxo SDD compatíveis com o repositório |
| [clickup-create-specs](skills/clickup-create-specs/SKILL.md) | Criar ou atualizar specs a partir de uma URL do ClickUp | Artefatos do SDD local com requisitos verificáveis e origem rastreável |

SDD significa **Spec-Driven Development** neste repositório. Spec Kit é uma implementação possível; nenhuma skill exige uma ferramenta específica ou substitui o padrão já adotado pelo projeto.

## Fluxo de uso

1. Configure o SDD do projeto com `sdd-setup`, caso ele ainda não tenha um padrão utilizável.
2. Revise a demanda com `clickup-review-task` para esclarecer escopo, critérios de aceite e divisão das entregas.
3. Gere as specs com `clickup-create-specs`, mantendo a relação entre tasks, requisitos e validações.
4. Após implementar a entrega, revise o PR com a ferramenta nativa do host (`/code-review` no Claude Code, `/review` no Codex), pedindo que compare a mudança com as specs da entrega. Regras de revisão específicas de cada projeto ficam no `AGENTS.md` ou `CLAUDE.md` dele, que essas ferramentas leem.

As skills também funcionam separadamente. A revisão de tasks não depende da configuração do SDD. A criação de specs usa a task no ClickUp como fonte: cabe a quem desenvolve garantir que as descrições estejam adequadas, aplicando antes a revisão quando necessário. Uma proposta de revisão não aplicada não é considerada.

Para validar a implementação contra os requisitos, executando testes e gerando relatórios, use a `requirements-test`, mantida fora deste catálogo.

Exemplos de pedidos após instalar as skills:

No Codex CLI ou na extensão de IDE:

```text
Use $sdd-setup para configurar SDD neste projeto.

Use $clickup-review-task para revisar e atualizar a task https://app.clickup.com/t/EXEMPLO
e suas subtasks, comparando com o código deste repositório.

Use $clickup-create-specs para criar as specs da task https://app.clickup.com/t/EXEMPLO
e suas subtasks conforme o SDD deste projeto.
```

No Claude Code, use `/sdd-setup`, `/clickup-review-task`, e `/clickup-create-specs` no chat, com o mesmo pedido e contexto. As duas ferramentas também podem selecionar uma skill automaticamente pela descrição.

Exemplos completos de entrada e saída, com dados fictícios:

- [Revisão de task, divergência com o código e decisão pendente](skills/clickup-review-task/references/example.md).
- [Configuração mínima de SDD e ensaio documental](skills/sdd-setup/references/example.md).
- [Criação de spec e tarefas em projeto sem plan.md](skills/clickup-create-specs/references/example.md).

## Instalação e requisitos

As skills usam o formato Agent Skills, com `SKILL.md`, frontmatter `name`/`description` e arquivos de apoio. A mesma pasta pode ser usada em Claude Code e Codex. `agents/openai.yaml` contém metadados da interface Codex; o procedimento compartilhado fica em `SKILL.md`.

| Escopo | Codex | Claude Code |
| --- | --- | --- |
| Pessoal | `~/.agents/skills/` | `~/.claude/skills/` |
| Por projeto | `.agents/skills/` no repositório consumidor | `.claude/skills/` no repositório consumidor |

Fontes: [documentação do Codex](https://learn.chatgpt.com/docs/build-skills) e [documentação do Claude Code](https://code.claude.com/docs/en/skills). Alguns ambientes existentes carregam `~/.codex/skills`; os exemplos abaixo usam o caminho pessoal atualmente documentado para Codex.

### Claude Code: plugin

O repositório também é um marketplace de plugins do Claude Code. Cada pessoa registra o catálogo uma vez e recebe atualizações pelo próprio Claude Code:

```sh
claude plugin marketplace add alanfoandrade/ai-skills
claude plugin install ai-skills@ai-skills
```

Instaladas como plugin, as skills recebem o prefixo do plugin: `/ai-skills:clickup-review-task`, `/ai-skills:sdd-setup` e assim por diante.

### Links simbólicos

Para usar uma cópia local deste repositório e atualizar com `git pull`, crie links simbólicos a partir da raiz. Os dois hosts aceitam pastas de skill por symlink. Crie somente as skills desejadas, em destinos que ainda não existam:

```sh
# Codex
mkdir -p ~/.agents/skills
for s in clickup-review-task sdd-setup clickup-create-specs; do
  ln -s "$PWD/skills/$s" ~/.agents/skills/$s
done

# Claude Code
mkdir -p ~/.claude/skills
for s in clickup-review-task sdd-setup clickup-create-specs; do
  ln -s "$PWD/skills/$s" ~/.claude/skills/$s
done
```

Se preferir uma cópia fixa, use `cp -R` no lugar de `ln -s`; nesse caso, as atualizações precisam ser copiadas de novo. Não instale a mesma skill como plugin e como pasta pessoal ao mesmo tempo, para evitar duas versões disponíveis.

Para instalação por projeto, use a pasta correspondente da tabela no repositório consumidor. Se um destino já existir, revise as diferenças antes de atualizá-lo. As pastas também podem ser distribuídas para outros agentes que entendam `SKILL.md`, adaptando a instalação ao ambiente.

As skills de ClickUp precisam de acesso às tasks por uma integração ou API disponível no ambiente, como o servidor MCP oficial do ClickUp (`https://mcp.clickup.com/mcp`, declarado em `agents/openai.yaml` para o Codex), e acesso de leitura ao código relevante. Credenciais ficam fora deste repositório. Sem integração, elas trabalham com uma exportação fornecida pelo usuário e entregam alterações locais para aplicação posterior, sem alegar atualização no ClickUp.

O pedido define as permissões: revisar gera uma proposta; pedir para atualizar descrições ou criar subtasks autoriza essas operações dentro do escopo informado. Antes de gravar, a revisão mostra uma prévia de descrições, comentários e subtasks e aguarda confirmação, salvo pedido para aplicar diretamente. Comentários de pendência são atribuídos a quem decide e, numa nova revisão, atualizados em vez de duplicados. Criar specs não autoriza editar tasks no ClickUp ou implementar código de produção.

## Manutenção

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para adicionar, validar e evoluir skills. Valide com `python3 scripts/validate_skills.py`. Esta primeira versão foi validada estruturalmente e revisada com cenários documentados; o uso real com ClickUp e projetos consumidores ainda precisa ser exercitado.

## Licença

Copyright (c) 2026 Hi-App Desenvolvimento. Distribuído sob a [CC BY-NC-SA 4.0](LICENSE): você pode usar, adaptar e redistribuir as skills sem fins comerciais, desde que credite a autoria e distribua as adaptações sob a mesma licença. Uso comercial exige autorização do autor.
