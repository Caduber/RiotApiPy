import requests
import json
import customtkinter as ctk



key = "RGAPI-98342377-da5d-4e05-acca-7a9ce8a7ef6b"


def getInvocador(nome, tag):
    # print((requests.get("https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + nome + "/" + tag + "?api_key=" + key)._content))
    conta = (requests.get("https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/" + nome + "/" + tag + "?api_key=" + key)._content).decode("utf-8")
    contaVetor = conta.split("\"")
    return contaVetor[3]

def getPerfil(puuid):

    bruto = (requests.get("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/" + puuid + "?api_key=" + key)._content).decode("utf-8")
    icon = bruto.split(":")
    icon = icon[4].split(",")

    level = bruto.split(":")
    level = level[6].split("}")
    
    return level[0], icon[0]




if __name__ == "__main__": 

    nome = "T1 Cazeus"
    tag = "LNA"
    puuid = getInvocador(nome, tag)

    sobre = getPerfil(puuid)
    nivel = sobre[0]
    icon = sobre[1]

    #teste = getPerfil(puuid)
    #print(teste)


    ##########################

    #Interface:

    app = ctk.CTk()
    app.title("Entradas e Respostas")
    app.geometry("1000x700")

    def criar_respostas():
        # Obtendo os valores das entradas
        nome = entrada1.get()
        tag = entrada2.get()

        resposta1 = f"Nome: {nome}"
        resposta2 = f"Tag: {tag}"
        resposta3 = f"PUUID: {puuid}"
        resposta4 = f"nivel: {nivel}"
        
        # Atualizando os textos dos rótulos
        label_nome.configure(text=resposta1)
        label_tag.configure(text=resposta2)
        label_puuid.configure(text=resposta3)
        label_nivel.configure(text=resposta4)

    # Criando as entradas de texto
    entrada1 = ctk.CTkEntry(app, placeholder_text="Nome de Invocador")
    entrada1.pack(pady=10)

    entrada2 = ctk.CTkEntry(app, placeholder_text="Tag (sem o #)")
    entrada2.pack(pady=10)

    # Criando o botão que atualiza as respostas
    botao = ctk.CTkButton(app, text="Procurar", command=criar_respostas)
    botao.pack(pady=20)

    # Criando os rótulos para exibir as respostas (inicialmente vazios)
    label_nome = ctk.CTkLabel(app, text="")
    label_nome.pack(pady=5)

    label_tag = ctk.CTkLabel(app, text="")
    label_tag.pack(pady=5)

    label_puuid = ctk.CTkLabel(app, text="")
    label_puuid.pack(pady=5)

    label_nivel = ctk.CTkLabel(app, text="")
    label_nivel.pack(pady=10)

    app.mainloop()


    ##########################


