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
    birth = request.args.get('birth')
    branch = request.args.get('branch')
    name = request.args.get('name')
    soldiers = []
    soldier = {}
    soldier['name'] = "Leo Abramoski"
    soldier['dob'] = "02/07/1933"
    soldier['dod'] = "07/28/1964"
    soldier['militaryBranch'] = "Army"
    soldier['rank'] = "CAPT"
    soldiers.append(soldier)
    soldier01 = {}
    soldier01['name'] = "Steve Rodgers"
    soldier01['dob'] = "09/23/1786"
    soldier01['dod'] = "Unknown"
    soldier01['militaryBranch'] = "Army"
    soldier01['rank'] = "Unknown"
    soldiers.append(soldier01)
    soldier02 = {}
    soldier02['name'] = "Jane Doe"
    soldier02['dob'] = "10/15/1786"
    soldier02['dod'] = "12/28/1821"
    soldier02['militaryBranch'] = "Army"
    soldier02['rank'] = "LTFC"
    soldiers.append(soldier02)
    soldier03 = {}
    soldier03['name'] = "Roberts Achas"
    soldier03['dob'] = "01/01/1943"
    soldier03['dod'] = "03/14/1965"
    soldier03['militaryBranch'] = "Marine Corp"
    soldier03['rank'] = "LCPL"
    soldiers.append(soldier03)
    soldier04 = {}
    soldier04['name'] = "Jesse Acosta"
    soldier04['dob'] = "08/06/1934"
    soldier04['dod'] = "05/16/1965"
    soldier04['militaryBranch'] = "Air Force"
    soldier04['rank'] = "SSGT"
    soldiers.append(soldier04)
    soldier05 = {}
    soldier05['name'] = "James Alexander"
    soldier05['dob'] = "10/07/1925"
    soldier05['dod'] = "02/10/1965"
    soldier05['militaryBranch'] = "Army"
    soldier05['rank'] = "SP5"
    soldiers.append(soldier05)
    soldier06 = {}
    soldier06['name'] = "James Bailey"
    soldier06['dob'] = "04/28/1928"
    soldier06['dod'] = "09/04/1964"
    soldier06['militaryBranch'] = "Army"
    soldier06['rank'] = "SSGT"
    soldiers.append(soldier06)
    return [s for s in soldiers if name in s['name']]
    return [s for s in soldiers if branch in s['branch']]
    return [s for s in soldiers if birth in s['birth']]
    # soldier9 = {}
    # soldier9['name'] = "Thomas Arthur Bain"
    # soldier9['dob'] = "04/24/1946"
    # sodlier9['dod'] = "10/07/1964"
    # soldier9['militaryBranch'] = "Army"
    # soldier9['rank'] = "PFC"
    # soldiers.append(soldier9)
    # soldier10 = {}
    # soldier10['name'] = "Secundino Baldonado"
    # soldier10['dob'] = "07/01/1927"
    # sodlier10['dod'] = "05/16/1965"
    # soldier10['militaryBranch'] = "Air Force"
    # soldier10['rank'] = "TSGT"
    # soldiers.append(soldier10)
    # soldier11 = {}
    # soldier11['name'] = "Alfons Aloyze Bankowski"
    # soldier11['dob'] = "06/15/1930"
    # sodlier11['dod'] = "05/23/1961"
    # soldier11['militaryBranch'] = "Air Force"
    # soldier11['rank'] = "SSGT"
    # soldiers.append(soldier11)
    # soldier12 = {}
    # soldier12['name'] = "Patrick Palmer Calhoun"
    # soldier12['dob'] = "03/19/1941"
    # sodlier12['dod'] = "04/19/1965"
    # soldier12['militaryBranch'] = "Army"
    # soldier12['rank'] = "2LT"
    # soldiers.append(soldier12)
    # soldier13 = {}
    # soldier13['name'] = "Gerald Carl Capelle"
    # soldier13['dob'] = "12/23/1934"
    # sodlier13['dod'] = "04/01/1965"
    # soldier13['militaryBranch'] = "Ary"
    # soldier13['rank'] = "CAPT"
    # soldiers.append(soldier13)
    # soldier14 = {}
    # soldier14['name'] = "William Thomas Cavanaugh"
    # soldier14['dob'] = "04/08/1941"
    # sodlier14['dod'] = "04/10/1964"
    # soldier14['militaryBranch'] = "Army"
    # soldier14['rank'] = "SP4"
    # soldiers.append(soldier14)
    # soldier15 = {}
    # soldier15['name'] = "Robert Lewis Clark"
    # soldier15['dob'] = "09/26/1931"
    # sodlier15['dod'] = "05/16/1965"
    # soldier15['militaryBranch'] = "Air Force"
    # soldier15['rank'] = "SSGT"
    # soldiers.append(soldier15)


if __name__ == '__main__':
    # print(data())
    #app.run()
    print(loaddata())

