from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel

model_name = "deepset/roberta-base-squad2"

# a. Initialize models in case the model has not been loaded yet.
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'who is the main character of this story?',
    'context': '''Centuries ago, mankind was slaughtered to near extinction by monstrous humanoid creatures called titans, forcing humans to hide in fear behind enormous concentric walls. What makes these giants truly terrifying is that their taste for human flesh is not born out of hunger but what appears to be out of pleasure. To ensure their survival, the remnants of humanity began living within defensive barriers, resulting in one hundred years without a single titan encounter. However, that fragile calm is soon shattered when a colossal titan manages to breach the supposedly impregnable outer wall, reigniting the fight for survival against the man-eating abominations.

After witnessing a horrific personal loss at the hands of the invading creatures, Eren Yeager dedicates his life to their eradication by enlisting into the Survey Corps, an elite military unit that combats the merciless humanoids outside the protection of the walls. Based on Hajime Isayama's award-winning manga, Shingeki no Kyojin follows Eren, along with his adopted sister Mikasa Ackerman and his childhood friend Armin Arlert, as they join the brutal war against the titans and race to discover a way of defeating them before the last walls are breached.

(Source: MAL Rewrite)
    '''
}
print(nlp)
res = nlp(QA_input)
print(res)

app=FastAPI() # instantiate fastAPI object

class Item(BaseModel):
    question:str | None = None
    context:str | None = None

@app.post('/')
async def res(
        item:Item
    ):
    QA_input = {
        'question':item.question,
        'context':item.context
    }
    try: 
        res = nlp(QA_input)
    except:
        res = {'answer':'Cannot be processed, please check whether the context or question is empty'}
        return {'result':res}
    return {'result':res}
