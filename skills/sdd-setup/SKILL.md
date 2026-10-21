---
name: sdd-setup
description: Adotar ou completar Spec-Driven Development (SDD) em um projeto, identificando convenções existentes e configurando documentação, templates e fluxo rastreável de requisitos, planejamento, implementação e validação. Usar quando pedirem para configurar, adotar ou completar SDD, Spec Kit, constituição ou templates de spec em um projeto; não implementa features.
license: CC-BY-NC-SA-4.0
---

# Configuração de SDD

Implemente um processo de Spec-Driven Development adequado ao projeto. O resultado deve permitir que outra pessoa crie uma spec e conduza uma entrega sem depender deste chat.

## Diagnóstico

Leia `AGENTS.md`, `CLAUDE.md` e demais instruções aplicáveis, documentação de contribuição, arquitetura, comandos de validação e uma amostra de entregas recentes. Procure constituição, templates, diretórios de specs e configurações de ferramentas, incluindo `.specify/` quando existir. Identifique idioma, localização, numeração, artefatos obrigatórios e fronteiras de edição.

Registre no resumo do diagnóstico a branch e o commit consultados e as alterações locais relevantes incluídas na análise, quando disponíveis. Cite os documentos que fundamentam as convenções preservadas. Não confunda o estado encontrado com novas políticas propostas nem com o estado do remoto ou de produção.

Se já houver SDD, preserve suas convenções e complete lacunas necessárias ao pedido. Não migre o processo nem gere estruturas paralelas só para uniformizar nomes. Em particular, não introduza `plan.md` em projetos que concentram o planejamento em `tasks.md`. Instruções de outro repositório não se tornam regras deste projeto.

SDD não implica instalação de Spec Kit. Quando o usuário escolher uma ferramenta, use a versão e as instruções disponíveis no projeto; consulte documentação oficial atual se precisar de informações externas de instalação ou comandos. Não invente comandos nem execute inicializadores que sobrescrevam configurações existentes sem antes inspecionar seus efeitos.

## Configuração

Para projetos sem padrão, consulte [references/bootstrap.md](references/bootstrap.md). Use [spec-template.md](assets/spec-template.md), [tasks-template.md](assets/tasks-template.md) e [constitution-template.md](assets/constitution-template.md) como base adaptável. Eles não substituem templates já adotados.

Configure apenas os arquivos necessários para estabelecer:

- Onde ficam as convenções e as specs, como identificar uma entrega e onde registrar sua origem.
- Como descrever requisitos e aceite, separar intenção de produto de solução técnica e representar dúvidas sem convertê-las em decisões.
- Como passar de especificação para plano de execução e validação, respeitando os artefatos locais.
- Como relacionar requisitos, trabalho e evidências; quando uma entrega pode iniciar e ser considerada concluída.
- Como lidar com mudança de escopo durante a implementação e quem pode confirmar decisões quando isso já estiver definido no projeto.

Documente regras observadas com suas fontes. Recomendações novas devem aparecer como propostas, não como políticas já aprovadas. Registre verificações desconhecidas como pendências em vez de inventar comandos de CI, donos ou garantias de segurança.

Faça alterações pontuais em arquivos existentes. Quando útil, acrescente aos arquivos de instruções usados pelo projeto (`AGENTS.md` e/ou `CLAUDE.md`) um link para a documentação canônica do SDD, sem duplicar regras ou reescrever instruções alheias ao pedido. Não crie arquivos por editor sem necessidade. Não altere código de produção, dependências, CI ou configuração de deploy por consequência da adoção do processo. Não execute git commit, push ou publicação sem pedido.

## Validação e entrega

Confira links, caminhos, consistência entre templates e convenções, e se os comandos documentados realmente existem. Quando o usuário pedir ou o fluxo for novo para o projeto, percorra uma demanda fictícia pequena para demonstrar origem → requisito → tarefa → validação; use um diretório temporário para esse ensaio, sem criar uma entrega fictícia no catálogo real de specs.

Informe arquivos criados ou atualizados, fluxo escolhido, ferramentas aproveitadas, exemplo de como começar uma spec e decisões ainda pendentes. Diferencie verificações estruturais do processo de qualquer validação de software que não tenha sido executada.

Para um exemplo completo de diagnóstico, configuração e ensaio opcional, consulte [references/example.md](references/example.md).
