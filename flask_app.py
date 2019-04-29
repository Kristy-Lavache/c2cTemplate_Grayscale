from flask import Flask, request, render_template
import json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")

@app.route('/form', methods=['GET'])
def form():
    # loaddata()
    return render_template("form.html")

@app.route('/data', methods=['GET'])
def data():
    #return render_template("data.html")
    return json.dumps(loaddata())


# def data():
#     file_object  = open("data.txt", "r")
#     line = file_object.readline()
#     info = line.split()
#     print(info)

def loaddata():
    name = request.args.get('name')
    branch = request.args.get('branch')
    birth = request.args.get('birth')
    death = request.args.get('death')
    soldiers = []
    soldier = {}
    soldier['name'] = "Leo Abramoski"
    soldier['dob'] = "1933-02-07"
    soldier['dod'] = "1964-07-28"
    soldier['militaryBranch'] = "Army"
    soldier['rank'] = "CAPT"
    soldiers.append(soldier)
    soldier01 = {}
    soldier01['name'] = "Steve Rodgers"
    soldier01['dob'] = "1786-09-23"
    soldier01['dod'] = "Unknown"
    soldier01['militaryBranch'] = "Army"
    soldier01['rank'] = "Unknown"
    soldiers.append(soldier01)
    soldier02 = {}
    soldier02['name'] = "Jane Doe"
    soldier02['dob'] = "1786-10-15"
    soldier02['dod'] = "1821-12-28"
    soldier02['militaryBranch'] = "Army"
    soldier02['rank'] = "LTFC"
    soldiers.append(soldier02)
    soldier03 = {}
    soldier03['name'] = "Roberts Achas"
    soldier03['dob'] = "1943-01-01"
    soldier03['dod'] = "1965-03-14"
    soldier03['militaryBranch'] = "Marine Corp"
    soldier03['rank'] = "LCPL"
    soldiers.append(soldier03)
    soldier04 = {}
    soldier04['name'] = "Jesse Acosta"
    soldier04['dob'] = "1934-08-06"
    soldier04['dod'] = "1965-05-16"
    soldier04['militaryBranch'] = "Air Force"
    soldier04['rank'] = "SSGT"
    soldiers.append(soldier04)
    soldier05 = {}
    soldier05['name'] = "James Alexander"
    soldier05['dob'] = "1925-10-07"
    soldier05['dod'] = "1965-02-10"
    soldier05['militaryBranch'] = "Army"
    soldier05['rank'] = "SP5"
    soldiers.append(soldier05)
    soldier06 = {}
    soldier06['name'] = "James Bailey"
    soldier06['dob'] = "1928-04-28"
    soldier06['dod'] = "1964-09-04"
    soldier06['militaryBranch'] = "Army"
    soldier06['rank'] = "SSGT"
    soldiers.append(soldier06)
    soldier07 = {}
    soldier07['name'] = "Thomas Bain"
    soldier07['dob'] = "1946-04-24"
    soldier07['dod'] = "1964-10-07"
    soldier07['militaryBranch'] = "Army"
    soldier07['rank'] = "PFC"
    soldiers.append(soldier07)
    soldier08 = {}
    soldier08['name'] = "Secundino Baldonado"
    soldier08['dob'] = "1927-07-01"
    soldier08['dod'] = "1965-05-16"
    soldier08['militaryBranch'] = "Air Force"
    soldier08['rank'] = "TSGT"
    soldiers.append(soldier08)
    soldier09 = {}
    soldier09['name'] = "Alfons Bankowski"
    soldier09['dob'] = "1930-06-15"
    soldier09['dod'] = "1961-05-23"
    soldier09['militaryBranch'] = "Air Force"
    soldier09['rank'] = "SSGT"
    soldiers.append(soldier09)
    soldier10 = {}
    soldier10['name'] = "Patrick Calhoun"
    soldier10['dob'] = "1941-03-19"
    soldier10['dod'] = "1965-04-19"
    soldier10['militaryBranch'] = "Army"
    soldier10['rank'] = "2LT"
    soldiers.append(soldier10)
    soldier11 = {}
    soldier11['name'] = "Gerald Capelle"
    soldier11['dob'] = "1934-12-23"
    soldier11['dod'] = "1965-04-01"
    soldier11['militaryBranch'] = "Army"
    soldier11['rank'] = "CAPT"
    soldiers.append(soldier11)
    soldier12 = {}
    soldier12['name'] = "William Cavanaugh"
    soldier12['dob'] = "1941-04-08"
    soldier12['dod'] = "1964-04-10"
    soldier12['militaryBranch'] = "Army"
    soldier12['rank'] = "SP4"
    soldiers.append(soldier12)
    soldier13 = {}
    soldier13['name'] = "Robert Clark"
    soldier13['dob'] = "1931-09-26"
    soldier13['dod'] = "1965-05-16"
    soldier13['militaryBranch'] = "Air Force"
    soldier13['rank'] = "SSGT"
    soldiers.append(soldier13)
    if name:
        soldiers = [s for s in soldiers if name in s['name']]
    if branch:
        soldiers = [s for s in soldiers if branch in s['militaryBranch']]
    if birth:
        soldiers = [s for s in soldiers if birth in s['dob']]
    if death:
        soldiers = [s for s in soldiers if death in s['dod']]
    return soldiers



if __name__ == '__main__':
    # print(data())
    #app.run()
    print(loaddata())

