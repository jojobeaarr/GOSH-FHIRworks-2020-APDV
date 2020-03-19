from flask import Flask, request, send_from_directory
from graph import gen_graph

app = Flask(__name__, static_url_path='')


@app.route('/graph', methods=['GET'])
def root():
    observation = request.args.get('observation')
    gen_graph(observation)
    return send_from_directory(
            '', 'result.png', cache_timeout=9999999
        )



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
