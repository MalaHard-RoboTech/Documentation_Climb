
--- 
## Index
- [[#Design and Schema]]
- Schema
- Example
- [[#What is the bi-level optimization]]
- [[#Reference:]]

--- 
## Design and Schema

Here you can find a brief schema:  [[bi_level_optimization.excalidraw]]


---
## What is the Bi-level optimization

Bi-Level optimization is a type of optimization problem where one optimization problem (Outer loop) is nested with another loop (Inner loop), it's used to define a structure that have 2 optimizer level.
Basically the Outer Loop aims to optimize its objective function, but its constraints or solution depend on the optimal solution of the inner loop process.
**key features:**
- **Hierarchical Structure:** The upper-level problem sets parameters or decisions that influence the lower-level problem. It possible say the Bi-level optimization like a Stackelberg game, where the upper-level acts as the "leader" making decisions first, and the lower-level acts as the "follower," optimizing its objective based on the leader's decisions.
Our Bi-Level Optimization is used toghether the [[#cross entropy method]].

### Cross-Entropy Method
Cross-Entropy Method is a probabilistic optimization (optimization algorithm) technique used to solve complex optimization problems, including bi-level optimization.
Is use to find the optimal solution to a problem by iteratively sampling from a probability distribution and updating that distibution to focus only the elite value.  It was originally developed for rare-event simulation but has been adapted for general optimization.
the Key part are the following: 
1. **Sampling:** Generate a set of random samples from the current probability distribution
2. **Evaluation:** Evaluate the objective function for each sample to define their performance, using for example a calc fitness .
3. **Selection and updating**: select the elite sempling and update the next loop 

#### Step flow:
1. built the possible combination
2. maintain a probability distribution over possible solutions
3. sample candidate solutions from this distriubtion
4. Evaluate their performance (fitness)
5. select the **elite set** (best-performing candidates).
6. Update the distribution to become closer to the **elites**
7. Repeat until convergence

Our implementation extends CEM to handle: 
- **Discrete Variables:** choices among a finite set. Modeled using **probability vectors** for each discrete dimension.
- **Continuous Variables:**  Modeled using **Gaussian distributions** (mean + standard deviation for each dimension).

#### Iteration process
1. **Generate population**:
    - Sample discrete candidates according to categorical distributions.
    - Sample continuous candidates from Gaussians, clamp within allowed range.
    - Optionally reuse some elites from past iterations.
2. **Evaluate population**:
    - An external fitness function provides a performance score for each candidate.
3. **Select elites**:
    - Rank all candidates by performance, pick the top `n_elites`.
4. **Update distributions**:
    - **Discrete**: probability vectors shift toward elite frequency counts.
    - **Continuous**: mean and variance are updated to elite statistics.
5. **Log best solution** so far.
This cycle continues until the stopping condition (e.g., number of iterations, convergence of distributions).

## Multi jump CEM

This code imlpement about of **bi-level optmization problem** for a locomotion/planning

- Set **start point** `P0_INIT` and **end point** `PF_INIT`
- The environment is represented by a **terrain point cloud** → converted into patches (flat surfaces).
- The robot may need to perform **intermediate jumps** on patches before reaching the goal.
- **Each jump** is optimized at a **low level** (with MATLAB dynamics solver), while the **high level** optimizer (CEM) decides:
    - **Discrete variables** (`xd`)→ number of jumps, which patches to land on.
    - **Continuous variables** (`xc`) → where inside each patch to land (normalized coordinates).

**Outer level** **CEM**:
- Samples candidate plans: how many jumps, which patches, where to land.
- Evaluates each candidate plan by running the inner loop.    
- Uses fitness scores to update distributions.

**Inner Level:**
- Given two points (start & landing), solve an **optimal control problem** for the jump trajectory.
- Compute feasibility (did it converge?), energy cost, duration, etc.
- Return results for fitness evaluation.

**Fitness value**: measures the quality of a candidate trajectory
F = w₁⋅(convergence) + w₂⋅(-energy) + w₃⋅(patch cost) + w₄⋅(landing cost)

## Online and Offline optimization:

#### Offline optimization part:


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
La parte Online è svolta da un File: **optimize_cpp_mex** realizato dal ottimizzatore di Matlab che permette di calcolare la traiettoria ottimale una volta forniti i parametri adeguati.

In output **optimize_cpp_mex** fornisce: 
- Traiettoria del centro di massa del robot
- Punto di Arrivo effettivo
- Durata del salto
- Energy consume
- tipo di problema risolto (Converge, unfeasible ...)


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
