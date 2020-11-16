# classe que representa uma maquia/estacao
class Estacao:
    def __init__(self, id, sending, mesage, p):
        self.id = id
        self.sending = sending
        self.mesage = mesage
        self.p = p
        self.tempoGasto = 0
        self.backoff_value = 0