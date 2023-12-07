# Northwind Project

* Esse é um projeto utilizando dados disponibilizados pela Microsoft de uma empresa fictícia chamada Northwind, envolvida em operações de fretes de produtos.
  
## Modelagem Transacional vs Modelagem Dimensional
* Os dados originais estão totalmente normalizados, sendo a modelagem ideal para bancos de dados transacionais, onde ocorrem diversas operações CRUD (Criar, Ler, Atualizar e Deletar) a todo momento, devido a interação de diversos usuários utilizando a aplicação.
  
<img alt="Northwind normalized schema" src="https://github.com/EduardoPeLima/data_engineering_northwind_project/blob/master/01_northwind_normalized_data/03_northwind_normalized_schema.png">

* Nosso objetivo é o desenvolvimento de uma camada analítica desses dados, portanto a normalização dos dados transacionais não é a melhor abordagem, pois além de ser mais complexa para o entendimento de pessoas não técnicas, apresenta pior desempenho num viés analítico, devido ser constante os cruzamento de tabelas (JOINs). Por exemplo, para analisar por cliente quais categorias de produtos ele já pediu, seria necessário o cruzamento de 5 tabelas: categories, products, order_details, orders e customers, sendo uma operação nada performática.
* Devido isso, iremos desenvolver a partir dos dados transacionais uma modelagem dimensional. O objetivo aqui é desenvolver uma tabela "fato" onde iremos registrar ocorrências de um determinado evento no mundo real, e tabelas de dimensões que permitem "fatiar" a tabela fato diretamente.
  
<img alt="Northwind dimensional schema" src="https://github.com/EduardoPeLima/data_engineering_northwind_project/blob/master/04_aws/04_rds_mysql_northwind_denormalized/project_northwind_dimensional_model.png">

* Agora para analisar o nosso exemplo anterior (quais categorias de produto um cliente já pediu) é necessário o cruzamento de apenas 3 tabelas: dim_products, fact_orders e dim_customers. Além de ser mais performático por precisar de menos cruzamentos de tabelas (JOINs), se torna mais simples o entendimento, mesmo para uma pessoa não técnica.

## Definindo nossa arquitetura
<img alt="Northwind dimensional schema" src="https://github.com/EduardoPeLima/data_engineering_northwind_project/blob/master/04_aws/aws_architecture.png">
