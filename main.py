import streamlit as st
from preprocess import model, load_data;

st.title("My Insurance Prediction Website")
st.markdown("### The ML model uses Liner Regression Algo to make predictions")



st.subheader("Select Values")

age = st.slider("Age", 0, 100)
bmi = st.slider("BMI", 10.0, 35.0)
children = st.slider("Children", 0, 10)
sex = st.selectbox("Sex", ["Male", "Female"])
smoker = st.selectbox("Somker", ["Yes", "No"])
region = st.selectbox("Region", ["northwest", "northeast", "southeast", "southwest"])

if (region == "northwest"):
    region = 0
elif (region == "northeast"):
    region = 1
elif (region == "southeast"):
    region = 2
elif (region == "southwest"):
    region = 3

if (sex == "Male"):
    sex = 0
else:
    sex = 1

if (smoker == 'No'):
    smoker = 0
else:
    smoker = 1


feature = [[age, sex, bmi, children, smoker, region]]

if (st.button("Predict")):

    my_model, acc = model()
    Prediction = my_model.predict(feature)

    st.success("Predicted Successfully")
    st.success("Our Model accuracy is ", acc)
    st.warning(f"Charges values is {round(Prediction[0],2)}")