import uvicorn
from fastapi import FastAPI
import pandas as pd


app = FastAPI()


@app.get("/")
async def root():

    
    return {"message": "Elige el año para ver el catálogo: 2019 / 2020 / 2021"}



@app.get("/2019")
async def cat_2019():
    
    datos = pd.read_csv(r'/app/Netflix_ok.csv', sep=';')
    datos['date_added'] = pd.to_datetime(datos['date_added'], errors='coerce')
    datos.sort_values(by=['date_added'], inplace=True)
    datos['director'] = datos['director'].replace('Not Given',None)
    mask_2019 = datos["release_year"].str.contains("2019", na=False)
    datos_2019 = datos[mask_2019]
    catalogo2019 = datos_2019.reset_index().to_dict(orient="index")
    
    return (catalogo2019)



@app.get("/2020")
async def cat_2020():
    
    datos = pd.read_csv(r'/app/Netflix_ok.csv', sep=';')
    datos['date_added'] = pd.to_datetime(datos['date_added'], errors='coerce')
    datos.sort_values(by=['date_added'], inplace=True)
    datos['director'] = datos['director'].replace('Not Given',None)
    mask_2020 = datos["release_year"].str.contains("2020", na=False)
    datos_2020 = datos[mask_2020]
    catalogo2020 = datos_2020.reset_index().to_dict(orient="index") 
    
    return (catalogo2020)



@app.get("/2021")
async def cat_2021():
    
    datos = pd.read_csv(r'/app/Netflix_ok.csv', sep=';')
    datos['date_added'] = pd.to_datetime(datos['date_added'], errors='coerce')
    datos.sort_values(by=['date_added'], inplace=True)
    datos['director'] = datos['director'].replace('Not Given',None)
    mask_2021 = datos["release_year"].str.contains("2021", na=False)
    datos_2021 = datos[mask_2021]
    catalogo2021 = datos_2021.reset_index().to_dict(orient="index")
    
    return (catalogo2021)