# docker1
Part of QuantiPhi workshop on Cloud Computing

## Use-Case 1:   
![image](https://user-images.githubusercontent.com/31621421/56863551-3df61a00-69d5-11e9-8cfc-e13ce20d880e.png)
![image](https://user-images.githubusercontent.com/31621421/56863571-9e855700-69d5-11e9-83d2-26a1a9733d01.png)  
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
 run the command: `mysql --host=127.0.0.1 --port=5001 -u root -p users < data.sql`  
 ( default password is root)   
 
 3) You can access the web app on `localhost:5000`   
 
 
 **Ports**
 5000 is for frontend, 5001 is for server communication.  
 
 **Working**  
 ![Screenshot from 2019-04-28 16-57-20](https://user-images.githubusercontent.com/19796784/56863693-4ea78f80-69d7-11e9-90fd-31ef7e0e8b9c.png)  
![Screenshot from 2019-04-28 16-57-53](https://user-images.githubusercontent.com/19796784/56863697-549d7080-69d7-11e9-8c4f-ec2c4ed4e495.png)  
![Screenshot from 2019-04-28 16-58-09](https://user-images.githubusercontent.com/19796784/56863698-55ce9d80-69d7-11e9-9b90-ad9d462cd439.png)  
 
 
 After registration, login. You can browse books and add them to your library.   
 After that you can read any book from your library  
 
 
 

