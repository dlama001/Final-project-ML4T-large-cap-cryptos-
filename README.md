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




# **2.Introduction**

Large-cap cryptocurrencies are generally considered to be safe crypto investments, these are companies with a market cap of more than $10 billion. The hypothesis of this project is that the prior view of crypto assets being decorrelated with traditional assets is no longer true; While this may be true for small and mid cap cryptos, large-cap cryptos are now being used by large institutional investors as a hedge on other assets. Yet, they are currently still view as "risk on" assets, this means that have significant correlation with high risk equities. The goal of this project is to use macro-indicator assests such as precious metals, stock indexes, interest rates and forex rates to anticipate crypto movements. With this in mind, we aim to trade large-cap cryptos based on traditional finance and macro indicators.
# **3. Market Universe**
## 3.1 Instruments

For our universe, we choose five of the top large-cap cryptos. The instruments, along with their approximate market caps as of May 2022 are as follows:

    Bitcoin (BTC) - $563B
    Ethereum (ETH) - $239
    Binance Coin (BNB) - $53B
    USD_Coin (USDC-USD) - $53B
    Cardano (ADA) - $17B

## **3.2. Data Sorces**
The datasets used for this project and the market caps values are from:

    https://www.yahoo.com
    https://coinmarketcap.com
    https://fred.stlouisfed.org


# **4. Data Analysis and Modeling**

## 4.1. Feature Engineering

We used feature engineering to prepare all the macro-indcators and add additional features such as momentum, historical returns and calculate the factor betas.

    Cryto Returns - these were the lags we used to calculate return (10 lags that capture short and long term past returns)
    Factor Betas - we calculated the factor betas for each stock to include them as features for our machine learning model
    Momentum - Traders and investors have long known about the effects of momentum and have found that these effects appear across a wide variety of markets and time frames. we added momentum factors to run these strategies on every singe single currency

## 4.2. Modeling

    We used the Random Forest model which took all of the different factors and features to try to predict the next two weeks of return
    We calculated the feature importance by extracting the most important variables (indicators) affecting each of the crypto currencies
    We applied our model to test data in order to test the returns

## 4.3. Macro Indicators
For our macro-indicators we used the top 20 Indicators having a direct effect on each coin from Fred and Yahoo Finance
### 1. 
<img width="514" alt="bnb" src="https://user-images.githubusercontent.com/70610666/170155846-799d723f-ed20-4411-a34e-fa2d1ad09323.png">
### 2.
<img width="531" alt="btc" src="https://user-images.githubusercontent.com/70610666/170155885-f2c46b19-e759-48dd-a98a-cc7c59e77449.png">
### 3. 
<img width="533" alt="btjdj" src="https://user-images.githubusercontent.com/70610666/170155904-76ca2079-0133-4a4a-b514-fbfe393eb2f9.png">
### 4.
<img width="516" alt="eht" src="https://user-images.githubusercontent.com/70610666/170155938-d5468c6d-cc5f-46c8-af2b-27340a9ae92d.png">
### 5.
<img width="524" alt="usdt" src="https://user-images.githubusercontent.com/70610666/170155974-18c352b0-4786-4c9a-b2f3-421bd125ece0.png">







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
