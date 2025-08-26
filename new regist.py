import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
scope=["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
@st. cache_resource
def init_connection():
	credentials=Credentials.from_service_account_info(st.secrets["gcp_service_account"],scopes=scope)
	clients=gspread.authorize(credentials)
	return clients
connect=init_connection()

client=connect.open("register12").sheet1

st.title("Over the counter registrationg form")

tab1,tab2=st.tabs(["Login","registration"])
with tab1:
	with st.form("Login"):
		username100=st.text_input("Enter username").strip().lower()
		password100=st.text_input("Enter password",type="password").strip()
		users=client.get_all_records()
		found=False
		if st.form_submit_button("Login"):
			if username100=="admin" and password100=="nana1":
				df=pd.DataFrame(users)
				st.dataframe(df)
			else:
				for user in users:
					if str(user["username"])==username100 and str(user["password"])==password100:
						found=True
						st.success(f"Welcome {username100}")
						break
				if not found:
							st.success("Wrong username or password")

with tab2:
	with st.form("registration"):
		user=client.get_all_records()
		name=st.text_input("enter your name").strip()
		username=st.text_input("enter your username").strip().lower()
		genda=st.radio("select gender:",("male","female","prefer not to tell"))
		code=st.selectbox("country code",["+233","+234","144","+1"])
		contact1=st.text_input("enter your contact").strip()
		code=code+contact1
		dob=st.text_input("enter your dob").strip()
		email=st.text_input("enter your email").strip()
		password=st.text_input("enter your password",type="password").strip()
		password2=st.text_input("repeat password",type="password").strip()
		if st.form_submit_button("register"):
			if password!=password2:
				st.success("password do not match")
			else:
			  client.append_row([name,username,genda,contact,dob,email,password])

			  st.success("registration successful")




