from flask import Flask, url_for, request
from toma import lemma_search, lexical_search
app = Flask(__name__)

@app.route('/search_site/')
def search_site():
    lines = ''
    for line in open('search.html'):
        lines += line + '\n'
    return lines

@app.route('/lexical_search/')
def lexical_search_handler():
    query = request.args.get('query', '')
    author = request.args.get('author', '')
    fromyear = request.args.get('fromyear', '')
    tillyear =  request.args.get('tillyear', '')
    return lexical_search(query, author, fromyear, tillyear)

@app.route('/lemma_search/')
def lemma_search_handler():
    query = request.args.get('query', '')
    author = request.args.get('author', '')
    fromyear = request.args.get('fromyear', '')
    tillyear =  request.args.get('tillyear', '')
    return lemma_search(query, author, fromyear, tillyear)


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=9000,debug = True)

