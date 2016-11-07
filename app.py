from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/", methods=['POST'])
def AnagramChecker():
    str1=request.form['str1']
    str2=request.form['str2']
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
    ret= "Yes"
    if hist1==hist2:
        ret="No"
    return render_template('index.html', AreAnagrams=ret)

if __name__ == "__main__":
    app.run()
