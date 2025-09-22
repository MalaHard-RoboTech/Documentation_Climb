
## Index

- Design
- Schema
- Example
- [[#Terrain simulation]]
- [[#Filter and point cloud manager]]
- [[#Patch manager]]
- [[#Reference:]]

---
## Design

**Objective**: Before jumping, givean ant 3D map, create a cost_map that associates each point on the 3D map, with cost function, indicating its ease of landing and thrust. 
We have an outer loop and inner loop to control the exact point to landing to achieve a position of the robot. 

---


## Filter and point cloud manager
The Filter types used are: 
- Blur

| **Blur**                                            |
| --------------------------------------------------- |
| \| 1  1  1 \|<br>\| 1  1  1 \| * 9<br>\| 1  1  1 \| |
Inside of the point cloud, it's used to reduce the noise

- Smoothing: 

| Smoothing:                                              |
| ------------------------------------------------------- |
| \| 1  2  1 \|<br>\| 2  4  2 \| * 1/16 <br>\| 1  2  1 \| |
used to "smussare" some points, but mantain the picchi e gradini

- Sobel (for I derivative):

| Sobel X                                            | Sobel Y                                               |
| -------------------------------------------------- | ----------------------------------------------------- |
| \| -1  0  1 \|<br>\| -2  0  2 \|<br>\| -1  0  1 \| | \| -1 -2 -1 \| <br>\|  0  0  0  \|<br>\|  1  2  1  \| |
used to find the "pendenza"(gradiente) 

- Laplacian:

| Laplacian:                                      |
| ----------------------------------------------- |
| \| 0  1  0 \|<br>\| 1 -4  1 \|<br>\| 0  1  0 \| |
second derivative, evidenzia zone di cambiamento brusco (trova curvature nel terreno)
valori positivi --> depressione/buchi
valori negadivi --> gobba i punte


- LoG (Laplace of Gaussian):

| Laplacian Of Gaussian                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------- |
| \| 0   0   1   0   0 \|<br>\| 0   1   2   1   0 \|<br>\| 1   2  -16  2  1\|<br>\| 0   1   2   1   0 \|<br>\| 0   0   1   0   0 \| |
simile al filtro laplaciano di derivata seconda ma con un gaussian filter.

> **Note:** nel codice i valori più bianchi sono valori che hanno la massima pendenza o bordo

It's decided to use the Kernel filter in 2 Dimension because is more rubost and fast and it's possible re adpt in different scenarios, also out of Point cloud sistem, but also using a normal camera or other stuff.
Use the principle of the [image processing](https://en.wikipedia.org/wiki/Image_processing), a **kernel**, **convolution matrix**, or **mask** is a small [matrix](https://en.wikipedia.org/wiki/Matrix_\(mathematics\) "Matrix (mathematics)") used like [edge detection](https://en.wikipedia.org/wiki/Edge_detection "Edge detection") in a image (a matrix much bigger). Or more simply, when each pixel in the output image is a function of the nearby pixels (including itself) in the input image, the kernel is that function.

---
### What is a convolution: 
link: [here](https://medium.com/advanced-deep-learning/cnn-operation-with-2-kernels-resulting-in-2-feature-mapsunderstanding-the-convolutional-filter-c4aad26cf32)
example: [here](https://medium.com/@ianormy/convolution-filters-4971820e851f)

A convolution matrix or kernel is a matrix used to apply a filter to an image or 3D matrices such as point clouds, by sliding the kernel across the entire input matrix

Example of the convolution matirx:
![[Pasted image 20250727162531.png]]

### Convolution with point cloud:
point cloud is a vector/matrix: N*3 ,where each row is a point (x,y,z)
### Interpolation in a grid
to use the filter in a point cloud, we interpolate the point cloud in a uniform grid.
to create a "2D image", or matrix where: 
- asse **Y → asse orizzontale** della parete (lunghezza)
- asse **Z → profondità**
- valore dei pixel = altezza `X` interpolata sulla griglia `(Y, Z)`
like an "MAPPA ALTIMETRICA"

---
## Reference

La mappa dei costi rappresenta quanto è "difficile" attraversare ciascun punto di un terreno in base alla pendenza o alle irregolarità.

- link: [cost_map_generator](https://chatgpt.com/c/687df412-3470-8013-a9fd-80f0f00c3b0a) 
- [RLOC: Terrain-Aware Legged Locomotion using Reinforcement Learning and Optimal Control](https://arxiv.org/pdf/2012.03094)
	- [code](https://github.com/ori-drs/rloc_manuscript_supplementary_code/tree/master?tab=readme-ov-file)
- [grid_map](https://github.com/ANYbotics/grid_map) --> general idea
- https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9133154
- https://arxiv.org/pdf/2206.14049
- [[Filter on point cloud and Cost]]





---
## Other Notes:

### [RLOC: Terrain-Aware Legged Locomotion using Reinforcement Learning and Optimal Control](https://arxiv.org/pdf/2012.03094)

**proprioceptive** --> internal robot sensors (IMU)
extereoceptive --> external robot sensor (camera)

in this paper used the on-board proprioceptive and extereoceptive feedback to map sensory information and commands into footstep plans using a reinforcement learning (RL) policy.
**Elevation Map Encoding** (elevetion mapping framework).
Sfrutta la consapevolezza del terreno calcolata in RL --> policy mappa direttamente le informazioni dei sensori + comandi di velocità desiderati della base in piani di appoggio.

Non sfrutta un metodo "sense-plan-act" (uso immediato dei valori del sensore).
In RLOC, la policy RL integra la percezione nel processo decisionale,diventando un sistema "sense-act" (percepisci-agisci), in cui la comprensione del terreno è incorporata all'interno della policy di controllo appresa.
Questo approccio può portare a tempi di reazione più rapidi e potenzialmente a comportamenti più robusti in ambienti dinamici e incerti, poiché evita la latenza e i potenziali errori.

In questo caso si addestra la policy in diversi terreni (sfrutta un multilayer perception).
la policy impara a "riconoscere" implicitamente caratteristiche come pendenze, gradini o fosse attraverso le loro firme sensoriali, senza la necessità di una rappresentazione geometrica.

Per capire il terreno usa: 
- **Stati Propriocezione** (posa IMU rotazioni dei giunti). 
- **Feedback Esterocettivo** (Visione) : uso di una depth camera per regolare la dinamica delle traiettorie
- **Comandi di Velocità Desiderati** : usati nella policy per indicare il movimento desiderato del robot.

La combinazione di feedback **propriocettivo ed esterocettivo** costituisce un input sensoriale
multimodale essenziale per una locomozione intelligente. 
La propriocezione fornisce le informazioni "qui e ora" per un controllo reattivo immediato, mentre .
L'esterocezione fornisce le informazioni "cosa c'è davanti" per una pianificazione proattiva e l'evitamento degli ostacoli.

Questa dualità è fondamentale per una navigazione robusta in ambienti complessi e dinamici. Permette al robot di essere sia agile nelle risposte immediate che lungimirante nella pianificazione del percorso, caratteristiche indispensabili per la locomozione dinamica su terreni accidentati

Le mappe di elevazione del terreno centrate sul corpo (heightmaps) usate per addestrare la policy "policy" in simulazione. 
Questo evidenzia una strategia comune per il trasferimento dalla simulazione al mondo reale (sim-to-real), dove una policy addestrata con dati ideali in simulazione viene poi adattata per operare con dati sensoriali più realistici.

dati grezzi + rappresentazioni elaborate (height maps)

Mentre i dati grezzi offrono immediatezza e evitano la perdita di informazioni, le rappresentazioni elaborate possono semplificare il compito di apprendimento e migliorare le
prestazioni in simulazione.

si usa una mappatura chiamata **Elevation Map Encoding** (elevetion mapping framework). 

Fase di apprendimento uso di: 
- Inferenza bayesiana + gaussian process
- 



step e ragioni del processo: 
1- usa extereoceptive value per filtrare i parametri di ingresso del sensore

2- denoising property, utile per fare trasferimenti tra sistemi reali e fisici,  Per ottenere una mappa altimetrica filtrata viene impiegata una tecnica di interpolazione dei vicini che spesso comporta distorsioni (ad esempio, i bordi dei gradini sono sfocati e spostati).

3- durante l'approccio di training, i valori di pre-train fanno in modo che l'agente di RL non deve imparare i parametri e le feature del terreno rendendo il processo più  veloce

4- ven though different strategies such as fast Fourier
transform (FFT) can be employed to compress the
elevation map, our work focuses on utilizing deep learn-
ing strategies for feature extraction. 

Questo ci permette di adattare la rete precedentemente addestrata a una classe di terreni diversi, riqualificando l'encoder. Inoltre,
strategie come l'apprendimento per trasferimento possono essere utilizzate per ridurre la complessità dell'addestramento. Anche l'estrattore di caratteristiche può essere riqualificato insieme a una politica RL per adattarsi a compiti diversi non introdotti durante il precedente addestramento.

**denoising convolutional auto-encoding strategy**

---
Point cloud: 
![[Pasted image 20250721093724.png]]
filtering + clustering




---

### GridMap by AnyBotics

Libreria universale per la mappatura a griglia di robotica mobile.
Libreria in C++ con interfaccia ROS, gestisce mappe a griglia bidimensionali con più livelli di dati. 
Permette di archiviaer dati come elevazione, varianza, colore, coefficiente di attrito, qualità del punto d'appoggio, normale della superficie e attraversabilità.

- **Funzioni di convenienza**: Include diversi metodi di supporto per un accesso comodo e sicuro ai dati delle celle, come funzioni di iterazione per regioni rettangolari, circolari, poligonali e linee.
- **Interfaccia OpenCV**: Le mappe a griglia possono essere convertite da e verso i tipi di immagine OpenCV.
- **Visualizzazioni**: Il plugin `grid_map_rviz_plugin` visualizza le mappe a griglia come grafici di superficie 3D (mappe di altezza) in RViz, e il pacchetto `grid_map_visualization` aiuta a visualizzare le mappe a griglia come nuvole di punti, griglie di occupazione, celle di griglia, ecc.

## **[rloc_manuscript_supplementary_code](https://github.com/ori-drs/rloc_manuscript_supplementary_code)**

By: Oxford Dynamic Robot Systems (ori-drs).
ontiene il **codice supplementare** e i **file di configurazione (principalmente in Python)** che servono a:

1. **Replicare o supportare i risultati e le dimostrazioni descritte in un manoscritto** (presumibilmente collegato a "rloc", che potrebbe riferirsi a "Robust Localization" o simili).
    
2. **"Skinnare" o adattare il framework "Director"** (una libreria e un'interfaccia utente per l'operazione di robot mobili) a un robot specifico o a un set di esperimenti, come quelli descritti nel manoscritto

nasce come uso insieme ad una interfaccia utente chiamata Director: 
https://github.com/ori-drs/director



other note: 

chatgpt detail : https://chatgpt.com/c/687d40a4-0550-8013-b12a-63f80f1e40e8
