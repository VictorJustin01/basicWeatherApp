import requests

API_Key = "4912514a06afa26de10d3cebaf19ecfe"
cidade = 'Dublin'
url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_Key}&lang=pt_br"

requisicao = requests.get(url)

requisicao_dic = requisicao.json()

descricao = requisicao_dic['weather'][0]['description']
temp = requisicao_dic['main']['temp'] - 273.15

print(cidade,descricao, round(temp,2),'graus')