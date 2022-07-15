import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from readability import readability, count_letters, count_words, count_sentences
from similarity import calcula_assinatura, compara_assinatura 

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.run(debug=True) # Delete this line when publish the application

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        # readability
        text_input = request.form.getlist("text_input")

        # create lists
        text_list = []
        readability_dict = []

        # checks if text is empty
        for text in text_input:
            if text != "":
                text_list.append(text)
        
        # loops all the texts in text_list through Readability
        for text in text_list:
            readability_dict.append({"text": text, "letters": count_letters(text), "words": count_words(text), "sentences": count_sentences(text), "result": readability(text)})

        similarity = -1
        sig_1 = []
        sig_2 = []

        if request.form.get("inlineCheckbox") == "similarity":
            sig_1 = calcula_assinatura(text_list[0])
            sig_2 = calcula_assinatura(text_list[1])
            sab = compara_assinatura(sig_1, sig_2)
            if sab > 10:
                similarity = 0
            else:
                similarity = abs(round((sab * 100) / 10) - 100)
        
        # return lists
        return render_template("result.html", readability_dict=readability_dict, similarity=similarity)
    
    # method == GET
    else:
        return render_template("index.html")