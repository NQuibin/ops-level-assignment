# ops-level-assignment
Ops Level Take Home Assignment
* Nikki Quibin
* nikki.quibin@gmail.com

## Setup
### Requirements
* [docker](https://www.docker.com/products/docker-desktop) (stable version)
* [Python3.8.5](https://www.python.org/downloads/) (install with brew if in macos)
* [Git](https://git-scm.com/downloads)
* API Clients such as [Insomnia](https://insomnia.rest/) or [Postman](https://www.postman.com/)
    * Can also use `curl` command.

### Steps
1. Clone repo.
    ```
    git clone https://github.com/NQuibin/ops-level-assignment.git
    ```
2. Create python virtual environment and enter.
    ```
    python3.8 -m venv venv
    source venv/bin/activate 
    ```
3. Install python packages.
    ```
    pip install -r requirements.txt
    ```
4. Run mongodb container with docker
    ```
    docker-compose up --build
    ```
    or in detached mode (won't be able to see logs).
    ```
    docker-compose up --build -d mongodb
    ```
5. Run local server with uvicorn
    ```
    uvicorn app.main:app --reload
    ```

6. Open API docs for more information for each endpoint:
    * http://127.0.0.1:8000/docs (Swagger)
    * http://127.0.0.1:8000/redoc (ReDoc)
   
### Notes
* API is created with the [FastAPI](https://fastapi.tiangolo.com/)
framework.
