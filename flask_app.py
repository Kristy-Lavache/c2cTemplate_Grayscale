from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")

@app.route('/form', methods=['GET'])
def form():
    return render_template("form.html")

def data():
    file_object  = open("data.txt", "r")
    line = file_object.readline()
    info = line.split()
    print(info)

if __name__ == '__main__':
    # app.run()
    data()
