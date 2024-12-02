import requests

key = "RGAPI-98342377-da5d-4e05-acca-7a9ce8a7ef6b"

nome = "T1 Cazeus"
tag = "LNA"
invocador = ""

invocador = ""

def getInvocador(nome, tag):
    print(requests.get("https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + nome + "/" + tag + "?api_key=" + key)._content)
    invocador = requests.get("https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + nome + "/" + tag + "?api_key=" + key)._content
          

getInvocador(nome, tag)    


# print("https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/T1%20Cazeus/LNA" + "?api_key=" + key)
# print(requests.get("https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/T1%20Cazeus/LNA" + "?api_key=" + key)._content)

