from flask import Flask, render_template, request, redirect
import test

app = Flask(__name__)

@app.route('/')
def get_username():
          
    return render_template('first_page.html')   

@app.route('/',methods=['POST'])
def index():
    list_images = test.img_coll()    
    if request.method == 'POST':
        user = request.form['username']

    return render_template('home.html',user=user, list_images=list_images)

@app.route('/news')
def get_news(): 

    item = test.cat_news()  
    return render_template('news.html',item=item, cat='news')       
    
@app.route('/sports/<cat>')
def get_sports(cat):

    news_sports_x = test.cat_sports(cat)
    return render_template('sports.html',news_sports_x=news_sports_x)

@app.route('/img')
def img_top():

    list_images = test.img_coll()
    return render_template('font.html',list_images=list_images)
         
if __name__ == "__main__":  
    app.run(debug=True)