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
Enter first name and last name in text fields  
`localhost:5000`  
![image](https://user-images.githubusercontent.com/31621421/56863551-3df61a00-69d5-11e9-8cfc-e13ce20d880e.png)   

See the results in
`localhost:5000/persistant`   
![image](https://user-images.githubusercontent.com/31621421/56863571-9e855700-69d5-11e9-83d2-26a1a9733d01.png)     


Stop the running container and resume it again from  
`localhost:5000/persistant`  
and you can see the last entered data in it  

## Use-Case 2:  

