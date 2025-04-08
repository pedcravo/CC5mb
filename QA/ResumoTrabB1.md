# **Resumo Organizado dos Trabalhos do 1º Bimestre**

Este resumo organiza os conteúdos fornecidos sobre qualidade em software e gestão de processos, cobrindo modelos e normas como MPS.BR, ISO/IEC 9000, ISO/IEC 9126/14598/SQuaRE, ISO/IEC 12207, ISO/IEC 15504, CMM/CMMI/SCAMPI, ISO/IEC 25000 e TMMi. Todas as anotações foram preservadas e estruturadas para clareza.

## **1. MPS.BR (Melhoria do Processo de Software Brasileiro)**

### **Contexto Histórico**
- **Década de 90**: A indústria de software no Brasil enfrentou dificuldades devido a cortes em educação e P&D, além de uma "não política" industrial/tecnológica, resultando em baixos investimentos em inovação.
- **CMMI na Época**: Era o principal modelo de melhoria de processos, mas caro e voltado ao mercado internacional, inacessível para muitas empresas brasileiras.
- **Criação em 2003**: Softex, Ministério da Ciência e Tecnologia (MCTI) e outras entidades criaram o MPS.BR para aumentar a competitividade das empresas brasileiras, baratear a certificação e melhorar processos, com apoio da "tripla hélice" (academia, governo, indústria).

### **Objetivo**
- Avaliar e aprimorar os processos de desenvolvimento de software, garantindo produtos de maior qualidade, mais eficientes e com menos falhas, especialmente para micro, pequenas e médias empresas (mPMEs).

### **Comparação com o CMMI**
- **Tabela Comparativa**:
  | **Característica**    | **MPS.BR**                     | **CMMI**                        |
  |-----------------------|--------------------------------|---------------------------------|
  | Origem               | Brasil (Softex)               | EUA (SEI - Carnegie Mellon)    |
  | Foco                 | Pequenas e médias empresas    | Empresas de qualquer porte     |
  | Níveis               | 7 (G a A)                     | 5 (1 a 5)                      |
  | Preço                | Mais barato                   | Mais caro                      |
  | Flexibilidade        | Adaptado ao mercado brasileiro| Baseado em padrões internacionais |
  | Certificação         | Mais acessível e rápida       | Mais rigorosa, válida globalmente |
- **Vantagens do MPS.BR**: Mais fácil subir de nível, melhor custo-benefício, compatível com CMMI, aceito em licitações públicas.
- **Desvantagem**: Não é suficiente para competitividade internacional.

### **Funcionamento**
- Baseado em CMMI, ISO/IEC 12207 (ciclo de vida de software) e ISO/IEC 15504 (avaliação de processos).
- Possui 7 níveis de maturidade (G a A), cada um com processos específicos.

### **Processo de Avaliação**
- Realizado por instituições credenciadas pela Softex:
  1. **Planejamento**: Define escopo, prazos e recursos.
  2. **Execução**: Avaliadores analisam documentos, entrevistam equipes e verificam processos.
  3. **Relatório**: Detalha pontos fortes e fracos.
  4. **Certificação**: Se aprovada, a empresa recebe o certificado; se não, ajusta processos e tenta novamente.

### **Benefícios**
- Redução do tempo de desenvolvimento, validação da qualidade, melhoria contínua, otimização de processos, diferenciação competitiva, melhor gestão de projetos, credibilidade com clientes.

### **Desafios e Críticas**
- Custo de treinamento pode ser alto para pequenas empresas.
- Exige compromisso a longo prazo.
- Nem sempre claro como aplicar a diferentes tipos de projetos.

### **Casos de Sucesso**
- Empresas como 7COMm (nível E), Consinco (níveis G e F), BHS (nível F) e Rightway (nível F) implementaram com sucesso.

### **Curiosidades**
- Pode ser usado para serviços e gestão de RH, além de software.
- Nível mais alto atingido até agora: C.

## **2. Família de Normas ISO/IEC 9000/9001/9003**

### **O que é ISO e IEC?**
- **ISO** (Organização Internacional de Normalização): Fundada em 1946, Genebra, desenvolve normas técnicas internacionais. Representada no Brasil pela ABNT.
- **IEC** (Comissão Eletrotécnica Internacional): Fundada em 1906, Genebra, foca em normas para tecnologias elétricas e eletrônicas. Normas ISO/IEC são colaborações.

### **Família ISO/IEC 9000**
- Conjunto de diretrizes para gestão de qualidade, aplicáveis a qualquer organização, visando consistência, satisfação do cliente e melhoria contínua.
- **ISO 9000**: Fundamentos e vocabulário, sem certificação.
- **ISO 9001**: Requisitos para Sistema de Gestão da Qualidade (SGQ), usada em mais de 170 países. Demonstra capacidade de atender requisitos do cliente e regulamentares.
- **ISO 9002**: Cancelada em 2000, integrada à ISO 9001. Focava em produção e instalação, sem design/desenvolvimento.
- **ISO 9003**: Cancelada em 2000, integrada à ISO 9001. Focava em inspeção e testes finais.
- **ISO 9004**: Diretrizes para melhorar desempenho e sucesso sustentado, sem certificação.

### **Certificação ISO 9001**
- Envolve implementação das normas (com consultores) e auditoria por órgão credenciado (ex.: Inmetro). Se aprovada, a empresa recebe o certificado.

### **Evolução das Normas**
- 1987: Primeira edição baseada na BS 5750.
- 1994: Ênfase em ações preventivas.
- 2000: Integração em ISO 9001:2000, foco em processos e melhoria contínua.
- 2008: Clarificações, sem novos requisitos.
- 2015: Estrutura de 10 cláusulas, liderança, pensamento baseado em risco, menos documentação obrigatória.
- 2025 (previsto): Revisão para resiliência, sustentabilidade e digitalização.

### **Princípios da ISO 9001**
1. Orientação ao cliente.
2. Liderança.
3. Compromisso das pessoas.
4. Abordagem por processos.
5. Melhoria.
6. Decisões baseadas em fatos.
7. Gestão de relações.

### **Benefícios**
- Redução de custos, otimização de processos, busca pela qualidade total, melhor relacionamento com clientes, desenvolvimento de colaboradores, reconhecimento internacional.

### **Exemplos**
- Petrobras, Câmara Municipal de Louveira, Multimóveis.


## **3. Normas ISO/IEC 9126, 14598 e SQuaRE (ISO/IEC 25000)**

### **ISO/IEC 9126**
- Define características e métricas de qualidade do software:
  - Funcionalidade, confiabilidade, usabilidade, eficiência, manutenibilidade, portabilidade.
- Foco em aspectos internos (código) e externos (uso).

### **ISO/IEC 14598**
- Detalha o processo de avaliação da qualidade do software, usando métricas da 9126.
- Estabelece como medir e melhorar a qualidade ao longo do desenvolvimento.

### **SQuaRE (ISO/IEC 25000)**
- Integra e expande 9126 e 14598, publicada em 2014.
- **Estrutura**:
  1. **Guia de Qualidade (2500n)**:
     - **ISO/IEC 25000**: Introdução, terminologia, modelos.
     - **ISO/IEC 25001**: Planejamento e gerenciamento.
  2. **Modelo de Qualidade (2501n)**:
     - **ISO/IEC 25010**: 9 características (ex.: adequação funcional, segurança).
     - **ISO/IEC 25012**: 15 características de qualidade de dados (ex.: precisão, completude).
  3. **Medição da Qualidade (2502n)**:
     - **ISO/IEC 25020**: Modelo de referência para medidas.
     - **ISO/IEC 25021 a 25024**: Medidas específicas.
  4. **Requisitos de Qualidade (2503n)**:
     - **ISO/IEC 25030**: Requisitos e recomendações.
  5. **Avaliação da Qualidade (2504n)**:
     - **ISO/IEC 25040**: Processo em 5 etapas (definir, projetar, planejar, executar, concluir).
     - **ISO/IEC 25041 e 25042**: Guias para avaliadores e módulos.
- **Padrões Destaques**:
  - **ISO/IEC 25059**: Extensão para sistemas de IA (transparência, robustez).

### **Comparação**
| **Aspecto**      | **ISO/IEC 9126**               | **ISO/IEC 14598**              | **SQuaRE (ISO/IEC 25000)**    |
|------------------|--------------------------------|--------------------------------|-------------------------------|
| Objetivo         | Define características         | Foca na avaliação              | Processo completo             |
| Foco Principal   | Qualidade interna e externa   | Processo de avaliação          | Qualidade e avaliação         |
| Escopo           | Métricas de qualidade          | Avaliação do desenvolvimento  | Todos os aspectos da qualidade|

### **Benefícios**
- Melhora confiabilidade e segurança, reduz custos de manutenção, garante conformidade internacional.

## **4. ISO/IEC 12207**

### **Introdução e Contexto**
- Publicada em 1995, revisada em 2008 e 2017.
- Padroniza processos do ciclo de vida de software, usada em aviação, saúde, e-commerce, reduzindo riscos e alinhando expectativas.

### **Estrutura**
1. **Aquisição e Fornecimento**:
   - **Aquisição**: Definição de necessidades, seleção de fornecedores, contratos, aceitação.
   - **Fornecimento**: Entrega do software pelo fornecedor.
2. **Desenvolvimento**: Análise de requisitos, design, codificação, integração, testes, liberação.
3. **Operação**: Uso em produção (execução, monitoramento, suporte ao usuário).
4. **Manutenção**: Corretiva (bugs), adaptativa (novas tecnologias), evolutiva (novas funcionalidades).
5. **Processos de Suporte**: Verificação, validação.

### **Exemplos e Aplicações**
- **NHS (2017)**: Falha pelo WannaCry (£92 milhões em prejuízo) mostra a importância de processos robustos.
- **E-commerce**: Integração de sistemas legados com Git e SonarQube, reduzindo conflitos e acelerando entregas.

### **Conclusão**
- Estrutura o ciclo de vida do software, promovendo qualidade desde a aquisição até a manutenção.

## **5. ISO/IEC 15504 (SPICE)**

### **Introdução e Objetivo**
- Surgiu nos anos 1990 para determinar a maturidade dos processos, identificando pontos fracos e oportunidades.
- Usada para certificações e benchmarking.

### **Histórico e Relações**
- Inspirada no CMMI, compatível com ISO/IEC 12207, parcialmente substituída pela ISO/IEC 33000.
- Avalia capacidade dos processos definidos pela 12207.

### **Estrutura**
- Cinco partes: conceitos, modelo de avaliação, guia prático, diretrizes para melhoria, modelo de referência.
- Processos:
  1. **Primários**: Desenvolvimento, aquisição, entrega.
  2. **De Suporte**: Testes, verificação, validação, garantia de qualidade.
  3. **Organizacionais**: Gestão de recursos, melhoria contínua.
  4. **De Gerenciamento**: Planejamento, monitoramento.

### **Níveis de Capacidade**
- 0 (incompleto) a 5 (otimizado).

### **Relação com Testes**
- Padroniza testes, mede eficiência (ex.: cobertura), integra à melhoria contínua.

### **Exemplos**
- **DocPath** (nível 2): Melhorou processos internos.
- **QualitApps** (nível 3): Padronizou procedimentos.

### **Benefícios e Críticas**
- **Benefícios**: Identifica gargalos, reduz defeitos, aumenta confiabilidade.
- **Críticas**: Complexa para pequenas empresas, focada em processos (não resultados), cara.
- **Alternativas**: CMMI v2.0, MPS.BR, ISO/IEC 33000.


## **6. CMM/CMMI e Método de Avaliação SCAMPI**

### **CMM**
- Cinco níveis:
  1. **Inicial**: Caótico, esforço individual.
  2. **Repetível**: Gerenciados, variáveis entre projetos.
  3. **Definido**: Padronizados, documentados.
  4. **Gerenciado Quantitativamente**: Uso de métricas.
  5. **Otimizado**: Melhoria contínua, inovação.

### **CMMI**
- Evolução do CMM, aplicável a:
  - **CMMI-DEV**: Desenvolvimento.
  - **CMMI-ACQ**: Aquisição.
  - **CMMI-SVC**: Serviços.
- Representações:
  - **Por estágios**: 5 níveis.
  - **Contínua**: Processos avaliados de 0 a 5.

### **SCAMPI**
- Método de avaliação:
  - **SCAMPI A**: Formal, certificação.
  - **SCAMPI B**: Diagnóstico.
  - **SCAMPI C**: Exploratório.
- Etapas: Planejamento, preparação, execução, relatório, acompanhamento.

### **Certificações**
- **Individuais**: Associate, Professional, Instructor, Lead Appraiser.
- **Organizacionais**: Níveis 2 a 5 (1 não certificado).

### **Benefícios**
- Melhoria na qualidade, redução de custos, melhor gestão, reconhecimento internacional.

## **7. ISO/IEC 25000 (SQuaRE)**

### **O que é?**
- Substitui ISO/IEC 9126 e 14598, publicada em 2014.
- Framework para especificar, medir e avaliar qualidade de software.

### **Estrutura**
1. **Guia de Qualidade**: ISO/IEC 25000, 25001.
2. **Modelo de Qualidade**: ISO/IEC 25010 (9 características), 25012 (15 características de dados).
3. **Medição da Qualidade**: ISO/IEC 25020 a 25024.
4. **Requisitos de Qualidade**: ISO/IEC 25030.
5. **Avaliação da Qualidade**: ISO/IEC 25040 (5 etapas), 25041, 25042.

### **Padrões Destaques**
- **ISO/IEC 25010**: Adequação funcional, segurança, etc.
- **ISO/IEC 25012**: Precisão, acessibilidade, etc.
- **ISO/IEC 25040**: Processo de avaliação.
- **ISO/IEC 25059**: Extensão para IA (transparência, robustez).

### **Benefícios**
- Melhora confiabilidade, segurança, reduz custos, conformidade internacional.

## **8. TMMi (Test Maturity Model Integration)**

### **O que é?**
- Criado pela TMMi Foundation, inspirado no CMMI, foca em testes de software.
- Objetivo: Avaliar e aprimorar maturidade dos processos de teste.

### **Os 5 Níveis**
1. **Inicial**: Caótico, sem processos definidos.
2. **Gerenciado**: Estratégia organizacional, planos baseados em riscos.
3. **Definido**: Processos padronizados, testes não funcionais.
4. **Medido**: Métricas para desempenho e qualidade.
5. **Otimizado**: Melhoria contínua, prevenção de defeitos.

### **Comparação com CMMI**
| **Característica** | **TMMi**                | **CMMI**                |
|---------------------|-------------------------|-------------------------|
| Foco               | Testes                  | Desenvolvimento geral   |
| Níveis             | 5                       | 5                       |
| Objetivo           | Melhorar testes         | Melhorar processos      |

### **Benefícios**
- Estrutura para evolução dos testes, redução de defeitos, compatibilidade com CMMI.

### **Desafios**
- Alto custo e tempo, rigidez em ambientes ágeis.


## **9. Comparação Geral e Conclusão**
- **MPS.BR**: Melhoria de processos no Brasil, acessível para mPMEs.
- **ISO/IEC 9000**: Gestão de qualidade universal.
- **ISO/IEC 9126/14598/SQuaRE**: Qualidade de produtos de software.
- **ISO/IEC 12207**: Estrutura o ciclo de vida do software.
- **ISO/IEC 15504**: Avalia capacidade dos processos.
- **CMM/CMMI/SCAMPI**: Maturidade organizacional.
- **ISO/IEC 25000**: Framework completo para qualidade de software.
- **TMMi**: Maturidade específica em testes.

**Conclusão**: Esses modelos e normas são complementares, abordando processos, gestão e qualidade do produto para garantir software eficiente e confiável.
