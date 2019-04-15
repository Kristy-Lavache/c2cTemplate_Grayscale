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
    soldiers = []
    soldier1 = {}
    soldier1['name'] = "Steve Rodgers"
    soldier1['dob'] = "09/23/1786"
    soldier1['dod'] = "Unknown"
    soldier1['militaryBranch'] = "Army"
    soldier1['rank'] = "Unknown"
    soldiers.append(soldier1)
    soldier2 = {}
    soldier2['name'] = "Jane Doe"
    soldier2['dob'] = "09/23/1786"
    soldier2['dod'] = "12/28/1821"
    soldiers.append(soldier2)
    return soldiers
    # soldier3 = {}
    # soldier3['name'] = "Leo Bert Abramoski"
    # soldier3['dob'] = "02/07/1933"
    # sodlier3['dod'] = "07/28/1964"
    # soldier3['militaryBranch'] = "Army"
    # soldier3['rank'] = "CAPT"
    # soldiers.append(soldier3)
    # soldier4 = {}
    # soldier4['name'] = "Roberts John Achas"
    # soldier4['dob'] = "01/01/1943"
    # sodlier4['dod'] = "03/14/1965"
    # soldier4['militaryBranch'] = "Marine Corp"
    # soldier4['rank'] = "LCPL"
    # soldiers.append(soldier4)
    # soldier5 = {}
    # soldier5['name'] = "Jesse Rodriquez Acosta"
    # soldier5['dob'] = "08/06/1934"
    # sodlier5['dod'] = "05/16/1965"
    # soldier5['militaryBranch'] = "Air Force"
    # soldier5['rank'] = "SSGT"
    # soldiers.append(soldier5)
    # soldier6 = {}
    # soldier6['name'] = "James Blair Alexander"
    # soldier6['dob'] = "10/07/1925"
    # sodlier6['dod'] = "02/10/1965"
    # soldier6['militaryBranch'] = "Army"
    # soldier6['rank'] = "SP5"
    # soldiers.append(soldier6)
    # soldier7 = {}
    # soldier7['name'] = "James Edwin Bailey"
    # soldier7['dob'] = "04/28/1928"
    # sodlier7['dod'] = "09/04/1964"
    # soldier7['militaryBranch'] = "Army"
    # soldier7['rank'] = "SSGT"
    # soldiers.append(soldier7)
    # soldier8 = {}
    # soldier8['name'] = "Leo Bert Abramoski"
    # soldier8['dob'] = "02/07/1933"
    # sodlier8['dod'] = "07/28/1964"
    # soldier8['militaryBranch'] = "Army"
    # soldier8['rank'] = "CAPT"
    # soldiers.append(soldier8)
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

