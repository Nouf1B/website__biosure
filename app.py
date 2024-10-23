import streamlit as st
import requests


# Set the page configuration
st.set_page_config(
    page_title="Biosure",
    layout="wide",
)

# Header and logo
st.markdown('<div class="header">', unsafe_allow_html=True)
st.image("/home/lewagon/code/Nouf1B/website__biosure/.images/logo5.png", width=70, use_column_width=False)  # Logo on the left
st.title("Biometric Secured Transactions")
st.markdown('</div>', unsafe_allow_html=True)
# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #161b4f;  /* Background color of the main app */
        color: #e9e9f2;              /* Font color for the main app */

    }

    /* Sidebar styles */
    .stSidebar {
        background-color: #e9e9f2;  /* Sidebar background color */
        color: #161b4f;              /* Sidebar font color */
    }

    /* Input cell styles */
    .stNumberInput, .stSelectbox {
        background-color: #d9e9fe;  /* Background color for input cells */
        color: #e9e9f2;              /* Font color for input cells */
        border: 1px solid #e9e9f2;  /* Border color for input cells */
    }

    /* Customizing the submit button */
    .stButton>button {
        background-color: #e9e9f2;   /* Background color of the button */
        color: #161b4f;              /* Text color of the button */
        border: none;                /* Remove border */
        border-radius: 5px;         /* Rounded corners */
        padding: 10px;              /* Padding */
        font-weight: bold;           /* Bold text */
    }

    /* Hover effect for the button */
    .stButton>button:hover {
        background-color: #ddd320;   /* Change background color on hover */
        color: #161b4f;              /* Change text color on hover */
    }

    /* Header styles */
    .header {
        margin-bottom: -20px;        /* Pull header up with negative margin */
        display: flex;               /* Flexbox for alignment */
        align-items: center;         /* Center align items vertically */
        padding: -1500px;              /* Add padding for better spacing */
    }

    /* Logo styles */
    .header img {
        margin-right: 10px;         /* Space between logo and title */

    }

    /* Description styles */
    .description {
        color: #e9e9f2;              /* Font color for the description */
        font-size: 16px;            /* Font size for better readability */
        padding: 0px;              /* Padding for better spacing */
    }

    .description h3 {
        color: #CCCCFF;             /* Color for the subtitle */
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Description
st.markdown(
    """
    <div class="description">
    <strong>Biosure</strong> is an innovative platform leveraging machine learning to enhance online security by analyzing user interaction patterns. By developing an adaptive behavioral biometrics authentication mechanism, it classifies transactions as legitimate or illegitimate. This approach empowers users to conduct online transactions safely and confidently, significantly reducing the risk of cybercrime.


    </div>
    """,
    unsafe_allow_html=True  # Allow HTML for better formatting
)


# Define test parameter sets
test_parameters = {
    "test1": {"dwell_avg": 0.080182080467542, "flight_avg": 1.63980659345785, "keyboard_avg": 1.71998867392539, "freq_mouse": 11,
              "traj_avg": 410.3350616185, "mouse_avg": 376.140473150291, "day_type": "Weekday", "freq_key": 48},
    "test2": {"dwell_avg": 0.0948973027142611, "flight_avg": 0.529685269702564, "keyboard_avg":0.624582572416825, "freq_mouse": 7,
              "traj_avg": 244.695773954496, "mouse_avg": 244.695773954496, "day_type": "Weekday", "freq_key": 44},
    # Add more tests here
}

# Select test
st.sidebar.header("Choose a Test to Predicit ")
selected_test = st.sidebar.selectbox("Select a Test", ["Select a test"] + list(test_parameters.keys()))

# Initialize parameter values based on selected test
if selected_test != "Select a test":
    parameters = test_parameters[selected_test]
else:
    parameters = {"dwell_avg": 0.0, "flight_avg": 0.0, "keyboard_avg": 0.0, "freq_mouse": 0,
                  "traj_avg": 0.0, "mouse_avg": 0.0, "day_type": "Weekday", "freq_key": 0}

# Sidebar form for user input
with st.sidebar.form(key='prediction_params'):
    col1, col2 = st.columns(2)

    with col1:
        dwell_avg = st.number_input("Average Dwell Time (ms)", min_value=0.0, step=0.1, format="%.1f", value=parameters["dwell_avg"])
        flight_avg = st.number_input("Average Flight Time (ms)", min_value=0.0, step=0.1, format="%.1f", value=parameters["flight_avg"])
        keyboard_avg = st.number_input("Average Keyboard Input (units)", min_value=0.0, step=0.1, format="%.1f", value=parameters["keyboard_avg"])
        freq_mouse = st.number_input("Mouse Frequency (events/min)", min_value=0, value=parameters["freq_mouse"])

    with col2:
        traj_avg = st.number_input("Average Trajectory Time (ms)", min_value=0.0, step=0.1, format="%.1f", value=parameters["traj_avg"])
        mouse_avg = st.number_input("Average Mouse Input (units)", min_value=0.0, step=0.1, format="%.1f", value=parameters["mouse_avg"])
        day_type = st.selectbox("Day Type", ["Weekday", "Weekend"], index=["Weekday", "Weekend"].index(parameters["day_type"]))
        freq_key = st.number_input("Keyboard Frequency (events/min)", min_value=0, value=parameters["freq_key"])
        day_type = 0 if day_type == 'Weekday' else 1
    submit_button = st.form_submit_button(label='Predict legitimation')

# Call the API and display the prediction
if submit_button:
    api_url = " http://127.0.0.1:8000/predict"  # Replace with your API endpoint

    # Prepare the payload for API
    payload = {
        "dwell_avg": dwell_avg,
        "flight_avg": flight_avg,
        "keyboard_avg": keyboard_avg,
        "freq_mouse": freq_mouse,
        "traj_avg": traj_avg,
        "mouse_avg": mouse_avg,
        "day_type": day_type,
        "freq_key": freq_key
    }

    try:
        # Make a POST request to the API
        response = requests.get(api_url, params=payload)
        prediction = response.json().get("pred")
    except Exception as e:
        prediction = f"Error occurred: {str(e)}"

    # Display prediction result
    st.header("Prediction Result")
    st.write(f"The prediction indicates that the user is: **{prediction}**")

# Description
st.markdown(
    """
    <div class="description">
    <h3>Done by:</h3>
    Nouf Alotaibi, Kawthar Almowallad, Razan Alzhrani, Amr ALGhasham
    </div>
    """,
    unsafe_allow_html=True
)
