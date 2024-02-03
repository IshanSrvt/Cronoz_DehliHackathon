from flask import Flask, render_template, request
import openai
app = Flask(__name__,template_folder='./')
openai.api_key  = "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"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = 'hehe'
    
    return response.choices[0].message["content"]
@app.route("/")
def home():    
    return render_template("index.html")
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = 'hehehe'
    #return str(bot.get_response(userText)) 
    return response
if __name__ == "__main__":
    app.run()