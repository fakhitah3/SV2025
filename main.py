import streamlit as st
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")



# Set up the Streamlit page configuration
st.set_page_config(
    page_title="Arts Faculty Data Analysis",
    layout="wide"
)

st.header("Arts Faculty Gender Distribution Analysis 🎨", divider="gray")

# URL for the dataset
url = "https://raw.githubusercontent.com/fakhitah3/SV2025/refs/heads/main/arts_faculty_data.csv"

# Load the data
try:
    arts_df = pd.read_csv(url)
    st.success("Data loaded successfully!")

    # Display the head of the DataFrame
    st.subheader("Raw Data Preview")
    st.dataframe(arts_df.head())
    
    # --- Plotly Pie Chart ---
    
    # Calculate the gender counts
    gender_counts = arts_df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']
    
    st.subheader("Gender Distribution in Arts Faculty")
    
    # Create the Plotly pie chart
    fig = px.pie(
        gender_counts, 
        values='Count', 
        names='Gender', 
        title='Distribution of Gender in Arts Faculty',
        # Customize the color map
        color_discrete_sequence=px.colors.sequential.Agsunset, 
        # Display percentage and label on hover
        hover_data=['Count'],
        labels={'Count':'Number of Students'}
    )
    
    # Customize the appearance of the chart (optional)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(showlegend=True)

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Error loading or processing data: {e}")
