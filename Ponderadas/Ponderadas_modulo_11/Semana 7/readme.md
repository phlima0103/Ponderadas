# Ponderada Semana 7 – Detecção de Fraudes em Cartões de Crédito

**Integrantes:**
- Pedro Henrique
- Kaylane Brito
- Daniel Mendez

## 🎯 Objetivo
O objetivo desta atividade foi analisar um dataset real de transações financeiras e desenvolver um modelo de **detecção de fraudes** utilizando **Redes Neurais com PyTorch**.  

O desafio incluía:  
1. **Exploração dos dados** para identificar padrões e desbalanceamento de classes.  
2. **Preparação do dataset** para treino e validação.  
3. **Construção e treinamento de um modelo supervisionado** para classificação.  
4. **Avaliação de métricas de desempenho** como AUC, matriz de confusão e classification report.  
5. **Visualização da curva de aprendizado** para verificar possíveis sinais de overfitting ou underfitting.  

---

## 📂 Estrutura do Notebook

1. **Importações das bibliotecas**  
   - `pandas`, `numpy` para manipulação de dados.  
   - `seaborn`, `matplotlib` para visualização.  
   - `scikit-learn` para pré-processamento, métricas e balanceamento (SMOTE).  
   - `PyTorch` para definição, treino e avaliação do modelo de deep learning.  
   - Definição de `seed` para reprodutibilidade.  

2. **Carregamento dos dados**  
   - Leitura do dataset `creditcard.csv`.  
   - Inspeção inicial com `.head()`, `.info()`.  
   - Visualização do desbalanceamento das classes (`sns.countplot`).  

3. **Análise Exploratória dos Dados (EDA)**  
   - Estatísticas descritivas (`.describe()`).  
   - Distribuições de `Amount` e `Time`.  
   - Correlação entre variáveis (heatmap).  
   - Identificação de outliers em `Amount` usando Z-Score.  
   - **Insight principal:** dataset é altamente desbalanceado (menos de 1% de fraudes).  

4. **Preparação dos Dados**  
   - Normalização de `Time` e `Amount` com `StandardScaler`.  
   - Criação de sequências temporais para alimentar a LSTM.  
   - Divisão em treino e teste (80/20, estratificado).  
   - Conversão para tensores PyTorch e DataLoader.  

5. **Treinamento do Modelo Base (LSTM)**  
   - Arquitetura inicial:  
     - 2 camadas LSTM com 64 neurônios cada.  
     - Batch Normalization.  
     - Camada densa final com saída sigmoide.  
   - Treinamento com `BCEWithLogitsLoss` e `Adam`.  
   - Registro das perdas e métricas de treino/validação.  

6. **Avaliação do Modelo Base**  
   - Classification Report (Precision, Recall, F1-score).  
   - Matriz de Confusão.  
   - ROC-AUC.  
   - Discussão: o modelo inicial apresentou baixa sensibilidade para fraudes devido ao desbalanceamento.  

7. **Curvas de Aprendizado**  
   - Plotagem do `train_loss` e `val_loss`.  
   - Análise de possíveis sinais de **overfitting** ou **underfitting**.  

8. **Otimização do Modelo**  
   Foram aplicadas as seguintes melhorias:  
   - **SMOTE**: oversampling da classe minoritária para reduzir o desbalanceamento.  
   - **Dropout**: adição de camadas dropout para reduzir overfitting.  
   - **Early Stopping**: monitoramento da validação para interromper o treino quando não houvesse mais ganho.  

9. **Avaliação do Modelo Otimizado**  
   - Reavaliação com as mesmas métricas (Precision, Recall, F1, ROC-AUC).  
   - Melhoria no **Recall** da classe fraude, com redução de falsos negativos.  

10. **Comparação entre Modelos**  
    - Tabela comparando métricas do **modelo base** vs **modelo otimizado**.  
    - Conclusão: o modelo otimizado obteve maior recall e AUC, mostrando-se mais adequado para o problema de negócio, mesmo ao custo de alguns falsos positivos.  

---

## 📊 Resultados
- **Modelo Base:** dificuldade em detectar fraudes devido ao desbalanceamento.  
- **Modelo Otimizado:** maior recall e AUC, atingindo melhor equilíbrio entre precisão e cobertura.  


