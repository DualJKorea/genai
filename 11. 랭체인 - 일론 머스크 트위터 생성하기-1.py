import openai
import os 
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI()

import json
import time
from io import BytesIO

with open("for-tune.jsonl","rb") as my_file:
    training_file = openai.files.create(
    file=my_file,
    purpose='fine-tune'
    )

try:
    job = openai.fine_tuning.jobs.create(
        training_file=training_file.id, model="gpt-3.5-turbo")
except Exception as e:
    print(e)
    
start = time.time()

while True:
    ftj = openai.fine_tuning.jobs.retrieve(job.id)
    if ftj.fine_tuned_model is None:
        print("Waiting for fine-tuning to complete... \n")
        print(f"Elapsed: {time.time() - start}", end="\r", flush=True)
        time.sleep(10)
    else:
        print("\n")
        print(ftj.fine_tuned_model, flush=True)
        break
         