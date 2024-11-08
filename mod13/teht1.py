from flask import Flask
app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = int(luku)
    for i in range(2, (luku // 2) + 1):
        if luku % i == 0:
            return {"Number": luku, "isPrime": False}
    else:
        return {"Number": luku, "isPrime": True}

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)