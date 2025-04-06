# Resumo cap 2 - Automatos finitos
---

## **Visão Geral do Capítulo 2: Autómatos Finitos**

Os dois documentos abordam o tema dos **autómatos finitos** como modelos formais para processar cadeias e reconhecer linguagens, com foco em **aceitadores determinísticos (DFA)**, **aceitadores não determinísticos (NFA)**, **linguagens regulares** e **transdutores (Mealy e Moore)**. Eles exploram definições formais, exemplos práticos, construções de autómatos e relações entre esses conceitos, além de aplicações como busca de texto e projeto de circuitos lógicos. Vamos unificar essas ideias em uma explicação coesa.

---

## **1. Introdução aos Autómatos Finitos**

Os autómatos finitos são máquinas abstratas com um número finito de estados, usadas para resolver o problema: *dada uma cadeia de caracteres, ela pertence a uma linguagem específica?* Eles são os modelos mais simples na hierarquia de autómatos, adequados para reconhecer **linguagens regulares**, que veremos mais adiante.

- **Componentes Básicos**:
  - **Entrada**: Uma cadeia sobre um alfabeto \(\Sigma\).
  - **Estados**: Um conjunto finito \(Q\).
  - **Estado Inicial**: \(q_0 \in Q\).
  - **Função de Transição**: Define como o autômato muda de estado ao ler símbolos.
  - **Saída**: Pode ser aceitação (em aceitadores) ou uma cadeia (em transdutores).

- **Tipos**:
  - **Aceitadores**: Decidem se uma cadeia pertence a uma linguagem (DFA e NFA).
  - **Transdutores**: Produzem uma saída a partir da entrada (Mealy e Moore).

---

## **2. Aceitadores Determinísticos (DFA)**

### **2.1 Definição Formal**
Um **DFA** (Deterministic Finite Accepter) é definido por um quinteto:
\[ M = (Q, \Sigma, \delta, q_0, F) \]
- \(Q\): Conjunto finito de estados.
- \(\Sigma\): Alfabeto de entrada.
- \(\delta: Q \times \Sigma \to Q\): Função de transição (total, ou seja, definida para todo par estado-símbolo).
- \(q_0 \in Q\): Estado inicial.
- \(F \subseteq Q\): Conjunto de estados finais (aceitadores).

O DFA é **determinístico** porque, para cada estado e símbolo de entrada, há exatamente um próximo estado.

### **2.2 Representação por Grafo**
- **Vértices**: Estados (círculo simples para normais, seta para inicial, duplo círculo para aceitador).
- **Arestas**: Transições etiquetadas com símbolos de \(\Sigma\).

**Exemplo**: Um DFA que aceita cadeias em \(\Sigma = \{0, 1\}\) terminadas em 1:
- \(Q = \{q_0, q_1\}\), \(q_0\) inicial, \(F = \{q_1\}\).
- \(\delta(q_0, 0) = q_0\), \(\delta(q_0, 1) = q_1\), \(\delta(q_1, 0) = q_0\), \(\delta(q_1, 1) = q_1\).
- Aceita: "01", "11", rejeita: "00", "10".

### **2.3 Função de Transição Estendida (\(\delta^*\))**
Para processar cadeias inteiras, define-se:
\[ \delta^*: Q \times \Sigma^* \to Q \]
- Recursivamente:
  - \(\delta^*(q, \lambda) = q\) (cadeia vazia mantém o estado).
  - \(\delta^*(q, wa) = \delta(\delta^*(q, w), a)\), para \(w \in \Sigma^*\), \(a \in \Sigma\).
- Exemplo: Para o DFA acima, \(\delta^*(q_0, 01) = \delta(\delta^*(q_0, 0), 1) = \delta(q_0, 1) = q_1\).

### **2.4 Linguagem Aceita**
A linguagem \(L(M)\) de um DFA é:
\[ L(M) = \{ w \in \Sigma^* \mid \delta^*(q_0, w) \in F \} \]
- Exemplo: O DFA anterior aceita \(L = \{ w \in \{0, 1\}^* \mid w \text{ termina em 1} \}\).

### **2.5 Construção de DFAs**
Construir um DFA requer identificar os estados necessários para "memorizar" a propriedade da linguagem:
- **Exemplo**: Cadeias com número ímpar de 1s em \(\Sigma = \{0, 1\}\):
  - Estados: \(P\) (par), \(I\) (ímpar, aceitador).
  - Transições: \(\delta(P, 0) = P\), \(\delta(P, 1) = I\), \(\delta(I, 0) = I\), \(\delta(I, 1) = P\).
  - \(q_0 = P\), \(F = \{I\}\).

---

## **3. Linguagens Regulares**

### **3.1 Definição**
Uma linguagem é **regular** se existe um DFA que a aceita:
\[ L = L(M) \]
- Exemplos: \(\{w \in \{0, 1\}^* \mid w \text{ termina em 00}\}\), \(\{a^n b^m \mid n, m \geq 0\}\).

### **3.2 Propriedades**
- Fechadas sob união, concatenação, complemento e fecho de Kleene (detalhes em capítulos futuros).
- Complemento de \(L(M)\): \(\text{Compl}(L(M)) = \{ w \in \Sigma^* \mid \delta^*(q_0, w) \notin F \}\), obtido trocando \(F\) por \(Q - F\).

---

## **4. Aceitadores Não Determinísticos (NFA)**

### **4.1 Definição Formal**
Um **NFA** (Nondeterministic Finite Accepter) é:
\[ M = (Q, \Sigma, \delta, q_0, F) \]
- \(\delta: Q \times (\Sigma \cup \{\lambda\}) \to 2^Q\): Retorna um conjunto de estados (não determinístico).
- Pode ter transições \(\lambda\) (sem consumir entrada).

### **4.2 Diferenças em Relação ao DFA**
- Múltiplas transições possíveis para um símbolo.
- Transições \(\lambda\) permitidas.
- \(\delta(q, a)\) pode ser vazio (\(\emptyset\)).

### **4.3 Linguagem Aceita**
\[ L(M) = \{ w \in \Sigma^* \mid \delta^*(q_0, w) \cap F \neq \emptyset \} \]
- \(\delta^*(q, w)\): Conjunto de estados alcançáveis após ler \(w\).
- Aceita se pelo menos um caminho leva a um estado final.

**Exemplo**: NFA para cadeias com "000" em \(\Sigma = \{0, 1\}\):
- \(Q = \{q_0, q_1, q_2, q_3\}\), \(q_0\) inicial, \(F = \{q_3\}\).
- \(\delta(q_0, 0) = \{q_0, q_1\}\), \(\delta(q_0, 1) = \{q_0\}\), \(\delta(q_1, 0) = \{q_2\}\), \(\delta(q_2, 0) = \{q_3\}\), etc.

---

## **5. Equivalência entre DFA e NFA**

- **Teorema**: Toda linguagem aceita por um NFA é aceita por um DFA equivalente.
- **Construção**:
  - Estados do DFA são subconjuntos de \(Q\) do NFA (método de subconjuntos).
  - Exemplo: Para o NFA acima, o DFA tem estados como \(\{q_0\}\), \(\{q_0, q_1\}\), etc., com transições calculadas.

---

## **6. Redução de Estados em DFAs**

- **Objetivo**: Minimizar o número de estados sem alterar \(L(M)\).
- **Método**:
  - Identificar estados indistinguíveis (mesmo comportamento para todas as entradas).
  - Exemplo: DFA com estados repetidos pode ser simplificado agrupando estados equivalentes.

---

## **7. Autómatos Transdutores**

### **7.1 Máquinas de Mealy**
- Definição: \(M = (Q, \Sigma, \Lambda, \delta, \gamma, q_0)\)
  - \(\Lambda\): Alfabeto de saída.
  - \(\gamma: Q \times \Sigma \to \Lambda\): Saída depende do estado e da entrada.
- **Exemplo**: Deslocamento à direita (entrada "101" → saída "λ10").

### **7.2 Máquinas de Moore**
- Definição: \(M = (Q, \Sigma, \Lambda, \delta, \gamma, q_0)\)
  - \(\gamma: Q \to \Lambda\): Saída depende apenas do estado.
- **Exemplo**: Similar ao Mealy, mas com mais estados.

### **7.3 Equivalência**
- Mealy e Moore são interconvertíveis, com Moore geralmente requerendo mais estados.

### **7.4 Aplicação**
- Usadas em circuitos lógicos (Mealy assíncrono, Moore síncrono).

---

## **8. Aplicações Práticas**

- **Busca de Texto**: NFAs reconhecem palavras-chave (ex.: "chave"), convertidos em DFAs para eficiência.
- **Circuitos Lógicos**: Transdutores modelam sistemas com entrada/saída.

---
