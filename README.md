Course work Team 1
=====

**NOTE**: This project uses `poetry` for controlling virtual env and dependencies,  
once installed run `poetry install && poetry shell` before running scripts.

### Contents

* `server.py` run first, this is a server of multi-agent system
* `client.py` run second, reads sensors data (from .csv file) and sends to server
* `data_prepare_agent.py` agent that prepares data
* `failure_estimation_agent.py` agent that makes a prediction
* `sensors.csv` a file with data from sensors

#### additional stuff
* `predictive_maintenance.csv` dataset used for training
* `NN.h5` pretrained model
* `course_work.ipynb` Jypiter notebook for model training
