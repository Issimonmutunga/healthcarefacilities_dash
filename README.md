🏥 Healthcare Facilities Dashboard
This is a Dash-based web application that visualizes healthcare facilities in Kenya using data from the EnergyData.info CKAN API and spatial shapefiles for county boundaries.

📌 Features
Interactive map displaying healthcare facilities by county

Facility names shown on hover

County boundaries overlayed using a shapefile

Built using Python, Dash, Plotly, GeoPandas, and CKAN API

📊 Data Sources
Healthcare Facilities: EnergyData.info API

County Boundaries: Shapefile loaded from a local path (County.shp)

🛠 Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/healthcare-dashboard.git
cd healthcare-dashboard
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Ensure you have the shapefile

Place the County.shp and its related files (.shx, .dbf, etc.) in the shp/ directory or update the path in the script.

🚀 Run the App
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:8050/ in your browser.

📦 Requirements
You can generate a requirements.txt using:

bash
Copy
Edit
pip freeze > requirements.txt
Example dependencies:

txt
Copy
Edit
dash
pandas
geopandas
plotly
requests
📍 Screenshot

![alt text](<Screenshot 2025-05-25 132149.png>)