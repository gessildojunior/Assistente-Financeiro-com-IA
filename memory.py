chat_memory = []

def salvar(msg):
    chat_memory.append(msg)

def obter():
    return chat_memory[-5:]
