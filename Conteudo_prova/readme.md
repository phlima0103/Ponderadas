# Conteúdos da Prova

## Programação

### BPMN (Business Process Model and Notation)

#### O que é BPMN?
BPMN é uma notação gráfica que permite modelar processos de negócios de maneira clara e padronizada. Sua estrutura facilita a comunicação entre diferentes perfis dentro de uma organização, como gestores, analistas de negócios e desenvolvedores.

#### Elementos principais do BPMN:
- **Eventos**: representados por círculos, indicam o que inicia ou termina um processo.
  - Exemplo: "Pedido recebido".
- **Atividades**: representadas por retângulos, descrevem as tarefas executadas no processo.
  - Exemplo: "Verificar estoque".
- **Gateways**: representados por losangos, são pontos de decisão no processo, permitindo caminhos alternativos.
  - Exemplo: "Estoque disponível?".
- **Fluxos**: setas que conectam eventos, atividades e gateways, mostrando a sequência de execução.

#### Exemplo de Aplicação:
Imagine um e-commerce que deseja mapear o fluxo de processamento de pedidos. O BPMN permite descrever visualmente todas as etapas, desde o momento em que o pedido é recebido até a expedição do produto ao cliente, incluindo decisões como a verificação de estoque e o pagamento aprovado.

#### Pontos importantes:
- **Pools e Lanes**: são usados para representar diferentes atores ou departamentos em um processo.
- **Subprocessos**: permitem que atividades complexas sejam detalhadas em processos menores.
- **Notação padrão**: facilita a comunicação entre membros técnicos e não técnicos da empresa.

---

### DMN (Decision Model and Notation)

#### O que é DMN?
DMN é uma notação complementar ao BPMN usada para modelar decisões empresariais. Enquanto o BPMN foca nos fluxos de trabalho, o DMN detalha como as decisões são tomadas, especialmente quando envolvem regras complexas.

#### Elementos principais do DMN:
- **Tabelas de Decisão**: principal ferramenta de DMN, usadas para definir regras e condições que orientam uma decisão.
  - Exemplo: Conceder empréstimo com base em idade e renda do cliente.
- **Input Data**: dados de entrada para a tomada de decisão.
  - Exemplo: "Renda mensal do cliente".
- **Decisão**: o resultado final com base nas regras estabelecidas.

#### Exemplo de Aplicação:
Uma empresa financeira pode usar DMN para decidir se um cliente está qualificado para um empréstimo. As regras podem envolver a verificação da renda, histórico de crédito e dívidas atuais.

#### Pontos importantes:
- **Tabelas de Decisão**: são o coração do DMN, permitindo descrever regras de forma clara.
- **Integração com BPMN**: facilita a automatização de decisões dentro de processos maiores.
- **Foco em lógica de negócios**: o DMN é voltado para decisões baseadas em regras, permitindo que as decisões sejam transparentes e facilmente revisáveis.

---

### Entidade e Relacionamento (ER)

#### O que é Entidade e Relacionamento?
O Modelo Entidade-Relacionamento (MER) é uma técnica usada para modelar dados em sistemas de banco de dados. Ele permite a visualização e organização dos dados através de entidades e seus relacionamentos.

#### Elementos principais do Modelo ER:
- **Entidades**: representam objetos ou conceitos do mundo real.
  - Exemplo: "Cliente", "Produto".
- **Atributos**: detalhes ou características das entidades.
  - Exemplo: "Nome do cliente", "Preço do produto".
- **Relacionamentos**: conectam as entidades e definem como elas interagem.
  - Exemplo: "Cliente faz pedido", "Produto faz parte de pedido".

#### Exemplo de Aplicação:
Em um sistema de gestão de alunos, as entidades "Aluno", "Curso" e "Professor" podem ser conectadas por relacionamentos que indicam que o aluno está matriculado em um curso, e que o curso é ministrado por um professor.

#### Pontos importantes:
- **Chaves Primárias**: identificam unicamente cada instância de uma entidade.
- **Chaves Estrangeiras**: conectam entidades através de relacionamentos.
- **Cardinalidade**: define a quantidade de relacionamentos entre entidades (ex.: 1:N, N:N).

---

### ERPs em Geral

#### O que são ERPs?
ERP (Enterprise Resource Planning) é um sistema que integra os processos centrais de uma organização em uma única plataforma, permitindo a automação e a centralização de dados de diferentes departamentos.

#### Funcionalidades dos ERPs:
- **Gestão de Vendas**: integra pedidos de clientes, emissão de faturas e entregas.
- **Controle de Estoque**: gerencia níveis de estoque em tempo real, controlando a entrada e saída de produtos.
- **Gestão Financeira**: facilita o controle de despesas, receitas e balanços financeiros.

#### Exemplo de Aplicação:
Uma fábrica pode usar um ERP para monitorar seu estoque, controlar ordens de produção e gerenciar suas finanças. Todas essas funções estão conectadas, permitindo uma visão completa do desempenho da empresa.

#### Pontos importantes:
- **Integração**: ERPs integram dados de vendas, finanças, estoque e outros departamentos.
- **Visibilidade e Controle**: gestores podem monitorar e tomar decisões informadas em tempo real.
- **Eficiência**: ao centralizar informações e automatizar processos, o ERP melhora a eficiência operacional.

---

## Negócios

### Balanço Patrimonial

#### O que é Balanço Patrimonial?
O Balanço Patrimonial é um demonstrativo financeiro que apresenta a posição patrimonial e financeira de uma empresa em um determinado momento, dividida entre **Ativos**, **Passivos** e **Patrimônio Líquido**.

#### Estrutura do Balanço Patrimonial:
- **Ativos**: são os bens e direitos da empresa.
  - Exemplo: Caixa, Imóveis, Contas a Receber.
- **Passivos**: são as obrigações e dívidas da empresa.
  - Exemplo: Empréstimos, Fornecedores.
- **Patrimônio Líquido**: é a diferença entre os ativos e passivos, representando o valor líquido pertencente aos proprietários da empresa.

#### Exemplo de Aplicação:
Uma empresa lista seus ativos, como imóveis, equipamentos e caixa. Ao mesmo tempo, lista seus passivos, como empréstimos bancários e contas a pagar. O patrimônio líquido reflete o valor que os acionistas possuem após a dedução dos passivos.

#### Pontos importantes:
- **Equação fundamental**: Ativos = Passivos + Patrimônio Líquido.
- **Classificação de ativos**: em circulantes e não circulantes.
- **Importância**: auxilia na análise da solvência da empresa, determinando se ela possui mais bens do que dívidas.

---

### DRE (Demonstração do Resultado do Exercício)

#### O que é DRE?
A DRE é um relatório financeiro que demonstra o desempenho da empresa ao longo de um período específico, mostrando suas receitas, custos e o resultado final (lucro ou prejuízo).

#### Estrutura da DRE:
- **Receita Líquida**: receita total menos devoluções e impostos.
- **Custo de Vendas**: custo diretamente associado à produção dos bens ou serviços vendidos.
- **Despesas Operacionais**: despesas que não estão diretamente ligadas à produção, como salários e marketing.
- **Lucro ou Prejuízo Líquido**: resultado final após dedução de todos os custos e despesas.

#### Exemplo de Aplicação:
Uma empresa usa a DRE para verificar se as suas vendas no último trimestre foram suficientes para cobrir os custos de produção e gerar lucro. A análise da DRE também pode revelar onde a empresa está gastando mais do que o planejado.

#### Pontos importantes:
- **Margem de lucro**: a DRE ajuda a calcular a margem de lucro da empresa.
- **Comparação de períodos**: permite avaliar o desempenho em diferentes períodos (trimestre a trimestre, ano a ano).
- **Decisões estratégicas**: as informações da DRE são essenciais para ajustar preços, controlar custos e reavaliar investimentos.

---

### EBITDA (Earnings Before Interest, Taxes, Depreciation, and Amortization)

#### O que é EBITDA?
O EBITDA é uma métrica que mede o desempenho operacional de uma empresa antes da dedução de juros, impostos, depreciação e amortização. Ele é amplamente usado para comparar empresas de diferentes setores ou países, pois elimina os efeitos das decisões de financiamento e políticas fiscais.

#### Cálculo do EBITDA:
- **Fórmula**: EBITDA = Lucro Operacional + Depreciação + Amortização.

#### Exemplo de Aplicação:
Duas empresas podem ser comparadas pelo seu EBITDA, mesmo que uma delas tenha uma dívida maior ou esteja em um país com uma carga tributária diferente. Isso porque o EBITDA foca apenas na performance operacional.

#### Pontos importantes:
- **Comparação entre empresas**: o EBITDA é útil para comparar empresas com diferentes estruturas de capital.
- **Foco em operações**: exclui fatores financeiros e contábeis, dando uma visão mais clara do desempenho operacional.
- **Indicador de eficiência**: empresas com EBITDA elevado costumam ser mais eficientes na gestão de suas operações.

---

### ROI (Return on Investment)

#### O que é ROI?
O ROI é uma métrica que mede a eficiência de um investimento, mostrando o retorno gerado em relação ao valor investido.

#### Cálculo do ROI:
- **Fórmula**: ROI = (Ganho do Investimento - Custo do Investimento) / Custo do Investimento.

#### Exemplo de Aplicação:
Uma empresa investe R$ 50.000 em uma campanha de marketing e gera R$ 70.000 em vendas adicionais. O ROI seria de 40%, indicando que o retorno sobre o valor investido foi positivo.

#### Pontos importantes:
- **Avaliação de investimentos**: o ROI é usado para avaliar a rentabilidade de projetos, campanhas ou qualquer outro tipo de investimento.
- **Decisões estratégicas**: com base no ROI, uma empresa pode decidir continuar investindo em um projeto ou alocar recursos de maneira diferente.
- **Benchmarking**: o ROI pode ser comparado entre diferentes investimentos para determinar quais são mais lucrativos.

---

## Matemática

### Juros Compostos

#### O que são Juros Compostos?
Os juros compostos são calculados sobre o valor inicial e também sobre os juros acumulados em períodos anteriores. Isso significa que os juros vão crescendo conforme o tempo passa, aumentando o montante final.

#### Fórmula dos Juros Compostos:
- **Fórmula**: \( M = P(1 + i)^n \)
  - \( M \): montante final.
  - \( P \): capital inicial.
  - \( i \): taxa de juros por período.
  - \( n \): número de períodos.

#### Exemplo de Aplicação:
Se você investir R$1.000 a uma taxa de 5% ao ano durante 3 anos, o montante final seria \( M = 1000(1 + 0,05)^3 \), resultando em aproximadamente R$ 1.157,63.

#### Pontos importantes:
- **Efeito do tempo**: quanto mais tempo o capital ficar investido, maior será o impacto dos juros compostos.
- **Aplicação prática**: investimentos financeiros, financiamentos, cartões de crédito, etc.

---

### Entropia

#### O que é Entropia?
Na teoria da informação, entropia é uma medida de incerteza ou imprevisibilidade associada a uma variável aleatória. Quanto maior a entropia, maior a incerteza e a quantidade de informação necessária para descrever o sistema.

#### Fórmula da Entropia:
- **Fórmula**: \( H(X) = - \sum p(x) \log_2 p(x) \)
  - \( H(X) \): entropia da variável \( X \).
  - \( p(x) \): probabilidade de um determinado evento \( x \).

#### Exemplo de Aplicação:
Na compressão de dados, a entropia mede a quantidade de informação contida em uma mensagem. Se uma mensagem contém muitos símbolos repetidos, sua entropia é baixa, pois há pouca incerteza. Se a mensagem contém símbolos diversos e sem padrão, a entropia é alta.

#### Pontos importantes:
- **Entropia e compressão de dados**: quanto menor a entropia de uma mensagem, mais eficiente é a compressão de dados.
- **Incerteza**: maior entropia implica maior incerteza ou desordem no sistema.

---

### Redes de Petri

#### O que são Redes de Petri?
Redes de Petri são uma ferramenta gráfica utilizada para modelar sistemas distribuídos, como fluxos de trabalho, sistemas de controle e automação. Elas permitem representar estados e transições em um sistema de forma clara e visual.

#### Componentes principais das Redes de Petri:
- **Lugares (Places)**: representam os estados do sistema.
  - Exemplo: "Máquina ociosa", "Pedido em espera".
- **Transições**: representam as mudanças de estado.
  - Exemplo: "Iniciar produção".
- **Tokens**: indicam o estado atual do sistema, movendo-se entre lugares conforme as transições ocorrem.

#### Exemplo de Aplicação:
Uma rede de Petri pode ser usada para modelar o fluxo de produção em uma fábrica, onde as máquinas alternam entre estados de ociosidade e produção conforme os pedidos são recebidos e processados.

#### Pontos importantes:
- **Modelagem de sistemas distribuídos**: amplamente usada em automação e controle de processos.
- **Análise de comportamento**: permite analisar se um sistema pode atingir um estado específico ou se há gargalos no processo.
