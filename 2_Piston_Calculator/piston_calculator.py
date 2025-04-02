import math

# Input da utente
diametro_mm = float(input("Inserisci l'alesaggio (diametro) in mm: "))
corsa_mm = float(input("Inserisci la corsa (stroke) in mm: "))
pressione_bar = float(input("Inserisci la pressione in bar: "))
massa_robot_kg = float(input("Inserisci la massa del robot in kg: "))

# Conversioni in metri e pascal
corsa_m = corsa_mm / 1000
raggio_m = (diametro_mm / 2) / 1000
pressione_pa = pressione_bar * 100_000

# Calcolo area in m²
area_m2 = math.pi * (raggio_m ** 2)

# Calcolo volume in m³
volume_m3 = area_m2 * corsa_m

# Calcolo forza in Newton
forza_n = pressione_pa * area_m2


accelerazione_m_s2 = forza_n / massa_robot_kg
tempo_spinta = math.sqrt((2 * corsa_m) / accelerazione_m_s2)
impulso = tempo_spinta * forza_n
velocita_finale = accelerazione_m_s2 * tempo_spinta
flusso_m3_s_massimo = area_m2 * velocita_finale


velocita_aria_tubo = 30  # m/s (valore tipico)
diametro_tubo_m = math.sqrt((4 * flusso_m3_s_massimo) / (math.pi * velocita_aria_tubo))
diametro_tubo_mm = diametro_tubo_m * 1000



# Output
print(f"\nArea: {area_m2:.6f} m²")
print(f"Volume: {volume_m3:.9f} m³")
print(f"Forza: {forza_n:.2f} N")
print(f"Massa del robot: {massa_robot_kg:.2f} kg")
print(f"Accelerazione: {accelerazione_m_s2:.2f} m/s²")
print(f"tempo di spinta: {tempo_spinta:.2f} s")
print(f"impulso: {impulso:.2f} N*s")
print(f"Velocità finale: {velocita_finale:.2f} m/s")
print(f"Flusso d'aria massimo: {flusso_m3_s_massimo:.5f} m³/s ({flusso_m3_s_massimo * 1000:.2f} L/s)")
print(f"Diametro interno minimo del tubo: {diametro_tubo_mm:.2f} mm (a {velocita_aria_tubo} m/s)")
