import pandas as pd
import altair as alt
import streamlit as st

# Loading the dataset
def load_data():
    url = "https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/licenses_fall2022.csv"
    return pd.read_csv(url)

df = load_data()

# Data cleaning
df['Original Issue Date'] = pd.to_datetime(df['Original Issue Date'], errors='coerce')
df_time = df.dropna(subset=['Original Issue Date'])


df_time['Year'] = df_time['Original Issue Date'].dt.year


#Yearly License Counts by License Type 
st.header("Yearly License Counts by License Type")
st.write("Visualizing yearly trends of license counts by license type.")

# Selecting a license type from dropdown
license_types = df_time['License Type'].dropna().unique()
selected_license_type = st.selectbox("Select a license type:", license_types)

# Filtering and grouping data by selected license type and year
license_type_counts = df_time[df_time['License Type'] == selected_license_type].groupby(['License Type', 'Year']).size().reset_index(name='Count')

# Creating a line chart
line_chart = alt.Chart(license_type_counts).mark_line(point=True).encode(
    x=alt.X('Year:O', title="Year"),
    y=alt.Y('Count:Q', title="Number of Licenses"),
    tooltip=['Year', 'Count']
).properties(title=f"Yearly License Counts for {selected_license_type}", width=800, height=400)

st.altair_chart(line_chart)

#  Top 10 Cities by License Status
st.header("Top 10 Cities for License Status")
st.write("Visualizing the top 10 cities based on the selected license status.")

# Selecting a license status
license_status_options = df['License Status'].dropna().unique().tolist()
selected_status = st.selectbox('Select License Status', license_status_options)

df_filtered = df[df['License Status'] == selected_status]
city_counts = df_filtered.groupby('City').size().reset_index(name='Count')

top_n = 10  
city_counts = city_counts.sort_values('Count', ascending=False).head(top_n)

# Creating a bar chart
bar_chart = alt.Chart(city_counts).mark_bar().encode(
    x='City:N', 
    y='Count:Q', 
    color='City:N',  
    tooltip=['City', 'Count:Q'] 
).properties(
    width=800,
    height=400
)

st.altair_chart(bar_chart, use_container_width=True)

line_chart.save('chart1.json')
bar_chart.save('chart2.json')

