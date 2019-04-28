# docker1
Part of QuantiPhi workshop on Cloud Computing

## Use-Case 1:

**Pull the image file directly from Docker Hub**  
`sudo docker pull dhairyashah98/web:l` 

**Create new volume for docker**  
`sudo docker volume create my-vol`

**Make sure port 5000 is open in the host machine.**  
If using AWS, edit inbound security group rule to include a new Custom TCP rule.

**Run the app using the mounted volume**  
`sudo docker run -d --mount 'type=volume,src=my-vol,dst=/usr/src/app' -p 5000:8080 dhairyashah98/web:l`

**Usage**
`localhost:5000`
Enter first name and last name in text fields

See the results in
`localhost:5000/persistant`

Stop the running container and resume it again from
`localhost:5000/persistant`
and you can see the last entered data in it

## Use-Case 2:  

This is a dockerized ebook library. It was built using flask and mysql, both are dockerized seperately. We use compose to connect between both of them.

 **Run the app**
 1) docker-compose up
 
 2)First you need to push existing databaase i.e. backend/data.sql on to mysql using mysql cli, 
 run the command: mysql --host=127.0.0.1 --port=5001 -u root -p users < data.sql
 ( default password is root)
 
 3) You can access the web app on localhost:5000
 
 
 **Ports**
 5000 is for frontend, 5001 is for server communication.
 
 **Working**
 After registration, login. You can browse books and add them to your library. 
 After that you can read any book from your library
 
 
 

