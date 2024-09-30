# Lista de Exercícios Resolvidos

## Programação

### BPMN (Business Process Model and Notation)

**Questão 1 - Objetiva:**
Dado o processo de compra de um produto online, qual dos seguintes elementos **não** é um componente do BPMN?
- a) Evento
- b) Atividade
- c) Gateway
- d) Diagrama de fluxo de dados

**Resposta:**
- **Alternativa D - Diagrama de fluxo de dados**. Esse diagrama é usado em outra metodologia de modelagem de sistemas, enquanto os demais elementos são específicos do BPMN.

---

**Questão 2 - Discursiva:**
Descreva um processo de emissão de fatura de um serviço usando os elementos de BPMN, e explique como as "lanes" podem ser usadas nesse contexto.

**Resposta:**
Um processo de emissão de fatura pode começar com um evento inicial, que é a solicitação de um serviço pelo cliente. A seguir, uma atividade "gerar fatura" é realizada pelo sistema financeiro. Em um gateway, verifica-se se o pagamento foi processado; se sim, o processo é concluído com um evento "fatura emitida". Caso contrário, o cliente é notificado para tentar novamente.

As "lanes" podem ser usadas para separar as responsabilidades entre o sistema financeiro (responsável pela emissão) e o cliente (responsável pelo pagamento). Isso deixa claro qual ator realiza cada parte do processo.

---

### DMN (Decision Model and Notation)

**Questão 1 - Objetiva:**
Qual das seguintes opções representa corretamente uma função do DMN?
- a) Definir fluxos de trabalho automatizados.
- b) Modelar decisões baseadas em regras.
- c) Criar entidades em banco de dados.
- d) Controlar a execução de atividades humanas.

**Resposta:**
- **Alternativa B - Modelar decisões baseadas em regras**. O DMN é utilizado para representar e automatizar decisões empresariais.

---

**Questão 2 - Discursiva:**
Explique como a DMN pode ser usada para automatizar a decisão de concessão de crédito em um banco e quais seriam os principais critérios usados.

**Resposta:**
A DMN pode ser usada para automatizar a decisão de concessão de crédito com base em critérios pré-definidos. Um banco pode usar uma tabela de decisão DMN com variáveis como "renda", "histórico de crédito", "valor solicitado" e "prazo de pagamento". O DMN analisaria esses fatores e aplicaria regras para determinar se o crédito deve ser aprovado, rejeitado ou submetido a revisão manual. Por exemplo, um cliente com histórico de crédito ruim e renda baixa pode ter seu pedido automaticamente rejeitado.

---

### Entidade e Relacionamento

**Questão 1 - Objetiva:**
Qual é o **tipo de relacionamento** que descreve uma relação onde cada instância de uma entidade A está associada a múltiplas instâncias de uma entidade B, e vice-versa?
- a) Um para um
- b) Um para muitos
- c) Muitos para muitos
- d) Nenhum dos anteriores

**Resposta:**
- **Alternativa C - Muitos para muitos**. Esse relacionamento indica que várias instâncias de A podem estar associadas a várias instâncias de B.

---

**Questão 2 - Discursiva:**
Explique, com um exemplo, como um relacionamento "muitos para muitos" pode ser modelado em um diagrama de entidade-relacionamento, e como ele seria implementado em um banco de dados.

**Resposta:**
Um relacionamento "muitos para muitos" ocorre quando várias instâncias de uma entidade podem se relacionar com várias instâncias de outra. Um exemplo comum é a relação entre "Alunos" e "Cursos". Um aluno pode se matricular em vários cursos, e um curso pode ter vários alunos.

Para implementar isso em um banco de dados relacional, uma tabela intermediária, chamada "tabela de junção", é criada. Essa tabela conteria as chaves primárias de "Alunos" e "Cursos" para associar um aluno a um curso. A tabela de junção permite que os relacionamentos sejam rastreados sem redundância de dados.

---

### ERPs em geral

**Questão 1 - Objetiva:**
Qual das seguintes áreas empresariais **não** costuma ser diretamente coberta por um sistema ERP?
- a) Finanças
- b) Recursos Humanos
- c) Operações de Marketing Digital
- d) Vendas

**Resposta:**
- **Alternativa C - Operações de Marketing Digital**. Sistemas de ERP tipicamente não incluem marketing digital, que é gerido por sistemas de marketing especializados.

---

**Questão 2 - Discursiva:**
Explique como um sistema ERP pode melhorar a eficiência de uma empresa, usando como exemplo a integração entre os módulos de vendas e estoque.

**Resposta:**
Um sistema ERP melhora a eficiência ao integrar diferentes áreas da empresa. No exemplo de vendas e estoque, quando uma venda é realizada no módulo de vendas, o ERP automaticamente atualiza o módulo de estoque, reduzindo a quantidade disponível em tempo real. Isso evita erros manuais e fornece uma visão clara da disponibilidade de produtos. Além disso, o ERP pode gerar pedidos de compra automaticamente quando o estoque atinge níveis críticos, agilizando o reabastecimento e garantindo que a empresa nunca fique sem produtos.

---

## Negócios

### Balanço Patrimonial

**Questão 1 - Objetiva:**
No balanço patrimonial, qual dos itens a seguir **não** faz parte do ativo?
- a) Caixa
- b) Estoque
- c) Fornecedores
- d) Contas a receber

**Resposta:**
- **Alternativa C - Fornecedores**. Fornecedores estão listados no passivo, pois representam obrigações (dívidas a pagar).

---

**Questão 2 - Discursiva:**
Explique como o balanço patrimonial reflete a saúde financeira de uma empresa, destacando a relação entre ativo, passivo e patrimônio líquido.

**Resposta:**
O balanço patrimonial reflete a saúde financeira de uma empresa ao listar seus ativos (bens e direitos), passivos (obrigações) e patrimônio líquido (diferença entre ativos e passivos). A equação básica é: **Ativo = Passivo + Patrimônio Líquido**. Se a empresa tem mais ativos do que passivos, seu patrimônio líquido é positivo, indicando uma boa saúde financeira. No entanto, se os passivos superam os ativos, o patrimônio líquido é negativo, sugerindo que a empresa pode enfrentar dificuldades para honrar suas dívidas.

---

### DRE (Demonstração do Resultado do Exercício)

**Questão 1 - Objetiva:**
Em uma DRE, qual das opções a seguir **não** é considerada uma despesa operacional?
- a) Aluguel
- b) Salários
- c) Juros sobre empréstimos
- d) Materiais de escritório

**Resposta:**
- **Alternativa C - Juros sobre empréstimos**. Juros sobre empréstimos são despesas financeiras, não operacionais.

---

**Questão 2 - Discursiva:**
Explique a importância da DRE para avaliar a performance de uma empresa e como ela difere do balanço patrimonial.

**Resposta:**
A DRE é fundamental para avaliar a performance de uma empresa ao mostrar se ela está gerando lucro ou prejuízo em um período específico. Ela detalha as receitas, custos de vendas e despesas operacionais, resultando no lucro líquido. Diferentemente do balanço patrimonial, que mostra a posição financeira em um dado momento, a DRE reflete o desempenho ao longo do tempo, permitindo avaliar a eficiência das operações e a rentabilidade do negócio.

---

### EBITDA

**Questão 1 - Objetiva:**
O EBITDA mede o desempenho operacional de uma empresa, **excluindo** os seguintes fatores:
- a) Despesas com juros
- b) Depreciação e amortização
- c) Impostos
- d) Todas as anteriores

**Resposta:**
- **Alternativa D - Todas as anteriores**. O EBITDA exclui juros, impostos, depreciação e amortização para focar no desempenho operacional.

---

**Questão 2 - Discursiva:**
Discuta como o EBITDA pode ser utilizado para comparar empresas de diferentes setores e por que ele pode ser considerado um indicador limitado.

**Resposta:**
O EBITDA é útil para comparar empresas de diferentes setores porque exclui despesas financeiras e fiscais, que podem variar muito entre empresas com estruturas de capital distintas. Isso permite que analistas avaliem a lucratividade operacional de forma mais objetiva. No entanto, ele é limitado porque não considera itens importantes como investimentos em capital (CAPEX) e custos com dívida, o que pode distorcer a percepção da saúde financeira de uma empresa.

---

### ROI

**Questão 1 - Objetiva:**
Se uma empresa investe R$50.000 em um projeto e obtém um retorno de R$70.000, qual é o ROI?
- a) 20%
- b) 30%
- c) 40%
- d) 50%

**Resposta:**
- **Alternativa C - 40%**. O ROI é calculado da seguinte forma: \( \frac{70.000 - 50.000}{50.000} = 0,40 \) ou 40%.

---

### ROI

**Questão 2 - Discursiva:**
Uma empresa investiu R$150.000 na construção de uma nova sede e, após 2 anos de operação, gerou um retorno adicional de R$250.000. Construa o cálculo do ROI com base nesses dados e explique a interpretação do resultado.

**Resposta:**
O ROI é calculado da seguinte forma:

\[
ROI = \frac{\text{Retorno do investimento} - \text{Custo do investimento}}{\text{Custo do investimento}} \times 100
\]

Substituindo os valores fornecidos:

\[
ROI = \frac{250.000 - 150.000}{150.000} \times 100
\]

\[
ROI = \frac{100.000}{150.000} \times 100 = 0,6667 \times 100 = 66,67\%
\]

Portanto, o ROI da construção da nova sede foi de **66,67%**. Isso significa que, para cada real investido, a empresa obteve um retorno adicional de R$0,67 ao longo dos dois anos. Esse é um indicador positivo, pois o retorno supera significativamente o valor do investimento inicial.

---

## Matemática

### Juros Compostos

**Questão 1 - Objetiva:**
Se você investe R$10.000 a uma taxa de juros compostos de 5% ao ano, qual será o valor acumulado após 3 anos?
- a) R$11.576,25
- b) R$11.500,00
- c) R$11.760,25
- d) R$11.682,50

**Resposta:**
A fórmula para calcular o montante com juros compostos é:

\[
M = P \times (1 + i)^n
\]

Onde:
- \(M\) é o montante final
- \(P\) é o principal (R$10.000)
- \(i\) é a taxa de juros (5% ou 0,05)
- \(n\) é o número de períodos (3 anos)

Substituindo os valores:

\[
M = 10.000 \times (1 + 0,05)^3 = 10.000 \times (1,157625) = 11.576,25
\]

Logo, a resposta correta é **a) R$11.576,25**.

---

**Questão 2 - Discursiva:**
Explique como o conceito de juros compostos pode ser aplicado no planejamento de um investimento de longo prazo. Se uma pessoa deseja ter R$20.000 em 5 anos com uma taxa de juros de 6% ao ano, quanto ela deve investir hoje?

**Resposta:**
A fórmula dos juros compostos é:

\[
M = P \times (1 + i)^n
\]

No planejamento de longo prazo, os juros compostos são vantajosos porque permitem que o dinheiro cresça de forma exponencial ao longo do tempo. Para saber quanto investir hoje (P) para atingir R$20.000 em 5 anos, com uma taxa de 6% ao ano, usamos a fórmula inversa:

\[
P = \frac{M}{(1 + i)^n}
\]

Substituindo os valores:

\[
P = \frac{20.000}{(1 + 0,06)^5} = \frac{20.000}{1,338225} = 14.944,31
\]

Portanto, a pessoa deve investir **R$14.944,31** hoje para ter R$20.000 em 5 anos com uma taxa de juros de 6% ao ano. Esse valor reflete o efeito dos juros compostos, onde o valor principal cresce ao reinvestir os ganhos ao longo do tempo.

---

### Entropia

**Questão 1 - Objetiva:**
Em termos de Teoria da Informação, qual das opções a seguir descreve corretamente o conceito de entropia?
- a) A taxa de crescimento de uma função linear.
- b) A medida de incerteza associada a uma variável aleatória.
- c) A perda de energia em um sistema físico.
- d) A diferença entre as probabilidades de dois eventos independentes.

**Resposta:**
- **Alternativa B - A medida de incerteza associada a uma variável aleatória**. A entropia é uma medida da quantidade de incerteza em uma distribuição de probabilidade, introduzida por Claude Shannon na teoria da informação.

---

**Questão 2 - Discursiva:**
Calcule a entropia de um sistema com duas possíveis mensagens, A e B, cujas probabilidades são \(P(A) = 0,75\) e \(P(B) = 0,25\). Explique a interpretação desse resultado.

**Resposta:**
A fórmula para calcular a entropia \(H(X)\) de uma variável aleatória \(X\) é:

\[
H(X) = - \sum_{i} P(x_i) \log_2 P(x_i)
\]

Substituindo os valores das probabilidades:

\[
H(X) = -[P(A) \log_2 P(A) + P(B) \log_2 P(B)]
\]
\[
H(X) = -[0,75 \log_2 0,75 + 0,25 \log_2 0,25]
\]
\[
H(X) = -[0,75 \times (-0,415) + 0,25 \times (-2)] = 0,311 + 0,5 = 0,811 \, \text{bits}
\]

A entropia de 0,811 bits significa que, em média, para transmitir informações sobre esse sistema, são necessários cerca de 0,811 bits por mensagem. Isso reflete a incerteza associada à escolha de uma das mensagens (A ou B).

---

### Redes de Petri

**Questão 1 - Objetiva:**
Qual das seguintes afirmações **não** é verdadeira em relação às Redes de Petri?
- a) Elas podem modelar sistemas concorrentes.
- b) Utilizam lugares, transições e fichas para representar estados e eventos.
- c) São adequadas apenas para modelar sistemas determinísticos.
- d) Permitem a representação gráfica de fluxos de controle em sistemas distribuídos.

**Resposta:**
- **Alternativa C - São adequadas apenas para modelar sistemas determinísticos**. Redes de Petri podem modelar sistemas não determinísticos, sendo amplamente utilizadas em sistemas concorrentes e distribuídos.

---

**Questão 2 - Discursiva:**
Explique como uma Rede de Petri pode ser utilizada para modelar o funcionamento de um sistema de fila em um banco, considerando diferentes estados como "cliente aguardando", "atendimento iniciado" e "atendimento concluído".

**Resposta:**
Uma Rede de Petri pode modelar o funcionamento de um sistema de fila no banco utilizando os seguintes componentes:
- **Lugares**: representam os estados do sistema, como "cliente aguardando", "atendimento iniciado" e "atendimento concluído".
- **Transições**: representam os eventos que mudam o estado do sistema, como "início do atendimento" e "fim do atendimento".
- **Fichas**: representam os clientes. Uma ficha em "cliente aguardando" significa que há um cliente na fila. Quando a transição "início do atendimento" ocorre, a ficha é movida para o lugar "atendimento iniciado". Após o "fim do atendimento", a ficha se move para "atendimento concluído".

Essa abordagem permite que o banco monitore a quantidade de clientes em cada estágio do processo, identifique gargalos e otimize o fluxo de atendimento. A flexibilidade das Redes de Petri também permite a modelagem de sistemas com múltiplos atendentes, filas paralelas, e eventos de tempo variável, o que aumenta a precisão da simulação do sistema.

---

## Construção do balanço patrimonial

Uma empresa apresentou os seguintes dados financeiros ao final do ano:
- Caixa: R$50.000
- Estoque: R$120.000
- Veículos: R$200.000
- Empréstimos Bancários a pagar: R$80.000
- Fornecedores: R$60.000
- Contas a Receber: R$90.000
- Imóveis: R$400.000
- Salários a Pagar: R$30.000
- Capital Social: R$600.000

Com base nessas informações, construa o Balanço Patrimonial da empresa, classificando corretamente os itens entre Ativos, Passivos e Patrimônio Líquido. Explique como a equação fundamental do balanço é respeitada.

**Resposta:**

### Passo 1: Identificar os Ativos
Ativos representam todos os bens e direitos da empresa. Eles são divididos em **Ativo Circulante** (recursos que serão realizados em curto prazo, até 12 meses) e **Ativo Não Circulante** (recursos de longo prazo, como imobilizado e investimentos).

- **Ativo Circulante:**
  - Caixa: R$50.000
  - Estoque: R$120.000
  - Contas a Receber: R$90.000
  
  **Total do Ativo Circulante: R$260.000**

- **Ativo Não Circulante:**
  - Veículos: R$200.000
  - Imóveis: R$400.000
  
  **Total do Ativo Não Circulante: R$600.000**

**Total de Ativos = R$260.000 (Circulante) + R$600.000 (Não Circulante) = R$860.000**

---

### Passo 2: Identificar os Passivos
Passivos representam as obrigações da empresa. São divididos em **Passivo Circulante** (dívidas que vencem em curto prazo, até 12 meses) e **Passivo Não Circulante** (dívidas de longo prazo).

- **Passivo Circulante:**
  - Empréstimos Bancários a Pagar: R$80.000
  - Fornecedores: R$60.000
  - Salários a Pagar: R$30.000
  
  **Total do Passivo Circulante: R$170.000**

Não há informações sobre Passivo Não Circulante, então não será incluído.

**Total de Passivos = R$170.000**

---

### Passo 3: Identificar o Patrimônio Líquido
O **Patrimônio Líquido** é a diferença entre os Ativos e os Passivos, e inclui o capital social e lucros retidos.

- **Capital Social:**
  - Capital Social: R$690.000
  
  **Total do Patrimônio Líquido = R$690.000**

---

### Passo 4: Montar o Balanço Patrimonial

| **Balanço Patrimonial**       | **Valor (R$)**    |
|-------------------------------|-------------------|
| **Ativos**                     |                   |
| **Ativo Circulante**           |                   |
| Caixa                          | 50.000            |
| Estoque                        | 120.000           |
| Contas a Receber               | 90.000            |
| **Total Ativo Circulante**     | 260.000           |
| **Ativo Não Circulante**       |                   |
| Veículos                       | 200.000           |
| Imóveis                        | 400.000           |
| **Total Ativo Não Circulante** | 600.000           |
| **Total de Ativos**            | 860.000           |
|                               |                   |
| **Passivos**                   |                   |
| **Passivo Circulante**         |                   |
| Empréstimos Bancários a Pagar  | 80.000            |
| Fornecedores                   | 60.000            |
| Salários a Pagar               | 30.000            |
| **Total Passivo Circulante**   | 170.000           |
| **Total de Passivos**          | 170.000           |
|                               |                   |
| **Patrimônio Líquido**         |                   |
| Capital Social                 | 690.000           |
| **Total do Patrimônio Líquido**| 690.000           |
|                               |                   |
| **Total Passivos + PL**        | 860.000           |

---

### Explicação
A equação básica do balanço patrimonial é: 

Ativos = Passivos + Patrimônio Líquido

Neste caso:

860.000 = 170.000 + 690.000
