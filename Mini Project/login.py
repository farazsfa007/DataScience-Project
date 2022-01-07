import streamlit as st

def main():
    """LogIn/SignUp"""

st.title("LogIn/SignUp")

menu = ["LogIn","SignUp"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "LogIn":
    st.subheader("LogIn")

    username=st.sidebar.text_input("User Name")
    password=st.sidebar.text_input("Password",type='password')
    if st.sidebar.button("LogIn"):
        st.success("Logged In as {}".format(username))

elif choice == "SignUp":
    st.subheader("Create New Account")
    username=st.sidebar.text_input("User Name")
    password=st.sidebar.text_input("Enter Password",type='password')
    if st.sidebar.button("Signup"):
        st.success("Account Created As as {}".format(username))

if __name__=='__main__':
    main()