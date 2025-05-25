🏥 Healthcare Facilities Dashboard
A Dash-based interactive web application that visualizes healthcare facilities in Kenya using data from the EnergyData.info CKAN API and shapefile-based county boundaries.

📌 Features
🗺️ Interactive map displaying healthcare facilities by county

🏥 Facility names shown on hover

🧭 County boundaries overlayed using a shapefile

🐍 Built with Python, Dash, Plotly, GeoPandas, and CKAN API

📊 Data Sources
Healthcare Facilities: EnergyData.info CKAN API

County Boundaries: Local shapefile (County.shp and associated files)

🛠 Installation
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/healthcare-dashboard.git
cd healthcare-dashboard
2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix/macOS:
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Prepare shapefiles
Ensure the following files are in the shp/ directory or update the path in the script:

Copy
Edit
County.shp
County.shx
County.dbf
County.prj
🚀 Run the App
bash
Copy
Edit
python app.py
Then open your browser and visit: http://127.0.0.1:8050/

📦 Requirements
You can generate your requirements.txt using:

bash
Copy
Edit
pip freeze > requirements.txt
Example dependencies:

nginx
Copy
Edit
dash
pandas
geopandas
plotly
requests
