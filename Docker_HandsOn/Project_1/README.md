# Docker Project 1

1. Install Docker
2. Clone Repo
   1. https://github.com/detronetdip/E-commerce.git
3. Execute following command
   1. Build database docker image
   ```
   docker build -t app_database -f Dockerfile .
   ```
   2. build app docker image
   ```
   docker build -t app -f Dockerfile .
   ```
   3. create network
   ```
    docker create network test
   ```
   4. run database
   ```
   docker run --name database -e MYSQL_ROOT_PASSWORD='passwd' --network test --hostname db -p 9306:3306 app_database
   ```
   5. run application
   ```
   docker run --name web_app --network ecommerce -p 3000:80 app
   ```