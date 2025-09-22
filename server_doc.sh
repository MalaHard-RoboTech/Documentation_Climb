#!/bin/bash
PORT=7002
python3 -m http.server $PORT &
sleep 2
xdg-open "http://localhost:$PORT/1_climb_robot_thesis/🧠-main_documentation.html"
echo "Server avviato su http://localhost:$PORT"
echo "Premi Invio per chiudere..."
read

