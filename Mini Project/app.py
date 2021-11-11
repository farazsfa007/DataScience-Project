import streamlit as st
from database import Classreport
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///mydatabase.sqlite3',
                       connect_args={'check_same_thread': False})
Session = sessionmaker(engine)
session = Session()

sidebar = st.sidebar

sidebar.header("Add Student Data here :-")
sidebar.markdown('---')

class_v = sidebar.text_input('Class ')
name_v = sidebar.text_input('Name')
subject_v = sidebar.text_input('Subject')

btn = sidebar.button("Save Data")

if btn:
    try:
        myphone = Classreport(class1=class_v, name=name_v,
                             course=subject_v)

        session.add(myphone)
        session.commit()

        st.success('Data Saved!!')
    except Exception as e:
        print(e)
        st.error('Error in saving data')

options = ['View Data', 'Search Data']

selOp = sidebar.selectbox('Select Option', options)


def showDetails():
    st.header('Class Report Generator')
    st.markdown('---')

    data = session.query(Classreport).all()

    col1, col2, col3, col4 = st.columns(4)

    col1.subheader("Id")
    col2.subheader("Class")
    col3.subheader("Student Name")
    col4.subheader("Subject")

    for entry in data:

        col1.text(entry.id)
        col2.text(entry.class1)
        col3.text(entry.name)
        col4.text(entry.course)


def searchStudent():
    st.header("Search Student")
    st.markdown("---")

    search_id = st.text_input("Enter id to search")
    search_btn = st.button("Search")

    if search_id and search_btn:
        res = session.query(Classreport).filter_by(id=search_id).first()
        col7, col8, col9, col10 = st.columns(4)
        if res:
            col7.text(res.id)
            col8.text(res.class1)
            col9.text(res.name)
            col10.text(res.course)


if selOp == options[0]:
    showDetails()
elif selOp == options[1]:
    searchStudent()