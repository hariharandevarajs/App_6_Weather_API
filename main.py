"""
first create for testing Purpose
"""
# from sympy.physics.units import temperature

# from flask import Flask,render_template
#
# app = Flask("Website")
# @app.route("/home/")
# def home():
#     return render_template("tutorial.html")
# @app.route("/about/")
# def About():
#     return render_template("about.html")
# app.run(debug=True)

"""
Now we dont need those tutorial and 
about page - we were created for testing 
so remove from template folder or drag out from that folder 
and create home.html
"""

# from flask import Flask,render_template
#
# app = Flask("Website")
# @app.route("/")
# def home():
#     return render_template("home.html")
# @app.route("/api/v1/<station>/<date>")
# def About(station,date):
#     template = 23
#     return {"station":station,
#             "date":date,
#             "template":template}
# if __name__ == "__main__":
#     app.run(debug=True)
#     #YOU CAN ABLE TO CHANGE THE PORT , BY DEFAULT 5000 ONLY THERE
#     # app.run(debug=True,port=5001)

"""
Stuent Project exercise
"""

# from flask import Flask, render_template, request
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return render_template('Student_home.html')
#
# @app.route('/api/v1/<word>')
# # def words(word):
# #     return {"desc":word.title(),
# #             "word":word.lower()}
# def words(word):
#     definiation = word.title()
#     result_disc={"desc":definiation,
#             "word":word}
#     return result_disc
# @app.route('/api/v1/sun')
# def sun():
#     return {"desc":"sun is yellow color",
#             "word":'SUN'}
# @app.route('/api/v1/earth')
# def earth():
#     return {"desc":"earth is blue",
#             "word":'EARTH'}
#
# if __name__ == '__main__':
#     app.run(debug=True,port=5002)

'''
Jupyter Lab Tutorial and installation
step 1: open cmdline , then enter py -3.11
if you already have python you get output like this 

Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

then click up arrrow enter along with exiting cmd like - py -3.11 -m pip install jupyterlab

then open any of the folder you want run program for example. download folder right click go cmd line and enter jupyter-lab
lab will open new screen then clcik python file , now you can ready to work on jupyter
'''

'''
why we use jupyter bcz if we use python sell 
in cmd line it will gone once i close the cmd line 
right ,but in the jupter it would create seperate file so you can reuse anytime , 
it will help to organize the code, and we can use mainly for data loding and plot graphs
'''


# Pandas Tutorial Start
#
# In cmd Line - type - where python
# there you use cmd - py -3.14 -m pip install pandas
# for eg.C:\Users\devap\AppData\Local\Programs\Python>py -3.14 -m pip install pandas
# then use cmd py -3.14 -m pip install matplotlib
# C:\Users\devap\AppData\Local\Programs\Python\Python314>py -3.14 -m pip install matplotlib
#
#



# In jupyter use this code in cell and execute this
# cell1 - import pandas as pd - check whether you get error or not - ctrl + enter
# cell2 - df= pd.read_csv(rf"C:\Users\devap\Downloads\Jupyter\data-small\TG_STAID000001.txt",skiprows=20,parse_dates=["    DATE"])
# //first 20row text no need so skip , and enter the Date and before space as it was in the .txt file then only we get correct output
# cell3 - df

"""
Here after in jupyter folder see jupyter file , there all panda related codes are there.
"""

"""
APT that return to wheather temperature Data
"""

# from flask import Flask,render_template
# import pandas as pd
#
# app = Flask(__name__)
# @app.route("/")
# def home():
#     return render_template("home.html")
# @app.route("/api/v1/<station>/<date>")
# def About(station,date):
#     filename="data-small/TG_STAID"+ str(station).zfill(6)+".txt"
#     df=pd.read_csv(filename,skiprows=20,parse_dates=['    DATE'])
#     temperature = df.loc[df['    DATE']==date]['   TG'].squeeze() /10
#
#     return {"station":station,
#             "date":date,
#             "template":temperature}
# if __name__ == "__main__":
#     app.run(debug=True)

"""
Next  Student project there in student_project.py just workout
"""

"""
then we show the station.txt file to frontend like table format
"""

from flask import Flask,render_template
import pandas as pd

app = Flask(__name__)


# variable = "hi how are you"
staions=pd.read_csv("data-small/stations.txt",skiprows=17)
# if you want customized columns go with this step

staions = staions[["STAID","STANAME                                 "]]



@app.route("/")
def home():
    # return render_template("home.html",data=variable)
    return render_template("home.html", data=staions.to_html())
@app.route("/api/v1/<station>/<date>")
def About(station,date):
    filename="data-small/TG_STAID"+ str(station).zfill(6)+".txt"
    df=pd.read_csv(filename,skiprows=20,parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE']==date]['   TG'].squeeze() /10
    station_name=staions.loc[staions['STAID']==int(station)]["STANAME                                 "].squeeze()
    # we get some type error bczs STAID - is numeric come from txt.file
    # station is string so we need to convert as int thats it error solved we got the output

    return {"station":station,
            "station_name":station_name,
            "date":date,
            "template":temperature}
if __name__ == "__main__":
    app.run(debug=True)