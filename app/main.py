from fastapi import FastAPI

app = FastAPI()


@app.get("/my-firts-api")
def get_tablas():

    import pandas as pd
    url ='https://github.com/emm-ac/proyecto1_sup07/blob/dad400563892759d73987edc3d1c0a21e925721b/Netflix_ok.csv'
    tablas = pd.read_csv(url)

    return tablas