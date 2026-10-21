# Exemplo de criação de specs

Cenário fictício; artefatos ilustrativos não representam arquivos criados nem uma implementação validada.

## Entrada

Pedido: “Crie as specs da task DEMO-200 e suas subtasks conforme o SDD de `notification-api`.”

- `AGENTS.md` aponta para a constituição; `CLAUDE.md` referencia o mesmo documento. O projeto usa português e `docs/specs/###-nome/{spec.md,tasks.md}`, sem `plan.md`. O template local de spec tem origem, estado, objetivo, requisitos e aceite.
- Nenhuma spec existente corresponde a DEMO-200. A próxima numeração livre é 007.
- Task `https://app.clickup.com/t/DEMO-200`: permitir ao proprietário cancelar uma notificação ainda não enviada.
- Subtask DEMO-201 e seu checklist: apenas o proprietário pode cancelar; tentativas posteriores ao cancelamento são recusadas.
- Resposta C-9 confirma que notificações já enviadas não podem ser canceladas. Documento vinculado confirma que o registro cancelado deve ser preservado.
- Anexo inacessível: material visual sem regras adicionais citadas pelas fontes acessíveis; aceite visual não será especificado.
- Código consultado: branch `develop`, commit abreviado `def5678`; existe uma alteração local em `docs/glossary.md`, incluída na consulta do vocabulário. O serviço ainda não expõe cancelamento.

## Saída esperada

`docs/specs/007-cancel-notification/spec.md`, usando a estrutura do template local:

```markdown
# Cancelamento de notificação

Origem: https://app.clickup.com/t/DEMO-200 e subtask DEMO-201.
Estado: pronta para planejamento.

## Objetivo

Permitir ao proprietário cancelar uma notificação ainda não enviada.

## Requisitos

- FR-001: QUANDO o proprietário solicitar cancelamento de uma notificação ainda não enviada e não cancelada, a notification-api DEVE cancelar a notificação preservando seu registro. Origem: DEMO-200 e documento vinculado.
- FR-002: SE o solicitante não for o proprietário da notificação, ENTÃO a notification-api DEVE recusar o cancelamento. Origem: DEMO-201.
- FR-003: SE a notificação já tiver sido enviada ou cancelada, ENTÃO a notification-api DEVE recusar o cancelamento. Origem: C-9 e checklist de DEMO-201.

## Aceite

- DADO uma notificação elegível, QUANDO o proprietário solicitar o cancelamento, ENTÃO o registro será preservado como cancelado (FR-001).
- DADO uma notificação de outro proprietário, QUANDO houver solicitação de cancelamento, ENTÃO ela será recusada (FR-002).
- DADO uma notificação enviada ou cancelada, QUANDO o proprietário solicitar o cancelamento, ENTÃO ela será recusada (FR-003).
```

`docs/specs/007-cancel-notification/tasks.md`:

```markdown
# Execução do cancelamento de notificação

Spec: [spec.md](spec.md)

## Trabalho

- [ ] T-001: implementar a operação de cancelamento conforme a arquitetura do projeto (FR-001, FR-002, FR-003).
- [ ] T-002: verificar cancelamento elegível e preservação do registro (FR-001).
- [ ] T-003: verificar recusa por solicitante que não é o proprietário (FR-002).
- [ ] T-004: verificar recusa de notificação enviada ou cancelada (FR-003).

## Fontes e cobertura

Task DEMO-200, subtask DEMO-201, checklist, C-9 e documento vinculado; consulta em 21/10/2026. Atualização remota não informada. Anexo visual inacessível; aceite visual não coberto.
```

O resumo da entrega informa uma entrega coesa, os dois arquivos produzidos, as fontes, a lacuna visual e o próximo passo local. Registra também o código consultado — `notification-api`, `develop`, `def5678`, com a alteração local de `docs/glossary.md` incluída — sem gravá-lo nos artefatos. Não cria `plan.md`, não altera o ClickUp e não marca T-001 a T-004 como concluídas. Uma dúvida que alterasse a elegibilidade do cancelamento deixaria a parte afetada em rascunho, com a pergunta bloqueante explícita.
