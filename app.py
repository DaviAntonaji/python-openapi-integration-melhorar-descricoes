import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("APIKEY")

descricao = "Casa térrea com aproximadamente 880,52 m². E com as seguintes características: 1 Área(s) de lazer com piscina e churrasqueira. 1 Área(s) de serviço. 1 Banheiro(s). 1 Cozinha(s) com armário. 1 Dependência de empregada. 1 Despensa(s). 1 Dormitório(s) com armário. 1 Escritório(s). 10 Garagem(ns) com cobertura. Itens de segurança como cerca elétrica. 1 Jardim(ins) de inverno. 1 Lavabo(s). 1 Sala(s) de estar. 1 Sala(s) de jantar. 1 Sala(s) de Tv. 1 Sala(s) de visita. 1 Copa. 4 Suíte(s). 1 Sala(s) de visita."

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f'Q:Melhore a seguinte descrição sem dizer que ela foi melhorada: "{descricao}" A:',
    temperature=0,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
)
answer = response.choices[0].text.strip()
print(answer)
