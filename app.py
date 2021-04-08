import ktrain
import pandas as pd
from flask import Flask, request,render_template

app = Flask(__name__)

def x(df):

    df2 = pd.read_excel(df)
    df2['text']=df2.iloc[:,0]

    text= []
    for i in range(len(df2)):
        text = text + [df2['text'][i]]
        
    tm = ktrain.text.get_topic_model(text, n_features=500)
    output0 = tm.topics
    result =[]
    for j in range(len(output0)):
       tid = str(j)  
       prefix = 'Topic ' +   tid + ":  "      
       suffix  = output0[j]
       result = result + [prefix + suffix]
    
    output = result

    
    return output

@app.route("/")
def my_form():
    
    return render_template('home.html')

@app.route("/", methods=["POST","GET"])

def plz():
    f = request.files['file']
    output = x(f)
    return render_template('home.html',output=output)



if __name__ == "__main__":
    app.run()
    

