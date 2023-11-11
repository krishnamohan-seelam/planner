## Learning Fast API 

- Either clone/download the application from github or checkout the planner-sql branch
>https://github.com/krishnamohan-seelam/planner.git
> cd planner 
- Create a virtual enviroment in the planner directory
> For Linux machines - python3 -m venv venv
> source venv/bin/activate
- Install the required python packages
> pip install -r requirements.txt
- Create a .env file in planner directory
- Add an entry ENV_STATE="DEV" 
- Run the application using the below comman
> uvicorn main:app