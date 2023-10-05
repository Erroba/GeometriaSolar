import numpy as np
import math
from matplotlib import pyplot as plt

# Calculo de la declinación para un día
initial_dn = 60
declinacion_inicial = 23.45 * math.sin(2 * math.pi * (initial_dn + 284) / 365)

print(f"Declinación en el día {initial_dn}: {declinacion_inicial}")


# Crea la lista de números de 1 a 365
dn = list(range(1, 366))

# Calcular declinación para cada día
declinacion = [23.45 * math.sin(2 * math.pi * (day + 284) / 365) for day in dn]

print(f"Lista de declinaciones: {declinacion}")


# Plot declinación solar todo el año
fig, ax = plt.subplots()
ax.plot(dn, declinacion)
ax.set(title="Sun Declination Over the Year", xlabel="Day Number", ylabel="Declination")
plt.show()

# Coordenadas geograficas en decimal
Latitud = 27.5
Longitud = -109.5

# Calcular el ángulo del amanecer en radianes
amanecer_radianes = math.acos(-math.tan(math.radians(declinacion_inicial)) * math.tan(math.radians(Latitud)))


# Convertir el ángulo del amanecer a grados
amanecer_grados = math.degrees(amanecer_radianes)

print(f"Amanecer Ws en radianes: {amanecer_radianes}")
print(f"Amanecer Ws en grados: {amanecer_grados}")

# Convertir el ángulo del amanecer a horas

amanecer_horas = amanecer_grados/15
print(f"Amanaecer en horas: {amanecer_horas}")

#Calculo de cenit solar

hora_inicial_grados = 60

cenit_solar_radianes = math.acos(math.cos(math.radians(declinacion_inicial))*math.cos(math.radians(hora_inicial_grados))*math.cos(math.radians(Latitud))+math.sin(math.radians(declinacion_inicial))*math.sin(math.radians(Latitud)))

cenit_solar_grados = math.degrees(cenit_solar_radianes)

print(f"Cenit solar en radianes: {cenit_solar_radianes}")
print(f"Cenit solar en grados: {cenit_solar_grados}")

# Cálculo del azimuth solar 

azimuth_inicial = math.atan2(
    -math.sin(math.radians(hora_inicial_grados)),
    math.cos(math.radians(hora_inicial_grados)) * math.tan(math.radians(Latitud)) - math.tan(math.radians(declinacion_inicial))
)

azimuth_inicial = math.degrees(azimuth_inicial)

print(f"Azimuth solar en grados: {azimuth_inicial}")

#Cálculo de corrección de huso horario
huso_horario = -7
huso_horario_grados = huso_horario*15

correccion_huso = Longitud - huso_horario_grados 

#Ecuación del tiempo

M = 2*math.pi*initial_dn/365.24

EoT = 229.18*(-0.0334*math.sin(M)+0.04184*math.sin(2*M+3.5884))

# Hora solar
TO = 13
AOT = 0

w = 15*(TO-AOT-12)+correccion_huso+EoT

print(f"La hora solar en grados para la hora oficial del sitio seleccionado es: {w}")

# Crear una lista de horas a lo largo del día
hours = np.arange(0, 24, 0.5)

days = [17, 45, 74, 105, 135, 161, 199, 230, 261, 292, 347]


# Calcular elevación y azimuth solar para cada hora
elevations = []
azimuths = []

for day in days:
    for hour in hours:
        # Calcular declinación para un día específico
        declinacion1 = 23.45 * math.sin(2 * math.pi * (day + 284) / 365)
        
        #Calcular la ecuación del tiempo para un día 
    
        M = 2*math.pi*day/365.24
    
        EoT = 229.18*(-0.0334*math.sin(M)+0.04184*math.sin(2*M+3.5884))
        
    
        # Calcular hora solar en grados
        w = 15*(hour-AOT-12)+correccion_huso+EoT
    
    
        # Calcular elevación solar
        cenit_solar_radianes = math.acos(
        math.cos(math.radians(declinacion1))*math.cos(math.radians(w))*math.cos(math.radians(Latitud))+math.sin(math.radians(declinacion1))*math.sin(math.radians(Latitud)))
        
        cenit_solar_grados = math.degrees(cenit_solar_radianes)
        
        elevacion_grados = 90 - cenit_solar_grados
        
    
        elevations.append(elevacion_grados)
    
        # Calcular azimuth solar
        azimuth = math.atan2(
        -math.sin(math.radians(w)),
        math.cos(math.radians(w)) * math.tan(math.radians(Latitud)) - math.tan(math.radians(declinacion1))
        )
        
    
        azimuths.append(math.degrees(azimuth))
    
# Plotear la elevación contra el azimuth
plt.figure(figsize=(10, 6))
plt.plot(azimuths, elevations, marker='o')
plt.title('Trayectoria Solar a lo Largo del Día')
plt.xlabel('Azimuth (grados)')
plt.ylabel('Elevación (grados)')
plt.grid(True)
plt.show()


#Radiacion solar en la superficie extraterrestre

B0 = 1367
excentri = 1 + 0.033*math.cos(2*math.pi*initial_dn/365)

teta = -15

B00 = abs(B0*excentri*math.cos(teta))

print(f"La irradiancia extraterrestre con la inclinación {teta} es : {B00}")

#Irradiación extra-atmosférica diaria (W/m2 ) 

B0d = -(24/math.pi)* B0*excentri*(
amanecer_grados*math.sin(math.radians(Latitud))*math.sin(math.radians(declinacion_inicial)) +
math.cos(math.radians(declinacion_inicial))* math.cos(math.radians(Latitud)) * math.sin(math.radians(amanecer_grados)))

print(f"La irradiación extraterrestre diaria es : {B0d}")




