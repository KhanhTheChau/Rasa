# Chatbot DD

### 1. Create NLU data

1.1 Edit data in `dataset/data.yaml`
1.2 Export data with command

```bash
python scripts/export_data.py
```

1.3 Edit `data/stories.yml` (optional)

### 2. Train rasa (NLU & Core)

#### 2.1 Train with **fasttext** pipeline (recommended)

- Download [cc.vi.300.bin](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.vi.300.bin.gz), move it to `.cache/fasttext`

```bash
rasa train --config config/fasttext.yml
```

#### 2.2 Train with other pipline

```bash
rasa train --config {config_file}
```

### 2.3 Train nlu only

```bash
rasa train nlu --config {config_file}
```

### 2.4 Test your assistant

```bash
rasa shell
# or
rasa shell nlu
```

### 3. Evaluate NLU

Example: 5 folds CV

```bash
rasa test nlu --config config/fasttext.yml --cross-validation --runs 5 --fold 5 --out results/fasttext
```

or run all configs, see `test_models.bat`

```bash
rasa test nlu --config config/custom.yml --cross-validation --runs 5 --fold 5 --out results/vectorcount
rasa test nlu --config config/fasttext.yml --cross-validation --runs 5 --fold 5 --out results/fasttext
rasa test nlu --config config/bert.yml --cross-validation --runs 5 --fold 5 --out results/bert
rasa test nlu --config config/phobert_base.yml --cross-validation --runs 5 --fold 5 --out results/phobert_base
rasa test nlu --config config/phobert_large.yml --cross-validation --runs 5 --fold 5 --out results/phobert_large
```

Prettify and display test result from `results/` folder

```bash
python eval.py

# Sample output
------
Model               |Acc       |Precision      |Recall 
------------------------------------------------------------
fasttext            |     0.967|          0.963|   0.96         
bert                |      0.92|           0.91|  0.901     
phobert_base        |     0.865|          0.854|  0.841     
phobert_large       |     0.863|           0.86|  0.853 
```

### 3. Install rasa x local mode

#### 3.1 Upgrade pip

```bash
pip install --upgrade pip
```

#### 3.2 Install rasa x

```bash
pip3 install rasa-x==1.0.1 --extra-index-url https://pypi.rasa.com/simple --use-deprecated=legacy-resolver
```

### 4. Deploy rasa x

- Required trained model with **{config_file}** before
```bash
rasa x --config {config_file}

# Sample output
Starting Rasa X in local mode... >
...
The server is running at http://localhost:5002/login?username=me&password=xxxxxxxxx
```
This should open a browser tab to [http://localhost:5002](http://localhost:5002) and login automatically


