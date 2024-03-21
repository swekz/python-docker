
#--install requirements-
pip install -r requirements.txt

#----replace this mongodb connection in login.py while running locally without using docker
client = pymongo.MongoClient("mongodb://localhost:27017/") 

#---replace this mongodb connection in login.py while running code through docker image and container
client = pymongo.MongoClient("mongodb://host.docker.internal:27017/")    

#----run the code in terminal
python3 login.py run        #---in windows use only python , python3 only in linux or ubuntu


#----create docker image
docker build -t my-python-app .

#---create and run container
docker run -p 4000:4000 -d --name test my-python-app

#----then in postman test the api's 
localhost:4000/signup   #---for signup
localhost:4000/login    #---for login


