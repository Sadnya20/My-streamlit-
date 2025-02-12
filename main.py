# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd
# from preprocessor import load_data, preprocess_data
# from visuals import (
#     plot_donut_chart,
#     plot_choropleth_map,
#     plot_bar_chart,
#     plot_line_chart,
#     plot_bubble_chart,
#     plot_treemap,
# )

# # Load and preprocess data
# data_file = "Exported_Startup_Filelatest.csv"  # Replace with your actual data file
# df = load_data(data_file)
# df = preprocess_data(df)

# # Sidebar for filters
# st.sidebar.title("Filters")

# # Create a multi-select for years
# selected_years = st.sidebar.multiselect("Select Year", sorted(df['first_funding_year'].unique()))

# # Create a multi-select for cities with a "Select All" checkbox
# cities = sorted(df['city'].dropna().unique())
# select_all_cities = st.sidebar.checkbox("Select All Cities", value=True)
# if select_all_cities:
#     selected_cities = cities
# else:
#     selected_cities = st.sidebar.multiselect("Select City", cities)

# # Create a multi-select for funding types with a "Select All" checkbox
# funding_types = sorted(df['funding_type'].dropna().unique())
# select_all_funding_types = st.sidebar.checkbox("Select All Funding Types", value=True)
# if select_all_funding_types:
#     selected_funding_types = funding_types
# else:
#     selected_funding_types = st.sidebar.multiselect("Select Funding Type", funding_types)

# # Create a multi-select for states with a "Select All" checkbox
# states = sorted(df['state_code'].dropna().unique())
# select_all_states = st.sidebar.checkbox("Select All States", value=True)
# if select_all_states:
#     selected_states = states
# else:
#     selected_states = st.sidebar.multiselect("Select State", states)



# # Create a multi-select for countries with a "Select All" checkbox
# countries = sorted(df['country_code'].dropna().unique())
# select_all_countries = st.sidebar.checkbox("Select All Countries", value=True)
# if select_all_countries:
#     selected_countries = countries
# else:
#     selected_countries = st.sidebar.multiselect("Select Country", countries)

# # Filter data based on selected filters
# filtered_data = df.copy()

# if selected_years:
#     filtered_data = filtered_data[filtered_data['first_funding_year'].isin(selected_years)]

# if selected_cities:
#     filtered_data = filtered_data[filtered_data['city'].isin(selected_cities)]

# if selected_funding_types:
#     filtered_data = filtered_data[filtered_data['funding_type'].isin(selected_funding_types)]

# if selected_states:
#     filtered_data = filtered_data[filtered_data['state_code'].isin(selected_states)]

# if selected_countries:
#     filtered_data = filtered_data[filtered_data['country_code'].isin(selected_countries)]

# # Display KPIs
# st.title("Startup Data Analysis Dashboard")
# st.header("Key Performance Indicators (KPIs)")

# # Calculate KPIs
# total_funding = filtered_data['funding_total_usd'].sum()
# total_startups = filtered_data['name'].nunique()
# average_funding = filtered_data['funding_total_usd'].mean()
# most_common_funding_type = filtered_data['funding_type'].mode()[0] if not filtered_data['funding_type'].mode().empty else "N/A"
# most_famous_segment_india = filtered_data[filtered_data['country_code'] == 'IND']['market'].mode()[0] if not filtered_data[filtered_data['country_code'] == 'IND']['market'].mode().empty else "N/A"
# most_famous_segment_usa = filtered_data[filtered_data['country_code'] == 'USA']['market'].mode()[0] if not filtered_data[filtered_data['country_code'] == 'USA']['market'].mode().empty else "N/A"


# # Display KPIs in two rows of three columns with background color
# kpi_style = """
# <style>
#     .kpi {
#         background-color: #704A4F;
#         color: white;
#         padding: 10px;
#         border-radius: 5px;
#         text-align: center;
#     }
# </style>
# """

# st.markdown(kpi_style, unsafe_allow_html=True)

# # First row of KPIs
# col1, col2, col3 = st.columns(3)
# col1.markdown(f'<div class="kpi">Total Funding (USD)<br>${total_funding:,.0f}</div>', unsafe_allow_html=True)
# col2.markdown(f'<div class="kpi">Total Startups<br>{total_startups}</div>', unsafe_allow_html=True)
# col3.markdown(f'<div class="kpi">Average Funding (USD)<br>${average_funding:,.0f}' if average_funding else "N/A" + '</div>', unsafe_allow_html=True)

# # Second row of KPIs
# col4, col5, col6 = st.columns(3)
# col4.markdown(f'<div class="kpi">Most Common Funding Type<br>{most_common_funding_type}</div>', unsafe_allow_html=True)
# col5.markdown(f'<div class="kpi">Most Famous Segment in India<br>{most_famous_segment_india}</div>', unsafe_allow_html=True)
# col6.markdown(f'<div class="kpi">Most Famous Segment in USA<br>{most_famous_segment_usa}</div>', unsafe_allow_html=True)

# # Add distance KPI


# # Visualizations
# st.header("Visualizations")
# st.subheader("Top 10 City-wise Investment Trends")
# donut_chart = plot_donut_chart(filtered_data)
# st.plotly_chart(donut_chart)

# st.subheader("Startup Funding by Country")
# choropleth_map = plot_choropleth_map(filtered_data)
# st.plotly_chart(choropleth_map)

# st.subheader("Top 10 Startup Categories by Funding")
# bar_chart = plot_bar_chart(filtered_data)
# st.plotly_chart(bar_chart)

# st.subheader("Funding Growth Over Time")
# bubble_chart = plot_bubble_chart(df)
# st.plotly_chart(bubble_chart)

# st.subheader("Yearly Total Funding Raised")
# line_chart = plot_line_chart(df)
# st.plotly_chart(line_chart)

# st.subheader("Total Funding Raised Across Industries")
# treemap = plot_treemap(filtered_data)
# st.plotly_chart(treemap)

# # Information Button
# if st.button("Information"):
#     st.info("This dashboard provides insights into startup funding trends, including total funding by industry, year, and geographical distribution.")
# 
# import streamlit as st






import streamlit as st


import pandas as pd
import streamlit as st
from preprocessor import load_data, preprocess_data
import sys
import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from visuals import (
    plot_donut_chart,
    plot_choropleth_map,
    plot_bar_chart,
    plot_line_chart,
    plot_bubble_chart,
    plot_treemap,
)

# Set the layout to wide
st.set_page_config(layout="wide")

# Load and preprocess data
data_file = "Exported_Startup_Filelatest.csv"  # Replace with your actual data file
df = load_data(data_file)
df = preprocess_data(df)

# Title for the dashboard
st.title("📊Startup Investment Dashboard")

# Sidebar for filters
st.sidebar.title("Filters")

# Create a multi-select for cities with a "Select All" checkbox
cities = sorted(df['city'].dropna().unique())
select_all_cities = st.sidebar.checkbox("Select All Cities", value=True)
if select_all_cities:
    selected_cities = cities
else:
    selected_cities = st.sidebar.multiselect("Select City", cities)

# Create a multi-select for funding types with a "Select All" checkbox
funding_types = sorted(df['funding_type'].dropna().unique())
select_all_funding_types = st.sidebar.checkbox("Select All Funding Types", value=True)
if select_all_funding_types:
    selected_funding_types = funding_types
else:
    selected_funding_types = st.sidebar.multiselect("Select Funding Type", funding_types)

# Create a multi-select for states with a "Select All" checkbox
states = sorted(df['state_code'].dropna().unique())
select_all_states = st.sidebar.checkbox("Select All States", value=True)
if select_all_states:
    selected_states = states
else:
    selected_states = st.sidebar.multiselect("Select State", states)

# Create a multi-select for countries with a "Select All" checkbox
countries = sorted(df['country_code'].dropna().unique())
select_all_countries = st.sidebar.checkbox("Select All Countries", value=True)
if select_all_countries:
    selected_countries = countries
else:
    selected_countries = st.sidebar.multiselect("Select Country", countries)

# Filter data based on selected filters
filtered_data = df.copy()

# Filter by year range
if 'first_funding_year' in df.columns:
    min_year = int(df['first_funding_year'].min())
    max_year = int(df['first_funding_year'].max())

if selected_cities:
    filtered_data = filtered_data[filtered_data['city'].isin(selected_cities)]

if selected_funding_types:
    filtered_data = filtered_data[filtered_data['funding_type'].isin(selected_funding_types)]

if selected_states:
    filtered_data = filtered_data[filtered_data['state_code'].isin(selected_states)]

if selected_countries:
    filtered_data = filtered_data[filtered_data['country_code'].isin(selected_countries)]

# Display KPIs
st.header("Key Performance Indicators (KPIs)")

# Calculate KPIs
total_funding = filtered_data['funding_total_usd'].sum()
total_startups = filtered_data['name'].nunique()
average_funding = filtered_data['funding_total_usd'].mean()
most_common_funding_type = filtered_data['funding_type'].mode()[0] if not filtered_data['funding_type'].mode().empty else "N/A"
most_famous_segment_india = filtered_data[filtered_data['country_code'] == 'IND']['market'].mode()[0] if not filtered_data[filtered_data['country_code'] == 'IND']['market'].mode().empty else "N/A"
most_famous_segment_usa = filtered_data[filtered_data['country_code'] == 'USA']['market'].mode()[0] if not filtered_data[filtered_data['country_code'] == 'USA']['market'].mode().empty else "N/A"

# Display KPIs in two rows of three columns with background color
kpi_style = """
<style>
    .kpi {
        background-color: #BE4793;
        color: white;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
</style>
"""

st.markdown(kpi_style, unsafe_allow_html=True)

# First row of KPIs
col1, col2, col3 = st.columns(3)
col1.markdown(f'<div class="kpi">Total Funding (USD)<br>${total_funding:,.0f}</div>', unsafe_allow_html=True)
col2.markdown(f'<div class="kpi">Total Startups<br>{total_startups}</div>', unsafe_allow_html=True)
col3.markdown(f'<div class="kpi">Average Funding (USD)<br>${average_funding:,.0f}' if average_funding else "N/A" + '</div>', unsafe_allow_html=True)
# Add space after the first row of KPIs
st.markdown("")  # This adds a blank line
# Second row of KPIs
col4, col5, col6 = st.columns(3)
col4.markdown(f'<div class="kpi">Most Common Funding Type<br>{most_common_funding_type}</div>', unsafe_allow_html=True)
col5.markdown(f'<div class="kpi">Most Famous Segment in India<br>{most_famous_segment_india}</div>', unsafe_allow_html=True)
col6.markdown(f'<div class="kpi">Most Famous Segment in USA<br>{most_famous_segment_usa}</div>', unsafe_allow_html=True)

# Year Slider (outside of sidebar, below KPIs)
if 'first_funding_year' in df.columns:
    selected_years = st.slider("Select Year", min_value=min_year, max_value=max_year, value=(min_year, max_year))

# Filter data based on selected year range
filtered_data = filtered_data[filtered_data['first_funding_year'].between(selected_years[0], selected_years[1])]

# Visualizations: Top 10 Startup Categories by Funding and Top 10 City-wise Investment Trends
# st.header("Visualizations")

# Create columns for side-by-side graphs
col1, col2 = st.columns(2)

# Top 10 Startup Categories by Funding
with col1:
    st.subheader("Top 10 Startup Categories by Funding")
    bar_chart = plot_bar_chart(filtered_data)
    st.plotly_chart(bar_chart)
    # Summary for the bar chart
    st.write("The chart shows the top 10 startup categories by funding, with biotechnology at the top with $73.372 billion followed by Mobile and Software.")

# Top 10 City-wise Investment Trends
with col2:
    st.subheader("Top 10 City-wise Investment Trends")
    donut_chart = plot_donut_chart(filtered_data)
    st.plotly_chart(donut_chart)
    # Summary for the donut chart
    st.write("It shows the top 10 cities in terms of investment trends. The top three cities, New York, San Francisco, and Unknown.")

# Visualizations: Top 10 Startup Categories by Funding and Top 10 City-wise Investment Trends
# st.header("Visualizations")

# Create columns for side-by-side graphs
col1, col2 = st.columns(2)

# Funding Growth Over Time
with col1:
    st.subheader("Funding Growth Over Time")
    bubble_chart = plot_bubble_chart(filtered_data)  # Use filtered_data for the bubble chart
    st.plotly_chart(bubble_chart,key="bubble_chart")
    st.write("The graph displays funding growth over time for different industries. The largest bubble is representing the \"Publishing\" industry with a total funding amount of approximately 30 Billion USD.")
# Total Funding Raised Across Industries
with col2:
    st.subheader("Total Funding Raised Across Industries")
    treemap = plot_treemap(filtered_data)  # Use filtered_data for the treemap
    st.plotly_chart(treemap,key="treemap")
    st.write("Total funding across various industries, with 'Biotechnology' receiving the largest share at 11%. 'Mobile' follows at 8%, while 'Software' and 'Clean Technology' each account for 6%, and 'Health Care' for 5%. A color gradient indicates funding levels, with purple representing the lowest and yellow the highest. This figure provides a detailed view of funding distribution compared to the previous graph.")
# Additional Visualizations
st.subheader("Startup Funding by Country")
choropleth_map = plot_choropleth_map(filtered_data)
st.plotly_chart(choropleth_map,key="choropleth_map")
st.write("The map displays total funding by country, with the United States highlighted in yellow as the highest recipient. Other countries are shown in varying shades of purple, indicating significant funding amounts, while those in grey have received the least. The color gradient reflects the level of funding received.")

st.subheader("Yearly Total Funding Raised")
line_chart = plot_line_chart(filtered_data)
st.plotly_chart(line_chart,key="line_chart")
st.write("The chart depicts yearly total funding, which remained near zero until the late 1990s. It began to rise in the early 2000s and saw significant growth in the 2010s, with the last recorded funding year being 2014.")














# # Additional Visualizations
# st.subheader("Startup Funding by Country")
# choropleth_map = plot_choropleth_map(filtered_data)
# st.plotly_chart(choropleth_map)

# st.subheader("Funding Growth Over Time")
# bubble_chart = plot_bubble_chart(df)
# st.plotly_chart(bubble_chart)

# st.subheader("Yearly Total Funding Raised")
# line_chart = plot_line_chart(df)
# st.plotly_chart(line_chart)

# st.subheader("Total Funding Raised Across Industries")
# treemap = plot_treemap(filtered_data)
# st.plotly_chart(treemap)

# Information Button
if st.button("Information"):
    st.info("The Growing Startup Industry The startup industry is rapidly expanding, with thousands of new companies emerging annually across various sectors. This growth is driven by technological advancements, increased access to capital, and a global shift towards innovation. As startups seek funding to scale, they attract diverse investors, including venture capitalists and angel investors.Challenges in Analyzing Funding Trends.Despite the opportunities, analyzing funding trends poses several challenges:")

    st.info("Data Overload: The sheer volume of funding data can overwhelm stakeholders, making it difficult to identify meaningful insights.Dynamic Market Conditions: The constantly evolving startup landscape requires real-time data analysis to keep up with economic shifts and consumer preferences.Diverse Funding Sources: Startups secure funding from various sources, each with unique criteria, complicating the analysis.Identifying Key Players: Understanding which industries attract the most investment and identifying top investors can be complex.Empowering Data-Driven Decisions.This dashboard addresses these challenges by providing essential insights into the startup funding landscape")

