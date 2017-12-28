from flask import Flask, render_template, request
import xml.etree.ElementTree as ET
import subprocess
import os
import speech
app = Flask(__name__)

select = "en-it"
 
@app.route('/new')
def render_static():
    return render_template('index.html')

@app.route('/new/record/', methods=['GET', 'POST'])
def record():

    if request.method == 'POST':
        
        
        print("hello")
        select =  request.form.get('languages')
        print(select)
        
    
    
        
    english, italian = speech.goldie(select).split('=')
    
    
    return render_template('index.html',result = english,result1 = italian)

if __name__ == '__main__':
    app.run()
