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

class_v = sidebar.text_input('Class')
name_v = sidebar.text_input('Name')
subject_v = sidebar.text_input('Subject')
tot_mrks_v= sidebar.number_input('Total Marks')
obt_mrks_v= sidebar.number_input(('Obtain Marks'))

btn = sidebar.button("Save Data")

if btn:
    try:
        myphone = Classreport(class1=class_v, name=name_v,
                        course=subject_v,total_marks=tot_mrks_v, obtain_marks=obt_mrks_v)

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

    col1, col2, col3, col4,col5,col6 = st.columns(6)

    col1.subheader("Id")
    col2.subheader("Class")
    col3.subheader("Student Name")
    col4.subheader("Subject")
    col5.subheader('Total Marks')
    col6.subheader('Obtain Marks')


    for entry in data:

        col1.text(entry.id)
        col2.text(entry.class1)
        col3.text(entry.name)
        col4.text(entry.course)
        col5.text(entry.total_marks)
        col6.text(entry.obtain_marks)


def searchStudent():
    st.header("Search Student")
    st.markdown("---")

    search_id = st.text_input("Enter id to search")
    search_btn = st.button("Search")

    if search_id and search_btn:
        res = session.query(Classreport).filter_by(id=search_id).first()
        col7, col8, col9, col10,col11,col12 = st.columns(6)
        if res:
            col7.text(res.id)
            col8.text(res.class1)
            col9.text(res.name)
            col10.text(res.course)
            col11.text(res.total_marks)
            col12.text(res.total_marks)


if selOp == options[0]:
    showDetails()
elif selOp == options[1]:
    searchStudent()