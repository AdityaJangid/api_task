# api_task 

###### Problem Statement 

Implement a server which should be capable of doing the following:

   - Exposes a GET API as "api/request?connId=19&timeout=80" 
 This API will keep the request running for provided time on the server side. After the successful completion of the provided time it should return {"status":"ok"}

   - Exposes a GET API as "api/serverStatus" 
 This API returns all the running requests on the server with their time left for completion. E.g {"2":"15","8":"10"} where 2 and 8 are the connIds and 15 and 10 is the time remaining for the requests to complete (in seconds).

   - Exposes a PUT API as "api/kill" with payload as {"connId":12} 
This API will finish the running request with provided connId, so that the finished request returns {"status":"killed"} and the current request will return {"status":"ok"}. If no running request found with the provided connId on the server then the current request should return "status":"invalid connection Id : <connId>"}

You can try running your application with curl for testing. Try to implement the solution which would be efficient and scalable.
Bonus Points
 
- We would like you to implement the above by building a socket server accepting HTTP requests. 
- there is also a bonus points if you have a UI to show 
 
Use any language you are comfortable with (python or nodejs preferably) 


### requirements 

#### `pip install flask` ##
#### `pip install flask-restfull` ##
#### `sudo apt-get install git git-core` ##


### Install the Api ###



#### `git clone https://github.com/AdityaJangid/api_task.git`

#### `cd api_task`

#### `python task.py`


### Every thing is set now


### Example

`1. http://localhost:5000/api/request?connid=19&tiomeout=60` to create a new request.
`2. http://localhost:5000/api/serverStatus` to show the server status
`3 http://localhost:5000/api/kil?connId=19 with payload as {"connId":"19"}` to kill the ongoing request with id 19.



