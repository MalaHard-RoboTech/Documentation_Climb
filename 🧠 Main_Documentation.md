~={red}**Welcome to the Climb Robot / Alpine Robot Project Documentation**=~

This documentation covers the complete development process of the Climb Robot (also known as the Alpine Robot). Here you will find detailed information about the design and implementation of the robot, including:

- Electrical components and circuit design
- Physics-based calculations for selecting and simulating mechanical parts
- Software architecture and Python tools used for various computations
- Helpful links and references to better understand the entire project

The main section of this document serves as a central hub, with an index of all related files and areas within the Obsidian workspace. Each section links to specific scripts, tools, and explanations that support the robot's development from concept to prototype.
for readme: [[README]]

---
## Schema of all structure
![[schema.canvas]]

---
## 🗃️ Index 

- [[🧾 BOM aspect]]
### ⚙️ Mechanical and physics part
- [[🧮 Old_calculations]]
- [[📊 Winch_calculations]]
- [[📊 Piston_calculations]]
- [[📊 Stabilizers calculations]]
### 💻 Software part 
- [[Software Part]]
- 
---
## 🔗 Link to schema and Colaboration GIT:

- Link Git collaboration:  [click here](https://github.com/MalaHard-RoboTech)
---

### 📊 Matlab Results
  
>[!Note] **NOTE**: to see value about matlab Simulation see the following excel file: 
  
 Here you can find the results calculated using simulation matlab of this repo: [Matlab_Scripts](https://github.com/MalaHard-RoboTech/Matlab_Scirpts)
in the following Excel
 - [Matlab_result](Misure_Matlab.xlsx)
 
 

---
## 🔗 Usefull Link

Motor_Driver: [link](https://www.youtube.com/watch?v=9UxTPxgvOAA)
Tutorial_gitSubmodule: [link](https://youtu.be/wTGIDDg0tK8?si=bb5k6O9tb5w0m2Zo)

--- 
## 🧾 Trick Code usefull if you clone repo

```
git config --global user.name TEXflip

git config --global user.email michele.tessari12@gmail.com

ssh-keygen

cat ~/.ssh/id_rsa.pub # add it to github

eval "$(ssh-agent -s)"

ssh-keygen -t rsa -b 4096 -C "ruben.malacarne@gmail.com"
Generating public/private rsa key pair.

ssh -T git@github.com

cat ~/.ssh/id_ed25519.pub
```