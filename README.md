# Polish based Chatbot implemented using RASA framework and SpaCy embeddings
Project created for Bachelor Thesis at Warsaw University of Technology.


#### Install
Run in terminal `./setup.sh`. It will install Java, GRAKN, NGROK, Conda virtual environment, SpaCy and Morfeusz.

In order to run only specific parts refer to the `setup.sh` script. 


`pip --version`
+ If not installed run:
+ Python:
  ```
  sudo apt update
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt install python3.7
  python --version
  ```
  + pip
  ```commandline
  sudo apt install python3-pip
  pip3 --version
  ```
+ Next install python-dev:
  - `sudo apt install python3-dev python3-pip`
+ Create virtual environment:
  - `python3 -m venv --system-site-packages ./venv`
+ Activate virtual environment
  - `source ./venv/bin/activate`
+ Install RASA
  - `python -m pip install rasa-x -i https://pypi.rasa.com/simple`
+ Install SpaCy:
  - `python -m pip install -U spacy`
  + OR
  - `python -m pip install rasa[spacy]`
+ In order to install english based SpaCy model:
```
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```
+ Polish based SpaCy model IPI PAN pl_spacy_model_morfeusz for ubuntu 18.04 python 3.7:
```
wget -O - http://download.sgjp.pl/apt/sgjp.gpg.key|sudo apt-key add -
sudo apt-add-repository http://download.sgjp.pl/apt/ubuntu
sudo apt update
sudo apt install morfeusz2 python3-morfeusz2
```
  + Download the newest version of SpaCy model pl_spacy_model_morfeusz from http://zil.ipipan.waw.pl/SpacyPL
  - `python -m pip install PATH/TO/pl_spacy_model_morfeusz-x.x.x.tar.gz`
+ In order to install library version from Sigmoidal:
```
python -m pip install https://github.com/spacy-pl/spaCy/archive/pl-release/lemmatizer-tagmap-and-tests.zip
python -m pip install https://storage.googleapis.com/spacy-pl-public-models/pl_model-1.0.0.tar.gz
```
+ Install GRAKN database https://dev.grakn.ai/docs/running-grakn/install-and-run
+ Start GRAKN database every time before running app
  - `sudo ./grakn/grakn-core-all-linux-1.5.9/grakn server start`
+ To check if GRAKN database is running:
  - `sudo ./grakn/grakn-core-all-linux-1.5.9/grakn server status`
+ In order to turn on server:
  - `sudo ./grakn/grakn-core-all-linux-1.5.9/grakn server stop`
+ In order to load data to database (run only during setup)
```
./grakn/grakn-core-all-linux-1.5.9/grakn console --keyspace course --file <absolute-path-to-knowledge_base/schema.gql>
python knowledge_base/migrate.py
```
+ Train chatbot
  - `python -m rasa train`
+ Run RASA action
  - `python -m rasa run actions`
+ In order to message with chatbot run in shell
  - `python -m rasa shell`

### Usage of polish based language model with Morfeusz
In order to use Morfeusz embeddings add in file `<PATH_TO_PYTHON_ENV>/lib/python3.7/site_packages/rasa_sdk/executor.py` at the beginning `import spacy`:

    import spacy

Next change in the class `ActionExecutor` initialization method with polish model. Method should look like this:


    class ActionExecutor:
        def __init__(self):
            self.actions = {}
            if spacy.util.is_package('pl_spacy_model_morfeusz'):
                self.nlp = spacy.load('pl_spacy_model_morfeusz')
            else:
                self.nlp = None

Further on change `run()` method in `ActionExecutor` class by adding `self.nlp` to action creation.


        if utils.is_coroutine_action(action):
            events = await action(dispatcher, tracker, domain, self.nlp)
        else:
            events = action(dispatcher, tracker, domain, self.nlp)

### Chatbot test in browser
+ Download https://github.com/scalableminds/chatroom
+ Install Yarn https://classic.yarnpkg.com/en/docs/install
+ Run in downloaded directory:
    + `yarn install` (once)
    ```
    yarn watch
    yarn serve
    ```
+ In directory with chatbot source code run:
        ```
        endpoints.yml na 5055
        python -m rasa run actions
        python -m rasa run  --m ./models --endpoints endpoints.yml --credentials credentials.yml --enable-api -vv --cors <TARGET_ADDRESS_FOR_SAFE_COMMUNICATION>
        ```

+ Forward from GCP VM:
    + `ssh -i <PATH_TO_SSH> -N -L localhost:8080:localhost:8080 -l <NAME> <ADDRESS_IP>`
    + `ssh -i <PATH_TO_SSH> -N -L localhost:5005:localhost:5005 -l <NAME> <ADDRESS_IP>`

+ Setup server through terminal ssh nohup
    + `nohup <command> &`
    + Close:
      - `ps x -> kill -s 15 PID`
