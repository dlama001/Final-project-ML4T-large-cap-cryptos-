---
#Final Project 
##Top 5 large cap crypto trading with macroeconomical variable"
Team: Digital Gold Digger
date: "04/01/2022"
---


Digital Gold Digger

By Estrella Moreira, Dawa Lama, Zhi Li, Ali Salem


---
# **1. Overview on project:**

We are here making trading strategies of top 5 cryptos they are Bitcoin, Ethereum, USDT Tether, USD Coin and Binance Coin with relationship with macroeconomic variable they are Federal fund interest rate, dallor exchnage rate, and S&P 500 index. Here our main aim is to see the effect of macroeconomic variables on trading of top 5 cryptos and we have calculate risk factor related to large cap cryptos trading.

----

Instruments use for trading(Top 5 large-cap Cryptos) have used here as our main instruments.
|S.N.| Symbol (Ticker)|	Crypto Name |	
|----|----------------|-------------|
|1	 |BTC             |	Bitcoin	    |
|2	 |ETH	          | Ethereum	|
|3	 |ADA-ETH	      | Cardano	    |
|4	 |BNB	          | Binance Coin|	
|5	 |USDC	          | USD Coin	|
Data reported time : 04/05/2022, 14:20
Data source: https://coinmarketcap.com/

---

Macroeconomic variables use for project
|s.n.    |       Name|  Data type|
|--------|-----------|-----------|
|1|Federl fund Interest rate| Daily|
|2|Gold Price|daily/Per ounce|
|3|S&P 500 data| Daily|
|4|Euro Exchange rate| Daily|



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
