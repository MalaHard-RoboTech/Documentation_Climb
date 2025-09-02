## How is it work?
The web app application is designed to monitor and control robot performance. It allow users to: 

- View real-time robot status
- Read sensor data
- Send commands from a PC to the robot
in general it's used like a GUI. and to support these functions, the interface includes several toolbars or panels, each offering specific insights and controls.
## Toolbars and Panels

| **~={Orange}Panel=~**       | ~={Orange}**Description**=~                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------- |
| ~={cyan}**Alpine**=~        | The main dashboard for visualizing the robot, selecting actions, and managing the general interactions. |
| ~={cyan}**Configuration**=~ | Allows users to adjust parameters and optimize robot settings for best performance.                     |
| ~={cyan}**Dashboard**=~     | Displays sensor readings and data from the robot and the ROS (Robot Operating System) environment.      |
| ~={cyan}**Check Board**=~   | Verifies system readiness, including voltage levels, safety checks, and other diagnostics.              |
| ~={cyan}**Inspector**=~     | A plotting environment for visualizing data trends and values through graphs.                           |
| ~={cyan}**3D Map Viewer**=~ | Renders the robot’s point cloud map for spatial awareness and navigation analysis.                      |

## Environments and the workflow

The environemt is split in the following way: 

![[web_app_schema.excalidraw]]

the workflow:
![[Alpine_workflow.excalidraw]]
## Future improvments
- add the 3D view inside the alpine display


