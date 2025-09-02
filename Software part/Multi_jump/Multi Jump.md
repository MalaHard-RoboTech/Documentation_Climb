
--- 
## Index
- Design
- Schema
- Example
- [[#What is the bi-level optimization]]
- [[#Reference:]]




---
## What is the bi-level optimization


#### Offline part

Per ottimizzazione offline si intende, un'ottimizzazione prima della fase di lancio, da un punto A a  un punto B.

è composto da outer e inner loop:
- **outer (outer optimization) loop**:  determinare i punti intermedi per andare da un punto a a un punto B, ottimizzando i punti di salto minimizzandoli
- **Inner loop**: ottimizzazione per saltare da un punto intermedio ad un altro (by Focchi).
questa fase quindi viene scomposta in una Bi-Level optimization, dove si scompone un mega salto in più saltelli.

#### Online Part
Uso del **MPC** --> ogni singola traiettoria di salto, si va a tracciare l'andamento

paper reference : [link](https://arxiv.org/pdf/2409.12366)
bi-level optmization **usa due ottimizzazioni a basso e alto livello (inner and outer loop).**

usata in **real-time Model Predictive Control (MPC)**

l’MPC (inner level) gira a _ogni_ ciclo di controllo, mentre l’ottimizzazione di alto livello viene lanciata solo ogni _k_ cicli; la parte eseguita in parallelo è il _line-search_ interno all’outer level, non l’intero bi-livello.

esmepio:
- **Livello basso (L-MPC)** – un MPC parametrizzato che, ad ogni ciclo di controllo, restituisce traiettorie di stato e forze di contatto risolvendo **solo un’** _approssimazione quadratica (QP)_ – lo stesso trucco “real-time iterations” usato in molti MPC veloci [ar5iv.org](https://ar5iv.org/pdf/2409.12366)
- **Livello alto** – ottimizza in tempo reale **il programma di contatto (contact schedule)**, cioè le tempistiche di “lift-off” e “touch-down” di ciascuna zampa, parametro che il livello basso prende come dato [ar5iv.org](https://ar5iv.org/pdf/2409.12366)[ar5iv.org](https://ar5iv.org/pdf/2409.12366).

---
## Reference:
- [Multi-Contact Agile Whole-Body Motion Planning via Contact Sequence Discovery](https://hal.science/hal-05072261/)
- [[Motion_planning_for_quadrupedal locomotion.pdf]]
- [Quadruped TAMOLS_filter_3d_map](https://arxiv.org/pdf/2206.14049)
- [Robust Rough-Terrain Locomotion with a Quadrupedal Robot](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8460731)

### Video
- [multi contact-planning with dog](https://www.youtube.com/watch?v=rAP7M4BL9sQ) 
- [humanoid](https://www.youtube.com/watch?v=2Vry-th8g2s)
### Scripts: 
- [py_cemmd](https://github.com/itsikelis/py_cemmd) --> by [Ioannis_Tsikelis](https://itsikelis.github.io/) --> [[Mixed Distribution Cross Entropy Method]]
- [[Climb_robot2_Light]] --> [link_code](https://github.com/mfocchi/robot_control/blob/traj_optimization/base_controllers/climbingrobot_controller/climbingrobot_controller2_light.py#L272)


---

---

## Notes:
**planning agile** with all body motions or for legged and humanoid robots is a fundamental capability for enabling dynamic task such as running, jumping, fast reactive maneuvers.

In questo [link](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=4HezbBsAAAAJ&sortby=pubdate&citation_for_view=4HezbBsAAAAJ:xtRiw3GOFMkC) usano il "**Multi-contact motion planning freamwork**" basato su bi level optimization -> (contact sequence discovery mechanism) usando il **Mixed Distribution Cross-Entropy Method (CEM-MD)**. Sfrutta anche la possibilità di utilizzare uno schema ottimizzato del calcolo delle traiettorie, usando transizioni dinamiche del corpo intero. L'uso di **Multi-contact motion planning** combinata con la parametrizzazione dello spazio tangente porta a sequenze di movimento altamente dinamiche, pur rimanendo efficiente dal punto di vista computazionale.

---
