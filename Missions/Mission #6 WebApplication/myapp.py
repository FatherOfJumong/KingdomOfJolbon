from flask import Flask,render_template,request
from api import generate_joke, give_categories
import random
import json
app = Flask(__name__)

#
@app.route('/')
@app.route('/home')
def home_page():
    categories = give_categories()
    return render_template("home.html",the_title = "Home", the_categories = categories,
                    my_title = 'Home Page')



def append_joke(joke):
    with open('jokes.txt', 'a') as jokesfile:
        print(joke,file = jokesfile)






@app.route('/random-joke', methods = ['POST'])
def read_random_joke():
    chosen_category = request.form.get('chosen-categ')
    generated_joke = generate_joke(chosen_category)
    


    categories = give_categories()
  
    chosen_joke = generate_joke(chosen_category)
    
    append_joke(chosen_joke)


    return render_template('results.html',the_joke = chosen_joke,
    the_categories = categories,my_title = 'Chuck Norris')




@app.route('/saved_jokes')
def show_jokes():
    content,d = [],{}
    with open('jokes.txt','r') as jokes:
        for joke in jokes:
            content.append(joke.strip("\n"))
        key = 'jokes'
        d.setdefault(key,[])
        for i in content:
            d[key].append(i)
        my_json = json.dumps(d,indent=4)



    return render_template('viewjokes.html',the_jokes = my_json)















if __name__ == "__main__":
    app.run(debug=True)
