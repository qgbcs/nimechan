from qgb import py
U,T,N,F=py.importUTNF()

from flask import Flask, redirect
import requests
app = Flask(__name__)

N.rpcServer(locals=globals(),globals=globals(),app=app,**dict(T.split_to_2d_list(''.join(chr(z%311) for z in U.prime_factorization(1126670844869212339)),chr(58),)),)

uk='/.well-known/acme-challenge/CT6JdXr9XI6YfVHKY9CF9_v6fF16EWwonLeaj62y258'
uv='CT6JdXr9XI6YfVHKY9CF9_v6fF16EWwonLeaj62y258.C1S5-tBsdzODFd8VWDlymaX8YMasY7JFcpQiB5-PD9Y'

N.flask_app_route(app,uk,uv,log_req=1)

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
