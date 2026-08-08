# Rubrica de Auditoria

Como avaliar um OS de forma que o conselho seja específico, honesto, e ligado ao objetivo e aos arquivos reais da pessoa. Uma auditoria genérica é uma auditoria fracassada.

## Antes de pontuar

1. Releia o **objetivo** dela e **para quem é** a partir de `memory.md`.
2. De fato abra a pasta: `CLAUDE.md`, o `substrate/` + `compendium.md`, `rules/`, `skills/`, `tools.md`, `agents/`. Olhe o que de fato está lá, não o que a memória alega.
3. Confronte cada camada com o objetivo. A pergunta nunca é "isso é um bom OS em geral" mas "essa camada move a pessoa em direção ao objetivo DELA."
4. **Checagem de dado sensível.** Se `memory.md` registra algum campo que a pessoa sinalizou como sensível, escaneie todo arquivo em busca desse campo aparecendo de forma literal. Qualquer vazamento (ou uma nota de sensibilidade que exclui um campo e depois o lista mesmo assim) é um achado grave: limite essa camada a `Started` e faça o conserto ser o movimento #1, porque um vazamento vindo de um arquivo guardável como `OS-AUDIT.md` é irreversível.

## Pontue cada camada

Use quatro níveis. Seja honesto. A maioria dos OSes recentes está majoritariamente Missing ou Started, e tudo bem.

- **Missing** - não existe, ou é um placeholder vazio.
- **Started** - existe mas é raso, genérico, ainda não ligado ao objetivo, ou responde só parte do que o objetivo precisa (por exemplo um rastreador que mostra o que vence em breve mas ainda não consegue dizer o que já está atrasado).
- **Solid** - real, específico, e passa a checagem de pronto completa da camada (responde cada parte da pergunta difícil da pessoa com os dados disponíveis, não só a metade fácil).
- **Compounding** - solid E melhora sozinho com o tempo (o substrato cresce, as skills são versionadas, as auditorias realimentam o ciclo).

## O teste do não-genérico

Toda linha que você escrever precisa falhar se for colada na auditoria de um estranho. Se uma frase seria verdadeira para qualquer OS, reescreva-a com as especificidades dela.

- Genérico (banido): "Adicione mais documentação ao seu substrato."
- Específico (exigido): "Seu objetivo é reconquistar assinantes que cancelaram, mas `substrate/` só tem `sources.md` e um `compendium.md` vazio. O movimento de maior alavancagem é puxar as mensagens de cancelamento dos últimos 90 dias para `substrate/churn/` e destilar os três motivos mais comuns em `compendium.md`."

Cite nomes reais de arquivos, lacunas reais, e o objetivo real em cada recomendação.

## Formato de saída

Escreva a auditoria exatamente assim (também salva em `OS-AUDIT.md`):

```
# Auditoria do OS - <YYYY-MM-DD>
Objetivo: <objetivo dela>

## Boletim
| Camada      | Nota        | Por quê (uma linha específica) |
|-------------|-------------|--------------------------|
| Identidade  | Solid       | ... |
| Substrato   | Started     | ... |
| Regras      | Missing     | ... |
| Skills      | Started     | ... |
| Ferramentas | Missing     | ... |
| Agentes     | Missing     | ... |

## Os três movimentos que mais importam (em ordem)
1. <camada> - <exatamente o que fazer, ligado ao objetivo e a um arquivo real> - <por que é a maior alavancagem agora>
2. ...
3. ...

## O que já está funcionando
- <um ou dois pontos fortes genuínos, específicos>

## A única coisa a fazer agora
<uma única ação concreta que ela pode tomar hoje>
```

## Lógica de priorização

Ordene os três movimentos por alavancagem em direção ao objetivo, não pela ordem das camadas. Aplique nesta precedência (a regra de cima vence quando duas competem):

1. **Uma regra dura faltando só vira #1 SE o pior erro possível for iminente ou irreversível** (dinheiro poderia se mover errado, dado privado poderia vazar, um prazo duro está perto). Caso contrário, fica abaixo do substrato.
2. **Do contrário, lacunas de substrato vencem.** Se os bastidores estão rasos, tudo o mais é construído sobre areia. Conserte dado e contexto primeiro.
3. **Skills só importam quando o substrato consegue alimentá-las.** Não empurre skills se não há nada para elas lerem.
4. **Agentes vêm por último.** Nunca recomende um agente antes de existirem as skills que ele orquestraria.

## Escrevendo o resultado de volta na memória

Depois da auditoria, atualize `memory.md`: anexe a manchete datada em `audit_log`, recarimbe `Updated` com a data de hoje, e reescreva o bloco de status das camadas a partir das suas notas usando este mapeamento:

- Missing -> `not started`
- Started -> `in progress`
- Solid -> `solid`
- Compounding -> `solid` (adicione a palavra "compounding" na nota)

## Tom

Encorajador e direto. Nomeie o que já é genuinamente bom antes do que está faltando. Nunca envergonhe uma camada vazia. Trate tudo como o próximo passo concreto, não como uma nota.
