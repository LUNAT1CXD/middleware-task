import json
import uvicorn
import boto3

from utils import load_data, save_data
from models import OutputMessage
from config import config

from fastapi import FastAPI, Request, Response, status, Query

s3 = boto3.client('s3',
                  aws_access_key_id=config.aws_access_key_id,
                  aws_secret_access_key=config.aws_secret_access_key)

app = FastAPI()


@app.get('/')
async def hello():
    return json.loads({"hello": "hello"})


@app.post('/ingest')
async def ingest(request: Request, response_model=OutputMessage):
    try:
        # Load the payload data from request
        data = await request.json()
        # function to load the existing data
        existing_data = load_data()
        if not isinstance(data, list):
            data = [data]
        existing_data.extend(data)
        existing_data.sort(key=lambda x: x.get('time', 0))
        # this function updates as well as returns the size of file
        total_size = save_data(existing_data)
        # Printing size just for dev ref
        print(total_size, ":", "Printing size just for dev ref")
        # if total size of file is greater then 1 MB it'll upload it to s3
        if total_size > 1024:
            # File will be uploaded to s3
            s3.upload_file('data.json', config.aws_bucket_name,
                           "kartik/kartik.json")
        return OutputMessage(success=True,
                             data=existing_data,
                             message="Payload saved successfully")
    except Exception as e:
        Response.status_code = status.HTTP_400_BAD_REQUEST
        return OutputMessage(success=False, message=str(e))


@app.get('/ingest')
async def get_ingest(start: int = Query(...), end: int = Query(...), text: str = Query(None)):
    logs_object = s3.get_object(
        Bucket=config.aws_bucket_name, Key="kartik/kartik.json")
    retrieved_data = json.loads(logs_object['Body'].read())
    print(retrieved_data)
    filtered_data = [
        data for data in retrieved_data if start <= data['time'] <= end]
    if text:
        filtered_data = [log for log in filtered_data if text in log['log']]
    return OutputMessage(success=True,
                         data=filtered_data)

if __name__ == "__main__":
    uvicorn.run(app=app)
