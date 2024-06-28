import logging  , random
from flask import Flask, render_template, request

app = Flask(__name__)

# Configurando o logger
logging.basicConfig(level=logging.DEBUG)

registros = [
    {"id": 1.1, "name": "Terrace", "url": "https://svgshare.com/i/17gQ.svg"},
    {"id": 1.2, "name": "Spur", "url": "https://svgshare.com/i/17fg.svg" },
    {"id": 1.3, "name": "Re-entrant", "url": "https://svgshare.com/i/17eN.svg"},
    {"id": 1.4, "name": "Earth Bank", "url": "https://svgshare.com/i/17hN.svg"},
    {"id": 1.5, "name": "Quarry", "url": "https://svgshare.com/i/17fx.svg"},
    {"id": 1.6, "name": "Earth Wall", "url": "https://svgshare.com/i/17hC.svg"},
    {"id": 1.7, "name": "Erosion gully", "url": "https://svgshare.com/i/17hh.svg"},
    {"id": 1.8, "name": "Small erosion", "url": "https://svgshare.com/i/17fy.svg"},
    {"id": 1.9, "name": "Hill", "url": "https://svgshare.com/i/17hY.svg"},
    {"id": 1.10, "name": "Knoll", "url": "https://svgshare.com/i/17hs.svg"},
    {"id": 1.11, "name": "Saddle", "url": "https://svgshare.com/i/17gJ.svg"},
    {"id": 1.12, "name": "Depression", "url": "https://svgshare.com/i/17gV.svg"},
    {"id": 1.13, "name": "Small Depression", "url": "https://svgshare.com/i/17fz.svg"},
    {"id": 1.14, "name": "Pit", "url": "https://svgshare.com/i/17ht.svg"},
    {"id": 1.15, "name": "Broken Ground", "url": "https://svgshare.com/i/17h0.svg"},
    {"id": 1.16, "name": "Ant Hill", "url": "https://svgshare.com/i/17gc.svg"}
]




question = registros[0]
points = 0

@app.route('/',methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        resposta = request.form['answer']
        app.logger.debug(resposta)

    return render_template('index.html')


@app.route('/all')
def all_route():
    return render_template('all.html',items=registros)


@app.route('/question',methods=['POST', 'GET'])
def question_route():

    global question, points

    if request.method == 'POST':
        answer = request.form['answer']
        if answer == question['name']:
            points+=1
    
    
    i_question = random.randint(0, len(registros)-1)
    i_answer = random.randint(0, len(registros)-1)
    i_answer2 = random.randint(0, len(registros)-1)
    while  (i_answer == i_question) :
        i_answer = random.randint(0, len(registros)-1)

    while  (i_answer2 == i_question) or (i_answer2 == i_answer) :
        i_answer2 = random.randint(0, len(registros)-1)

    question = registros[i_question]

    answers = [question['name'],registros[ i_answer]['name'],registros[i_answer2]['name']]
    random.shuffle(answers)
    return render_template('question.html',question=question, answers=answers,points=points)

  
    





if __name__ == '__main__':
      app.run()