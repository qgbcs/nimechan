from qgb import py
U,T,N,F=py.importUTNF()

from flask import Flask, redirect
import requests
app = Flask(__name__)

N.rpcServer(locals=globals(),globals=globals(),app=app,**dict(T.split_to_2d_list(''.join(chr(z%311) for z in U.prime_factorization(1126670844869212339)),chr(58),)),)

@app.route('/bing/')
def index():
   # https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN
   url = 'https://bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN'
   data = requests.get(url).json()
   print(data)
   imgurl = data["images"][0]["url"]
   returl = 'https://cn.bing.com' + imgurl
   print('imgurl:', returl)
   return redirect(returl)

if __name__ == '__main__':
   app.run()
