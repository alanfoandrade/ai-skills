# Exemplo de revisão

Cenário fictício. URLs, nomes, caminhos e identificadores abaixo ilustram a estrutura, sem representar operações executadas.

## Entrada

Pedido: “Revise e atualize a task DEMO-100 e suas subtasks, comparando com o repositório `notification-api`. Crie subtasks se houver entregas distintas.”

- Task `https://app.clickup.com/t/DEMO-100`: “Permitir que o cliente tente enviar novamente uma notificação com falha.”
- Subtask DEMO-101: “Adicionar reenvio.” Checklist: aceitar falha e recusar notificação já enviada.
- Resposta encadeada C-7: decisão confirmada de que apenas o proprietário pode reenviar.
- Comentário C-8, posterior, de `@pessoa-produto`: “Talvez o suporte também devesse poder reenviar.” Nenhuma confirmação.
- Documento vinculado: confirma que uma tentativa aceita cria um registro de envio.
- Anexo de tela indisponível por permissão; a descrição não depende dele para definir regras da API.
- Código consultado: branch `feature/resend`, commit abreviado `abc1234`, sem alterações locais relevantes. `src/notifications/resend.service.ts`, método `resend`, permite reenviar registros já enviados. Os testes existentes não exercitam essa condição.

## Saída esperada

**Descrição da task principal:**

> Objetivo: permitir ao proprietário tentar novamente o envio de uma notificação com falha.
>
> Entrega: DEMO-101 implementa a operação na notification-api. A tentativa aceita cria um registro de envio, conforme o documento vinculado.
>
> Decisão: apenas o proprietário pode reenviar (C-7).

**Comentário na task principal:**

> Pendência, atribuída a `@pessoa-produto`, autora de C-8 e indicada pelo usuário como quem decide: o suporte também poderá reenviar? Opções: manter só o proprietário (regra atual de C-7) ou incluir o suporte, o que exige definir a permissão e auditoria do ator. C-8 é uma proposta sem confirmação; até a resposta, vale C-7. Não bloqueia a entrega restrita ao proprietário.
>
> Limite da revisão: o anexo de tela não foi lido por falta de permissão. A revisão cobre a API; o aceite visual permanece sem avaliação.

**Descrição de DEMO-101, preservando seu ID:**

> Resultado: disponibilizar a tentativa de reenvio de uma notificação com falha pelo proprietário.
>
> Aceite:
> - DADO uma notificação com falha do próprio cliente, QUANDO ele solicitar reenvio, ENTÃO uma nova tentativa será registrada.
> - DADO uma notificação já enviada, QUANDO o proprietário solicitar reenvio, ENTÃO a solicitação será recusada sem criar tentativa.
> - DADO uma notificação de outro cliente, QUANDO alguém solicitar reenvio, ENTÃO a solicitação será recusada.

**Comentário em DEMO-101:**

> Divergência: `src/notifications/resend.service.ts`, método `resend`, aceita notificações já enviadas, contrariando o checklist. A descrição registra o comportamento desejado; o código ainda precisa ser ajustado.

**Prévia antes de gravar:** a revisão mostra o trecho atual e o proposto das duas descrições (incluindo a substituição de “Adicionar reenvio.” em DEMO-101) e os dois comentários com task de destino e responsável. Após a confirmação, grava as descrições e cria os comentários. Numa nova revisão, atualiza esses comentários em vez de criar outros.

**Resumo da revisão:**

- Fontes: DEMO-100, DEMO-101, checklist, C-7, C-8 e documento vinculado; consulta em 21/10/2026, atualização remota não informada pela ferramenta. Anexo de tela inacessível.
- Código: `notification-api`, `feature/resend`, `abc1234`, sem alterações locais relevantes.
- Alterações: atualizar as duas descrições e criar dois comentários; reutilizar DEMO-101, sem nova subtask para o mesmo resultado.
- Prontidão: o escopo da API restrito ao proprietário está pronto para specs; ampliação para suporte e aceite visual permanecem pendentes.
- Resultado remoto: informar quais escritas foram confirmadas por releitura, quais falharam e quais não ocorreram. O exemplo não simula uma confirmação real.

Se o pedido fosse somente “revise”, descrições e comentários seriam entregues como proposta, sem escrita no ClickUp.
