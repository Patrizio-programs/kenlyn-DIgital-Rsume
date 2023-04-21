import streamlit as st

# Set the layout to wide mode
st.set_page_config(page_title="Kenlyn| Digital CV",
                   page_icon=":guardsman:",
                   layout="wide",
                   initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    body {
        background-color: #FFFFFF;
        color: #000000;
    }
    
    </style>
     <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
            unsafe_allow_html=True)
st.image("https://i.ibb.co/HHf7pss/profile-pic-2.png", width=300)

# Define the layout
st.title('Kenlyn Butler-Medley - Digital CV')

st.header('Personal Information')
# Personal Information
col1, col2 = st.columns(2)

with col1:
  st.text('Name:')
  st.text('Date of Birth:')
  st.text('Address:')
  st.text('Marital Status:')
with col2:

  st.text('Kenlyn Butler-Medley')
  st.text('January 19th, 1993')
  st.text('Redemption sharps, Kingstown, ST. Vincent')
  st.text('Married')

st.header('Contact Information')
# Contact Information
col1, col2 = st.columns(2)

with col1:
  st.text('Cell Phone:')
  st.text('Work Phone:')
  st.text('Email Address:')
with col2:
  st.text('1 (784) 528-7298')
  st.text('1(784) 457-1504 or 1 (784) 457-2960')
  st.text('lyn_butler1@hotmail.com or kenlyn.partners@gmail.com')

# Work Experience
st.header('Work Experience')
col1, col2 = st.columns(2)
with col1:
  st.subheader('Guest Service Agent (PART TIME)')
  st.text('Grenadine House, Kingstown Park, St. Vincent')
  st.text('2008-2011, June-August')

  st.subheader('Clerical Officer')
  st.text('Partners of the Americas, A Ganar programme')
  st.text('2012-2015, September-September')

  st.subheader('Assistant Programme Coordinator')
  st.text('Partners of the Americas, A Ganar Programme')
  st.text('2014-2015, August-September')
with col2:
  st.subheader('Clerk Exams')
  st.text('Division of Adult and Continuing Education, Kingstown, St. Vincent')
  st.text('2015-2019, October-December')

  st.subheader('Facilitator - Social Studies')
  st.text(
    'Department of Adult and Continuing Education, Kingstown, St. Vincent')
  st.text('2018-2019, September-March')

  st.subheader('Zone Coordinator')
  st.text(
    'Department of Adult and Continuing Education, Kingstown, St. Vincent')
  st.text('2019, March-Present')

# Education
st.header('Education')
st.text('Bishop’s college Kingstown, 2004-2009')
st.text(
  'St. Vincent community college: Division of Technical and Vocational Education, 2009-2011'
)
st.text(
  'Associates Degree in Business Management and Business Law, St. Vincent and the Grenadines Community College – Division of Technical and Vocational Ed, September 2009 – June 2011'
)

# Qualifications
st.header('Qualifications')
col1, col2 = st.columns(2)
with col1:
  st.text('Principles of Accounting, CXC, General, III, 2009')
  st.text('Principles of Business, CXC, General, II, 2009')
  st.text('Social Studies, CXC, General, II, 2009')
  st.text('Economics, CXC, General, III, 2009')
with col2:
  st.text('Office Administration, CXC, General, II, 2009')
  st.text('English Language, CXC, General, III, 2009')
  st.text('English Literature, CXC, General, III')
  st.text('Mathematics, CXC, General, II, 2016')

# Computer Skills
st.header('Computer Skills')
st.text('Proficient in Microsoft Word, Excel, and Database')
st.text('Familiar with software QuickBooks')

# Other Skills & Experiences
st.header('Other Skills & Experiences')
st.text('Facilitator, A Ganar, St. Vincent')
st.text('Mentor, A Ganar, St. Vincent')
st.text('President, Redemption Sharps Police Youth Club, St. Vincent')
st.text('Intern, Cocoa Cultivation and Harvesting, Sena, Colombia')
st.text(
  'Committee Member, SVG 1st National Congress for Women, St. Vincent and the Grenadines'
)
st.text('President, Debate Team, Bishop’s College Kingstown')
st.text('President, Interact Club, Bishop’s College Kingstown')
st.text('Head Girl, Student Body, Bishop’s College Kingstown')
st.text('Member, Central Kingstown Development Organization')

# References
st.header('References')
st.text(
  'Mr. Wayne Williams, Country Coordinator, St. Vincent A Ganar, Kingstown, St. Vincent, Tel: (784) 531-9900'
)
st.text(
  'Mrs. Kolene Thomas – Williams, Business Skills Instructor, Department of Adult and Continuing Education, Kingstown, Tel: (784) 434-3855'
)
st.text(
  'Ms. Kathleen Jeffers, Director, Department of Adult and Continuing Education, Ministry of Education, Kingstown, St. Vincent, Tel: 1(784) 457-1504'
)
