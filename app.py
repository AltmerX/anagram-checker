from flask import Flask, request, render_template
import sys
import os

app = Flask(__name__)
@app.route("/")
def Display():
    str1=""
    str2=""
    return render_template('index.html', AreAnagrams="", str1=str1, str2=str2)    

@app.route("/", methods=['POST'])
def AnagramChecker():
    str1=request.form['str1']
    str2=request.form['str2']
    if str1=="" and str2=="":
        return render_template('index.html', AreAnagrams="Please enter strings!", str1=str1, str2=str2)
    hist1={}
    for i in str1:
        if i not in hist1:
            hist1[i]=0
        else:
            hist1[i]+=1
    hist2={}
    for i in str2:
        if i not in hist2:
            hist2[i]=0
        else:
            hist2[i]+=1
    ret= "No"
    if hist1==hist2:
        ret="Yes"
    return render_template('index.html', AreAnagrams=ret, str1=str1, str2=str2)

if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)
