


  

## first winch cable

we proposed a zinc cable to be flexible, lightweight and conductive so to power the robot via the winch wires. So for a 10kg robot even with extreme acceleration will not eccede maximum tensile strength of a 1mm  wire. 1.770 N/mmq

  

![[rope_load.png]]

  

our real limiting factor is the max amp capacity of the wire to power the robot. To properly size the wire diameter the following characteristic have to be taken into account.

1) the zinc layer is few microns high so it doesn't really play big on the conductivity side.

2) copper has conductivity  5.96 * 10^7

3) inox has conductivity:      1.45 * 10^6

$$

$$

$$

\text{Factor} = \frac{\sigma_{\text{Cu}}}{\sigma_{\text{Inox}}} = \frac{5.96 \times 10^7}{1.45 \times 10^6} \approx 41.1

$$

  

([material table](https://www.youmath.it/lezioni/fisica/elettricita/4912-conduttivita-elettrica.html))

So we need 41 times bigger wire to carry the same amps. relative to a standard copper wire.

  

Suppose a 600W robot powered by 48v (we could use higher voltages for transmission but 48 transformer is easy to find)  we have around 12.5 amp, so the cable rating for it is 16-gauge that has area of 1.31 mm².

  

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