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



---

### example.py

Esempo che utilizza CEM (cross entropy method) per problemi misti (continui e discreti). 

- usa "**`ProcessPoolExecutor`**" per eseguire funzioni in paralleto

la funzione "**eval_pop**" usata per determinare una regola di combinazione,**Tiene le migliori combinazioni** e le usa per generare nuove combinazioni più promettenti.

---
