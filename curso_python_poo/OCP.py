class Notificador():
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por MAIL a {self.usuario.email}")
    
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por MAIL a {self.usuario.sms}")
        