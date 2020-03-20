from flask import Flask, request, send_from_directory
from graph import gen_graph

app = Flask(__name__, static_url_path='/static')


@app.route('/graph', methods=['GET'])
def root():
    observation = request.args.get('observation')
    # print(observation)
    img_id = gen_graph(observation)
    # return send_from_directory('', f'result.png', cache_timeout=9999999)
    return f"/static/{img_id}.png"

@app.route('/')
def index():
    return send_from_directory("", "index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
