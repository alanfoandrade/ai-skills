# Rastreabilidade e cobertura

Use o formato do projeto. Esta matriz é uma opção para `tasks.md` ou outro artefato apropriado; não crie um arquivo extra se os links já garantirem o mesmo resultado.

| Fonte | Regra ou decisão | Requisito | Trabalho e validação |
| --- | --- | --- | --- |
| URL da task principal | Resultado global confirmado | FR-001 | IDs das tarefas técnicas e aceite observável |
| URL da subtask | Exceção específica | FR-002 | Trabalho correspondente e verificação negativa |
| Comentário ou decisão identificável | Restrição confirmada | FR-003 | Verificação compatível com a restrição |

Um requisito pode consolidar várias fontes; uma task pode originar vários requisitos. Rastreie também critérios transversais da task principal.

## Estado das fontes

No artefato que o padrão local permitir, registre URLs/IDs, data de consulta e última atualização informada pelas fontes, quando disponíveis. Identifique comentários, respostas, checklists, documentos e anexos que fundamentaram decisões, junto de limitações de leitura e seus impactos. Para exportações, indique arquivo e data conhecida; não presuma sincronização com o ClickUp. Registre uma vez e use links nos demais artefatos.

O estado do código consultado (branch, commit, alterações locais) pertence ao resumo da entrega: ele descreve a sessão de trabalho e perde sentido para quem lê o artefato depois.

## Antes de marcar como pronta

- Cada regra e critério relevante tem requisito correspondente, ou exclusão justificada por fonte e escopo. Conteúdo ausente não equivale a exclusão aceita.
- Cada requisito tem origem confirmada, sistema responsável e aceite observável; propostas continuam identificadas como propostas.
- Cada trabalho planejado se relaciona a um requisito ou a uma necessidade técnica justificada da entrega. Não acrescente refatorações oportunistas.
- Contratos entre serviços distinguem obrigações próprias de dependências externas; artefatos técnicos contêm detalhes de implementação somente onde o padrão permite.
- Perguntas bloqueantes têm impacto e parte afetada identificados. Premissas relevantes não estão escondidas em requisitos definitivos.
- IDs e links resolvem; itens concluídos e decisões válidas foram preservados ao atualizar uma spec existente.

## Reexecução

Compare a nova demanda com o que já foi especificado. Amplie ou ajuste os requisitos preservando IDs ainda válidos. Mudanças em itens concluídos devem aparecer como novo trabalho ou revisão explícita; não reabra checkboxes ou apague evidências automaticamente.
