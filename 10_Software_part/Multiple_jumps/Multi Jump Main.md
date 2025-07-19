
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
- [[#Description]]
- [[Bi-level optimization]]
- 
### Scripts: 
- [py_cemmd](https://github.com/itsikelis/py_cemmd) --> by [Ioannis_Tsikelis](https://itsikelis.github.io/) --> [[Mixed Distribution Cross Entropy Method]]
- [[Climb_robot2_Light]] --> [link_code](https://github.com/mfocchi/robot_control/blob/traj_optimization/base_controllers/climbingrobot_controller/climbingrobot_controller2_light.py#L272)
### [[Handle_map]]

---
## Flow of blocks:
- [[Multi_jump_workflow.canvas|Multi_jump_workflow]]
### Description
#### Offline part

Per ottimizzazione offline si intende, un'ottimizzazione prima della fase di lancio, da un punto A a  un punto B.

è composto da outer e inner loop:
- **outer (outer optimization) loop**:  determinare i punti intermedi per andare da un punto a a un punto B, ottimizzando i punti di salto minimizzandoli
- **Inner loop**: ottimizzazione per saltare da un punto intermedio ad un altro (by Focchi).
questa fase quindi viene scomposta in una Bi-Level optimization, dove si scompone un mega salto in più saltelli.

#### Online Part
Uso del **MPC** --> ogni singola traiettoria di salto, si va a tracciare l'andamento

---




---
## Notes:
**planning agile** with all body motions or for legged and humanoid robots is a fundamental capability for enabling dynamic task such as running, jumping, fast reactive maneuvers.

In questo [link](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=4HezbBsAAAAJ&sortby=pubdate&citation_for_view=4HezbBsAAAAJ:xtRiw3GOFMkC) usano il "**Multi-contact motion planning freamwork**" basato su bi level optimization -> (contact sequence discovery mechanism) usando il **Mixed Distribution Cross-Entropy Method (CEM-MD)**. Sfrutta anche la possibilità di utilizzare uno schema ottimizzato del calcolo delle traiettorie, usando transizioni dinamiche del corpo intero. L'uso di **Multi-contact motion planning** combinata con la parametrizzazione dello spazio tangente porta a sequenze di movimento altamente dinamiche, pur rimanendo efficiente dal punto di vista computazionale.

---
