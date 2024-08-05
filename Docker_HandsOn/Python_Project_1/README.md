# Python Project with Docker

# Steps
1. Create a [Dockerfile](/DevOps/Docker_HandsOn/Python_Project_1/Dockerfile)
2. Create [app.py](/DevOps/Docker_HandsOn/Python_Project_1/app.py) which is just a sample python file with a single statement to print.
```
print("This is my first App with Docker Image")
```
3. Create a image by running the command.
```
docker build -t myfirstpythonapp .
```
4. Run Image
```
docker run myfirstpythonapp
```
5. Now let modify the [app.py](/DevOps/Docker_HandsOn/Python_Project_1/app.py) to display the working dir, for this will `import os` module and print the current working directory, just to showcase that the `app.py` is running in container.
```
import os
print("Current Dir is ", os.getcwd())
```
6. As we have modified the file(s) we have to rebuild the image to reflect the changes.

