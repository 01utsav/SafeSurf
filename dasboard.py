import streamlit as st
import requests
import json
import plotly.graph_objects as go
import random

st.title("SAFE SURF")
st.subheader("Privacy Policy Checker")

# Input field for URL
url = st.text_input("Enter URL:")


def create_gauge(score, max_score, total_risk):
    # Calculate percentage
    percentage = (score / max_score) * 100
    print(score, max_score, total_risk)

    # Create the gauge figure with Plotly
    fig = go.Figure(go.Indicator(
        mode="gauge+number",  # Displays the gauge and the number
        value=percentage,  # Use the percentage for the gauge value
        title={'text': f" {percentage:.1f}"},  # Display score and percentage
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {
                'range': [None, 100],
                'tickwidth': 1,
                'tickcolor': "darkblue",
                'tickvals': [0, 25, 50, 75, 100],
                'ticktext': ['Very Safe', 'Safe', 'Risk', 'Very Risky', 'Danger']
            },
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 25], 'color': 'lightgreen'},
                {'range': [25, 50], 'color': 'yellow'},
                {'range': [50, 75], 'color': 'orange'},
                {'range': [75, 100], 'color': 'red'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': (total_risk / max_score) * 100  # Assuming total_risk is also to be shown as a percentage
                
            }
        }
    ))

    return fig


def simulate_api_call():
    """ Simulate API response """
    return {
        'status': 'DONE',
        'data': {
            'score': random.randint(10, 100),
            'maxScore': 100,
            'totalRisk': random.randint(10, 100)
        }
    }

def calculate_score(value, ranges):
    """Calculate the score rating for a given value based on specified ranges."""
    for i, range_max in enumerate(ranges):
        if value <= range_max:
            return f"{i}/5"
    return f"{len(ranges)}/5"

def fetch_data(url):
    """ Fetch data from the server and handle errors. """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        st.error(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        st.error(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        st.error(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        st.error(f"Other Error: {err}")
        return None  # Return None to indicate failure

ranges = [50, 100, 150, 200, 250]  # Define the maximum values for each rating level
    
def generate_random_values():
    score = random.randint(60, 80)
    max_score = random.randint(60, 80)
    total_risk = random.randint(60, 80)
    return score, max_score, total_risk


# Button to trigger genReport API call  
if st.button("Generate Report"):
    if url and id:
        try:
            response = requests.get(f"http://127.0.0.1:5000/genReport?id={id}&url={url}")
            response.raise_for_status()  # Checks if the request was successful
            result = response.json()
            
            core = result['data']['score']
            max_score = result['data']['maxScore']
            total_risk = result['data']['totalRisk']
            
            score_rating = calculate_score(score, ranges)
            risk_rating = calculate_score(total_risk, ranges)

            gauge_fig = create_gauge(score, max_score, total_risk)
            print(1)
            st.plotly_chart(gauge_fig)

            st.markdown("### Privacy Report")
            st.write(f"**Accessing Necessary User Data:** {score_rating}")
            st.write(f"**Data Sharing/Retention:** {risk_rating}")
            st.button("Read More")
            st.button("Close")

            
        except Exception as e:
            # Use random values for any other exceptions
            st.error(f"An error occurred: {str(e)}")
            score, max_score, total_risk = generate_random_values()
            gauge_fig = create_gauge(score, max_score, total_risk)
            print(2)
            st.plotly_chart(gauge_fig)
            print(score, max_score, total_risk)

        
                
    else:
        st.error("Please provide both ID and URL")
