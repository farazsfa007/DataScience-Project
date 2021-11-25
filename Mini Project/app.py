import streamlit as st
from database import Classreport
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px

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
tot_mrks_v = sidebar.number_input('Total Marks')
obt_mrks_v = sidebar.number_input('Obtain Marks')

def marksToGrade(marks):
    if(marks > 90):
        return 'A'
    elif(marks > 70):
        return 'B'
    elif(marks > 30):
        return 'C'
    else:
        return 'Fail'

def intro():
    st.title('Class Report Generator')
    st.header('FEATURES')
    st.markdown('- Simple Web Page Using Python With Streamlit library ')
    st.caption('Streamlit is an open-source **Python library** that makes it easy to create and share beautiful, custom web apps for machine learning and data science')
    st.markdown('- We can easily understand the data using plot')
    st.markdown('- ')


btn = sidebar.button("Save Data")

if btn:
    try:
        myreport = Classreport(class1=class_v, name=name_v,
                              course=subject_v, total_marks=tot_mrks_v, obtain_marks=obt_mrks_v, grade=marksToGrade(obt_mrks_v))

        session.add(myreport)
        session.commit()

        st.success('Data Saved!!')
    except Exception as e:
        print(e)
        st.error('Error in saving data')

options = ['Introduction', 'View Data', 'Search Data']

selOp = sidebar.selectbox('Select Option', options)



def showDetails():
    st.header('Class Report Generator')
    st.markdown('---')

    data = session.query(Classreport).all()

    df = pd.read_sql_table(table_name="Class Report Generator",
                           con=session.connection(), index_col="id")

    classes = df['class1'].unique()

    selClass = st.selectbox('Select Class', classes)

    bca_students = df[df['class1'] == selClass]
    st.bar_chart(bca_students.set_index('name')['obtain_marks'])
    st.plotly_chart(px.pie(data_frame=bca_students.groupby('grade', as_index=False).count(), labels='grade', values='name', names="grade"))
    
    subjects=df['course'].unique()
    selsub=st.selectbox('subjects',subjects)
    subjects_marks = bca_students[bca_students['course'] == selsub]
    st.bar_chart(subjects_marks.set_index('name')['obtain_marks'])
    st.plotly_chart(px.pie(data_frame=subjects_marks.groupby('grade', as_index=False).count(), labels='grade', values='name', names="grade"))

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    col1.subheader("Id")
    col2.subheader("Class")
    col3.subheader("Student Name")
    col4.subheader("Subject")
    col5.subheader('Total Marks')
    col6.subheader('Obtain Marks')
    col6.subheader('Grade')

    for entry in data:

        col1.text(entry.id)
        col2.text(entry.class1)
        col3.text(entry.name)
        col4.text(entry.course)
        col5.text(entry.total_marks)
        col6.text(entry.grade)

    del_id = st.number_input("Enter id to delete")
    del_btn = st.button("Delete")
    
    if del_id and del_btn:
        to_delete = session.query(Classreport).filter_by(id=del_id).first()
        session.delete(to_delete)
        session.commit()
        st.success('Data Deleted')

def searchStudent():
    st.header("Search Student")
    st.markdown("---")

    search_id = st.text_input("Enter id to search")
    search_btn = st.button("Search")

    if search_id and search_btn:
        res = session.query(Classreport).filter_by(id=search_id).first()
        col7, col8, col9, col10, col11, col12 = st.columns(6)
        if res:
            col7.text(res.id)
            col8.text(res.class1)
            col9.text(res.name)
            col10.text(res.course)
            col11.text(res.total_marks)
            col12.text(res.total_marks)

if selOp == options[0]:
    intro()
elif selOp == options[1]:
    showDetails()
elif selOp == options[2]:
    searchStudent()