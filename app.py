# import streamlit as st
# import pickle
# import streamlit_option_menu as option_manue


# dibatese_model = pickle.load(open(r"C:\Users\Dell\Desktop\New folder\model.pkl","rb"))

# with st.sidebar:
    
#     selected = option_manue('Dibatese Pridiction system',
#                  ["Dibatese Prediction using ML",
#                   "Model 1","Model 2"],defult_index = 0)

                 
import streamlit as st
import pickle

# Load the diabetes model from the pickle file
diabetes_model =diabetes_model = pickle.load(open(r"C:\Users\HOME\OneDrive\Desktop\webapplive\model.pkl", "rb"), encoding="utf-8")
# Create a sidebar with the option menu
with st.sidebar:
    selected = st.selectbox('Diabetes Prediction System',
                            ["Diabetes Prediction using ML",
                             "Model 1", "Model 2"], index=0)

# Main application
if selected == ("Diabetes Prediction using ML"):
    st.title("Dibatese Pridiction using ML")

    # excessive_thurst = st.text("Did you feel excessive thirst? \t (yes/no)")
    # urinationn = st.text("Are you experiencing frequent urination? (yes/no)")
    #  st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    
    with col1:
        excessive_thurst = st.selectbox('Did you feel excessive thirst ?',options=["select option","yes","no"],index=0)
    
    if excessive_thurst.lower() == "yes":
        excessive_thurst = 1
    elif excessive_thurst == "no":
        excessive_thurst = 0
    else:
        st.error("Enter the valid input (yes or no)")
    
        
    with col2:
        urination = st.selectbox('Are you experiencing frequent urination ?',options=["select option","yes","no"],index=0)
    
    if urination.lower() == "yes":
        urination = 1
    elif urination == "no":
        urination = 0


    with col1:
        fatigue = st.selectbox('Do you often feel fatigued or weak ?',options=["select option","yes","no"],index=0)

    if fatigue.lower() == "yes":
        fatigue = 1
    elif fatigue == "no":
        fatigue = 0


    
    with col2:
        glucose = st.selectbox('Are you currently taking any medications that may affect blood sugar levels?',options=["select option","yes","no"],index=0)

    if glucose.lower() == "yes":
        glucose = 1    
    elif glucose == "no":
        glucose = 0


    with col1:
        vision_b = st.selectbox('Have you noticed any vision problem or blurred vision ?',options=["select option","yes","no"],index=0)


    if vision_b.lower() == "yes":
        vision_b = 1
    elif vision_b == "no":
        vision_b = 0

    with col2:
        numbness = st.selectbox('Are you experiencing any tingling or numbness in your extremities?',options=["select option","yes","no"],index=0)


    if numbness.lower() == "yes":
        numbness = 1
    elif numbness == "no":
        numbness = 0

    with col1:
        healing =  healing = st.selectbox('Have you noticed slow healing of wounds or infections?', options=["select option","yes","no"],index=0)


    if healing.lower() == "yes":
        healing = 1
    elif healing == "no":
        healing = 0

    with col2:
        genitics = st.selectbox("Does any one in your family hav history of  diabetes ?",options=["select option","yes","no"],index=0)


    if genitics.lower() == "yes":
        genitics = 1
    elif genitics == "no":
        genitics = 0
    with col1:
        Age = st.text_input('Age of the Person')



    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[excessive_thurst, urination, fatigue, glucose, vision_b, numbness , healing,genitics, Age]])
        if excessive_thurst == '' or urination == '' or fatigue == '' or glucose == '' or vision_b == '' or numbness == '' or healing == '' or genitics == '' or Age == '':
            st.error("Please fill in all the fields before making the prediction.")
        else:
            if (diab_prediction[0] == 1):
                diab_diagnosis = ('The person is diabetic')
            else:
                diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)










elif selected == "Model 1":
    st.title("My Next Model")
    pass
elif selected == "Model 2":
    st.title("page not found")
    pass

elif selected == "Model 1":
    st.title("page not")
    pass
elif selected == "Model 2":
    # Your code for Model 2 goes here
    pass
