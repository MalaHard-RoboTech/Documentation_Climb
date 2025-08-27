#calculator 
## Introduction
> This section contains all the engineering calculations used to select the right piston for the Alpine robot.

We document here the full analytical process used to determine the required **Piston** and associated hardware.

To enable the Alpine Robot to perform its jump, each leg must exert approximately **270 N** of force.  
We have selected a **pneumatic system** consisting of a **piston** and a **proportional valve** to control airflow and pressure.

- **Required leg force**: 270 N  
- **Max pressure in current setup**: 4.5 bar  
- **Chosen piston**: 200 mm stroke, 32 mm diameter  

---

In order to make the jump F_leg need to  be 271N.
We have choosen a pneumatic system comprised of a piston,  and a proportional vale to control it. 
F_leg = 270 N
max pressure 4.5 bar -> in our current setup.

proposing a standard piston size we have a 200mm strike and 32mm head

Corsa in metri:
$$
s = \frac{\text{corsa\_mm}}{1000} = \frac{\text{200}}{1000} = 0.2 m
$$

Raggio in metri:
$$
r = \frac{\text{diametro\_mm}}{2 \cdot 1000} = \frac{\text{32}}{2 \cdot 1000} = 0.016 \text{ m}^2
$$
head area:
$$
A = \pi \cdot r^2 = \pi \cdot (0.016)^2 = 0.000804 \, \text{m}^2
$$


forza massima esercitabile
$$
P = 4.5 \, \text{bar} = 450{,}000 \, \text{Pa}
$$
Forza:
$$
F = P \cdot A = 450{,}000 \cdot 0.000804 = 361.8 \, \text{N}
$$
sufficenti ai 280N richiesti dal salto


([piston link](https://www.amazon.it/cilindro-pneumatico-compressore-dazione-alluminio/dp/B07TR2JCMM/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.xqCpkE-NaDwQM6SIGaxsPLuJAcOTuQPEzIO1qLt_6hr9qwaeiK3PMg60RDAZEosuUXsCXq5xhcNUMccoAC7HYuRRxMJI9fiKD2Xnf2cW6g-_jVcRjJ-ONSW_oXggM5IHZ3taA9AWvLwfYtfsN8CCYgXFIyDNulH1WZD0t6l8cnLAsXgQu0TXYK3ih3fKeknYOvc4Hapgdc9B13iaCJf6ke9WomZGtSSwIIwO77gfJVhYcK_H9t8ss9-3GC_WHaQ9zLrs-brga-3t-hqS60aWz3vJP5EuYEOn-emOR4lmCAg.edrC3ESrgHuw8Q34VZss_xklT5Ts35wFryQOGGou21M&dib_tag=se&keywords=pistone+aria+200mm&qid=1743525747&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1))
![[piston.png]]
## calcolo diamtero tubazioni


Volume spostato

$$
V = A \cdot s = 0.000804 \cdot 0.2 = 0.0001608 \, \text{m}^3
$$

 Accellerazione

$$
a = \frac{F}{m} = \frac{361}{10} = 36.1 \, \text{m/s}^2
$$

  Tempo di percorrenza del pistone (moto uniformemente accelerato, da fermo)

$$
s = \frac{1}{2} a t^2 \Rightarrow t = \sqrt{\frac{2s}{a}} = \sqrt{\frac{2 \cdot 0.2}{36.1}} \approx 0.105 \, \text{s}
$$



 Velocità finale

$$
v = a \cdot t = 36.1 \cdot 0.105 = 3.79 \, \text{m/s}
$$


 Flusso d’aria massimo

Area del pistone:
$$
A = 0.000804 \, \text{m}^2
$$

$$
Q = A \cdot v = 0.000804 \cdot 3.79 \approx 0.00305 \, \text{m}^3/\text{s} = 3.05 \, \text{L/s}
$$
Flusso richiesto:
$$
Q = 3.05 \, \text{L/s} = 0.00305 \, \text{m}^3/\text{s}
$$

Diametro interno del tubo:
$$
d = 8 \, \text{mm} = 0.008 \, \text{m}
$$

Area della sezione

$$
A = \frac{\pi \cdot d^2}{4} = \frac{\pi \cdot 0.008^2}{4} = 5.027 \cdot 10^{-5} \, \text{m}^2
$$

Velocità dell’aria

$$
v = \frac{Q}{A} = \frac{0.00305}{5.027 \cdot 10^{-5}} \approx 60.7 \, \text{m/s}
$$


questa velocità è leggermente alta ma i tubi sono i piu grossi che si trovano in commercio.
inoltre le perdite di carico possono essere trascurate essendo poca la lughezza del tubo.


([tube link](https://www.amazon.it/HUAZIZ-Pneumatica-Poliuretano-Pneumatico-Connettore/dp/B0BLGS26SY/ref=sr_1_5?crid=3LFA2XY8E6Z0X&dib=eyJ2IjoiMSJ9.KVdDa6DQjr3QYxMemKPa_974-Loj4E1du5rU4UrQUiVptFEiO3zHr0LR9i7GYRwdSlGjtOL-yBLD1CzqcrFE_jJrZLHWEtejGnNLwp0wbsW5rcd4pGSShxngs4733K_Tbr-n5SuCjZbZHk7Abp06hgQ89WMyp4sQYy1EXVHpgk24y59Zf1trIlKzHX7qHmDMQC-26HAWz4fjVSbiRO4cboD48hk25aYM-esImIsUA6LNseHCukxV7wdjS3aWkNLh3TpKVPqWMye0ijTI8tAeiX9iH9wdX_7ahTZFNrm2v4aPaH0vtzXUqrUPl09kmGDJqUGwgPhvntexDmpNgBlm7oTVUGPTPjvGicnhTtBv7MJ4ndt-u9kGFUPMJL9dGv9RvEePf_m1uiD-P_upgwbxEVejYKH05COK6Y1K_vLOfUcmaI-r2PoAU6_sV4bY7SZW.ArssPCHCEcVmKMRgAWHKaDE0lVKQH0xcwzh53a-hDGU&dib_tag=se&keywords=tubo%2Baria%2B12mm&qid=1743538755&sprefix=tuno%2Baria%2B12mm%2Caps%2C90&sr=8-5&th=1))

![[air_tube.png]]



