import io
import sys
import folium
from PyQt5 import QtWidgets, QtWebEngineWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ## tiles 종류 : OpenStreetMap(X), Stamen Toner(O), Stamen Terrain(O), cartodbpositron(O)
    m = folium.Map(location=[37.564214, 127.001699], tiles="cartodbpositron", zoom_start=11)

    data = io.BytesIO()
    m.save(data, close_file=False)

    w = QtWebEngineWidgets.QWebEngineView()
    w.setHtml(data.getvalue().decode())
    w.resize(640, 480)
    w.show()

    sys.exit(app.exec_())