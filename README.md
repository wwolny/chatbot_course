# Polish based Chatbot implemented using RASA framework and SpaCy embeddings
Project created for Bachelor Thesis at Warsaw University of Technology.


#### Install
Run in terminal `./setup.sh`. It will install Java, GRAKN, NGROK, Conda virtual environment, SpaCy and Morfeusz.

In order to run only specific parts refer to the `setup.sh` script.

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
