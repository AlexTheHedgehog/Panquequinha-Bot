from random import *

prefix = "$"

def handle_response(message: str) -> str:
    p_message = message[1:].lower()

    if p_message.startswith("dado") or p_message.startswith("dice"):
        if len(p_message) > 4 and p_message[4:].strip().isnumeric():
            lados = int(p_message.strip()[4:])
        else:
            lados = 6
        face = str(randint(1, lados))

        print(p_message)
        print(str(lados))

        return f"Você rolou um dado de {lados} lados, que caiu em {face}!"
    
    if p_message.startswith("moeda") or p_message.startswith("coin"):
        moeda = str(choice(["cara", "coroa"]))
        print("Comando $moeda")
        return f"Caiu em {moeda}!"
    
    if p_message.startswith("tabuada") or p_message.startswith("mt"):
        num = int(p_message[p_message.find(' ')+1:])
        msg = f"Tabuada do número {num}:"

        for c in range(1, 10):
            msg += f"\n{num} x {c} = {num*c}"
            print("Comando $tabuada")
        return msg
    
    if p_message.startswith("shipp"):
        p1 = p_message[p_message.find(' '):p_message.rfind(' ') + 1]
        p2 = p_message[p_message.rfind(' '):]
        prob = int(randint(0, 100))

        msg = f':heart: O shipp entre{p1}e{p2} tem {prob}% de chance de dar certo. :heart:'

        if 0 < prob <= 20:
            msg2 = 'Que pena... Parece que esse shipp não vai funcionar muito bem... 💔'
        elif 20 < prob <= 40:
            msg2 = 'Hmmm... esse shipp tem um pouco de potencial... 💙'
        elif 40 < prob <= 70:
            msg2 = 'Eles parecem bem apegados. será que conseguem fazer esse amor crescer? :heart:'
        elif 70 < prob <= 99:
            msg2 = 'Oooh... se eles dessem mais alguns passos... 💝'
        elif prob == 0:
            msg2 = 'Esse casal não tem a mínima chance... 😭'
        else:
            msg2 = '💞 CASAL PERFEITO!!! 💞'

        return f'{msg}\n{msg2}'

    if p_message.startswith("ajuda"):
        return f'''```Prefixo: {prefix}
dice/dado [número] - rola um dado, com o limite sendo o número que você escolher. (ex: $dado 6)
help/ajuda - Mostra a lista de comandos do bot.
info - Mostra as informações do bot.
shipp [nome 1] [nome 2] - Veja a probabilidade do seu shipp preferido!
coin/moeda - Gire uma moeda para ver se cai cara ou coroa.
tabuada/mt [número] - escolha um número para ver a tabuada!```'''

    if p_message.startswith("ajuda"):
        print("Comando $info")
        return "Bot criado para entretenimento por AlexTheHedgehog (aka Daniel Gomes Chaves)."
