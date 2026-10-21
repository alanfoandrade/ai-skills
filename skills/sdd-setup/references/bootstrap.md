# Base para projetos sem SDD

Adapte esta base ao tamanho e à documentação do projeto. O padrão mínimo contém uma convenção canônica, templates e uma pasta para entregas. Não requer CLI, prompts por editor ou automações próprias.

## Organização sugerida

```text
docs/sdd/README.md
docs/sdd/constitution.md
docs/sdd/templates/spec-template.md
docs/sdd/templates/tasks-template.md
docs/specs/<id>-<nome-curto>/spec.md
docs/specs/<id>-<nome-curto>/tasks.md
```

Crie a pasta de uma entrega quando existir uma demanda real. Se o projeto já usa outro diretório ou identificadores de tickets, aproveite essa convenção. Ao usar numeração sequencial, consulte os identificadores existentes e verifique colisões antes de gravar; não renumere entregas anteriores.

## Conteúdo de `docs/sdd/README.md`

Documente localização e identificação das specs; idioma; papel de cada artefato; fluxo e critérios abaixo; comandos de validação encontrados no projeto; regra para manutenção dos artefatos. A constituição concentra princípios; os templates orientam a redação; o guia liga o fluxo às ferramentas do repositório.

| Etapa | Saída e critério para avançar |
| --- | --- |
| Especificar | Objetivo, escopo, requisitos identificados, aceite e fontes. Perguntas que alteram comportamento estão respondidas ou a parte afetada está bloqueada explicitamente |
| Planejar | Tarefas ligadas aos requisitos, dependências, impactos em contratos/dados e validações pertinentes. Decisões técnicas ficam aqui, salvo convenção diferente |
| Implementar | Execução do plano com progresso rastreável. Contradições com a spec são registradas e resolvidas conforme as instruções do projeto antes de alterar comportamento |
| Validar | Evidências de atendimento aos requisitos e verificações técnicas. Se algo não foi validado, o resultado informa a lacuna |

Não imponha aprovação formal em toda etapa quando o projeto não a exige. Uma pergunta de produto continua em aberto até existir resposta; silêncio não confirma uma premissa.

## Uso dos templates

Copie os arquivos de `assets/` para a localização escolhida e adapte o vocabulário, o idioma, os comandos e os papéis ao projeto. Marcadores entre colchetes são campos a preencher em futuras entregas. Não deixe campos de fatos do projeto em aberto na documentação de configuração sem identificá-los como pendências.

O padrão mínimo usa `spec.md` para o quê/por quê e `tasks.md` para como implementar/verificar. Acrescente outros artefatos somente quando uma necessidade do projeto justificar, como um contrato extenso ou uma decisão arquitetural que já tenha local canônico.
