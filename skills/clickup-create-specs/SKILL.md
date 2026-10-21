---
name: clickup-create-specs
description: Criar ou atualizar specs a partir de uma task e suas subtasks do ClickUp informadas por URL ou ID, seguindo a constituição, os templates e o fluxo SDD do projeto, com rastreabilidade entre fontes, requisitos e trabalho. Usar quando pedirem para especificar uma task do ClickUp ou gerar e atualizar spec.md, tasks.md ou artefatos equivalentes a partir dela. Não configura um novo processo SDD nem implementa a feature.
license: CC-BY-NC-SA-4.0
---

# Criação de specs a partir do ClickUp

Converta uma demanda em artefatos SDD compatíveis com o projeto. Não implemente código de produção, não marque trabalho como concluído e não altere o ClickUp apenas por ter gerado uma spec.

## Descobrir o padrão e as fontes

1. Identifique o repositório da demanda e leia `AGENTS.md`, `CLAUDE.md` e demais instruções aplicáveis, constituição, templates, fluxo e uma amostra representativa de specs. Confirme localização, idioma, nomenclatura, responsáveis e fronteiras entre requisitos e planejamento. Se houver múltiplos repositórios plausíveis, esclareça o destino antes de escrever.
2. Resolva a URL ou o ID por uma integração ou API disponível; [references/clickup-access.md](references/clickup-access.md) reúne detalhes de IDs, subtasks, comentários e formatação. Leia task, subtasks acessíveis em todos os níveis, critérios, checklists, decisões, comentários relevantes e suas respostas encadeadas, além das dependências pertinentes. Percorra paginação. Consulte documentos e anexos vinculados quando sustentarem os requisitos; registre conteúdo ilegível, imagens não interpretadas, respostas indisponíveis e restrições de permissão. Se não houver acesso, use conteúdo ou exportação fornecidos pelo usuário e explicite limitações de atualização e completude.
3. A task no ClickUp — descrições, subtasks e comentários — é a fonte da demanda. Propostas de revisão não aplicadas, rascunhos e resumos de conversa não a substituem. Se a descrição for insuficiente para especificar, aponte o que falta e recomende revisá-la e atualizá-la no ClickUp antes, por exemplo com a skill `clickup-review-task`, quando disponível.
4. Compare o pedido ao código, testes e contratos relevantes para compreender o estado atual e a responsabilidade de cada sistema. Cite evidências técnicas no artefato permitido pelo padrão local; não transporte detalhes de implementação para uma spec que os proíba.

Se o projeto não tiver um padrão SDD utilizável, entregue o diagnóstico e o conteúdo de requisitos que puder preparar, e peça a definição do padrão ou autorização para configurá-lo. Não instale ferramentas nem invente uma estrutura paralela. A skill `sdd-setup`, quando disponível, pode atender esse pedido separado.

## Delimitar entregas

- Procure specs existentes por URL, IDs e assunto antes de criar uma nova. Reutilize a entrega correspondente e preserve identificadores, decisões e progresso válido em arquivos de trabalho.
- Agrupe task e subtasks por resultado coeso e responsabilidade. Não crie automaticamente uma spec por subtask nem uma única spec para sistemas independentes. Em demandas entre serviços, especifique apenas o comportamento de cada sistema em seu repositório e explicite contratos e dependências; não atribua a ele requisitos de outro serviço.
- Separe requisito confirmado, estado atual, premissa e questão em aberto. Uma divergência entre código e task não autoriza escolher o código como comportamento desejado. Decisões conflitantes precisam de fonte e confirmação; perguntas de negócio não se resolvem por inferência técnica. Um comentário mais recente só substitui uma regra quando registra uma decisão confirmada; perguntas e sugestões continuam como tal.
- Quando houver dúvida bloqueante, documente a pergunta e o impacto, crie um rascunho se o fluxo permitir e avance nas partes independentes. Represente a dúvida com o marcador do projeto, como `[NEEDS CLARIFICATION: ...]` no Spec Kit. Não apresente como pronta uma entrega cujas regras ou fronteiras ainda dependam de resposta.

## Escrever e verificar

Use os templates locais e somente os artefatos exigidos ou necessários. Gere `spec.md`, `tasks.md`, `plan.md` ou equivalentes conforme o fluxo adotado; não crie `plan.md` se o projeto o exclui. Se houver scripts locais de geração, inspecione seus efeitos sobre branches e arquivos antes de executá-los; prefira criar os artefatos diretamente quando o script exigir ações fora do pedido.

Escreva requisitos identificáveis, observáveis e atribuídos ao sistema correto. Cubra permissões, exceções e contratos quando relevantes e sustentados pelas fontes. Registre lacunas em vez de inventar métricas, payloads, status ou regras. As tarefas técnicas devem apontar para requisitos e incluir verificação proporcional à mudança.

Leia [references/traceability.md](references/traceability.md) para mapear fontes e validar cobertura sem duplicar conteúdo. Antes de finalizar, confira alterações nas tasks quando houver suporte; mudanças relevantes pedem reconciliação com o rascunho. Se o ambiente não permitir detectar atualizações, informe que a spec se baseia no conteúdo efetivamente lido.

Valide os artefatos com os verificadores locais pertinentes, quando existirem, e confira links e referências. Releia as fontes para garantir que nenhum critério desapareceu ou virou uma decisão inventada. Não execute testes de aplicação como evidência de uma implementação que ainda não foi feita.

## Entrega

Informe caminhos criados ou alterados, tasks de origem, divisão das specs, cobertura, pendências e estado de prontidão. Registre no resumo, não nos artefatos, a branch, o commit e as alterações locais relevantes consultadas em cada repositório; sem esses metadados, informe a limitação sem presumir equivalência com o remoto ou produção. Diga qual é o próximo passo previsto pelo fluxo local. Se faltarem fontes ou acesso, distinga conteúdo preparado de entrega completa. Não faça commit, push ou publicação sem pedido.

Para um exemplo completo de entrada e saída em um projeto sem `plan.md`, consulte [references/example.md](references/example.md).
