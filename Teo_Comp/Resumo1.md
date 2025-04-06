# Resumo cap 1 e 2
---

## **1. Introdução à Teoria da Computação**
A Teoria da Computação é uma área das Ciências da Computação que estuda as capacidades e limitações dos computadores. Ela se estrutura em torno de três temas centrais:

- **Autómatos**: Modelos abstratos de máquinas que processam informações.
- **Computabilidade**: O que pode ou não ser resolvido por um computador.
- **Complexidade**: A quantidade de recursos (tempo, espaço) necessários para resolver problemas.

Esses temas buscam responder à pergunta: *O que é computável?* Desde os anos 1930, com os trabalhos de Alan Turing, Alonzo Church e outros, a teoria evoluiu para formalizar os conceitos de máquinas e programas, usando modelos matemáticos simples.

---

## **2. Conceitos Básicos: Alfabeto, Cadeias e Linguagens**

### **2.1 Alfabeto**
- **Definição**: Um alfabeto (geralmente denotado por $\(\Sigma\))$ é um conjunto finito e não vazio de símbolos. Esses símbolos podem ser letras, números ou qualquer entidade abstrata.
  - Exemplos:
    - $\(\Sigma = \{a, b\}\)$
    - $\(\Sigma = \{0, 1\}\)$ (alfabeto binário)
    - $\(\Sigma = \{0, 1, 2, \ldots, 9\}\)$ (algarismos árabes)
- **Observação**: Um conjunto infinito (como os números naturais) ou vazio não é considerado um alfabeto válido neste contexto.

### **2.2 Cadeias (ou Palavras)**
- **Definição**: Uma cadeia (ou palavra) é uma sequência finita de símbolos de um alfabeto. Pode ser vazia, denotada por $\(\lambda\)$ ou $\(\varepsilon\)$.
  - Exemplos em $\(\Sigma = \{a, b\}\)$:
    - $\(w = a\)$
    - $\(w = abba\)$
    - $\(w = \lambda\)$ (cadeia vazia, com comprimento $\(|\lambda| = 0\))$
- **Comprimento**: O comprimento de uma cadeia $\(|w|\)$ é o número de símbolos que ela contém. Exemplo: $\(|abba| = 4\)$.
- **Operações**:
  - **Concatenação**: Junta duas cadeias. Se $\(w = ab\)$ e $\(v = cd\)$, então $\(wv = abcd\)$.
    - Propriedades: Associativa $(\(u(vw) = (uv)w\))$ e possui elemento neutro $(\(\lambda w = w \lambda = w\))$.
  - **Potência**: $\(w^n\)$ é a concatenação de $\(w\)$ consigo mesma $\(n\)$ vezes. Exemplo: $\(a^3 = aaa\)$, $\(w^0 = \lambda\)$.
  - **Reversa**: $\(w^R\)$ é $\(w\)$ com a ordem dos símbolos invertida. Exemplo: $\((abba)^R = abba\)$.
- **Prefixo, Sufixo e Subcadeia**:
  - **Prefixo**: Qualquer sequência inicial de $\(w\)$. Exemplo: Para $\(w = abba\)$, prefixos são $\(\{\lambda, a, ab, abb, abba\}\)$.
  - **Sufixo**: Qualquer sequência final de \(w\). Exemplo: Para \(w = abba\), sufixos são \(\{abba, bba, ba, a, \lambda\}\).
  - **Subcadeia**: Qualquer sequência contígua de \(w\). Exemplo: \(bb\) é uma subcadeia de \(abba\).

### **2.3 Linguagem Formal**
- **Definição**: Uma linguagem \(L\) sobre um alfabeto \(\Sigma\) é um conjunto de cadeias formado por símbolos desse alfabeto, ou seja, \(L \subseteq \Sigma^*\), onde \(\Sigma^*\) é o conjunto de todas as cadeias possíveis sobre \(\Sigma\) (inclui \(\lambda\)).
  - \(\Sigma^+\) é \(\Sigma^*\) sem a cadeia vazia: \(\Sigma^+ = \Sigma^* - \{\lambda\}\).
- **Exemplos**:
  - \(\Sigma = \{a, b\}\):
    - \(L = \{a, ab, abb\}\) (finita)
    - \(L = \{a^n b^n \mid n \geq 0\}\) (infinita, como \(\{\lambda, ab, aabb, aaabbb, \ldots\}\))
  - Palíndromos: Cadeias onde \(w = w^R\), como \(\{\lambda, a, b, aa, bb, aba, bab, \ldots\}\).
- **Operações sobre Linguagens**:
  - **União**: \(L_1 \cup L_2 = \{w \mid w \in L_1 \text{ ou } w \in L_2\}\)
  - **Intersecção**: \(L_1 \cap L_2 = \{w \mid w \in L_1 \text{ e } w \in L_2\}\)
  - **Concatenação**: \(L_1 \cdot L_2 = \{uv \mid u \in L_1, v \in L_2\}\)
  - **Complemento**: \(\text{Compl}(L) = \Sigma^* - L\)
  - **Reversa**: \(L^R = \{w^R \mid w \in L\}\)
  - **Fecho Estrela (Kleene Star)**: \(L^* = L^0 \cup L^1 \cup L^2 \cup \ldots\), onde \(L^0 = \{\lambda\}\). Inclui todas as concatenações de zero ou mais cadeias de \(L\).
  - **Fecho Positivo**: \(L^+ = L^1 \cup L^2 \cup \ldots = L^* - \{\lambda\}\) (se \(\lambda \notin L\)).

---

## **3. Gramáticas**
Gramáticas são ferramentas formais para gerar linguagens, superando as limitações da notação de conjuntos ao especificar regras finitas que produzem cadeias (potencialmente infinitas).

### **3.1 Definição**
- Uma gramática \(G\) é um quarteto \(G = (V, T, S, P)\), onde:
  - \(V\): Conjunto finito de variáveis (não-terminais).
  - \(T\): Conjunto finito de símbolos terminais (o alfabeto da linguagem).
  - \(S \in V\): Símbolo inicial (axioma).
  - \(P\): Conjunto finito de produções (regras).
- \(V\) e \(T\) são disjuntos (\(V \cap T = \emptyset\)).

### **3.2 Produções**
- Formato: \(x \rightarrow y\), onde \(x \in (V \cup T)^+\) (não vazio) e \(y \in (V \cup T)^*\) (pode ser vazio).
- Significado: \(x\) é substituído por \(y\) em uma derivação.
- Exemplo: \(S \rightarrow aS\), \(S \rightarrow \lambda\).

### **3.3 Derivação**
- Processo de aplicar produções a partir de \(S\) para gerar cadeias.
  - Notação:
    - \(w \Rightarrow z\): Um passo de derivação.
    - \(w \Rightarrow^* z\): Zero ou mais passos.
  - Exemplo: Para \(G = (\{S\}, \{a, b\}, S, \{S \rightarrow aSb, S \rightarrow \lambda\})\):
    - \(S \Rightarrow aSb \Rightarrow aaSbb \Rightarrow aabb\) (deriva \(aabb\)).

### **3.4 Linguagem Gerada**
- \(L(G) = \{w \in T^* \mid S \Rightarrow^* w\}\): Conjunto de todas as cadeias terminais derivadas de \(S\).
- Exemplo: A gramática acima gera \(L(G) = \{a^n b^n \mid n \geq 0\}\).

### **3.5 Exemplos Práticos**
- **Palíndromos**: \(G = (\{S\}, \{a, b\}, S, \{S \rightarrow aSa, S \rightarrow bSb, S \rightarrow a, S \rightarrow b, S \rightarrow \lambda\})\).
  - Gera: \(\{\lambda, a, b, aa, bb, aba, bab, \ldots\}\).
- **Números Naturais**: \(G = (\{N, D\}, \{0, 1, \ldots, 9\}, N, \{N \rightarrow D, N \rightarrow DN, D \rightarrow 0|1|\ldots|9\})\).
  - Gera: \(\{0, 1, 2, 12, 123, \ldots\}\).

---

## **4. Autómatos**
Autómatos são modelos abstratos de computação que "reconhecem" ou "processam" cadeias de uma linguagem.

### **4.1 Definição Geral**
- Componentes:
  - **Entrada**: Cadeia em um alfabeto.
  - **Unidade de Controle**: Conjunto finito de estados.
  - **Memória**: Pode variar (nenhuma, pilha, fita infinita).
  - **Saída**: Opcional (aceitação ou produção de cadeias).
  - **Função de Transição**: Define como o estado muda com base na entrada e memória.
- Funciona em passos discretos: \(q_{k+1} = f(q_k, s_k, m_k)\).

### **4.2 Tipos**
- **Autómatos Finitos**: Sem memória adicional, apenas estados finitos.
  - Exemplo: Interruptor on-off com estados \(A\) (on) e \(F\) (off).
- **Autómatos de Pilha**: Memória em formato LIFO (last in, first out).
- **Máquinas de Turing**: Memória em fita infinita, lida e escrita em qualquer ordem.
- **Determinísticos vs. Não Determinísticos**:
  - Determinísticos: Um único próximo estado por configuração.
  - Não Determinísticos: Múltiplas possibilidades por configuração.

### **4.3 Exemplo: Porta Automática**
- Alfabeto: \(\{a = 00, b = 01, c = 10, d = 11\}\) (combinações de sensores frontal e traseiro).
- Estados: \(F\) (fechada), \(A\) (aberta).
- Transições:
  - \(F \xrightarrow{c} A\) (abre se alguém está na frente e ninguém atrás).
  - \(A \xrightarrow{a} F\) (fecha se ninguém está presente).
- Uso: Modela controle de sistemas com estados finitos.

---

## **5. Os Três Paradigmas da Computação**
A computação pode ser vista sob três perspectivas inter-relacionadas:

### **5.1 Computação de Funções**
- Calcula valores numéricos.
- Exemplo: \(f(n) = n\)-ésimo número primo (\(f(3) = 5\)).

### **5.2 Reconhecimento de Linguagens**
- Decide se uma cadeia pertence a uma linguagem.
- Exemplo: \(w = aba\) é um palíndromo? (Sim, pois \(w = w^R\)).

### **5.3 Transdução**
- Transforma cadeias (ex.: reverter \(aba \rightarrow aba\)).
- Exemplo: Produzir a saída \(ba\) a partir de \(ab\).

### **5.4 Inter-redutibilidade**
- Os paradigmas são equivalentes:
  - Computação de \(f(5) = 11\) pode ser reduzida a reconhecer se \(101\#1011 \in L\).
  - Reconhecimento de palíndromos pode ser uma função \(\chi(n)\) (1 se \(n\) codifica um palíndromo, 0 caso contrário).

---

## **6. Unificação e Reflexão**
Os materiais convergem em torno de:
- **Linguagens como base**: Tudo começa com alfabetos, cadeias e operações, levando à definição de linguagens formais.
- **Gramáticas como geradoras**: Especificam como cadeias são formadas, conectando-se às linguagens.
- **Autómatos como reconhecedores**: Processam cadeias e decidem sua pertinência a uma linguagem.
- **Paradigmas como visão geral**: Mostram que computação vai além de cálculos numéricos, abrangendo reconhecimento e transformação.

Essa estrutura reflete a interconexão entre os conceitos: uma linguagem pode ser definida por uma gramática e reconhecida por um autômato, unindo teoria e prática.

---
