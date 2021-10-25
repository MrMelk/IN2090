import pandas as pd
#Oppgave 1
kurs = pd.read_csv("kurs.csv")
studenter = pd.read_csv("studenter.csv")
tar_kurs = pd.read_csv("tar_kurs.csv")

def string_to_list(streng):
    s = []
    for i in streng:
        s.append(i)
    return s

"""
etternavn = studenter["etternavn"]
print(etternavn)
print(len(etternavn))


print(string_to_list(etternavn[0]))
navn = studenter[["fornavn", "etternavn"]]
h = navn[navn.etternavn == "borg"]
print(h)
print(list(h.itertuples(index = False, name = None))[0][0])
def get_cum(names, letter): #finner fornavn og etternavn basert på start bokstav i etternavn
    for_navn = names["fornavn"]
    etter_navn = names["etternavn"]

    print("etternavn", etter_navn)
    cum = []
    for name in etter_navn:
        print("navn og bokstav", name, letter)
        s = string_to_list(name)
        if s[0] == letter:
            full_name = names[names.etternavn == name]
            full_name = list(full_name.itertuples(index = False, name = None))[0]
            full_name = full_name[0] + " " + full_name[1]
            cum.append(full_name)
    print(cum)
    return cum

print(get_cum(navn, "g"))
"""
"""
#2
print(kurs["kurskode"])
def get_kurs(kurs_liste, fakultetkode):
    kode_liste = kurs_liste["kurskode"]
    our_course = []
    fakkode = list(fakultetkode)
    for streng in kode_liste:
        pass
        temp = []
        for s in streng:
            if s.isdigit():
                break
            else:
                temp.append(s)

        if len(temp) == len(fakultetkode):
            if temp == fakkode:
                our_course.append(streng)

    return our_course

#test = get_kurs(kurs, "IN")
#print(test)
"""
def get_cum2(courses, emnekode):#finner kurs med en gitt emnekode
    "Skal få oversikt over alle kurs som starter med IN, det inkluderer INF"
    kode_liste = courses["kurskode"]
    our_courses = []
    print(courses["kurskode"])
    for course in kode_liste:
        print("hei", course)
        temp = ""
        for i in range(len(emnekode)):
            temp += course[i]
        if temp == emnekode:
            our_courses.append(course)
    return our_courses
"""
swag = get_cum2(tar_kurs, "IN")
print(swag)

print(tar_kurs.loc[tar_kurs["kurskode"] == "IN2000"])#Får alle som tar kurset IN2000
deltagere_og_kurs_info = pd.merge(kurs, tar_kurs)
df3 = deltagere_og_kurs_info#trenger vel egt ikke dette
#print(df3.columns)
"""
def get_id_from_course(signed_up, course):
    ids = []
    koder = get_cum2(signed_up, course)
    for kode in koder:
        student = signed_up.loc[signed_up["kurskode"] == kode]
        studentid = student["studentid"]
        ids.append(studentid)
    return ids

print(kurs.loc[1][0])#test
print(tar_kurs.shape[0])
print()


def remove_cum(students, birthdate): #removes students if they were born before a certain year
    new_students = students[students.født > birthdate]
    return new_students
n_Students = remove_cum(studenter, "1992-01-01")
