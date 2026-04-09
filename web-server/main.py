from store import get_categories
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3]

@app.get('/items', response_class=HTMLResponse)
def read_items():
    return """ 
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML</h1>
            <p>This is a pharaf</p>
        </body>
    </html>
    """

def run():
    get_categories()
    
if __name__ == '__main__':
    run()