# P75
# Napisz program do generowania wyników urządzenia pomiarowego:
# Użytkownik może wykonać pomiar (M)
# Użytkownik może zapisać pomiar (S) do pliku
# Użytkownik może dalej wykonywać pomiary dopisując ich wynik do pliku (A)
# Użytkownik może wyjść z programu (Q)
# Wynik pomiaru powinien być sformatowany w następujący sposób:
# Dane użytkownika
# Data pomiaru
# Wynik pomiaru -> przykładowy: User;Data,Result
import datetime
from os import getcwd, chdir
from pliki_pd.user import User
import random


class GenerateController():
    def __init__(self):
        self.users = []

    def __str__(self):
        output = ''
        for user in self.users:
            output += user.__str__() + "\n"
        if (output != ''):
            return "| %3s | %15s | %15s | %15s | %25s | %25s |" % ("ID", "Login", "Name", "Lastname", "Data Time", "Measurement")  + "\n" + output
        return ''

    def addUser(self, login, name, lastname):
        user = User(login, name, lastname)
        self.users.append(user)

    def findUserById(self, user_id_no):
        for user in self.users:
            if user.user_id_no == user_id_no:
                return user
        return None

    def deletedUserById(self, user_id_no):
        findUserById = self.findUserById(user_id_no)
        if findUserById != None:
            self.users.remove(findUserById)
            print("Usunięto urzytkownia " + findUserById.__str__())
        else:
            print("Brak takiego urzytkownika")

    def addTakeMeasurementById(self, user_id_no, from_no=1, to_no=49, n=6):
        """
        Randomly genearates a measurment: list of length n with max values to_no
        and min_values from_no. Appends measurment to users measurments
        :param user_id_no: user_id
        :param from_no: minimal measurment value
        :param to_no: maximal_measuement value
        :param n: sample size
        :return: None
        """
        self.from_no = from_no
        self.to_no = to_no
        self.n = n
        findUserById = self.findUserById(user_id_no)
        if findUserById != None:
            findUserById.data = []
            findUserById.measurement = []
            findUserById.data.append(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S"))
            findUserById.measurement.append(random.sample(range(from_no, to_no), n))
        else:
            print("Brak takiego urzytkownika")

    def deleteTakeMeasurementById(self, user_id_no):
        findUserById = self.findUserById(user_id_no)
        if findUserById != None:
            findUserById.data = []
            findUserById.measurement = []
        else:
            print("Brak takiego urzytkownika")

    def writeTakeMeasurement(self, name_file):
        url = getcwd()
        chdir(url)
        self.name_file = str(name_file) + ".txt"
        file = open(self.name_file, "w+", encoding="UTF-8")
        for user in self.users:
            file.write(str(user.user_id_no) + ';' + user.login + ';' + user.name + ';' + user.lastname + ';' + str(user.data) + ';' + str(user.measurement) + "\n")
        file.close()

    def addwriteTakeMeasurement(self, name_file):
        url = getcwd()
        chdir(url)
        name_file = str(name_file) + ".txt"
        file = open(name_file, "a")
        for user in self.users:
            file.write(str(user.user_id_no) + ';' + user.login + ';' + user.name + ';' + user.lastname + ';' + str(user.data) + ';' + str(user.measurement) + "\n")
        file.close()

    def readTakeMeasurement(self, name_file):
        url = getcwd()
        chdir(url)
        name_file = str(name_file) + ".txt"
        file = open(name_file, "r")
        print(file.read())
        file.close()