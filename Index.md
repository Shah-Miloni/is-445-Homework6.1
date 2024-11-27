
# IS 445 - Homework 6.1
## Creating Visualizations using Licenses Dataset

**Submitted By Miloni Shah (mkshah4@illinois.edu)**

**The Data:** [Licenses Dataset](https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/licenses_fall2022.csv)  
**The Analysis:** [Jupyter Notebook Analysis](https://github.com/Shah-Miloni/is-445-Homework6.1/blob/main/Workbook.py)

---

## Visualization 1

<div id="chart1-container"></div>

<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>

<script>
  vegaEmbed('#chart1-container', 'chart1.json').catch(console.error);
</script>

---

### **Writeup for Visualization 1**

#### Description  
This line chart visualizes the yearly trends of license counts by license type. The x-axis represents the years, while the y-axis shows the total number of licenses issued for each year. The user can select a specific license type from a dropdown, and the chart dynamically updates to display the trend for that selected license type over time.
#### Encoding Types  
- **X-axis (Ordinal):** Represents the years, which are shown as categorical variables to visualize yearly trends.
- **Y-axis Quantitative)**: Represents the count of licenses issued for each year.
- **Tooltip:** Displays details on the selected year and the corresponding license count.
- As this is a line chart, no color encoding is used, but the chart uses a default color scheme for the lines.  

#### Data Transformations  
The dataset was filtered based on the selected License Type, then grouped by Year to calculate the total number of licenses issued per year. Missing values were removed to ensure a clean dataset for analysis.

#### Interactivity  
A dropdown menu allows the user to select a specific license type, dynamically updating the line chart to reflect yearly trends for the chosen license type.

#### Impact of Interactivity  
The ability to select a license type helps users focus on specific trends and observe how different types of licenses have evolved over time.

#### Overlaps with Homework #7
While the same dataset was used, this visualization is not the same as previous homework. It provides a different view by focusing on yearly trends for each license type.

<div id="chart2-container"></div>
<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>


<script>
  vegaEmbed('#chart2-container', 'chart2.json').catch(console.error);
</script>

---

### **Writeup for Visualization 2**

#### Description  
This bar chart visualizes the top 10 cities based on the selected License Status. The x-axis represents the city names, while the y-axis shows the count of licenses for the selected status in each city. The chart updates dynamically based on the user's choice of license status from the dropdown menu, allowing them to explore the distribution of licenses across cities.
#### Encoding Types  
- **X-axis (Nominal):** Displays city names, representing the categorical variable of cities.
- **Y-axis (Quantitative):** Represents the count of licenses with the selected status in each city.
- **Color Nominal):** Differentiates cities using unique colors to enhance visual distinction.
- **Tooltip:** Shows the city name and corresponding license count for the selected status when hovering over the bars.
- 
#### Color Scheme  
A categorical color palette is applied to visually differentiate the cities in the chart. This ensures that each city is represented with a distinct color

#### Data Transformations  
The dataset was filtered based on the selected License Status to focus on a specific status. Afterward, the data was grouped by City, and the count of licenses for the selected status in each city was calculated. The top 10 cities were then sorted by the count of licenses and displayed on the chart.

#### Interactivity  
A dropdown menu allows the user to select a specific License Status. Upon selection, the chart dynamically updates to display the top 10 cities based on the count of licenses for that status.

#### Impact of Interactivity  
The dropdown filter enhances the interactivity of the visualization by enabling users to focus on specific license statuses, making it easier to analyze trends and distributions of license counts across cities.

#### Overlaps with Homework #7
While this visualization too uses a bar chart like one of the visualizations in the previous homeworks, it offers a fresh perspective by focusing on the distribution of licenses based on status.

---
