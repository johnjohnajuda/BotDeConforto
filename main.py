from flask import Flask, render_template, request
import openai

openai.api_key = "SUA_CHAVE_AQUI"

app = Flask(__name__)

mensagem_do_usuario = """
Estou sobrecarregada. Tenho muitas responsabilidades na escola, todos me veem como a melhor, sou representante de sala, a protagonista, e isso está me cansando muito. Quero palavras que tirem essa carga, me confortem, tragam foco e motivação. Escreva como se estivesse cuidando de mim.
"""

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""
    if request.method == "POST":
        resposta = enviar_mensagem(mensagem_do_usuario)
    return render_template("index.html", resposta=resposta)

def enviar_mensagem(mensagem):
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Você é um bot de conforto pessoal, fala com carinho, como uma pessoa que cuida."},
                {"role": "user", "content": mensagem}
            ],
            max_tokens=250
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
