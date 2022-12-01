from airflow.models import DAG
import pendulum
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.macros import ds_add
from os.path import join
import pandas as pd


with DAG(
    "dados_climaticos",
    start_date=pendulum.datetime(2022, 11, 26, tz="UTC"),
    schedule_interval='0 0 * * 1' #executando toda segunda-feira
    ) as dag:

        tarefa_1 = BashOperator(
            task_id = 'cria_pasta',
            bash_command='mkdir -p "/home/brunoaugp/Documentos/airflow-alura/semana={{data_interval_end.strftime("%Y-%m-%d")}}"'
        )

        def extrai_dados(data_interval_end):

            #definindo localização e configurando URL
            city = 'RiodeJaneiro'
            key = '5RPTFYSVC9MH2NDBNXGJ3VJ9F'

            URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',f'{city}/{data_interval_end}/{ds_add(data_interval_end,7)}?unitGroup=metric&include=days&key={key}&contentType=csv')

            #lendo arquivo csv com pandas
            dados = pd.read_csv(URL)

            #definindo caminho de output
            file_path = f'/home/brunoaugp/Documentos/airflow-alura/semana={data_interval_end}/'

            #salvando dados como csv
            dados.to_csv(file_path+'dados_brutos.csv')
            dados[['datetime','tempmin','temp','tempmax']].to_csv(file_path+'temperatura.csv')
            dados[['datetime','description','icon']].to_csv(file_path+'condicoes.csv')

        tarefa_2 = PythonOperator(
            task_id = 'extrai_dados',
            python_callable = extrai_dados,
            op_kwargs = {'data_interval_end':'{{data_interval_end.strftime("%Y-%m-%d")}}'}
        )

        tarefa_1 >> tarefa_2

