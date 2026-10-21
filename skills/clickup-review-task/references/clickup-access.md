# Acesso ao ClickUp

Detalhes da API v2 e do servidor MCP oficial que costumam causar leitura incompleta ou escrita incorreta. Ferramentas e integrações variam: confirme o comportamento no ambiente e consulte a documentação atual do ClickUp se algo não corresponder.

## Identificar a task

- `https://app.clickup.com/t/<id>` usa o ID interno. `https://app.clickup.com/t/<team_id>/<custom_id>` usa um custom ID, como `DEMO-100`.
- Na API, custom IDs exigem `custom_task_ids=true` e `team_id`. Depois de resolver a task, use o ID interno nas escritas e registre também o custom ID exibido ao time.

## Ler conteúdo completo

- `GET /task/{id}` só traz subtasks com `include_subtasks=true`. Subtasks de subtasks precisam ser lidas individualmente.
- Para obter a descrição com formatação, use `include_markdown_description=true`; o campo `description` é texto simples.
- Checklists, dependências e anexos vêm na própria task (`checklists`, `dependencies`, `attachments`).
- `GET /task/{id}/comment` retorna os comentários mais recentes em páginas; continue com `start` e `start_id` do comentário mais antigo recebido até esgotar.
- Respostas encadeadas não vêm na listagem: use `GET /comment/{comment_id}/reply` para comentários com `reply_count` maior que zero.
- Docs vinculados do ClickUp são lidos pela API de Docs; um link na descrição não traz o conteúdo.

## Escrever

- Para criar ou atualizar descrições preservando a formatação, use o campo Markdown da integração (`markdown_content` na API v2). Gravar em `description` substitui o conteúdo por texto simples.
- Para que quem decide seja notificado, atribua o comentário (`assignee` na criação do comentário); isso não altera o responsável da task. Uma menção escrita como texto `@nome` pode não notificar.
- Para atualizar um comentário anterior em vez de duplicá-lo, use `PUT /comment/{comment_id}`.
- Comentários e subtasks não são idempotentes: após falha ou timeout, procure o item criado antes de repetir.

## Servidor MCP oficial

O ClickUp mantém um servidor MCP remoto em `https://mcp.clickup.com/mcp`, com autenticação OAuth. Os nomes e parâmetros das ferramentas dependem do cliente; verifique se cobrem subtasks aninhadas, respostas de comentários e descrição em Markdown antes de alegar leitura completa.
