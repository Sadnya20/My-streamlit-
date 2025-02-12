import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
# pip install plotly

def plot_donut_chart(df):
    """Create a donut chart for top 10 city-wise investment trends."""
    city_funding = df.groupby('city')['funding_total_usd'].sum().sort_values(ascending=False).head(10).reset_index()
    explode = [0.1 if city in city_funding.head(3)['city'].values else 0 for city in city_funding['city']]
    
    fig = go.Figure(data=[go.Pie(
        labels=city_funding['city'], 
        values=city_funding['funding_total_usd'], 
        hole=0.4,
        textinfo='percent+label',
        pull=explode,
        marker=dict(colors=px.colors.sequential.Plasma)
    )])
    
    fig.update_layout(title="Top 10 City-wise Investment Trends", showlegend=True, height=600)
    return fig

def plot_choropleth_map(df):
    """Create a choropleth map for funding by country."""
    fig = px.choropleth(
        df.groupby('country_code')['funding_total_usd'].sum().reset_index(),
        locations='country_code',
        color='funding_total_usd',
        hover_name='country_code',
        color_continuous_scale='Viridis',
        labels={'funding_total_usd': 'Total Funding (USD)'},
        title="Startup Funding by Country"
    )
    
    fig.update_geos(showcoastlines=True, coastlinecolor="Black", projection_type="natural earth", projection_scale=1.2)
    fig.update_layout(geo=dict(showland=True, landcolor="lightgray", showlakes=True, lakecolor="lightblue"), height=600)
    return fig

def plot_bar_chart(df):
    """Create a bar chart for top 10 startup categories by funding."""
    top_categories = df.groupby('market')['funding_total_usd'].sum().nlargest(10)
    fig = px.bar(
        top_categories, 
        x=top_categories.index, 
        y=top_categories.values, 
        title="Top 10 Startup Categories by Funding",
        labels={"x": "Startup Category", "y": "Total Funding (USD)"},
        color=top_categories.values,
        color_continuous_scale="Viridis",
        height=600
    )
    
    for i, v in enumerate(top_categories.values):
        fig.add_annotation(x=top_categories.index[i], y=v, text=f"${v:,.0f}", showarrow=False, font=dict(size=12, color="black"), align="center", yshift=10)
    
    fig.update_layout(xaxis_title="Startup Category", yaxis_title="Total Funding (USD)", plot_bgcolor="#f5f5f5", title=dict(x=0.5), margin=dict(l=40, r=40, t=40, b=40))
    return fig

def plot_bubble_chart(df):
    """Create a bubble chart for funding growth over time."""
    bubble_fig = px.scatter(df,
        x="first_funding_year",
        y="funding_total_usd",
        size="funding_total_usd",
        color="market",
        hover_name="market",
        size_max=50,
        title="Funding Growth Over Time (Bubble Chart)",
        labels={"first_funding_year": "Year", "funding_total_usd": "Total Funding (USD)"},
        hover_data=["funding_total_usd", "first_funding_year"],
    )
    
    bubble_fig.update_layout(
        title="Funding Growth Over Time",
        xaxis_title="Year",
        yaxis_title="Total Funding (USD)",
        showlegend=True,
        plot_bgcolor="#f5f5f5",
        xaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.1)'),
        yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.1)'),
        margin=dict(l=40, r=40, t=40, b=40),
        hovermode="closest",
        dragmode="zoom",
    )
    
    return bubble_fig

def plot_line_chart(df):
    """Create a line chart for yearly total funding raised."""
    funding_yearly = df.groupby('first_funding_year')['funding_total_usd'].sum().reset_index()
    last_funding_year = funding_yearly['first_funding_year'].max()
    last_funding_amount = funding_yearly[funding_yearly['first_funding_year'] == last_funding_year]['funding_total_usd'].values[0]
    
    fig = px.line(funding_yearly, x='first_funding_year', y='funding_total_usd', title="Yearly Total Funding Raised", markers=True)
    
    fig.add_annotation(
        x=last_funding_year,
        y=last_funding_amount,
        text=f"Last Funding Year: {last_funding_year}",
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40,
        font=dict(size=12, color="black"),
        bgcolor="#CB7CA8",
        borderpad=5,
        bordercolor="black"
    )
    
    fig.update_layout(plot_bgcolor="#f5f5f5", xaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.1)'), yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.1)'), title=dict(x=0.5), margin=dict(l=40, r=40, t=40, b=40))
    return fig

def plot_treemap(df):
    """Create a treemap for total funding raised across industries."""
    industry_funding = df.groupby('market')['funding_total_usd'].sum().reset_index()
    total_funding = industry_funding['funding_total_usd'].sum()
    industry_funding['percentage'] = (industry_funding['funding_total_usd'] / total_funding) * 100

    fig = px.treemap(
        industry_funding,
        path=['market'],
        values='funding_total_usd',
        color='funding_total_usd',
        color_continuous_scale='Viridis',
        title="Total Funding Raised Across Industries (with Percentage Share)",
        labels={'funding_total_usd': 'Total Funding (USD)'},
        hover_data={'percentage': True}
    )





    
    fig.update_traces(textinfo="label+value+percent entry")
    return fig
 