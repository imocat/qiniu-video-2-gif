# coding: utf-8

from flask import Flask, request, make_response

import os
import urllib
import commands

app = Flask(__name__)

@app.route('/health')
def health():
    return 'ok'

@app.route('/handler',methods=['GET','POST'])
def handler():
    
    cmd = request.args.get('cmd', request.form.get('cmd',''))
    url = request.args.get('url', request.form.get('url',''))
    size = request.args.get('size', request.form.get('size',''))
    start = request.args.get('start', request.form.get('start','00:00:00'))
    duration = request.args.get('duration', request.form.get('duration','1'))
    rate = request.args.get('rate', request.form.get('rate','5'))
    scale = request.args.get('scale',request.form.get('scale','1'))

    input_file = 'tmp.mp4'
    output_file = 'tmp.gif'
 
    urllib.urlretrieve(url, input_file)

    cmd = 'ffmpeg -y -i %(input)s -ss %(start)s -r %(rate)s %(size)s -vf scale=%(scale)s -t %(duration)s %(output)s' % {
        'input': input_file,
        'output': output_file,
        'start': start,
        'duration': duration,
        'rate': rate,
        'size': '-s %s' % (size) if size else '',
        'scale': 'iw*%s:-1' % (scale)
    }

    print(request.query_string)
    print(cmd)

    status, output = commands.getstatusoutput(cmd)

    if status:
        resp = make_response('fail', 200)
        return resp

    with open(output_file,'rb') as fp:
        gif_content = fp.read()
        resp = make_response(gif_content, 200)
        resp.headers['content-type'] = 'image/gif'
        return resp

is_debug = int(os.getenv('DEBUG','1')) == 1
app.run(host='0.0.0.0', port=9100,debug=is_debug)