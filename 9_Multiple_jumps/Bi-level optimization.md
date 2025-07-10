paper reference : [link](https://arxiv.org/pdf/2409.12366)
bi-level optmization **usa due ottimizzazioni a basso e alto livello (inner and outer loop).**

usata in **real-time Model Predictive Control (MPC)**

l’MPC (inner level) gira a _ogni_ ciclo di controllo, mentre l’ottimizzazione di alto livello viene lanciata solo ogni _k_ cicli; la parte eseguita in parallelo è il _line-search_ interno all’outer level, non l’intero bi-livello.

esmepio:
- **Livello basso (L-MPC)** – un MPC parametrizzato che, ad ogni ciclo di controllo, restituisce traiettorie di stato e forze di contatto risolvendo **solo un’** _approssimazione quadratica (QP)_ – lo stesso trucco “real-time iterations” usato in molti MPC veloci [ar5iv.org](https://ar5iv.org/pdf/2409.12366)
- **Livello alto** – ottimizza in tempo reale **il programma di contatto (contact schedule)**, cioè le tempistiche di “lift-off” e “touch-down” di ciascuna zampa, parametro che il livello basso prende come dato [ar5iv.org](https://ar5iv.org/pdf/2409.12366)[ar5iv.org](https://ar5iv.org/pdf/2409.12366).