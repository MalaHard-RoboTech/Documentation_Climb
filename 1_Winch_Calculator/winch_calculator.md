#calculator
This is our calculation to select right motors for  "arganelli".
here you can found aother point about calculus: Excel (Misure da matlab).


table reference worst case scenario: jump 3 class 10 kg.

![[reference_table.jpg]]

### Data taken into account from the table and from matlab

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

You can find the original motor of Odrive here: [link](https://shop.odriverobotics.com/collections/motors/products/odrive-custom-motor-d6374-150kv)
instead you can find the datasheet and the simulation here: [datasheet](https://docs.odriverobotics.com/v/latest/hardware/odrive-motors.html#d6374-150kv) and [simulation](https://docs.odriverobotics.com/v/latest/hardware/odrive-motors.html#d6374-150kv)

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
Given that the amount of current draw on the robot could be significant depending on the equipment in use we propose to use a flexible copper wire so that it can conduct but also wrap around the winch shaft, reinforced by a Kevlar or other fibers to bear the traction load.
![[guaina_pet.png]]
We have tested to make sure it can handle at least 500N.


Suppose we want 600W of available power onboard for electronics and other actuators we should use a high voltage for decreasing transmission losses like 48 V we have  12.5 A  a 14 awg cable can be suitable.  [[BOM aspect]] 



