# **ENTENDIMENTO DO NEGÓCIO**

## **QUAL É A EMPRESA?**

A Rossmann é uma das maiores redes de drogarias da Europa, com cerca de 56.200 funcionários e mais de 4.000 lojas. Em 2019, a Rossmann teve um faturamento de mais de € 10 bilhões na Alemanha, Polônia, Hungria, República Tcheca, Turquia, Albânia, Kosovo e Espanha.

## **QUAL É O MODELO DE NEGÓCIO?**

A Rossmann é uma das maiores redes de drogarias da Europa, operando mais de 4.000 drogarias em 8 países. Sua gama de produtos inclui até 21.700 itens e pode variar dependendo do tamanho da loja e da localização. Além de produtos de drogaria com foco em pele, cabelo, corpo, bebê e saúde, a Rossmann também oferece itens promocionais ("Mundo das Ideias"), pet food, serviço de fotos e uma ampla variedade de alimentos e vinhos naturais. Existe também uma gama de perfumes com cerca de 200 marcas comerciais.

## **QUAL É O PROBLEMA DE NEGÓCIO?**

Os gerentes de loja da Rossmann precisam de previsões diárias de vendas com até seis semanas de antecedência para planejar os investimentos em infraestrutura em suas lojas (as vendas nas próximas seis semanas serão altas o suficiente para equilibrar o investimento em infraestrutura?).

# **ENTENDIMENTO DO PROBLEMA**

## **QUAL O DESAFIO QUE ESTE PROJETO VISA SUPERAR?**

Produzir um modelo que seja capaz de prever o faturamento das próximas seis semanas para cada loja da rede.

**Referências:**

https://www.kaggle.com/c/rossmann-store-sales

https://en.wikipedia.org/wiki/Rossmann_(company)

# **BUSINESS ASSUMPTIONS**

**HYPOTHESIS**

In order to make predictions for the next six weeks, Rossmann company has to provide data about its stores for this time interval. Such data, for each store, must include: store model, store assortment level and if the given store will be on continuous promotion.

**Referências:**

https://www.kaggle.com/c/rossmann-store-sales


# **CICLO DO PROJETO**

![crisp-ds](references/crisp.png)

## Step 00. Settings and Data Extraction
* Importação das bibliotecas, pacotes e funções necessárias.
* Carregamento e verificação dos dados disponíveis através de um arquivo CSV.

## Step 01. Data Description:
* Renomeação das colunas e verificação do tamanho do dataset (avaliar a necessidade de ferramentas para tratar grande volume de dados).
* Verificação dos tipos de dados em cada coluna e mudanças de tipo que se façam necessárias para melhor tratamento pelos algoritmos posteriormente.
* Verificação de dados faltantes e decisão de como tratá-los (remoção, reamostragem artificial, inviabilidade da solução).
* Breve descrição estatística dos atributos numéricos e categóricos a fim de detectar anomalias que fogem do escopo do problema, bem como a presença de possíveis outliers que irão impactar a performance dos algoritmos posteriormente.

## Step 02. Feature Engineering:
* Levantamento de uma lista de hipóteses de negócio.
* Criação de variáveis (features) relevantes para a resolução do problema.

## Step 03. Data Filtering:
* Filtragem de linhas e deleção de colunas que não contém informações relevantes para a modelagem ou não ajudam a resolver o problema.

## Step 04. Exploratory Data Analysis:
* Análise isolada de cada feature e sua relação com as demais.
* Exploração dos dados a fim de validar hipóteses de negócio e obter insights a respeito do negócio.

## Step 05. Data Preparation:
* Preparação dos dados a fim de ajudar os modelos de machine-learning a aprenderem e performarem com maior facilidade. Aqui são feitas Normalização, Reescala e Transformação dos dados.

## Step 06. Feature Selection:
* Separação dos dados em treino e validação.
* Seleção das features mais relevantes para treinar os modelos. Aqui se usam algoritmos de seleção de features como o Boruta.

## Step 07. Machine Learning Modelling:
* Teste de diferentes modelos de Machine Learning.
* Seleção do modelo que apresenta melhor performance com base em métricas apropriadas que mitigam os erros.

## Step 08. Hyperparameter Fine Tuning:
* Escolha dos melhores valores para cada parâmetro do modelo escolhido que maximizam a sua performance.

## Step 09. Performance Evaluation and Interpretation:
* Comparação entre as previsões dadas pelo modelo e os dados de validação (avaliação da sua capacidade de aprendizado) a fim de detectar desvios de comportamento (overfitting e underfitting)
* Teste do Modelo treinado com dados equivalentes aos dados de produção (avaliação da sua capacidade de generalização) e conversão da performance do modelo em resultados de negócios (financeiros)

## Step 10. Deployment:
* Criação da API (Application Programming Interface) para disponibilizar previsões em solicitações de internet. A API ficará hospedada num servidor na nuvem.(Heroku)
* Em seguida, para o usuário final, criar um bot do Telegram onde o usuário digita o número da loja e o bot responde com a previsão de vendas dessa determinada loja nas próximas seis semanas.

# **TOP 3 INSIGHTS**

## H2. Lojas com competidores mais próximos deveriam vender menos.

> Falsa: Lojas com COMPETIDORES MAIS PRÓXIMOS vendem MAIS.

![h2_hypothesis](references/h2_hypothesis.png)

**INSIGHT**: a existência de competidores próximos parece estimular o consumo, talvez pelo fato de que os clientes prefiram comprar em regiões onde há mais opções de lojas e a oferta de produtos é maior.

## H6. Lojas com mais promoções consecutivas deveriam vender mais.

> Falsa: Lojas com MAIS PROMOÇÕES CONSECUTIVAS vendem MENOS.

![h6_hypothesis](references/h6_hypothesis.png)

**INSIGHT**: o prolongamento de promoções parece causar um efeito negativo na percepção de valor dos produtos pelos clientes.  

## - H7. Lojas abertas durante o feriado de Natal deveriam vender mais do que nos demais feriados.

> Falsa:  Lojas abertas NO FERIADO DE NATAL vendem MENOS do que nos demais feriados.

![h7_hypothesis](references/h7_hypothesis.png)

**INSIGHT**: o tipo de assortment das lojas parece não influenciar o consumo dos clientes durante o feriado natalino.

# **MACHINE LEARNING RESULTS**

> Após o treinamento de alguns modelos de ML, foi feita uma avaliação comparativa entre os modelos com base nas métricas de estimativas de erros escolhidas para este problema de regressão. As métricas foram o MAE (Mean Absolute Error), o MAPE (Mean Absolute Percentage Error) e o RMSE (Root Mean Square Error).

![ml_results](references/ml_results.png)

> Decidindo pelo uso do modelo de XGBoost, devido sua performance ser razoavelmente semelhante ao modelo mais acurado, mas cujo tamanho que ocupa em armazenamento ser significativamente menor, foi feito um processo de refinamento dos seus parâmetros (Fine Tuning) a fim de melhorar um pouco mais a sua performance (diminuir os erros de suas previsões)

![model_tunned](references/model_tunned.png)

> Pode-se avaliar também a capacidade de aprendizado do modelo ao se aplicá-lo aos dados de validação, acompanhando o quão próximo ele acerta as previsões de lojas que já sabemos o montante faturado mas o modelo ainda não viu os dados. Este processo visa detectar e corrigir pośsiveis problemas com overfitting. Os gráficos abaixo demonstram que o modelo possui um erro percentual médio (MAPE) em torno de 10%, quando ele erra para mais ou para menos do valor real das vendas ao longo das últimas 6 semanas.

![model_fit](references/model_fit.png)


# **BUSINESS RESULTS**

> Os resultados obtidos pelas previsões do modelo escolhido (XGBoost) levam em conta o melhor e o pior cenários, calculados pela variação do erro MAE (Mean Absolute Error). A Tabela a seguir mostra os valores somados de faturamento de todas as lojas previstos para as pŕoximas 6 semanas, considerando o pior cenário (quando o modelo superestima o valor das vendas) e o melhor cenário (quando o modelo subestima o valor das vendas)

| Cenários  |  Valores  |
| --------- | -------- |
|  Predições |  $ 283.951.842,24 |
|  Pior |  $ 283.203.495,28 |
|  Melhor |  $ 284.700.189,21 |


# **BUSINESS SOLUTION**

**A seguinte imgagem explica a arquitetura de deploy utilizada na solução deste problema**

![deployment](references/deploy_rossmann.png)

## **Telegram Bot**

Para tornar as previsões mais simples para o usuário final, foi criado um bot do Telegram para que o usuário só precise digitar o número da loja e o bot responderá rapidamente a previsão de vendas dessa determinada loja nas próximas seis semanas.


# **CONCLUSIONS**

It took me a while to go from the very beginning till the very end of the project (actually, it took me about two weeks).

**Even within just two weeks, we can easily see that Data Science projects could deploy straightforward solutions to support business team decisions, making these decisions not more precise, but also easier**.

# **LESSONS LEARNED**

**How to do an end-to-end Data Science project.**

**How to build a Flask API, data App, Telegram bot and host all of them on Heroku cloud so that the solution is available online.**

**It's important to focus on the business solution and don't get lost in 'playing' different tools.**

**The most important thing is the business solution so, if one tool is not working or if it is taking too much time to implement, find another one that will keep the project pacing forward.**

**On the first project cycle, it's important to keep things simple and not try to get the best solution because this can only be achieved through many project cycles.**

# **NEXT STEPS TO IMPROVE**

**Streamlit**: make App run faster and create more options for the user to further analyse prediction data.

**Telegram Bot**: create more options for the user so, for example, the user could get a chart with sales predictions besides the single value prediction.

**Features**: try different variables, scalers and encodings so that ML performance improves.

**API**: implement data validation on API requests to make it less error-prone and more easily debugged in case of error.

**Machine Learning Models**: test more ML models to find one with better results.

**Code**: review the whole code once more to make it clearer and more efficient (faster and less resource-intensive).
