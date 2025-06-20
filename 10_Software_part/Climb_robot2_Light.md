## Index: 
- [[#Some_tircks]]
- Functions
## Explanation: 

In ***talker*** si va a settare la state machine e il collegamento al robot reale. in `params.py`  si settano i parametri del robot e si inizializza HW interface con il robot reale.

Dopo si inizializza il programma, punto di start e punto iniziale.
Si imposta il punto finale.

loop di ros:
nel `while not ros.is_shutdown():`  si parte con la macchina a stati:
1. ***p.updateKinematicsDynamics()***: inizializza la dinamica
2. Partenza da ***idle*** : qunado il tempo diventa superiore a ***start_jump*** lui inzializza il salto, orienta la zampa
3. **Orienting_leg:** Calcolo ***leg orient***
4. **Thrusting:** fase dello sforzo della zampa
5. **flying:** calcolo del MPC e confronto con OCP per tensionare le corde e setttare l'atterraggio 

## ~={Orange}Functions=~:

### utility functions:

#### apply propeller moment: 
applica un **momento torcente** attorno all'asse z (cioè una rotazione) usando una coppia di forze simulate (simalazione delle corde) collegati a sinistra e a destra di un punto di sollevamento.

#### apply_propeller_force

applica una **forza propulsiva** in una certa direzione, simulando l'effetto di una **forza generata da un'elica o motore**, **senza momento torcente**.
#### updateKinematicsDynamics

fase di aggiornamento dello stato dinamico e cinematico, calcolo di tutte le **variabili dinamiche e cinematiche** rilevanti per controllare e simulare

#### getRobotMass

estituisce la **massa totale del robot**, **a partire da un determinato giunto** in poi (***wire_base_yaw_l***)
#### _receive_contact

#### getImpulseAngle
#### computeJointVariables

#### detectTouchDown

#### computeMPC

#### onlinePlotMPC

#### computeJumpEnergyConsumption


### Other functions: 

#### loadModelAndPublishers
Generazione del robot dal URDF
#### deregister_node

#### startupProcedure
#### initVars

#### resetRope

#### initOptim


## ~={Orange}Talker=~



## ~={Orange}Parametri di movimento: =~

p.startJump = 2.5  
p.orientTime = 1.0  
p.stateMachine = 'idle'  
p.jumpNumber  = 0  
p.numberOfJumps = 1  
p.start_logging = np.inf


## ~={Orange}Some_tircks=~

- **landing**:
```python
if  p.landing:  
    p.stateMachine = 'flying_and_wait_for_touchdown'  
```
se a **true** si va a fare una fase aggiuntiva in cui cerca di capire in che fase del MPC di trova e se c'è una fase di landing salta in landing phase attivando i PID joint e va in touch down.

la fase di landing lascia i PID controller.

a False non fa la fase di landing ma solo la fase di fly.

- **flage real_robot:** 
flag che in params.py che se messo a True, connette il robot reale con il codice.


## Bugs: 
``` python
import sys  
sys.path.append('/home/ruby/ros_ws/src/locosim/robot_control')
```