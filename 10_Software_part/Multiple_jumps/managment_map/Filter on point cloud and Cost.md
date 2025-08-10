
## Index
- Height filter
- Smooth filter
- Sobel filter 
- Slope deviation on neighbour filter
- Curvature filter
- Cost computation
---
## Convolutional filter with point cloud
### What is a convolution: 
link: [here](https://medium.com/advanced-deep-learning/cnn-operation-with-2-kernels-resulting-in-2-feature-mapsunderstanding-the-convolutional-filter-c4aad26cf32)
example: [here](https://medium.com/@ianormy/convolution-filters-4971820e851f)
matrice di convoluzione o kernel è una matrice usata per applicare un filtro ad un immagine o matrici 3D come point cloud, facendo scorrere il kernel su tutta la matrice di input. 


matrice di convoluzione:
![[Pasted image 20250727162531.png]]

### Convolution with point cloud:
point cloud is a vector/matrix: N*3 ,where each row is a point (x,y,z)


### Interpolation in a grid
to use the filter in a point cloud, we interpolate the point cloud in a uniform grid.
to create a "2D image", or matrix where: 
- asse **Y → asse orizzontale** della parete (lunghezza)
- asse **Z → profondità**
- valore dei pixel = altezza `X` interpolata sulla griglia `(Y, Z)`
come se fosse una mappa altimetrica

---
## Sobel Filter
used to find the contour of an image.
Have a small computation

Example on 2 coordinates:
![[Screenshot from 2025-07-27 16-39-48.png]]
viene usato in 


---
## Height filter:
In that case we impose a threshold to delete the points that ara under or above a certain limits.



---
## Smooth filter:


---
