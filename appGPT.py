import requests
import customtkinter as ctk
from PIL import Image
import io

key = "RGAPI-98342377-da5d-4e05-acca-7a9ce8a7ef6b"

def getInvocador(nome, tag):
    response = requests.get(f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{nome}/{tag}?api_key={key}")
    if response.status_code == 200:
        conta = response.json()
        return conta["puuid"]
    else:
        print("Erro ao buscar invocador:", response.status_code)
        return None

def getPerfil(puuid):
    response = requests.get(f"https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}?api_key={key}")
    if response.status_code == 200:
        perfil = response.json()
        level = perfil["summonerLevel"]
        icon = perfil["profileIconId"]
        return level, icon
    else:
        print("Erro ao buscar perfil:", response.status_code)
        return None, None

def get_icon_image(icon_id):
    url = f"https://raw.communitydragon.org/14.23/game/assets/ux/summonericons/profileicon{icon_id}.png"
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(io.BytesIO(response.content))
    else:
        print("Erro ao carregar o ícone:", response.status_code)
        return None

if __name__ == "__main__": 
    # Interface
    app = ctk.CTk()
    app.title("Entradas e Respostas")
    app.geometry("1000x700")

    # Inicialmente vazio
    icon_image_label = ctk.CTkLabel(app, text="")
    icon_image_label.pack(pady=20)

    def criar_respostas():
        nome = entrada1.get()
        tag = entrada2.get()

        puuid = getInvocador(nome, tag)
        if not puuid:
            return
        
        nivel, icon_id = getPerfil(puuid)
        if nivel is None or icon_id is None:
            return
        
        resposta1 = f"Nome: {nome}"
        resposta2 = f"Tag: {tag}"
        resposta3 = f"PUUID: {puuid}"
        resposta4 = f"Nível: {nivel}"
        
        label_nome.configure(text=resposta1)
        label_tag.configure(text=resposta2)
        label_puuid.configure(text=resposta3)
        label_nivel.configure(text=resposta4)

        # Carregar o ícone do invocador
        icon_image = get_icon_image(icon_id)
        if icon_image:
            icon_ctk = ctk.CTkImage(light_image=icon_image, size=(100, 100))
            icon_image_label.configure(image=icon_ctk)
            icon_image_label.image = icon_ctk  # Manter referência para evitar garbage collection

    # Entradas
    entrada1 = ctk.CTkEntry(app, placeholder_text="Nome de Invocador")
    entrada1.pack(pady=10)

    entrada2 = ctk.CTkEntry(app, placeholder_text="Tag (sem o #)")
    entrada2.pack(pady=10)

    # Botão
    botao = ctk.CTkButton(app, text="Procurar", command=criar_respostas)
    botao.pack(pady=20)

    # Rótulos
    label_nome = ctk.CTkLabel(app, text="")
    label_nome.pack(pady=5)

    label_tag = ctk.CTkLabel(app, text="")
    label_tag.pack(pady=5)

    label_puuid = ctk.CTkLabel(app, text="")
    label_puuid.pack(pady=5)

    label_nivel = ctk.CTkLabel(app, text="")
    label_nivel.pack(pady=10)

    app.mainloop()
