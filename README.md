# devopsProj1_PythonServer
Python Server with Docker file and Jenkins file which will be used for CI CD pipeline


Docker Build
1) docker build -t python_server:latest .

Docker Run
2) docker run -it -v C:\xampp\htdocs\uploads:/app/uploads -v C:\xampp\htdocs\uploadsMoved:/app/uploadsMoved python_server

