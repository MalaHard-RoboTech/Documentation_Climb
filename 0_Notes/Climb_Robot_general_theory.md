- [[Report_focchi_RAS.pdf]] --> [[Notes_report_focchi_ras]]
- [Github alpine robot](https://github.com/mfocchi/climbing_robots2)
- [Github_Collaboration](https://github.com/MalaHard-RoboTech/Alpine_Climbing_robots.git)
- [[Componenti]]
- [[Circuito]]
- [[Guide Reinforcement learning]]
- [[Physics part]]

Nome - ALPINE robot
# Introduction

Applicazioni e obiettivi:
- operazioni in ambienti impervi per togliere massi, arbusti, rillevamento del terreno

>[!Idea]
>robot appeso a delle corde, con l'uso di una gamba retrattile per saltare dalle pareti della montagna.

Requirments:__
- portare peso (strumenti)
- movimenti veloci ed efficenti
- Attraversare superfici irregolari
- Semi autono
- eseguire operazioni di spinta e atterraggio con dissipazione dell'energia cientica

**~={Orange}Fasi=~**
1. **Stacco**
2. **Pattern di forze**
3. **Posizionamento**


**This robot has low "versatility":**
![[Pasted image 20241208182805.png]]


## Actual SOLUTION:
![[Pasted image 20241209150003.png]]
- Two ropes (con meccanismi di avvolgimento e svolgimento)
- A retractable leg (which can push on the wall making the robot jump) A landing mechanism
- landing mechanism (reaction wheel + stuff to landing)
## Rope solution

- Allow to carry heavy payloads and remain in a stationary position without consuming significant energy (breaks)
- The combination of jumps and mixed vertical/lateral motions allows the robot to move quickly
- 3D movements allow to swing over the wall surface most of the time, overcoming irregularities and obstacles (use legged machine)
- The landing mechanism allow to robot to dissipate the "eccesso of kinetic energy" without re-jump

## Landing phase:

per l'atterraggio vengono usati i propellers e una disspazione dell'energia cinetica usando un virtual spring

## Application:  
- Foratura, ripozioni blocchi, iniezione di resine nel muro

!! these example can be to generate an oscilation on robot and the position become, bad.

Per fare operazioni (es foratura) e’ necessario stimare la massima forza che il trapano puo’ esercitare sulla roccia senza far ribaltare il robot.
![[Pasted image 20241209152000.png]]


# Controllo

1) La zampa retrattile agisce in maniera impulsiva e la sua forza laterale e’ limitata dall’attrito
2) Le corde possono creare forze nella direzione di “tiro”
![[Pasted image 20241208185003.png]]
__Ottimizzazione riguarda__ (constraint):
- Range force for motor
- Leg can only jump / rope only pull
- Attriti
- Not go throught inside of wall
**Actual Ottimization:** 
1. Distance between landing point and target
2. Energy consumtion
**Optimal solution:**
- Optimal pulse for leg
- Optimal solution for path finding
- Pattern force on rope


## 