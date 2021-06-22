from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
async def inicio():
    contenido_html = """
    <html>
    <head>
        <title> Equipo 6</title>
    </head>
    <body>
        <h3> Bienvenidos </h3>
        <p> Este sitio pertenece al Equipo6 y mostrará los datos de los integrantes</p>
        <a href="orlando.html">orlando </a>
    </body>
    </html>
    """
    return HTMLResponse(content= contenido_html, status_code=200)