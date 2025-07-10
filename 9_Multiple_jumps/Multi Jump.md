
--- 
## Usefull link:
- [Multi-Contact Agile Whole-Body Motion Planning via Contact Sequence Discovery](https://hal.science/hal-05072261/)
- [[Motion_planning_for_quadrupedal locomotion.pdf]]
- [Quadruped TAMOLS_filter_3d_map](https://arxiv.org/pdf/2206.14049)
- [Robust Rough-Terrain Locomotion with a Quadrupedal Robot](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8460731)
### Video
- [multi contact-planning with dog](https://www.youtube.com/watch?v=rAP7M4BL9sQ) 
- [humanoid](https://www.youtube.com/watch?v=2Vry-th8g2s)
### Theory
- [[Bi-level optimization]]
### Scripts: 
- [py_cemmd](https://github.com/itsikelis/py_cemmd) --> by [Ioannis_Tsikelis](https://itsikelis.github.io/) --> [[#Code_cemmd_explain]]
- [[#Climbingrobot_controller2_light]] --> [link_code](https://github.com/mfocchi/robot_control/blob/traj_optimization/base_controllers/climbingrobot_controller/climbingrobot_controller2_light.py#L272)
---
## Code_cemmd_explain
Minimal Python implementation of a Mixed Distribution Cross Entropy Method
Questo codice implementa un **algoritmo evolutivo che lavora su variabili miste** (discrete + continue), mantenendo e aggiornando una popolazione, selezionando gli elite e aggiornando le distribuzioni di probabilità per concentrare la ricerca verso le regioni promettenti dello spazio delle soluzioni.
### Algo.py
- Used to optimize discrete variable and continue variable in the same time.

**`CemParams`** :
- contains al possible configurations parameters
	- `seed`: seme per il generatore casuale
	- `parallel`, `n_threads`: per esecuzione parallela (non usati direttamente nel codice qui)    
	- `cem_iters`, `pop_size`, `n_elites`: numero di iterazioni, dimensione della popolazione, numero di elite (i migliori)
	- `decrease_pop_factor`, `fraction_elites_reused`: opzioni avanzate di controllo sulla popolazione
- Descrete variables
- Continuos variables

**`IterationLog`** : tiene traccia delle migliori iterazioni, sia discrete che continue
			

**`CrossEntropyMethodMixed`**:
	classe principle, le funzioni principali: 
		***generate_population:***
			***generate_population_discrete***:
				Genera la parte **discreta** della popolazione in base alle probabilità correnti. from `pop_size`
			***generate_population_continuous***:
					general la parte continua della popolazione usando una distribuzione normale (`𝒩(mu, std)`)
					qui abbiamo un array nei limiti, dove ogni valore dell'array è un giunto per esempio
		***update_distribution:***
			***Update_distribution_discrete:***
				prima ordina in basea alla migliore performance, poi prende n elite migliori. e aggiorna la dimensione di variabili discrete 
			***Update_distribution_continuous:***
				anceh qui  si ordina con la migliore, poi prende n elite migliori e fa l'aggiornamento.

### example.py

Esempo che utilizza CEM (cross entropy method) per problemi misti (continui e discreti). 

- usa "**`ProcessPoolExecutor`**" per eseguire funzioni in paralleto

la funzione "**eval_pop**" usata per determinare una regola di combinazione,**Tiene le migliori combinazioni** e le usa per generare nuove combinazioni più promettenti.

---





---
## Climbingrobot_controller2_light

- **Flusso**:
	- **Setup** (Gazebo,load URDF, inizializzazione di Pinocchio, start topic).
	- **Ottimizzazione offline** (chiamata _optimize_cpp_mex_) per generare la traiettoria di salto ideale e i profili di forza alle funi.
	- **Orientamento della gamba** verso l’angolo ottimale di spinta.
	- **Impulso**: applicazione di una forza breve ma intensa sulla gamba retrattile e di tensioni pre-calcolate sulle funi.
	- **Volo controllato**: un **MPC** corregge in tempo reale le tensioni e, se abilitato, la spinta dei propulsori per ridurre l’errore di tracking.
	- **Touch-down e landing**: rilevata la forza di contatto, vengono ripristinati i PD.
	- **Logging and plotting**.

- **orientarsi nel codice**:

| **Parametri tunabili**   | All’inizio di `__init__` e in `base_controllers/params.yaml` |
| ------------------------ | ------------------------------------------------------------ |
| **Modello dinamico**     | `updateKinematicsDynamics`                                   |
| **Ottimizzazione salto** | `initOptim` (offline) e `computeMPC` (online)                |
| **Macchina a stati**     | Corpo della `while` in `talker(p)`                           |
| **Propulsori**           | `apply_propeller_moment`, `apply_propeller_force`            |
| **Logging & Debug**      | `initVars`, `logData`, `plotStuff`                           |





---
## key points
- **Populations**: 
in algoritmi evolutivi, una popolazione e un insieme di soluzioni candiate ("individi") che vengono valutate in ogni generazione per trovare la migliore soluzione al problema. ad esempio una combinazione di parametri

`pop_size` : numero di individui per ogni generazione

- **elite**: 
migliori individui, basati sulla variabile fitness, usati per guidare l'evoluzione dell'algoritmo, i quali lo aggiornano la distribuzione

- **iverfitting**:
modello statistico molto complesso si adatta ai dati osservati perchè a un numero eccessivo di parametri rispetto al numero di osservazioni

- **Fitenss**: 
Valore numerico che dice quanto bene una soluzione soddisfa l'obbiettivo del problema

- **Corss-entropy:**
misura di distanza tra due distribuzioni di probabilità.
È spesso usata per dire **quanto è diversa** la distribuzione predetta da quella reale (target).  
Più piccola è la cross entropy, più simili sono le due distribuzioni.

- **CEM**:
Il **CEM** è un algoritmo che aggiorna iterativamente una distribuzione (o più) per **avvicinarla** alle regioni dello spazio in cui si ottiene **fitness elevata**. In ogni iterazione:

1. Si **campiona** una popolazione dalla distribuzione corrente.
2. Si valuta la **fitness** di ciascun individuo.
3. Si seleziona un sottoinsieme di **élite** (i migliori).
4. Si **aggiorna la distribuzione** in modo che sia più vicina alla distribuzione degli élite.

---

---


## Notes:
**planning agile** with all body motions or for legged and humanoid robots is a fundamental capability for enabling dynamic task such as running, jumping, fast reactive maneuvers.

In questo [link](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=4HezbBsAAAAJ&sortby=pubdate&citation_for_view=4HezbBsAAAAJ:xtRiw3GOFMkC) usano il "**Multi-contact motion planning freamwork**" basato su bi level optimization -> (contact sequence discovery mechanism) usando il **Mixed Distribution Cross-Entropy Method (CEM-MD)**. Sfrutta anche la possibilità di utilizzare uno schema ottimizzato del calcolo delle traiettorie, usando transizioni dinamiche del corpo intero. L'uso di **Multi-contact motion planning** combinata con la parametrizzazione dello spazio tangente porta a sequenze di movimento altamente dinamiche, pur rimanendo efficiente dal punto di vista computazionale.

---
