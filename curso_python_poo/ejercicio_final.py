"""from textblob import TextBlob


class AnalizadorDeSentimientos:
    def analizar_sentimiento(self,texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "positivo"
        elif analisis.sentiment.polarity == 0:
            return "neutral"
        else: 
            return "negativo"
        
analizador = AnalizadorDeSentimientos()

resultado = analizador.analizar_sentimiento("hello, im bad")

print(resultado)"""

import openai 

openai.api_key = ""

system_rol = '''hace de cuenta que sos un analizaador de sentimientos.
               Yo te paso sentimientos y vos analizas el sentimiento de los mensajes
               y medas una respuesta con al menos 1 caracter y como maximo 4 caracteres
               SOLO RESPUESTAS NUMERICAS. donde -1 es negatividad maxima, 0 neutras y 1 es positividad maxima
               (puedes responder solo con ints o floats)'''

mensajes = [{"role": "system", "content": system_rol}]

class AnalizadorDeSentimientos:
    def analizador_sentimiento(self, polaridad):
        if polaridad > -0.6 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo" + "\x1b[1;37m"  
        elif polaridad > -0.3 and polaridad < -0.1:
            return "\x1b[1;31m" + "Algo Negativo" + "\x1b[1;37m"  
        elif polaridad >= -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[1;37m"  
        elif polaridad >= 0.1 and polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo positivo" + "\x1b[1;37m"  
        elif polaridad >= 0.4 and polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo"+ "\x1b[1;37m"  
        elif polaridad >  0.9:
            return "\x1b[1;32m" + "muy positivo"   + "\x1b[1;37m"  
        else:
            return  "\x1b[1;31m" + "muy negativo"   + "\x1b[1;37m"  
        


analizador = AnalizadorDeSentimientos()

while True:
    user_promt = input( "\x1b[1;33m" + "\nDecime Algo: " +  "\x1b[1;37m")
    mensajes.append({"role": "user","content": user_promt})

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        menssages = mensajes,
        max_tokens = 8
    )
    respuesta = completion.choices[0].message["content"]
    mensajes.append({"role": "assistant", "content": respuesta})

    sentimiento = analizador.analizador_sentimiento(float(respuesta))