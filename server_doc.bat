@echo off
set PORT=8080
start "" "http://localhost:$PORT/1_climb_robot_thesis/🧠-main_documentation.html"
python -m http.server %PORT%
pause

