#calculator
This is our calculation to select right motors for  "arganelli"

here you can found aother point about calculus: Excel (Misure da matlab)


table reference worst case scenario: jump 3 class 10 kg

![[reference_table.jpg]]

### data taken into account from the table and from matlab

$\text{Robot mass} = 10\, \mathrm{kg}$  
$\text{Jump reference (m)}: [0.5, 1, -10] \rightarrow [0.5, 4, -2]$  
$\Delta \text{Jump} = [0, 3, 8]$  
$\text{Energy consumed} = 1000\, \mathrm{J}$  
$\text{Time} = 1.65\, \mathrm{s}$  
$\text{Average load} = 600\, \mathrm{W}$  
$\text{Peak power} = 700\, \mathrm{W}$  
$\text{Max rope vel} = 7.8\, \mathrm{m/s} \approx 8\, \mathrm{m/s}$ 
$\text{Max rope acceleration} = 16\, \mathrm{m/s}^2$

$\text{suppose a winch drum of 5 cm in diameter}$
$\text{drum radius} = 0.025 m$

$\text{Calculate max Angular Speed } \omega:$  
$\omega = \dfrac{v}{r} = \dfrac{8}{0.025} = 320\, \mathrm{rad/s}$
$\text{Convert Angular Speed to RPM:} \ \mathrm{ Max RPM} = \omega \times \dfrac{60}{2\pi} = 320 \times \dfrac{60}{2\pi} \approx 3056\, \approx 3000  \mathrm{ RPM}$

$\text{Forces and torque on the drum, by dead lifting the weight}$
$\text{Force} = m \cdot (g + a) = 10\, \mathrm{kg} \cdot (9.81 + 16)\, \mathrm{m/s^2} = 258.1\, \mathrm{N}$
$\tau = F \cdot r = 258.1\, \mathrm{N} \cdot 0.025\, \mathrm{m} = 6.45\, \mathrm{Nm} \approx 6.5  \mathrm{Nm}$

$\text{peak power at the drum}$
$\text{Power} = \tau \cdot \omega = 6.5\, \mathrm{Nm} \cdot 320\, \mathrm{rad/s} = 2080 \approx 2000\, \mathrm{W}$


Here arises a big discrepancy; from the simulation motor peak power should be 700W but the drum power is 2000W even without considering power train transmission losses. And with a 1:1 ratio the power shlould be the same.

continuing with an ideal power train loss, because we are already over sizing the calculations anyway, I've found this motor that meets the power hungriness requirements of the winch
![[motor_choice.png]]

([motor link](https://www.amazon.it/Dingln-Outrunner-Compatibile-Bilanciamento-Skateboard/dp/B08GWZV7XX/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.zRnsXJbSDBNHhbCPWiuuWNG-NQSjtbGCmGKcV9o69jGowmzJW2oldmW9fZFgN4QMu4amM1Q3BVLgMcyQtX5bp4FNYtfAVmg9TBUJZ4VYJNvz9Rlx0jb1dcbLvrp14ymipZmlZ6vqzrf9ga-Zjcc1Sc6SsutgULlGO-eU8iPuxQ5eE_dInWJb-PvbmSONyze8dY7coI7S22nuK_hOvuQnYvZquxpVu8MnywCm7uq7Ka8gGcVxW1K8u5KOMWwsXy-a0wY_EFS2xvwOgAgNpywt9ztmK65jCcBKjOdfvTrA-uQ.cN9p7v9RetkG4vxiTPCnl10qLSAYbvmHxUXgAqb3t6A&dib_tag=se&keywords=6384+120KV+BLDC&qid=1742896479&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1))


## Transmission

This motor suggest a 1:1 gear ration, but for out lighter robot a 2:1 could stress less the motor. we can use a timing belt to move the drum further from the motor shaft.
A HTD 5M  15mm wide belt can support up to 920N but a 20mm belt maybe is better to prevent slippage, an idler has to be included in the design as well, also is good practice to have the pulley diameter grater that the width of the belt to prevent early wear. after all is all a gear ration game.
([HTD-5M reference](https://www.tyma.eu/pdf/elatech-htd-5m-timing-belts.pdf?srsltid=AfmBOoqvrD9hQ6XPvBO5HT7VPnTQQhwGAuddtTdY99Ezh_RLl6LqRd2y))

([belt link](https://www.amazon.it/dp/B0D66MPMLX/ref=sspa_dk_hqp_detail_aax_0?psc=1&sp_csd=d2lkZ2V0TmFtZT1zcF9ocXBfc2hhcmVk))

![[belt_HTD-5M.png]]




This type of pulleys are hard to find online but i thing we can try to 3d print those without any problem. 

## braking system

An important feature for this robot and for the motor longevity is the ability of the robot to stay stationary without consuming motor power so we discussed a braking system, a cheap but powerful brake kit should do the work just fine, they will be servo actuated and normally closed.  [NC]
([brake system link](https://www.amazon.it/bicicletta-meccanico-anteriore-posteriore-equitazione/dp/B0BTPBTRWZ/ref=sr_1_12?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2706CBRONK2E&dib=eyJ2IjoiMSJ9._NwUE0GvqpW6cEZMUF9KM7E1EXPV0poo_vuuPL_tCbBG7LuavIDuHrxs4l2EF6iApadSmooWXlmmEWcG09NyE1dBtL2uvTNSQKK1IlaG_X5vZ41Bllb0xEjfa9WajkIB7N68Kn3TGNL5k9TK0T2DvesMWeV5OJrQHfArRvE9Gb9EaTMkOKaU4HW_x0y2fWtpmHXvW3nQvf9ZrxRHPZGfWiUQwv-I6qhczNPh2o9hu-93owU8C0qO8Wa6iRWRkjImhByEh1Wkad5XwkpAOctGTTSHQSlS0LQJBBuoBhzbwO8frdZyz3yGaLpqgl3gbG0XfE2T4vWWq7QzHkQygEUOvRnpQDrz8UWIHzCFrFGU77ja5CVfhVR164gx0cx8ilzjCtfMeyNPL5j7uH0jWstPx12LB4ideaFsE041k9n1sd9JEKiePa-m31XEpvxYeQCL.lC4ffUXE8f7wsNoI8tANl5n0WzfJGSlOUb0LnNAVyXM&dib_tag=se&keywords=Kit+freni+a+disco+meccanici+per+bicicletta&qid=1742899341&sprefix=kit+freni+a+disco+meccanici+per+bicicletta%2Caps%2C92&sr=8-12))

![[brake_system.png]]
## winch electronics

As the motor has a maximum voltage of 36V that's what we are going to propose as main power supply for the winches, a separate one for the robot will be used. 
the biggest power supply i could find is 1200w at 36v. if under powered we can use 2, one for each winch.
([power supply link](https://www.amazon.it/Alimentatore-Trasformatore-Telecamera-Sicurezza-Dispositivo/dp/B0C2R2HS62/ref=sr_1_9?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=CB6KVSTORKR9&dib=eyJ2IjoiMSJ9.UnhK0YfdsgMP0AHob2rT1YQlgSfvcFRO0C5_sAXeRgSOE7AkkzzzwTKjhSA1YXDkdFGew_mn3cyOWTn58230Wb6BARFvMxOqzjzm1Sk-JuDHCS-AA01awPhIDqenWKPUVnKCrtJ7GlP7uSE_bFMn0Roy5qQN3cfV626KYI86R2VcL4sUIOg3Bv_8G1C8GkKHT61MxoSPo7ZK91VoKrKBlm8i7FRUnj7ah9Xvf2I9MaLH2nPKPQ2HEdX8riZiEi7otaw4cPVFK9ZHb5btgULb0SwIMxwn_ai1c79JcCW8sfFEQM2Ahltc6DsUE5rtbVAaJE_ghk1I26NucNGE0TU1u44H8jvw7qh26EX8SlaM8Yj4kIz3dkg0gRMMwWljcU0r72Kao5n4-2TcCCqesvBBSZ39RuS1XedTILkcZfZ2ULLbamd_oZdnJL-mILO6X34_.wKlzBA_5EoQKGBRYn19Ph83O5VbS-oOICnk76EvvOJw&dib_tag=se&keywords=power+supply+2000w+36v&qid=1742901222&sprefix=power+supply+2000w+36v%2Caps%2C97&sr=8-9))
![[power_suppply_36v.png]]

### drive motor controller
As the robot is torque controlled, we choose a FOC BLCD controller based on odesc V4.2, it has proven reliable and up to the standards,  with up to 56V and 120A of peak current. 

([odesc link](https://www.amazon.it/gp/product/B0DYVLWJZS/ref=ewc_pr_img_2?smid=A38GRUO0066PF0&psc=1))
![[odesc.png]]

## winch cable
we proposed a zinc cable to be flexible, lightweight and conductive so to power the robot via the winch wires. So for a 10kg robot even with extreme acceleration will not eccede maximum tensile strength of a 1mm  wire. 1.770 N/mmq

![[rope_load.png]]

our real limiting factor is the max amp capacity of the wire to power the robot. To properly size the wire diameter the following characteristic have to be taken into account. 
1) the zinc layer is few microns high so it doesn't really play big on the conductivity side.
2) copper has conductivity  5.96 * 10^7
3) inox has conductivity:      1.45 * 10^6
$$
$$
$$
\text{Factor} = \frac{\sigma_{\text{Cu}}}{\sigma_{\text{Inox}}} = \frac{5.96 \times 10^7}{1.45 \times 10^6} \approx 41.1
$$

([material table](https://www.youmath.it/lezioni/fisica/elettricita/4912-conduttivita-elettrica.html))
So we need 41 times bigger wire to carry the same amps. relative to a standard copper wire.

Suppose a 600W robot powered by 48v (we could use higher voltages for transmission but 48 transformer is easy to find)  we have around 12.5 amp, so the cable rating for it is 16-gauge that has area of 1.31 mm².

$$
A_{\text{new}} = 1.31\ \text{mm}^2 \times 40 = 52.4\ \text{mm}^2
$$
$$
d = \sqrt{\frac{4A}{\pi}} = \sqrt{\frac{4 \times 52}{\pi}} \approx 8.14\ \text{mm}
$$
if we fix 2 mm wire and compare it to a copper, if a 2mm copper wire can carry 20 amp.
our inox wire will carry:
$$
\text{Ampacity}_{\text{wire}} \approx \frac{\text{Ampacity}_{\text{Cu}}}{\sqrt{40}} \approx \frac{20}{6.32} \approx 3.16\,\text{A}
$$
not much for out propellers on the robot. 150w at most with 48v.


Needed discussion to change material/technique, proposing a 
Steel Wire Armored (SWA) Cables or Aerial Bundled Cables (ABC) that are both conductive and suitable for bearing load



## piston calculation

in order to make the jump F_leg need to  be 271N.
We have choosen a pneumatic sytem comprised of a piston,  and a proportional vale to control it. 
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



