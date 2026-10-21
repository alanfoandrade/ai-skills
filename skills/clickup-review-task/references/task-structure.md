# Estrutura das descrições, comentários e passagem para specs

Use apenas seções úteis à entrega e preserve convenções do workspace. Este modelo define conteúdo, não obriga a substituir uma descrição inteira.

## Task principal

- **Objetivo e contexto:** problema, beneficiário e resultado esperado. Diferencie comportamento atual de desejado.
- **Escopo e limites:** capacidades incluídas, sistemas responsáveis e exclusões relevantes.
- **Entregas:** links para subtasks, resultado de cada uma e dependências entre elas; não reproduza suas descrições.
- **Critérios de aceite transversais:** condições observáveis que comprovam o objetivo global.
- **Decisões confirmadas:** regras que afetam mais de uma entrega, com origem.

## Task executável ou subtask

- **Resultado esperado:** uma entrega delimitada e seu sistema responsável.
- **Comportamento e regras:** gatilho, condições, resposta esperada, permissões e falhas relevantes. Um critério pode usar DADO/QUANDO/ENTÃO quando isso melhorar a precisão.
- **Critérios de aceite:** verificações observáveis, incluindo casos negativos que mudam o resultado. Não invente métricas ou regras ausentes.
- **Dependências e contratos:** o que precisa existir, quem fornece e qual entrega depende disso. Diferencie responsabilidade própria de expectativa sobre outro sistema.
- **Evidências técnicas:** caminhos/símbolos e comportamento encontrado. Branch, commit e alterações locais ficam no resumo da revisão.
- **Decisões confirmadas:** somente as específicas da entrega; referencie as transversais.

## Registros de incerteza e decisão

| Tipo | Onde registrar | Conteúdo mínimo |
| --- | --- | --- |
| Pendência | Comentário na task afetada, atribuído a quem decide | Pergunta objetiva, alternativas, impacto e se bloqueia as specs |
| Divergência | Comentário na task afetada | Fontes em conflito, evidência de cada uma e consequência; resolução somente se confirmada |
| Premissa | Comentário na task afetada | Hipótese ainda não confirmada, como validar e efeito se for falsa |
| Limite de cobertura | Comentário na task principal | Fonte não lida ou aspecto não avaliado e seu efeito na prontidão |
| Decisão | Descrição | Regra acordada, justificativa disponível, origem e autor/data quando constarem da fonte |

Um comentário pode reunir vários registros da mesma task. Atribua o comentário de pendência a quem decide, com a pergunta, as alternativas e o impacto de cada uma; se ninguém estiver indicado, pergunte ao usuário antes de publicar. Quando uma pendência for respondida com decisão confirmada, a regra passa para a descrição com sua origem.

Nunca atribua autor ou data que a fonte não informa. Uma sugestão do agente deve continuar identificada como proposta até ser aceita.

## Prontidão para specs

Uma entrega está pronta quando objetivo, fronteira de responsabilidade e aceite são verificáveis, dependências estão identificadas e nenhuma dúvida em aberto altera suas regras ou seu escopo. Detalhes técnicos que cabem ao planejamento não precisam ser definidos antecipadamente.

Se não estiver pronta, registre a pergunta bloqueante e o que pode avançar. A task no ClickUp — descrições, subtasks e comentários — é a fonte para criar specs: o próximo agente deve conseguir identificar o resultado desejado, as evidências, as decisões e os limites lendo-a, sem depender do histórico do chat. Uma proposta de revisão não aplicada não serve de fonte.
