import MySQLdb as mdb
from collections import Counter
import sys
import codecs


def queryDB(str):
    con = mdb.connect('localhost', 'root', 'G8l8GmeX', 'Ben-Yehuda', charset='utf8');

    with con:

        cur = con.cursor()
        cur.execute(str)

        rows = cur.fetchall()
        response = []
        for row in rows:

            response.append(row)
    return response


def gen_lexical_html(response,originalquery):
    out = ''
    for row in response:
        out += '<div class="alert alert-warning">' +'<a href="' + row[4] +'"> link to original text </a> | '+ row[8].replace(originalquery, '<u>'+originalquery+'</u>') + ' | ' + row[5] + ' | ' +  row[6] + '</div>'
    return out


def gen_lemma_html(response):
    out = '<table class="table"><tr><td>count</td><td>lemma</td></tr>'
    response = map(lambda x:x[0],response)
    counter = Counter(response)

    for row in counter:
        out += '<tr><td>'+str(counter[row])+'</td><td><a onclick="no_refresh_lexsearch(\''+row+'\')">'+row+'</td></tr>'
    return out


def lexical_search(query, author = None, from_year = None, till_year = None):
    sys.stdout.flush()
    SQLQuery = 'select tokens.workID, tokens.SentenceID, tokens.Index, works.workID, works.BYlink, works.author, works.work_name, works.year_written, sentences.sentence from tokens, works, sentences where tokens.word = "'+query+'" '
    #if from_year:
        #SQLQuery += 'AND works.year_written >= ' +str(from_year) + ' '
    #if till_year:
        #SQLQuery += 'AND works.year_written <= ' +str(from_year) + ' '

    SQLQuery += 'and works.workID = tokens.WorkID and works.workID = sentences.workID and sentences.sentenceID = tokens.SentenceID limit 50'
    response = queryDB(SQLQuery)
    print len(response)
    return gen_lexical_html(response, query)
    #return '\n'.join(open('lexical_template').readlines())

def lemma_search(query, author, from_year, till_year):
    SQLQuery = 'select tokens.word from tokens where tokens.lemma like "'+query+'"'
    return gen_lemma_html(queryDB(SQLQuery))
    #return '\n'.join(open('lemma_template').readlines())


def test():
    answer = queryDB(open('queryExample').readline())
    print answer

if __name__ == "__main__":
    test()