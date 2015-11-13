from flask import Flask, request
from StaticMap import StaticMap

app = Flask(__name__)

@app.route('/')
def index():
    lat = float(request.args.get('lat'))
    lon = float(request.args.get('lon'))
    zoom = int(request.args.get('zoom'))
    width = int(request.args.get('width'))
    height = int(request.args.get('height'))
    
    map = StaticMap(center=(lat,lon),zoom=zoom, width=width, height=height)
    
    imageName = "static/test.png"
    
    map.createBaseMap()
    map.addCenter()
    
    map.saveMap(imageName)
    
    #print "Content-Type: text/html"
    #print
    return '<img src="/%s" />' % imageName

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)