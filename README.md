# Welcome to project from implemention test

this project has the propose to be used with different implementation tools


## SET ENVIRONMENT VARIABLES (LINUX)

Well, before start, create a .env file into root project folder. In this file, add the following variables:

    PYTHONPATH=${PWD}
    PYTHONUNBUFFERED=1
    PYTHONDONTWRITEBYTECODE=1

    # change the connection url for your chosen database.
    # Here, we use sqlite database in memory mode
    DATABASE_URL=sqlite://

After that, save .env file and open you system terminal to run following command <code>export $(cat .env)</code>


# RUN
The project have a interest to be more easy possible to configure and run. So, after performing the initial configuration, you just need to run the project with the command:

    python3 main.py