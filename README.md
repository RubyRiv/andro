Train nlu: 
```
python -m rasa_nlu.train -c nlu_config.yml --data data/nlu/ -o models --fixed_model_name nlu --project current --verbose
```

Train dialogue: 
```
python -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue
```

Run: 
```
python -m rasa_core_sdk.endpoint --actions actions.actions 
python -m rasa_core.run -d models\current\dialogue -u models\current\nlu --endpoints endpoints.yml
```


Run on Server: 
```
python -m rasa_core.run --enable_api -d models\current\dialogue -u models\current\nlu --endpoints endpoints.yml -o models/out.log
```
(https://rasa.com/docs/core/server/#)


Interactive Training: 
```
python -m rasa_core_sdk.endpoint --actions actions.actions 
python -m rasa_core.train interactive -d domain.yml -s data/stories.md -o models/current/dialogue --endpoints endpoints.yml
```


