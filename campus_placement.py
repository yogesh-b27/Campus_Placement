import pandas as pd
df = pd.read_csv("C:\\Users\\bidav\\Downloads\\Placement_Data.csv")
# print(df.head())

inputs = df.drop(["status"] , axis = 'columns')
# print(inputs.head())

target = df['status']
# print(target.head())

from sklearn.preprocessing import LabelEncoder
le_gender  = LabelEncoder()
le_hscs    = LabelEncoder()
le_degreet = LabelEncoder()
le_wrokex  = LabelEncoder()

inputs['gender_n'] = le_gender.fit_transform(inputs['gender'])
inputs['hscs_n'] = le_gender.fit_transform(inputs['hsc_s'])
inputs['degreet_n'] = le_gender.fit_transform(inputs['degree_t'])
inputs['workex_n'] = le_gender.fit_transform(inputs['workex'])
# inputs.head()

inputs_n = inputs.drop(['gender', 'degree_t' , 'hsc_s' , 'workex'] , axis = 'columns')
# inputs_n.head()

from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(inputs_n , target )


import streamlit as st 
from PIL import Image
st.title('Campus Placement Predictor')
st.markdown("***")
img = Image.open("C://Users//bidav//OneDrive//Desktop//campus//placement.jpg")
st.image(img , width = 500)
st.write('')

name = st.text_input("Enter Your Name " )

gender = st.radio("Select Your Gender ", ( ' Male ' , ' Female '))
if gender == ' Male ':
    gender = 1
else:
    gender = 0

sscp = st.slider("Enter Your SSC Percentage")

hscs = st.selectbox('HSC Stream ',['Arts' , 'Commerce' , 'Science'])
if hscs == "Science":
    hscs = 1
elif hscs == "Commerce":
    hscs = 2
else:
    hscs = 0

hscp = st.slider("Enter Your HSC Percentage")

degreet = st.selectbox('Degree Type',['Commerce' , 'Science' , 'Other'])
if degreet == "Science":
    degreet = 2
elif degreet == "Commerce":
    degreet = 0
else:
    degreet = 1

degreep = st.slider("Enter Your DEGREE Percentage")

workex = st.radio("Do You Have Any Work Experience" , (' Yes ' , ' No '))
if workex == ' Yes ':
    workex = 1
else:
    workex = 0


if(st.button('Predict')):
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)

    result = model.predict([[ sscp , hscp , degreep , gender , hscs , degreet , workex ]])
    if result == "Placed":
        st.success(f"CONGRATULATIONS {name}! \nYOU ARE PLACED ")
        st.balloons()
    else:
        st.error(f"SORRY {name} YOU ARE NOT PLACED \n BETTER LUCK NEXT TIME")


