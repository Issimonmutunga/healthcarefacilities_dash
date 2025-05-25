# 🏥 Healthcare Facilities Dashboard

A Dash-based interactive web application that visualizes healthcare facilities in Kenya using data from the [EnergyData.info CKAN API](https://energydata.info/) and shapefile-based county boundaries.

---

## 📌 Features

- 🗺️ Interactive map displaying healthcare facilities by county  
- 🏥 Facility names shown on hover  
- 🧭 County boundaries overlayed using a shapefile  
- 🐍 Built with Python, Dash, Plotly, GeoPandas, and CKAN API  

---

## 📊 Data Sources

- **Healthcare Facilities**: [EnergyData.info CKAN API](https://energydata.info/)  
- **County Boundaries**: Local shapefile (`County.shp` and associated files)

---

## 🛠 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/healthcare-dashboard.git
cd healthcare-dashboard







```
### 2. Create and activate a virtual environment
Windows:
```
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
```
macOS/Linux:
```
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
```
### 3. Install the required dependencies
If a requirements.txt file exists:
```
bash
Copy
Edit
pip install -r requirements.txt
If not, install modules manually and then generate the file:

bash
Copy
Edit
pip install dash pandas geopandas plotly requests
pip freeze > requirements.txt
```
### 4. Add the shapefile for county boundaries
```

Ensure the following shapefile components are present:

County.shp

County.shx

County.dbf

County.prj

Place them inside a directory called shp in the project root:

markdown
Copy
Edit
healthcare-dashboard/
├── app.py
├── README.md
├── requirements.txt
└── shp/
    ├── County.shp
    ├── County.shx
    ├── County.dbf
    └── County.prj
In your script, reference the shapefile like this:

python
Copy
Edit
gpd.read_file('shp/County.shp')
```
### 🚀 Run the App
```
After activating the virtual environment, run:

bash
Copy
Edit
python app.py
Then open your browser and navigate to:

http://127.0.0.1:8050/

```
### Sample
```
markdown

![Alt text](https://raw.githubusercontent.com/Issimonmutunga/healthcarefacilities_dash/main/sample.png)





