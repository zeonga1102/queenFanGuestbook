from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://#####################################')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    nickname = request.form['nickname_give']
    comment = request.form['comment_give']

    doc = {
        'nickname': nickname,
        'comment': comment
    }

    db.guestbook.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    guestbookList = list(db.guestbook.find({}, {'_id': False}))
    return jsonify({'guestbook': guestbookList})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)