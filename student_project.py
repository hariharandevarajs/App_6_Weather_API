from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

print("hello")
df = pd.read_csv(rf"C:\Users\devap\Downloads\app6_weather_api\dictionary.csv")

@app.route("/")
def home():
    return render_template("Student_home.html")

@app.route("/api/v1/<word>")
def words(word):
        print("Hi")
        # df = pd.read_csv(rf"C:\Users\devap\Downloads\app6_weather_api\dictionary.csv")
        # we need to load one timme is enough no need to load every time right thats why i moved this line outside of the function
        # hi print multiple times but hello print once bczs when server startiing time onlly print all this
        definition_ans = df.loc[df['word']==word]['definition'].squeeze()

        final_result={
        "word":word,
        "definition": definition_ans,
                     }
        return final_result

if __name__ == "__main__":
    app.run(debug=True)

