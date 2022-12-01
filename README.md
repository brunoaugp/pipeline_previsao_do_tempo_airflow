# Pipeline Para Coleta Semanal de Dados da Previsão do Tempo através de API e utilizando Apache Airflow 

>Projeto realizado juntamente com o Curso da Alura:  _Apache Airflow: orquestrando seu primeiro pipeline de dados_

O seguinte projeto tem como finalidade a coleta periódica da previsão do tempo para uma Empresa de Turismo (fictícia) que oferece seus serviços de acordo com as previsões de cada cidade.

Através do pipeline é realizada a coleta dos dados previsão do tempo semanalmente utilizando a API do site: ["Visual Crossing: Weather Data & API"](
https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/ "Link da documentação da API")


Com o código Python _"dados_climaticos.py"_, gera-se uma pasta datada semanalmente com os seguintes arquivos csv (orquestração realizada pelo Apache Airflow):

* **dados_brutos**: Coleta de todos os dados meteorológicos disponíveis para a cidade escolhida dos 8 dias posteriores à data da execução da DAG.
* **condicoes**: Coleta da descrição da previsão do tempo dos 8 dias posteriores à data da execução da DAG.
* **temperatura**: Coleta dos dados de temperatura mínima, média e máxima dos 8 dias posteriores à data da execução da DAG.


## Exemplo de Uso

Para o projeto foi utilizada como cidade alvo a cidade do Rio de Janeiro e feita a coleta dos dados da previsão do tempo do dia 28/11/2022 até o dia 05/12/2022.

## Arquivos do projeto

Encontram-se na pasta do projeto:
* Script Python do pipeline de coleta de dados (pasta "dags")
* Arquivos "condicoes.csv", "dados_brutos.csv" e "temperatura.csv" com os dados meteorológicos da cidade do Rio de Janeiro para o período de 28/11/2022 à 05/12/2022.


-----------------------------
## Meta

Bruno Augusto --- [Linkedin](https://www.linkedin.com/in/brunoaugp/) --- brunoaugp@hotmail.com

Link do Curso:  https://cursos.alura.com.br/course/apache-airflow-primeiro-pipeline-dados


<https://github.com/brunoaugp>


