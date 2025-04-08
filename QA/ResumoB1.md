# Resumo 1 Bimestre de QA
- [Garantia da Qualidade de Software][Arq1]
- [Processos de desenvolvimento][Arq2]
 
## Qualidade no Desenvolvimento de Software

#### **Histórico da Qualidade**
A evolução do conceito de qualidade reflete mudanças tecnológicas, sociais e econômicas ao longo da história. Vamos explorar os principais marcos mencionados:

- **Antiguidade (Egípcios, há mais de 4 mil anos):** 
  - Os egípcios usavam o "cúbito" (medida baseada no comprimento do braço do faraó) para padronizar construções como as pirâmides. Isso mostra que a qualidade, mesmo na época, estava ligada à consistência e precisão quantitativa. Exemplo: se cada bloco de pedra tivesse um tamanho diferente, a estrutura não seria estável.
  - Esse foi um dos primeiros registros de "controle de qualidade" rudimentar, antes mesmo do termo existir formalmente.

- **Revolução Industrial (século XVIII-XIX):**
  - Com a automação (máquinas a vapor, tear mecânico) e a produção em massa, surgiram indústrias em grande escala. Isso aumentou a concorrência entre empresas, forçando-as a melhorar seus produtos para atrair consumidores.
  - Exemplo: Uma fábrica de tecidos que produzia roupas com defeitos (fios soltos, costuras frágeis) perdia mercado para outra com melhor acabamento. A qualidade passou a ser um diferencial competitivo.

- **Década de 1920:**
  - A produção em massa atingiu um pico, mas verificar cada produto manualmente tornou-se inviável. Isso levou ao surgimento do controle estatístico de qualidade (ex.: amostragem), desenvolvido por Walter Shewhart, que introduziu gráficos de controle para monitorar processos.

- **Década de 1940:**
  - Após a Segunda Guerra Mundial, organizações como a ASQC (American Society for Quality Control), ABNT (Associação Brasileira de Normas Técnicas) e ISO (International Standardization Organization) foram criadas para estabelecer padrões globais de qualidade.
  - No Japão, Kaoru Ishikawa desenvolveu o Diagrama de Ishikawa (ou "espinha de peixe"), uma ferramenta para identificar causas de problemas de qualidade, marcando o início da gestão moderna de qualidade.

- **Década de 1950-1960:**
  - A Lei de Grosch (desempenho do computador proporcional ao quadrado do preço) incentivou a compra de máquinas mais potentes, mas os softwares não acompanharam essa evolução, levando à "crise do software" (1968). Projetos atrasavam, falhavam ou entregavam produtos inutilizáveis.
  - Exemplo: Um sistema bancário que parava de funcionar por erros de cálculo devido à falta de testes adequados.
  - Isso deu origem à Engenharia de Software como disciplina, focada em processos sistemáticos para melhorar a qualidade do software.

- **Evolução (1900-1990):**
  - 1900: Inspeção pós-produção (verificar defeitos após fabricar).
  - 1940: Controle estatístico (prevenir defeitos no processo).
  - 1950: Avaliação do processo (melhorar como o trabalho é feito).
  - 1960: Educação das pessoas (treinar equipes).
  - 1970: Otimização de processos (eficiência e qualidade juntas).
  - 1980: Projeto robusto (qualidade desde o design).
  - 1990: Engenharia simultânea (qualidade na concepção do produto).

**Exemplo prático:** Imagine uma linha de produção de carros. No início (1900), verificavam-se defeitos após a montagem. Hoje, com engenharia simultânea, a qualidade é planejada desde o design, evitando problemas antes da produção.

---

#### **O que é Qualidade?**
O conceito de qualidade varia dependendo da perspectiva. Aqui estão as definições detalhadas e suas implicações:

- **Philip B. Crosby ("Conformidade com os requisitos"):**
  - Qualidade é atender exatamente ao que foi especificado, sem margem para interpretação subjetiva. Foco no processo: se os requisitos dizem "o botão deve ser azul", qualquer outra cor é um defeito.
  - Exemplo: Um aplicativo de delivery deve entregar pedidos em 30 minutos, conforme prometido. Se demorar mais, não tem qualidade, mesmo que o cliente ache o serviço "bom".
  - Limitação: Depende de requisitos bem definidos, o que nem sempre é possível no início de projetos complexos.

- **Joseph M. Juran ("Conveniência para uso"):**
  - Qualidade é atender às expectativas do cliente, incluindo aspectos implícitos não especificados. Foco no resultado e na experiência do usuário.
  - Exemplo: Um celular pode atender aos requisitos técnicos (bateria de 8 horas), mas se o carregador for frágil e quebrar em um mês, não é "conveniente para uso".
  - Parâmetros: Qualidade de projeto (o produto foi bem planejado?) e qualidade de conformidade (foi bem executado?).

- **NBR 8402:**
  - Define qualidade como a capacidade de um produto ou serviço satisfazer necessidades explícitas (requisitos documentados) e implícitas (expectativas não ditas).
  - Exemplo: Um prato de comida deve ser saboroso (explícito) e servido em um ambiente limpo (implícito).

- **Roger S. Pressman (contexto de software):**
  - Qualidade em software envolve:
    1. Conformidade com requisitos funcionais (ex.: o app calcula corretamente o frete).
    2. Conformidade com requisitos de desempenho (ex.: carrega em menos de 2 segundos).
    3. Seguir padrões de desenvolvimento (ex.: código limpo, documentado).
    4. Características implícitas (ex.: interface intuitiva, mesmo sem ser exigida explicitamente).

- **Qualidade Relativa:**
  - Depende do contexto e do público-alvo. Exemplo: Para um carro popular, qualidade pode ser custo-benefício; para um carro de luxo, é desempenho e conforto.
  - Problemas comuns: Especificações mal definidas ou expectativas desalinhadas entre cliente e desenvolvedor.

**Exemplo prático:** Um jogo mobile pode ter gráficos incríveis (conformidade técnica), mas se travar constantemente, não terá qualidade na visão do usuário (conveniência para uso).

---

#### **Garantia da Qualidade no Processo de Desenvolvimento**
A garantia da qualidade (QA) em software visa assegurar que o produto final seja confiável e atenda às expectativas. Vamos detalhar:

- **Definição:**
  - Conjunto de atividades técnicas aplicadas em todas as fases do ciclo de vida do software (análise, design, codificação, teste, manutenção) para atingir níveis de qualidade especificados.
  - Exemplo: Revisão de código (técnica) para evitar bugs antes do teste.

- **Verificação e Validação (V&V):**
  - **Verificação:** "Estamos construindo corretamente o produto?"
    - Foco na consistência interna e na aderência às especificações em cada fase.
    - Exemplo: Revisar se o design do banco de dados segue o diagrama UML definido na análise.
  - **Validação:** "Estamos construindo o produto certo?"
    - Foco na conformidade com os requisitos do cliente no produto final.
    - Exemplo: Testar se o sistema de login aceita senhas conforme o cliente pediu (ex.: mínimo de 8 caracteres).
  - Diferença prática: Verificação evita erros no processo (ex.: código com sintaxe errada); validação evita erros no resultado (ex.: o app não faz o que o cliente queria).

- **Ciclo de Vida e QA:**
  - QA está presente em todas as fases genéricas:
    - **Análise:** Definir requisitos claros e testáveis.
    - **Planejamento:** Estabelecer padrões de qualidade (ex.: tempo de resposta < 1s).
    - **Codificação:** Aplicar boas práticas (ex.: modularidade).
    - **Teste:** Executar casos de teste para verificar e validar.
  - Exemplo: Um bug encontrado na fase de teste pode ser rastreado até um requisito mal escrito na análise, mostrando a importância da QA contínua.

**Exemplo prático:** No desenvolvimento de um app de banco, a verificação checa se o código de transferência segue o padrão de segurança (ex.: criptografia). A validação testa se o cliente consegue transferir dinheiro com facilidade no app final.

---

### **Documento 2: Modelo Tradicional, Manifesto Ágil e Scrum**

#### **Modelo Tradicional (Cascata)**
O modelo Cascata (Waterfall) é uma abordagem linear e sequencial para gestão de projetos, amplamente usada em software desde 1970. Vamos aprofundar:

- **Características Principais:**
  - Fluxo unidirecional: Cada fase (análise, projeto, implementação, verificação, manutenção) é concluída antes da próxima começar.
  - Ênfase em documentação: Tudo é detalhado antes da codificação.
  - Exemplo: Um projeto de 12 meses pode ter 2 meses de análise, 3 de projeto, 5 de implementação, 1 de teste e 1 de lançamento.

- **Fases Detalhadas:**
  1. **Análise e Requisitos:**
     - Coleta de todos os requisitos (funcionais e não funcionais) com stakeholders.
     - Produção de documentos como especificação de requisitos e estudo de viabilidade.
     - Exemplo: Definir que um sistema de vendas deve suportar 100 usuários simultâneos.
  2. **Projeto (Design):**
     - Traduz requisitos em representações técnicas (ex.: diagramas UML, wireframes).
     - Avaliação preliminar da qualidade do design antes da codificação.
     - Exemplo: Criar o layout de uma tela de checkout para um e-commerce.
  3. **Implementação:**
     - Codificação baseada no design, transformando especificações em software executável.
     - Exemplo: Programar o backend de um sistema de reservas em Java.
  4. **Verificação:**
     - Testes estruturais (lógica interna, ex.: cobertura de código) e funcionais (comportamento externo, ex.: botões funcionam?).
     - Revisão pelo cliente para confirmar conformidade.
     - Exemplo: Testar se o login rejeita senhas inválidas.
  5. **Manutenção:**
     - Correção de bugs, adaptação a mudanças (ex.: novas leis) e melhorias pós-entrega.
     - Exemplo: Atualizar um app para suportar uma nova versão do iOS.

- **Benefícios:**
  - Organização: Fácil de gerenciar devido à estrutura rígida.
  - Previsibilidade: Cronogramas e custos são estimados no início.
  - Documentação robusta: Útil para projetos regulados (ex.: sistemas médicos).

- **Problemas:**
  - Inflexibilidade: Não permite voltar a fases anteriores sem reiniciar o projeto.
  - Entrega tardia: O cliente só vê o software funcionando no final.
  - Risco de requisitos errados: Mudanças no meio do projeto são difíceis de acomodar.
  - Exemplo: Um cliente percebe que quer uma funcionalidade extra na fase de teste, mas isso atrasa tudo.

**Exemplo prático:** Desenvolver um sistema de folha de pagamento com Cascata exige definir todos os cálculos (salário, impostos) na análise. Se o cliente mudar as regras tributárias na implementação, o projeto pode atrasar meses.

---

#### **Manifesto Ágil**
O Manifesto Ágil (2001) surgiu como resposta às limitações do Cascata, propondo uma abordagem mais flexível e colaborativa.

- **História:**
  - Em 2001, 17 especialistas em desenvolvimento de software se reuniram em Utah, EUA, para criar um modelo alternativo ao tradicional. Resultado: o Manifesto Ágil, com 4 valores e 12 princípios.
  - Contexto: Frustração com projetos longos, caros e que muitas vezes falhavam (ex.: crise do software revisitada).

- **Quatro Valores:**
  1. **Indivíduos e interações > processos e ferramentas:**
     - Pessoas motivadas e comunicação direta são mais valiosas que processos rígidos.
     - Exemplo: Uma reunião rápida entre desenvolvedores resolve um bug mais rápido que seguir um manual de 50 páginas.
  2. **Software funcionando > documentação abrangente:**
     - Entregar algo utilizável é prioritário; documentação é secundária.
     - Exemplo: Um protótipo funcional de um app é mais útil que um relatório de 100 páginas sobre ele.
  3. **Colaboração com o cliente > negociação de contratos:**
     - Trabalhar junto ao cliente para ajustar o produto é melhor que discutir cláusulas contratuais.
     - Exemplo: Mostrar versões intermediárias ao cliente evita surpresas no final.
  4. **Responder a mudanças > seguir um plano:**
     - Adaptabilidade é essencial, já que requisitos mudam.
     - Exemplo: Um app de delivery adiciona uma funcionalidade de rastreamento em tempo real após feedback, mesmo no meio do projeto.

- **Doze Princípios (Resumo Detalhado):**
  1. Satisfazer o cliente com entregas contínuas e valiosas.
  2. Aceitar mudanças de requisitos, mesmo tardiamente.
  3. Entregar software funcional frequentemente (semanas ou meses).
  4. Colaboração diária entre desenvolvedores e negócio.
  5. Construir projetos com indivíduos motivados e suporte adequado.
  6. Comunicação face a face como método mais eficaz.
  7. Software funcionando como medida de progresso.
  8. Promover desenvolvimento sustentável (ritmo constante).
  9. Excelência técnica e bom design aumentam a agilidade.
  10. Simplicidade (fazer o necessário, evitar excessos).
  11. Equipes auto-organizáveis criam as melhores soluções.
  12. Reflexão regular para melhorar processos.

**Exemplo prático:** Um time ágil desenvolvendo um site de notícias entrega uma versão básica em 2 semanas (notícias estáticas), ajusta com base no feedback (adiciona busca) e refina continuamente, ao invés de planejar tudo por 6 meses.

---

#### **Framework Scrum**
Scrum é um framework ágil que organiza o desenvolvimento em ciclos curtos (sprints) para entregar valor incrementalmente.

- **História:**
  - Inspirado no rugby ("scrum" = formação ordenada), foi criado por Jeff Sutherland e Ken Schwaber em 1986 para projetos de manufatura e adaptado para software.
  - Foco em autonomia e entregas priorizadas.

- **Componentes Principais:**
  - **Artefatos:**
    1. **Product Backlog:** Lista viva de requisitos priorizados pelo Product Owner (ex.: "adicionar login com Google").
    2. **Sprint Backlog:** Tarefas selecionadas para uma sprint (ex.: "codificar tela de login").
    3. **Incremento:** Produto funcional entregue ao final da sprint.
    - Exemplo: Um app de tarefas tem um Product Backlog com 20 itens; 5 são escolhidos para uma sprint de 2 semanas.
  - **Papéis:**
    1. **Product Owner:** Define o "o quê" (prioridades), representando o cliente.
    2. **Scrum Master:** Facilita o processo, remove obstáculos, mas não gerencia o time.
    3. **Development Team:** Equipe auto-organizável que executa o trabalho (codifica, testa).
    - Exemplo: O Product Owner decide que "notificações" são prioridade; o Scrum Master resolve um bloqueio técnico; o time implementa.
  - **Cerimônias:**
    1. **Sprint Planning:** Planejamento do que será feito na sprint (ex.: 8 horas para definir tarefas).
    2. **Daily Scrum:** Reunião diária de 15 minutos para alinhamento (ex.: "O que fiz ontem? O que farei hoje?").
    3. **Sprint Review:** Demonstração do incremento ao cliente (ex.: mostrar um novo recurso).
    4. **Sprint Retrospective:** Reflexão sobre o processo (ex.: "Como melhorar a comunicação?").
    - Duração típica de sprint: 2-4 semanas.

- **Definition of Done (DoD):**
  - Critérios para considerar um item concluído (ex.: "testado, documentado, sem bugs críticos").
  - Exemplo: Um recurso só é "done" se passou por code review e testes de regressão.

- **Vantagens:**
  - Entregas frequentes permitem ajustes rápidos.
  - Priorização garante que o mais importante seja feito primeiro.
  - Exemplo: Um sistema de e-commerce entrega o carrinho de compras em 2 semanas, ajustando o design com base no feedback.

- **Limitações:**
  - Depende de equipes disciplinadas e auto-gerenciáveis.
  - Pode ser caótico sem um Product Owner claro ou com mudanças excessivas.

**Exemplo prático:** Um time Scrum desenvolve um app de notas. Na sprint 1, entrega a criação de notas; na sprint 2, adiciona sincronização na nuvem, ajustando conforme o feedback do cliente.

[Arq1]: https://github.com/pedcravo/CC5mb/blob/main/QA/2%20-%20Garantia%20da%20Qualidade%20de%20Software.pdf
[Arq2]: https://github.com/pedcravo/CC5mb/blob/main/QA/1%20-%20Processo%20de%20Desenvolvimento%20-%20Cascata%20-%20Manifesto%20-%20Agil%20(1).pdf
