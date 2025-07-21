import streamlit as st
import speech_recognition as sr
import pyttsx3
import base64
import threading



st.set_page_config(page_title="GIFT Chatbot",page_icon="logo.png ",layout="centered")
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #e0ffe0, #f4fff4);
    }
    .glass-box {
        backdrop-filter: blur(12px);
        background-color: rgba(255, 255, 255, 0.6);
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.1);
        padding: 20px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
""", unsafe_allow_html=True)


# ✅ SIDEBAR STYLING SECTION
st.markdown("""
    <style>
    /* Sidebar Background */
    section[data-testid="stSidebar"] {
        background-color: #e6f4ea;
        padding: 20px 15px;
        border-right: 2px solid #c0e4c0;
        box-shadow: 2px 0 10px rgba(0,0,0,0.05);
    }

    /* Sidebar Headings */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4,
    section[data-testid="stSidebar"] h5,
    section[data-testid="stSidebar"] h6 {
        color: #1b4332;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
    }

    /* Sidebar Links */
    section[data-testid="stSidebar"] a {
        color: #1b4332 !important;
        text-decoration: none;
        font-weight: 600;
        font-size: 15px;
    }

    section[data-testid="stSidebar"] a:hover {
        color: #2d6a4f !important;
        background-color: #d3f2dd;
        padding: 4px 6px;
        border-radius: 6px;
        display: inline-block;
    }

    /* Sidebar Image Styling */
    section[data-testid="stSidebar"] img {
        border-radius: 12px;
        margin-bottom: 10px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
    }

    /* Sidebar Info Box Styling */
    .stSidebar .stMarkdown .stAlert {
        background-color: #d8f3dc;
        color: #1b4332;
        border-left: 5px solid #40916c;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)


# Add this CSS just after setting the background image
st.markdown(
    """
    <style>
    /* Hide Streamlit's top padding */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
    }

    /* Hide top right menu (hamburger) */
    header .stMenu {
        visibility: hidden;
    }

    /* Optional: hide entire header (logo + hamburger) */
    header {
        visibility: hidden;
    }

    /* Optional: hide footer */
    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Function to add background from image URL
# ✅ Background Image & Logo with Heading
def set_bg_local(img_path):
    with open(img_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
with st.sidebar:
    st.markdown("## 🎓 GIFT Chatbot")
    try:
        st.image("gift-autonomous-college-bhubaneswar2-1.jpg", width=180)
    except:
        st.image("https://gift.edu.in/wp-content/uploads/2022/01/gift-logo.png", width=180)

    st.markdown("---")
    st.markdown("### 📌 Quick Links")
    st.markdown("- [About](https://top-autonomous-college-in-odisha.gift.edu.in/about-the-institute//)")
    st.markdown("- [Admissions](https://top-autonomous-college-in-odisha.gift.edu.in/admission-inquiry//)")
    st.markdown("- [Courses](https://top-autonomous-college-in-odisha.gift.edu.in/)")
    st.markdown("- [Hostel Info](https://top-autonomous-college-in-odisha.gift.edu.in/in-campus-hostels/)")
    st.markdown("- [Official Website](https://top-autonomous-college-in-odisha.gift.edu.in/)")
    st.markdown(
    "<ul><li><a href='https://mail.google.com/mail/?view=cm&to=info@gift.edu.in' target='_blank' style='text-decoration:none; font-weight:600; color:#1b4332;'> Contact</a>",
    unsafe_allow_html=True
)

    st.markdown("---")
    st.info("Created by Riya✨")
    
    

    st.markdown(
    """
    <style>
    /* Existing header/footer hiding... (keep this) */

    /* ✅ Sidebar background color & text styling */
    section[data-testid="stSidebar"] {
        background-color: #e6f4ea; /* pastel green */
        color: #1b4332;
        padding: 15px;
        border-right: 1px solid #b7ddb1;
    }

    /* Sidebar title and links text */
    .css-ng1t4o {  /* Sidebar section headings */
        color: #1b4332;
        font-weight: 600;
    }

    .css-1v0mbdj a {
        color: #1b4332 !important;
    }

    /* Optional: sidebar image border-radius */
    section[data-testid="stSidebar"] img {
        border-radius: 12px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Example usage
set_bg_local("gift-autonomous-college-bhubaneswar2-1.jpg")



# Title
st.markdown("""
    <div style='text-align: center;'>

    </div>
""", unsafe_allow_html=True)

# Text-to-Speech engine
engine = pyttsx3.init()

# Chatbot response function
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! 👋 How can I assist you at GIFT today?"
    
    elif "admission" in user_input:
        return "🎓 Admissions are open! Visit <a href='https://top-autonomous-college-in-odisha.gift.edu.in/admission-inquiry/' target='_blank'><b>Admission Page</b></a> for full details and application process."

    elif "placement" in user_input:
        return "💼 GIFT students are placed in top companies like <b>Tech Mahindra</b>, <b>Amazon</b>, <b>HGS</b>, <b>ADP</b>, <b>Tech Ahead</b>, and more. Visit the <a href='https://top-autonomous-college-in-odisha.gift.edu.in/placement/' target='_blank'><b>Placement Page</b></a>."

    elif "course" in user_input or "courses" in user_input:
        return """
        <div style='background-color: #e9ffe9; padding: 15px; border-radius: 12px;'>
        <h4>📚 <b>GIFT College offers the following programs:</b></h4>
        <ul style='font-size: 17px; line-height: 1.6'>
            <li>🔷 <b>B.Tech Programs:</b>
                <ul>
                    <li><a href='https://top-autonomous-college-in-odisha.gift.edu.in/cse/' target='_blank'>Computer Science & Engineering (CSE)</a></li>
                    <li><a href='https://top-autonomous-college-in-odisha.gift.edu.in/eee/' target='_blank'>Electrical & Electronics Engineering (EEE)</a></li>
                    <li><a href='https://top-autonomous-college-in-odisha.gift.edu.in/mech/' target='_blank'>Mechanical Engineering (MECH)</a></li>
                    <li><a href='https://top-autonomous-college-in-odisha.gift.edu.in/civil/' target='_blank'>Civil Engineering</a></li>
                    <li><a href='https://top-autonomous-college-in-odisha.gift.edu.in/ece/' target='_blank'>Electronics & Communication Engineering (ECE)</a></li>
                </ul>
            </li>
            <li>🔷 <b>MBA:</b> <a href='https://top-autonomous-college-in-odisha.gift.edu.in/mba/' target='_blank'>Master of Business Administration</a></li>
            <li>🔷 <b>MCA:</b> <a href='https://top-autonomous-college-in-odisha.gift.edu.in/mca/' target='_blank'>Master of Computer Applications</a></li>
            <li>🔷 <b>Diploma Courses:</b> <a href='https://top-autonomous-college-in-odisha.gift.edu.in/diploma-in-cse-syllabus/' target='_blank'>Diploma Programs</a></li>
        </ul>
        <p style='margin-top: 15px;'>👉 <b>Explore all programs:</b> <a href='https://top-autonomous-college-in-odisha.gift.edu.in/#' target='_blank'>GIFT Courses Page</a></p>
        </div>
        """

    elif "fees" in user_input or "fee structure" in user_input:
        return "💰 For fee details, visit the official <a href='https://top-autonomous-college-in-odisha.gift.edu.in/' target='_blank'><b>Fee Structure Page</b></a>."

    elif "hostel" in user_input or "accommodation" in user_input:
        return "🏠 GIFT offers separate hostel facilities for boys and girls with modern amenities. More info at <a href='https://top-autonomous-college-in-odisha.gift.edu.in/in-campus-hostels/' target='_blank'><b>Hostel Info</b></a>."

    elif "facilities" in user_input or "infrastructure" in user_input:
        return "🏫 GIFT provides smart classrooms, digital library, canteen, sports facilities, and more. Explore at <a href='https://top-autonomous-college-in-odisha.gift.edu.in/' target='_blank'><b>Campus Facilities</b></a>."

    elif "contact" in user_input or "phone number" in user_input:
        return "📞 You can contact GIFT at +91-XXXXXXXXXX or email <a href='https://mail.google.com/mail/?view=cm&to=info@gift.edu.in' target='_blank'><b>info@gift.edu.in</b></a>."

    elif "location" in user_input or "where is gift" in user_input:
        return "📍 GIFT is located in Bhubaneswar, Odisha. Here's the map: <a href='https://www.google.com/maps/search/gift+bhubaneswar+google+map/' target='_blank'><b>Google Maps</b></a>."

    elif "website" in user_input:
        return "🌐 Visit our official website here: <a href='https://top-autonomous-college-in-odisha.gift.edu.in/' target='_blank'><b>GIFT Website</b></a>."

    elif "department" in user_input or "branches" in user_input:
        return "🏢 We offer departments like CSE, ECE, Mechanical, Civil, Electrical, MBA, MCA etc. Check all at <a href='https://top-autonomous-college-in-odisha.gift.edu.in/' target='_blank'><b>Departments Page</b></a>."

    elif "thank you" in user_input:
        return "You're welcome! 😊"
    
    elif "xyz" not in user_input:
        return (
        "❓ I didn’t get that.<br>"
        "You can ask me about: <br>"
        "➡️ Admissions <br>➡️ Courses <br>➡️ Hostel <br>➡️ Placement"
    )


    else:
        return (
            "❓ Sorry, I didn't understand that.<br>"
            "👉 You can visit our official site for more info: "
            "<a href='https://top-autonomous-college-in-odisha.gift.edu.in/' target='_blank'><b>GIFT Autonomous College Bhubaneswar</b></a>"
        )


# Thread function for text-to-speech
def speak_response(response):
    try:
        engine.say(response)
        engine.runAndWait()
    except RuntimeError as e:
        st.error(f"Error in speech synthesis: {e}")


# Voice Input Section
st.markdown("### 🎤 Speak Now or Type Below")
recognizer = sr.Recognizer()



# Button to start voice recognition
if st.button("🎙️ Click to Speak"):
    with sr.Microphone() as source:
        st.markdown("""
    <div style='
        background-color: #e0f7fa;
        color: #006064;
        padding: 10px 15px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 500;
        max-width: 400px;
        box-shadow: 1px 1px 6px rgba(0, 0, 0, 0.1);
        margin-top: 15px;
    '>
        🎤 Listening...
    </div>
""", unsafe_allow_html=True)

        try:
            audio = recognizer.listen(source, timeout=5)
            user_input = recognizer.recognize_google(audio)
            st.markdown(
    f"""
    <div style='
        background-color: #f1f8e9;
        color: #33691e;
        padding: 10px 15px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 500;
        max-width: 500px;
        margin-top: 10px;
        box-shadow: 1px 1px 6px rgba(0, 0, 0, 0.1);
    '>
        ✅ You said: <i>{user_input}</i>
    </div>
    """,
    unsafe_allow_html=True
)
            response = chatbot_response(user_input)
            st.markdown(
    f"""
    <div style='
        background-color: rgba(255, 255, 255, 0.85);
        color: #000000;
        padding: 15px 20px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 600;
        line-height: 1.5;
        max-width: 800px;
        margin: 20px auto;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
        border-left: 6px solid #1b5e20;
    '>
        🤖 <b>Bot:</b> {response}
    </div>
    """,
    unsafe_allow_html=True
)




            # Start speaking in a separate thread
            threading.Thread(target=speak_response, args=(response,)).start()
        except Exception as e:
           st.markdown("""
    <div style='
        background-color: #f8d7da;
        color: #721c24;
        padding: 15px 20px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 500;
        margin: 15px auto;
        text-align: center;
        max-width: 500px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        border-left: 6px solid #f5c6cb;
    '>
        ❌ Could not understand your voice. Please try again.
    </div>
""", unsafe_allow_html=True)

            # ✅ Text Input
text_input = st.text_input("👇 Type your message here:")

if text_input:
    response = chatbot_response(text_input)

    # ✅ Center-aligned and styled bot response
    st.markdown(
        f"""
        <div style='
            background-color: #eaffea;
            color: #1b5e20;
            padding: 10px 15px;
            border-radius: 12px;
            display: inline-block;
            font-size: 18px;
            font-weight: 500;
            margin-top: 15px;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
        '>
            🤖 Bot: {response}
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # ✅ Voice thread for response
    threading.Thread(target=speak_response, args=(response,)).start()

    # Start speaking in a separate thread
    threading.Thread(target=speak_response, args=(response,)).start()
    