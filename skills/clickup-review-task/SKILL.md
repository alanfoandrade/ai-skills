---
name: clickup-review-task
description: Revisar tasks e subtasks do ClickUp a partir de uma URL ou ID, confrontar descrições com o código e organizar escopo, critérios de aceite, pendências, divergências e decisões para posterior criação de specs SDD. Atualizar descrições, criar subtasks e registrar pendências em comentários quando solicitado. Usar quando pedirem para revisar, refinar, esclarecer ou quebrar uma task do ClickUp em entregas antes de especificar ou implementar.
license: CC-BY-NC-SA-4.0
---

# Revisão de task do ClickUp

Deixe a demanda suficientemente clara para gerar specs sem redescobrir seu escopo. Esta skill revisa a demanda; não implementa funcionalidades nem cria specs completas.

## Fontes e cobertura

- Resolva a URL ou o ID com a integração ou API de ClickUp disponível; [references/clickup-access.md](references/clickup-access.md) reúne detalhes de IDs, subtasks, comentários e formatação. Leia a task, a hierarquia completa de subtasks acessíveis, descrições, critérios, checklists, dependências, comentários relevantes e suas respostas encadeadas. Percorra paginação e níveis aninhados. Consulte documentos e anexos vinculados quando sustentarem regras ou decisões da demanda; registre arquivos ilegíveis, imagens não interpretadas, respostas indisponíveis e restrições de permissão. Siga tasks relacionadas somente quando necessárias à demanda.
- Confirme o repositório pela relação com a demanda, instruções locais e código. Se houver mais de um candidato plausível, pergunte qual usar antes de registrar conclusões específicas. Leia `AGENTS.md`, `CLAUDE.md` e instruções aplicáveis ao caminho analisado, além das convenções SDD existentes.
- No resumo da revisão, não nas descrições, registre as URLs/IDs das fontes, a data de consulta e a última atualização informada pela ferramenta, diferenciando conteúdo lido, não lido e inacessível e o efeito de cada lacuna na prontidão. Por repositório, registre branch, commit e alterações locais relevantes incluídas na análise. Sem esses metadados, informe a limitação; não presuma que a cópia local representa o remoto ou produção. Credenciais e dados pessoais desnecessários não entram no registro.
- Sem acesso ao ClickUp, peça uma exportação ou conteúdo das tasks e prossiga com uma proposta local, registrando o arquivo e a data informada sem tratá-la como conteúdo atual. Sem código, faça a revisão textual e registre que a comparação técnica está pendente. Não apresente conteúdo parcial como revisão completa.

## Revisão e decomposição

1. Identifique objetivo, atores, comportamento atual e desejado, limites da entrega, critérios observáveis e dependências. Compare com pontos concretos do código e testes relevantes; cite caminhos e símbolos, além de linhas quando úteis. Ausência de teste não prova ausência de comportamento.
2. Separe **fato observado**, **requisito solicitado**, **divergência**, **pendência**, **premissa** e **decisão confirmada**. O código descreve o estado atual; não substitui uma decisão de produto. Registre evidência e impacto de conflitos entre task, comentários, código e documentação. Um comentário mais recente só substitui uma regra quando registra uma decisão confirmada; perguntas e sugestões continuam como tal.
3. Reutilize subtasks que já representem uma entrega. Crie novas divisões somente quando houver resultado verificável, responsabilidade ou dependência distinta. Não replique regras entre task principal e subtasks: mantenha o objetivo e índice na principal e o escopo executável em cada filha. Uma etapa técnica pequena pode ser checklist em vez de subtask.
4. Use [references/task-structure.md](references/task-structure.md) ao redigir descrições e comentários e ao avaliar prontidão para specs. As descrições contêm objetivo, escopo, entregas, aceite, dependências e decisões confirmadas; pendências, divergências, premissas e limites de cobertura vão para comentários na task afetada. Preserve contexto, links, IDs e decisões válidas existentes. Consolide redundâncias sem apagar evidências úteis ou resolver dúvidas por suposição.
5. Faça primeiro o mapeamento entre tasks existentes e alterações propostas. Perguntas que afetam escopo, contrato ou regra de negócio devem incluir alternativas e impacto. Continue a revisão do que independe dessas respostas.

## Aplicação no ClickUp

Se o usuário pediu apenas revisão, entregue a proposta. Se pediu atualizar descrições, criar subtasks ou registrar pendências, execute as operações solicitadas usando a ferramenta disponível, respeitando permissões do ambiente.

Escritas notificam pessoas e ficam visíveis para o time. Antes de gravar, mostre uma prévia de todas elas — trecho atual e proposto de cada descrição, cada comentário com a task de destino e o responsável, e as subtasks a criar — e só aplique depois da confirmação, salvo se o pedido disser para aplicar diretamente.

Atribua cada comentário de pendência a quem decide, usando o responsável indicado na task, na spec ou pelo usuário. Se ninguém estiver indicado, pergunte ao usuário; não atribua por palpite.

Ao revisar novamente uma task, procure os comentários da revisão anterior. Atualize o comentário que trata do mesmo registro em vez de criar outro, publique só o que mudou e não repita pendências já respondidas. Uma pendência respondida só vira decisão na descrição quando a resposta confirmar a regra.

Antes de escrever, releia as tasks afetadas e incorpore edições concorrentes; se mudarem a decisão ou o escopo, esclareça o conflito. Preserve o conteúdo não relacionado. Não altere status, responsável, prazo, prioridade, localização ou dependências formais, nem exclua ou mova tasks, sem isso fazer parte do pedido. Escreva no formato que preserva a formatação da descrição, conforme a referência de acesso.

Mantenha o vínculo entre entrega proposta e ID remoto. Se houver falha ou timeout de escrita, consulte o estado antes de repetir, principalmente na criação de subtasks e comentários. Sem conseguir verificar se a criação ocorreu, pare essa escrita e relate o resultado desconhecido. Depois de uma atualização, releia os campos afetados para confirmar persistência.

## Entrega

Informe as tasks revisadas e seus links, mudanças aplicadas ou propostas, comentários criados, cobertura da análise de código, pendências com responsável quando conhecido e prontidão de cada entrega para specs. Diferencie operações confirmadas, falhas e não executadas. Uma demanda com dúvida bloqueante pode ter partes prontas; identifique quais.

Para um exemplo completo de entrada e saída, consulte [references/example.md](references/example.md).
