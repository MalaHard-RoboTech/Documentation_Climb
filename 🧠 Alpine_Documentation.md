~={red}**Welcome to the Climb Robot / Alpine Robot Project Documentation**=~

This documentation covers the complete development process of the Climb Robot (also known as the Alpine Robot). Here you will find detailed information about the design, structure and implementation of the robot, including:

- Electrical components and circuit design
- Mechanical components and design 
- Physics-based calculations for selecting and simulating mechanical parts
- Software architecture and Python tools used for various computations (like multi jump and single jump)
- Helpful links and references to better understand the entire project

The main section of this document serves as a central hub, with an index of all related files and areas within the Obsidian workspace. Each section links to specific scripts, tools, and explanations that support the robot's development from concept to prototype.
for readme: [[README]]

---
## Schema of all structure
this following schema represent the structure about of the our space
![[schema.canvas]]

Instead the work flow communication in Software part see this schema:
![[Alpine_workflow.excalidraw]]

---
## 🗃️ Index 
- [[🧾 State of art climb robot]]
- [[🧾 Introduction climb robot]]
- [[🤝 Team of the Climbing Robot]]
- [[🧾 BOM climbing robots]]
### [[⚙️ Hardware (mechanical) part]]
- [[🧮 Old_calculations]]
- [[📊 Winch_calculations]]
- [[📊 Piston_calculations]]
- [[📊 Stabilizers calculations]]
### [[💡 Hardware (electric) part]]

### [[💻 Software part]] 

### 📝 Thesis
- Mechatronics Design of the Alpine Climbing Robot
- Multi-jump Trajectory Optimizer and Software Design of the Alpine Climbing Robot 

### Notes
 - [[🧾 Climb Robot general theory]]
---
## 🔗 Link to schema and Colaboration GIT:

- Link Git collaboration:  [click here](https://github.com/MalaHard-RoboTech)
---

### 📊 Matlab Results
  
>[!Note] **NOTE**: to see value about matlab Simulation see the following excel file: 
  
  - [Matlab_Scripts](https://github.com/MalaHard-RoboTech/Matlab_Scirpts)
 - [Matlab_result](Misure_Matlab.xlsx)
---
## 🔗 Usefull Link and software used

- Odrive tool
Odrive_link: [link](https://odriverobotics.com/)
Odirve_GUI: [link](https://gui.odriverobotics.com/)
Torque_speed_simulation:[link](https://www.desmos.com/calculator/1bw85mchnu)

- Tutorial:
Motor_Driver: [link](https://www.youtube.com/watch?v=9UxTPxgvOAA)
Tutorial_gitSubmodule: [link](https://youtu.be/wTGIDDg0tK8?si=bb5k6O9tb5w0m2Zo)

- Software and environments used: 
ROS1: [link](https://docs.ros.org/)
ROS2: [link](https://docs.ros.org/en/jazzy/index.html)
MATLAB: [link](https://it.mathworks.com/?s_tid=user_nav_logo)
Fusion360: [link](https://www.autodesk.com/it/products/fusion-360/overview)


--- 
## 🧾 Trick Code usefull if you clone repo

```
git config --global user.name name

git config --global user.email name.surname@gmail.com

ssh-keygen

cat ~/.ssh/id_rsa.pub # add it to github

eval "$(ssh-agent -s)"

ssh-keygen -t rsa -b 4096 -C "ruben.malacarne@gmail.com"
Generating public/private rsa key pair.

ssh -T git@github.com

cat ~/.ssh/id_ed25519.pub
```