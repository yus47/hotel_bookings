import streamlit as st
import pandas as pd
import pickle
from datetime import datetime
import plotly.graph_objects as go
from PIL import Image

# Set page config
st.set_page_config(page_title="Hotel Cancellation Predictor", page_icon="🏨", layout="wide")

# Load the model
@st.cache_resource
def load_model():
    with open('hotel_cancel_xgb_model.sav', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

# Function to convert date to week number
def get_week_number(date):
    return date.isocalendar()[1]

# Function to create gauge chart
def create_gauge_chart(probability):
    # Detect the current theme
    is_dark_theme = st.get_option("theme.base") == "dark"
    
    # Set colors based on the theme
    bg_color = "rgba(0,0,0,0)" if is_dark_theme else "white"
    text_color = "white" if is_dark_theme else "black"
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = probability,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Cancellation Probability", 'font': {'size': 24, 'color': text_color}},
        number = {'font': {'size': 20, 'color': text_color}},
        gauge = {
            'axis': {'range': [0, 1], 'tickwidth': 1, 'tickcolor': text_color},
            'bar': {'color': "#4CAF50"},
            'bgcolor': bg_color,
            'borderwidth': 2,
            'bordercolor': text_color,
            'steps': [
                {'range': [0, 0.5], 'color': "#90EE90"},
                {'range': [0.5, 0.7], 'color': "#FFA500"},
                {'range': [0.7, 1], 'color': "#FF6347"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 0.7}}))
    
    fig.update_layout(
        paper_bgcolor = bg_color,
        font = {'color': text_color, 'family': "Arial"},
        height = 300,
        margin = dict(l=10, r=10, t=50, b=10)
    )
    return fig

# Header
header_image = Image.open("hotel_image.png")
st.image(header_image, use_column_width=True)

# Navigation
col1, col2, col3 = st.columns([1,2,1])
with col1:
    st.write("")  # This is to create some space
# with col2:
    # st.title("Vila Galé Hotels")
with col3:
    predictor_button = st.button("Predictor")
    about_button = st.button("About Us")

# Main content
if about_button:
    st.title("About Us")
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    .team-member {
        font-size:18px !important;
        margin-left: 20px;
    }
    .about-container {
        background-color: #f0f0f0;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="about-container">', unsafe_allow_html=True)
    st.markdown('<p class="big-font">This Hotel Cancellation Predictor was created by Alpha-Group:</p>', unsafe_allow_html=True)
    st.markdown('<p class="team-member">🧑‍💻 Arief Luqman Hakiem</p>', unsafe_allow_html=True)
    st.markdown('<p class="team-member">👨‍💻 Samuel Semaya</p>', unsafe_allow_html=True)
    st.markdown('<p class="team-member">🧑‍💻 Yusuf Sidharta</p>', unsafe_allow_html=True)

else:  # Default to Predictor page
    st.title("🏨 Hotel Cancellation Prediction")

    # Input form
    st.subheader("📝 Enter Booking Details")

    col1, col2 = st.columns(2)

    # Categorical Features
    with col1:
        hotel = st.selectbox("Hotel", options=['Resort Hotel', 'City Hotel'])
        agent = st.selectbox("Agent ID", options=['Undefined'] + list(range(1, 1001)))
        company = st.selectbox("Company ID", options=['Undefined'] + list(range(1, 1001)))
        customer_type = st.selectbox("Customer Type", options=['Transient', 'Contract', 'Transient-Party', 'Group'])
        deposit_type = st.selectbox("Deposit Type", options=['No Deposit', 'Non Refund', 'Refundable'])
        distribution_channel = st.selectbox("Distribution Channel", options=['Direct', 'Corporate', 'TA/TO'])
        market_segment = st.selectbox("Market Segment", options=['Direct', 'Corporate', 'Online TA', 'Offline TA/TO', 'Complementary', 'Groups'])
        meal = st.selectbox("Meal", options=['BB', 'HB', 'FB', 'SC'])
        is_local = st.checkbox("Is Local")
        was_in_waiting_list = st.checkbox("Was in Waiting List")
        is_repeated_guest = st.checkbox("Is Repeated Guest")

    # Numerical Features
    with col2:
        adr = st.number_input("Average Daily Rate (ADR)", min_value=0.0, max_value=5000.0, value=100.0, step=0.01)
        adults = st.number_input("Number of Adults", min_value=0, max_value=10, value=2)
        booking_changes = st.number_input("Booking Changes", min_value=0, max_value=20, value=0)
        lead_time = st.number_input("Lead Time (days)", min_value=0, max_value=365, value=30)
        previous_cancellation_ratio = st.number_input("Previous Cancellation Ratio", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
        total_of_special_requests = st.number_input("Total of Special Requests", min_value=0, max_value=5, value=0)
        duration_of_stay = st.number_input("Duration of Stay (nights)", min_value=1, max_value=30, value=3)
        
        # Date input for arrival
        arrival_date = st.date_input("Arrival Date", value=datetime.now())
        
        # Convert arrival date to week number
        arrival_date_week_number = get_week_number(arrival_date)

    # Calculate adr_third_quartile_deviation
    adr_third_quartile = 131.4
    adr_third_quartile_deviation = (adr - adr_third_quartile) / adr_third_quartile

    # Prepare input data
    input_data = pd.DataFrame({
        'hotel': [hotel],
        'agent': [0 if agent == 'Undefined' else int(agent)],
        'company': [0 if company == 'Undefined' else int(company)],
        'customer_type': [customer_type],
        'deposit_type': [deposit_type],
        'distribution_channel': [distribution_channel],
        'market_segment': [market_segment],
        'meal': [meal],
        'is_local': [int(is_local)],
        'was_in_waiting_list': [int(was_in_waiting_list)],
        'is_repeated_guest': [int(is_repeated_guest)],
        'adr_third_quartile_deviation': [float(adr_third_quartile_deviation)],
        'adults': [int(adults)],
        'booking_changes': [int(booking_changes)],
        'lead_time': [int(lead_time)],
        'previous_cancellation_ratio': [float(previous_cancellation_ratio)],
        'total_of_special_requests': [int(total_of_special_requests)],
        'duration_of_stay': [int(duration_of_stay)],
        'arrival_date_week_number': [int(arrival_date_week_number)]
    })

    # Make prediction
    if st.button("Predict Cancellation Probability"):
        try:
            prediction = model.predict_proba(input_data)[0][1]
            
            # Create and display gauge chart
            fig = create_gauge_chart(prediction)
            st.plotly_chart(fig, use_container_width=True)
            
            # Determine risk level and background color
            if prediction < 0.5:
                risk_level = "Low"
                bg_color = "rgba(144, 238, 144, 0.3)"
            elif prediction < 0.7:
                risk_level = "Moderate"
                bg_color = "rgba(255, 165, 0, 0.3)"  
            else:
                risk_level = "High"
                bg_color = "rgba(255, 99, 71, 0.3)"  
            
            # Create a container with the background color
            with st.container():
                st.markdown(
                    f"""
                    <div style="background-color: {bg_color}; padding: 10px; border-radius: 5px;">
                        <h3 style="text-align: center;">{risk_level} risk of cancellation: {prediction:.2%}</h3>
                        <p style="text-align: center;">Calculated ADR Third Quartile Deviation: {adr_third_quartile_deviation:.4f}</p>
                        <p style="text-align: center;">Arrival Week Number: {arrival_date_week_number}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")
            st.write("Input data:")
            st.write(input_data)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Created by Alpha-Group using Streamlit</p>", unsafe_allow_html=True)