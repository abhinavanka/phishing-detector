import streamlit as st
import joblib
import numpy as np

# Load the trained model
import os
model = joblib.load(os.path.join(os.path.dirname(__file__), "model.pkl"))
st.title("Phishing Website Detector")
st.write("This app predicts whether a website is likely phishing or safe, based on 30 features extracted from its URL and structure.")

st.subheader("Enter feature values")
st.write("For now, set each feature to 1 (suspicious/present) or -1 (safe/absent) based on the dataset's convention.")

feature_names = ["UsingIP","LongURL","ShortURL","Symbol@","Redirecting//","PrefixSuffix-",
"SubDomains","HTTPS","DomainRegLen","Favicon","NonStdPort","HTTPSDomainURL","RequestURL",
"AnchorURL","LinksInScriptTags","ServerFormHandler","InfoEmail","AbnormalURL",
"WebsiteForwarding","StatusBarCust","DisableRightClick","UsingPopupWindow",
"IframeRedirection","AgeofDomain","DNSRecording","WebsiteTraffic","PageRank",
"GoogleIndex","LinksPointingToPage","StatsReport"]

user_input = []
for name in feature_names:
    val = st.selectbox(name, options=[1, 0, -1], index=1, key=name)
    user_input.append(val)

if st.button("Predict"):
    features = np.array(user_input).reshape(1, -1)
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.success("This looks SAFE.")
    else:
        st.error("This looks like PHISHING.")
