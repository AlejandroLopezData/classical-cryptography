import os
import sys
import random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from break_caesar import chi_squared, break_caesar
from caesar import encrypt_cesar
from basics import alphabet

#texts, i use gemini LLM to make them, the texts are 2 diferent stories one in ENG and one in ESP
en_text = """
The Architecture of Time and NatureFor centuries, humanity has attempted to categorize, measure, and tame the concept of time. We have built intricate clocks with ticking gears, divided solar cycles into precise calendars, and structured our days around digital alarms. Yet, despite our structural obsession, time remains an elusive, fluid river—one that flows at its own unyielding pace. When we step away from the urban grid and enter the wilderness, the rigid ticks of the clock melt away, replaced by the grand, sweeping rhythms of the natural world.In the heart of an ancient forest, time is measured not in seconds, but in rings within a tree trunk. A towering oak does not rush its growth; it reaches toward the canopy over centuries, surviving fierce winters and scorching summers. Each season leaves a physical imprint, a quiet testament to endurance. The forest floor, blanketed in moss and decaying leaves, acts as a biological archive. Here, the decay of the old directly fuels the birth of the new. This cyclical recycling reminds us that in nature, an ending is rarely a final stop; it is simply a quiet prelude to a fresh beginning.Furthermore, the wildlife inhabiting these spaces operates on an internal, instinctual clock perfectly attuned to the planet's pulse. Birds do not consult maps or calendars to begin their thousands-of-miles migration across continents. Instead, they read subtle shifts in daylight, variations in wind currents, and the invisible magnetic fields of the Earth. Similarly, nocturnal predators emerge precisely as the twilight fades, executing a finely choreographed dance of survival that has repeated for millennia. This seamless integration shows how deeply connected every living organism is to the environment it calls home.When humans immerse themselves in these natural spaces, a psychological shift known as "biophilia" often occurs. Our heart rates slow, our focus sharpens, and the persistent anxiety born of modern hyper-connectivity begins to quiet down. In a world that demands instant responses and constant productivity, standing before a vast mountain range or listening to the rhythmic crash of ocean waves offers a vital perspective. It reminds us that we are not separate from nature, but an intrinsic part of it. Embracing these slower, organic tempos might just be the ultimate antidote to the frantic pace of modern life.
"""
es_text="""
La Biblioteca Invisible: La Memoria en la Era DigitalDurante miles de años, la memoria humana fue el principal cofre del tesoro de nuestra especie. Desde los poetas de la antigua Grecia que memorizaban epopeyas enteras gracias a la rima, hasta los abuelos que transmitían la historia familiar de viva voz, el cerebro era el único archivo disponible. Sin embargo, la llegada del siglo XXI y la expansión de los teléfonos inteligentes han cambiado por completo la forma en que guardamos la información. Hoy en día, no necesitamos recordar un dato; solo necesitamos saber en qué barra de búsqueda encontrarlo.Este fenómeno psicológico se conoce como el "Efecto Google" o amnesia digital. Diversos estudios demuestran que nuestro cerebro tiende a olvidar la información que sabe que está guardada de forma segura en un dispositivo externo. Si sabemos que una dirección, un número de teléfono o una fecha histórica están a un clic de distancia, nuestra mente libera ese espacio para concentrarse en otras tareas. De este modo, los teléfonos se han convertido en una especie de "disco duro externo" para nuestra conciencia, una prótesis cognitiva que aligera nuestra carga mental pero que también debilita el músculo del recuerdo autónomo.No obstante, esta transformación digital no es del todo negativa. Al externalizar los datos puramente fácticos —como los nombres de las capitales del mundo o las fórmulas matemáticas complejas—, el cerebro humano puede redirigir su energía hacia capacidades más complejas. Entre ellas destacan el pensamiento crítico, la creatividad y la resolución de problemas. La verdadera inteligencia ya no se mide por la cantidad de datos que una persona puede recitar de memoria, sino por su habilidad para conectar esos datos dispersos, detectar noticias falsas y construir argumentos sólidos.El verdadero desafío de nuestra era radica en encontrar un equilibrio saludable. Depender por completo de los algoritmos nos vuelve vulnerables a la distracción y reduce nuestra capacidad de concentración profunda, un estado indispensable para el aprendizaje real. Leer un libro en papel sin notificaciones flotantes o forzarnos a recordar una ruta sin activar el navegador satelital son pequeños actos de resistencia mental. Al final del día, la tecnología debe ser una herramienta para expandir nuestras capacidades, no un sustituto que apague la chispa de nuestra propia mente.
"""

def norm(text):
    result = ""
    for ch in text.upper():
        if ch in alphabet:
            result += ch
    return result

leng = [1,5,10,20,30,40,60,100]

def creator(text,l):
    txt = norm(text)
    a = {}
    for n in l:
        start = random.randint(0, len(txt) - n)
        a[n] = txt[start:start + n]
    return a

lista_en = creator(en_text,leng)
lista_es= creator(es_text,leng)


def measure():
    for language, text in [("es", es_text), ("en", en_text),("en",es_text)]:

        print(language.upper())
        print("--------------------")

        for n in leng:
            correct = 0

            for i in range(200):
                txt = creator(text,leng)
                key = random.randint(0, 25)

                encrypted = encrypt_cesar(txt[n], key)
                recovered = break_caesar(encrypted, language)

                if recovered[0] == key:
                    correct += 1

            rate = correct / 200 * 100

            print("length:", n, "correct:", rate, "%")

        print()

if __name__ == "__main__":
    measure()

# we can observe that with a 95% of confidence the text can be broken if has more than 20 letters
# but text of 5 can be too but with a 50% of prob, and txt of 10 with 80.5
# i tested it with more lengths to see how it works in a better perspective