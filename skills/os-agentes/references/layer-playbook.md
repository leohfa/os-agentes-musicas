# Guia de Camadas

Como treinar cada camada para uma pessoa não técnica. Para cada camada você tem: o que é em palavras simples, uma analogia, as perguntas a fazer, o artefato que você constrói, a checagem de pronto, e o erro comum a evitar.

Sempre adapte o artefato ao **objetivo dela** a partir de `memory.md`. Construa o arquivo/pasta para ela, então explique em um parágrafo curto.

---

## 1. Identidade - a alma

**Palavras simples:** Uma nota curta que diz ao OS quem ele é, a quem ele ajuda, e o que ele nunca deve fazer. Tudo o mais parte daqui.

**Analogia:** A descrição de cargo e a personalidade que você daria a um assistente novo no primeiro dia.

**Pergunte (escolha 2-3):**
- Em uma frase, para que serve este OS?
- A quem ele serve: só você, seu time, ou seus clientes?
- Qual é uma coisa que ele deve sempre fazer, e uma que ele nunca deve fazer?

**Você constrói:** `CLAUDE.md` nesta pasta. Mantenha enxuto (mire abaixo de 30 linhas). Inclua: quem ele é, a quem serve, o objetivo, 2-3 padrões (como deve se comportar), e 2-3 recusas inegociáveis. Escreva na voz dela, ancorado nas respostas dela.

**Checagem de pronto:** Um estranho conseguiria ler `CLAUDE.md` e descrever corretamente para que serve este OS e uma coisa que ele vai recusar a fazer.

**Erro comum:** Deixar longo e genérico. Corte até doer. Uma identidade inchada confunde o OS.

---

## 2. Substrato / Contexto - os bastidores

**Palavras simples:** Todo o conhecimento real em que o OS roda, reunido num só lugar e enxugado para ser fácil de usar. Esta é a maior camada e a que mais gente pula.

**Analogia:** Você não cozinha uma boa refeição numa cozinha cheia de comida estragada e potes sem etiqueta. Arrume os bastidores primeiro.

**Pergunte (escolha 2-3):**
- Quais fontes guardam o conhecimento de que este OS precisa (documentos, trabalhos passados, sites, especialistas em quem você confia)?
- Se você pudesse fazer uma pergunta difícil a este OS e receber uma ótima resposta, qual seria? (Isso diz o que reunir.)
- Alguma coisa disso é privada ou sensível? (Para mantermos fora de qualquer coisa compartilhada.)

**Você constrói:** uma pasta `substrate/` e um plano para preenchê-la. Use estes caminhos canônicos (para que as auditorias consigam achar):
- `substrate/sources.md` listando de onde o material bruto vai vir,
- `substrate/compendium.md` (a referência destilada que o OS vai de fato ler),
- se útil, `substrate/subject-matter-expertise/` com uma subpasta por fonte.
Ofereça-se para de fato colher e destilar se ela já tiver o material pronto. Anote em `memory.md` o que ainda falta reunir.

**Desidentifique o que ela sinalizou.** Se ela nomeou algum campo como sensível (muitas vezes os próprios nomes ou valores que você fica tentado a escrever no rastreador), não escreva esses valores em `substrate/`, `memory.md`, ou em qualquer outro lugar da pasta. Use uma referência estável que não identifica (iniciais, "Casal A", "Cliente 1") e mantenha o mapeamento para o valor real fora da pasta. Nunca escreva uma nota de sensibilidade que diz que um campo está excluído e depois liste esse campo mesmo assim, essa contradição já é um vazamento. Se uma referência tornasse o OS inutilizável para ela, pergunte antes de escrever valores reais em vez de decidir por ela.

**Checagem de pronto:** `substrate/compendium.md` existe, está organizado em vez de ser uma pilha, e consegue responder **cada parte** da pergunta difícil acima com os dados disponíveis. Se a pergunta tiver mais de uma parte (por exemplo "o que vence em breve E o que eu já estou atrasada") e um dado necessário ainda estiver faltando, a camada está `in progress`, não `solid`. Diga claramente qual parte ela ainda não consegue responder e qual dado resolveria isso.

**Erro comum:** Tentar despejar tudo cru. Destile. Um compêndio pequeno e limpo vale mais que um gigante bagunçado.

---

## 3. Regras & Hooks - as cercas

**Palavras simples:** As linhas preto-no-branco que o OS nunca deve cruzar, mais alguns reflexos automáticos que as reforçam sem que ninguém precise lembrar.

**Analogia:** Uma regra é uma placa que diz "não entre". Um hook é uma porta trancada que fisicamente não consegue abrir. Hooks são mais fortes.

**Pergunte (escolha 2-3):**
- Qual é o pior erro que este OS poderia cometer? (Isso vira uma regra dura.)
- Existe algo que deveria acontecer automaticamente toda vez (um lembrete, uma checagem, um backup)?
- Algum dado privado que nunca deve sair desta pasta ou ser compartilhado?

**Você constrói:** uma pasta `rules/` com `always.md` (restrições que ele deve seguir) e `never.md` (paradas duras), escritas a partir das respostas dela. Se ela nomeou um comportamento automático, anote como um hook a adicionar depois e descreva o que ele guardaria. Se ela tem dados privados, adicione uma regra "nunca commitar ou compartilhar".

**Checagem de pronto:** A resposta do pior-erro está escrita como uma regra-nunca clara, e pelo menos um reflexo automático foi identificado.

**Erro comum:** Regras vagas ("tenha cuidado"). Deixe-as concretas e testáveis ("nunca misturar os números de dois clientes").

---

## 4. Skills - os verbos conquistados

**Palavras simples:** Os trabalhos repetíveis que este OS faz, escritos de forma que aconteçam sempre do mesmo jeito. Você conquista uma skill fazendo o trabalho na mão algumas vezes primeiro, depois capturando os passos.

**Analogia:** Um cartão de receita. Nas primeiras vezes você cozinha no feeling, depois escreve a receita para que qualquer um consiga repetir.

**Pergunte (escolha 2-3):**
- Qual é uma tarefa que você se pega repetindo e gostaria que rodasse sempre igual?
- Me guie por como você faz na mão, passo a passo.
- Como você sabe que ficou bem feito?

**Você constrói:** uma pasta `skills/`, e uma subpasta por skill com um `SKILL.md` simples capturando: quando usar, os passos, e como é "bem feito". Comece com UMA skill, o trabalho mais repetido dela. Diga a ela que uma skill nunca está terminada; ela vai continuar melhorando.

**Checagem de pronto:** Um trabalho real e repetido está escrito como skill com passos claros e uma linha de "como é bem feito".

**Erro comum:** Tentar escrever dez skills de uma vez, ou escrever uma skill para algo que ela nunca fez de verdade na mão. Conquiste primeiro.

---

## 5. Ferramentas / Conexões - os fios pra fora

**Palavras simples:** Como o OS alcança com segurança fontes de dados reais (um banco, uma agenda, uma planilha, um site). Somente-leitura por padrão, sem nada secreto guardado na pasta.

**Analogia:** Uma janela pela qual o OS consegue olhar, não uma chave da casa inteira. Ele pode ler, mas não pode remexer.

**Pergunte (escolha 2-3):**
- De quais fontes externas este OS precisa ler para bater o seu objetivo?
- Para cada uma, ele só precisa olhar (ler), ou também mudar coisas (escrever)?
- Há segredos envolvidos (senhas, chaves)? (Esses nunca vão nesta pasta.)

**Você constrói:** um `tools.md` que lista cada conexão, para que ela serve, e se é somente-leitura ou escrita, mais uma nota de uma linha de "como conectar depois". Para cada fonte, ajude-a a decidir o caminho mais simples: uma skill pronta, um pequeno wrapper de linha de comando, ou um conector já existente. Mantenha todos os segredos fora da pasta.

**Checagem de pronto:** Toda fonte que o objetivo precisa está listada com seu nível de acesso, e nenhum segredo mora na pasta.

**Erro comum:** Ligar acesso de escrita em tudo. O padrão é somente-leitura. Adicione escrita só onde for realmente necessário.

---

## 6. Agentes - papéis com julgamento

**Palavras simples:** Uma skill é um único verbo. Um agente é um trabalhador com um papel que decide quais skills usar e em que ordem, e então roda uma checagem antes de qualquer coisa sair.

**Analogia:** Skills são ferramentas de cozinha. Um agente é o chef que sabe qual ferramenta pegar e prova o prato antes de ele sair da cozinha.

**Pergunte (escolha 2-3):**
- Existe uma rotina recorrente em que você se pega encadeando várias das suas skills na mão?
- O que um "gerente" confiável deste OS checaria antes de deixar o trabalho sair?
- Cada trabalho deveria ser mantido separado (por exemplo, um cliente de cada vez)?

**Você constrói:** uma pasta `agents/` com um `AGENT.md` para o primeiro papel que vale promover: seu trabalho, quais skills ele orquestra, e o passo obrigatório de revisão antes do resultado sair. Só crie um agente para uma rotina que ela de fato faz na mão hoje.

**Checagem de pronto:** Uma rotina orquestrada real está capturada como um agente com um portão de revisão claro.

**Erro comum:** Construir agentes antes de existirem skills, ou construir um agente "faz tudo". Um agente, um papel claro.

---

## Dicas de treino que valem para toda camada

- Comemore cada camada concluída rapidamente, então aponte para a próxima.
- Se ela travar, dê um exemplo concreto a partir do próprio objetivo dela, não um exemplo de livro-texto.
- Se uma camada ainda não se aplica ao objetivo dela, diga isso com honestidade e marque como `not started` com uma nota, em vez de inventar trabalho.
- Mantenha a pasta arrumada conforme avança. A pasta É o OS.
