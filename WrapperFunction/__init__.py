import azure.functions as func
import fastapi
from dotenv import load_dotenv
import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

load_dotenv()

app = fastapi.FastAPI()

@app.get("/sample")
async def index():
    return {"Name": os.getenv("Name")}
    # return {
    #     "AzureWebJobsStorage": os.getenv("AzureWebJobsStorage"),
    #     "name": os.getenv("https://fasttry4keyvault.vault.azure.net/secret/name"),
    # }


@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": os.getenv("Name"),
    }
