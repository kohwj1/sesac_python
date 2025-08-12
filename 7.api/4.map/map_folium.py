from flask import Flask, render_template, request
import folium

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    latitude = 37.5195  # Default latitude for 63 Building
    longitude = 126.9405  # Default longitude for 63 Building

    if request.method == 'POST':
        latitude = float(request.form.get('latitude', latitude))
        longitude = float(request.form.get('longitude', longitude))
    # Create a map centered at the given location
    m = folium.Map(location=[latitude, longitude], zoom_start=15)

    # Add a marker at the given location
    folium.Marker([latitude, longitude], popup="Selected Location").add_to(m)

    # Render the map
    map_html = m._repr_html_()

    return render_template('map.html', latitude=latitude, longitude=longitude, map_html=map_html)

if __name__ == '__main__':
    app.run(debug=True)
