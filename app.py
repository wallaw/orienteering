import logging  , random, os
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

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
    {"id": 1.16, "name": "Ant Hill", "url": "https://svgshare.com/i/17gc.svg"},
    {"id": 2.1, "name": "Cliff", "url": "https://svgshare.com/i/17i1.svg"},
    {"id": 2.2, "name": "Rock Pillar", "url": "https://svgshare.com/i/17i4.svg"},
    {"id": 2.3, "name": "Cave", "url": "https://svgshare.com/i/17fb.svg"},
    {"id": 2.4, "name": "Boulder", "url": "https://svgshare.com/i/17i5.svg"},
    {"id": 2.5, "name": "Boulder Field", "url": "https://svgshare.com/i/17gC.svg"},
    {"id": 2.6, "name": "Boulder Cluster", "url": "https://svgshare.com/i/17g1.svg"},
    {"id": 2.7, "name": "Stone Ground", "url": "https://svgshare.com/i/17ni.svg"},
    {"id": 2.8, "name": "Bare Rock", "url": "https://svgshare.com/i/17gg.svg"},
    {"id": 2.9, "name": "Narrow Passage", "url": "https://svgshare.com/i/17iE.svg"},
    {"id": 2.10, "name": "Trench", "url": "https://svgshare.com/i/17i6.svg"},
    {"id": 4.1, "name": "Open Land", "url": "https://svgshare.com/i/17mf.svg"},
    {"id": 4.2, "name": "Semi Open Land", "url": "https://svgshare.com/i/17mS.svg"},
    {"id": 4.3, "name": "Forest Corner", "url": "https://svgshare.com/i/17nY.svg"},
    {"id": 4.4, "name": "Clearing", "url": "https://svgshare.com/i/17oB.svg"},
    {"id": 4.5, "name": "Thicket", "url": "https://svgshare.com/i/17n3.svg"},
    {"id": 4.6, "name": "Linear Thicket", "url": "https://svgshare.com/i/17nh.svg"},
    {"id": 4.7, "name": "Vegetation Boundary", "url": "https://svgshare.com/i/17o0.svg"},
    {"id": 4.8, "name": "Copse", "url": "https://svgshare.com/i/17n2.svg"},
    {"id": 4.9, "name": "Prominent Tree", "url": "https://svgshare.com/i/17nM.svg"},
    {"id": 4.10, "name": "Prominent Vegetation Feature", "url": "https://svgshare.com/i/17nX.svg"}
]




question = registros[0]

@app.route('/',methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        resposta = request.form['answer']
        app.logger.debug(resposta)

    return render_template('index.html')


@app.route('/all')
def all_route():
    return render_template('all.html',items=registros)


@app.route('/quiz_sinaletica',methods=['POST', 'GET'])
def quiz_sinaletica_route():

    global question

    points = get_points()

    question_list = get_question(registros)
    question = question_list[0]
    answers = question_list[1]

    return render_template('quiz_sinaletica.html',question=question, answers=answers,points=points)



def get_question(base_questoes):
    i = random.randint(0, len(base_questoes)-1)
    j = random.randint(0, len(base_questoes)-1)
    k = random.randint(0, len(base_questoes)-1)

    while  (j == i) :
        j = random.randint(0, len(base_questoes)-1)

    while  (i == k) or (j== k) :
        k = random.randint(0, len(base_questoes)-1)

    question = base_questoes[i]
    answers = [question['name'],base_questoes[ j]['name'],base_questoes[k]['name']]
    random.shuffle(answers)

    return [question,answers]
  
    
@app.route('/quiz_sinaletica_fast',methods=['POST', 'GET'])
def quiz_sinaletica_fast_route():
    global question
    points = get_points()

    question_list = get_question(registros)
    question = question_list[0]
    answers = question_list[1]

    return render_template('quiz_sinaletica_fast.html',question=question, answers=answers, points=points)

def get_points():
    global question

    if 'points' in session:
        points = session['points']
    else:
        session['points'] = 0
        points = 0
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == question['name']:
            points+=1
            session['points'] = points
    return points




if __name__ == '__main__':
      app.run()