import streamlit as st

st.title("👤 User Profile Page")

st.write("This is the profile page in our multi-page app!")

with st.form("profile_form"):
    st.write("### Update Your Profile")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    bio = st.text_area("Bio")
    
    submitted = st.form_submit_button("Save Profile")
    if submitted:
        st.success("Profile updated successfully!")
        st.write(f"**Name:** {name}")
        st.write(f"**Email:** {email}")
        st.write(f"**Bio:** {bio}")