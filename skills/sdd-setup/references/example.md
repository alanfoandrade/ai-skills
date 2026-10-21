# Exemplo de configuração de SDD

Cenário fictício para demonstrar o resultado da skill, sem impor este fluxo a projetos com convenções próprias.

## Entrada e diagnóstico

Pedido: “Configure SDD neste projeto usando um processo mínimo.”

- Repositório `notification-api`, branch `main`, commit abreviado `123abcd`, sem alterações locais relevantes antes da configuração.
- `AGENTS.md` descreve arquitetura e aponta para `docs/testing.md`; `CLAUDE.md` também é usado e aponta para o guia de contribuição.
- Não há constituição, templates nem diretório de specs.
- O projeto escreve documentação em português. `package.json` define `npm run typecheck` e `npm test`.
- Não foi solicitado instalar Spec Kit, configurar CI ou implementar uma entrega real.

## Saída esperada

```text
docs/sdd/README.md
docs/sdd/constitution.md
docs/sdd/templates/spec-template.md
docs/sdd/templates/tasks-template.md
```

O guia resultante estabelece `docs/specs/<id>-<nome>/` para futuras entregas, em português, usando `spec.md` e `tasks.md`. Ele descreve especificação → planejamento → implementação → validação, os critérios para avançar e os comandos existentes. A constituição distingue convenções observadas de políticas novas propostas. `AGENTS.md` e `CLAUDE.md` recebem apenas um link para o guia canônico, quando permitido pelas instruções locais.

Trecho ilustrativo de `docs/sdd/README.md`:

> Para uma demanda real, escolha um identificador livre e crie a pasta da entrega. Preencha `spec.md` com origem, objetivo, requisitos identificados e aceite. Registre dúvidas bloqueantes antes do planejamento da parte afetada. Em `tasks.md`, relacione cada tarefa e sua validação aos requisitos. Os comandos disponíveis são `npm run typecheck` e `npm test`; o resultado da execução deve ser registrado quando a implementação ocorrer.

## Ensaio opcional em diretório temporário

Demanda fictícia: “O proprietário pode cancelar uma notificação ainda não enviada.”

| Origem | Requisito | Trabalho | Validação prevista |
| --- | --- | --- | --- |
| DEMO-300 | FR-001: cancelar notificação própria elegível | T-001: implementar a operação; T-002: verificar o comportamento | Confirmar cancelamento e preservação do registro |

Como o fluxo é novo para o projeto, o ensaio preenche os templates fora do catálogo real de specs e confere se a passagem entre etapas é compreensível. A saída informa os arquivos criados, os links conferidos, a revisão consultada e as pendências. Testes de aplicação não são declarados executados por causa desse ensaio documental.

Em um projeto que já tenha Spec Kit e proíba `plan.md`, o resultado esperado muda: completar as lacunas nos artefatos existentes, sem criar `docs/sdd/` ou outro processo concorrente.
