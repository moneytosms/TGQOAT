name = ''
user = ''


def signup():
    global name
    global user
    import mysql.connector as f
    x = f.connect(host='localhost', user='root', passwd='mysql', charset='utf8')
    c = x.cursor()
    c.execute('create database if not exists quiz')
    c.execute('use quiz')
    c.execute(
        'create table if not exists quiz_entries(User_ID int auto_increment, Name varchar(30) NOT NULL,Age varchar(4) '
        'NOT NULL, Username varchar(30) NOT NULL,Password varchar(20) NOT NULL, Total_Score int NOT NULL, '
        'HighScore int NOT NULL, primary key(User_ID))')
    c.execute('select * from quiz_entries')
    n = input("Enter your name ")
    name = n
    name.title()
    a = input("Enter your age ")
    y = input("Create username ")
    hscore = 0
    user = y
    pscore = 0
    up = c.fetchall()

    list = []
    for i in up:
        list.append(i[3])
    while y in list:
        print("Username already exists choose new username")
        y = input("Enter new username ")

    p = input("Create password ")
    c.execute(
        "insert into quiz_entries (Name,Age,Username,Password,Total_Score,HighScore) values('%s','%s','%s','%s',%d,%d)" % (
            n, a, y, p, pscore, hscore))
    x.commit()
    print('signed in successfully')


def login():
    global user
    import mysql.connector as f
    x = f.connect(host='localhost', user='root', passwd='mysql', charset='utf8')
    c = x.cursor()
    c.execute('use quiz')

    u = input('Enter Username ')

    user = u
    p = input('Enter Password ')

    c.execute('select username, password from quiz_entries')

    data = c.fetchall()
    l = []
    for i in data:
        l.append(i[0])
        l.append(i[1])
    for j in data:
        if j[0] == user:

            if j[1] == p:
                return True

    if user not in l:
        return False

    elif p not in l:
        return False


def viewprofile():
    # global t_score
    global user
    import mysql.connector as f
    x = f.connect(host='localhost', user='root', passwd='mysql', charset='utf8')
    c = x.cursor()
    c.execute('use quiz')
    c.execute('select * from quiz_entries')
    data = c.fetchall()

    for i in data:

        if i[3] == user:
            print("Name: ", i[1], "   Age: ", i[2], "   Username: ", i[3], "   Password: ", i[4], "   Total Score: ",
                  i[5], "   HighScore:", i[6])


def delete():
    global user
    import mysql.connector as f
    x = f.connect(host='localhost', user='root', passwd='mysql', charset='utf8')
    c = x.cursor()
    c.execute('use quiz')
    c.execute('select * from quiz_entries')
    data = c.fetchall()

    b = input('Enter password ')
    for i in data:

        if i[3] == user:

            while i[4] != b:
                print("Password incorrect please re enter")
                b = input("Re enter password ")

    c.execute('delete from quiz_entries where username = "%s"' % (user))
    x.commit()
    print("Deleted successfully")


def ldb():
    import mysql.connector as f
    x = f.connect(host='localhost', user='root', passwd='mysql', database='quiz', charset='utf8')
    c = x.cursor()
    c.execute('use quiz')
    c.execute('select * from quiz_entries order by HighScore desc')
    data = c.fetchall()
    print("Name                Score")
    for i in data:
        n = 20 - len(i[1])
        print(i[1], " " * n, i[6])


def update():
    global user
    import mysql.connector as f
    x = f.connect(host='localhost', user='root', passwd='mysql', database='quiz', charset='utf8')
    c = x.cursor()
    c.execute('use quiz')
    c.execute('select * from quiz_entries where username="%s"' % (user))
    data = c.fetchall()

    a = input('Enter password ')
    for i in data:
        if i[3] == user:
            while i[4] != a:
                print("Incorrect password try again")
                a = input('Re enter password ')
            b = input('Enter new password ')
    pp = ('update quiz_entries set password=%s where password=%s')
    c.execute(pp, (b, a))
    x.commit()
    print("Password updated successfully")


def vt():
    import mysql.connector as f
    x = f.connect(host='localhost', user='root', passwd='mysql', charset='utf8')
    c = x.cursor()
    c.execute('use quiz')
    c.execute('select * from quiz_entries')
    data = c.fetchall()

    for i in data:
        print("Name: ", i[1], "   Age: ", i[2], "   Username: ", i[3], "   Score: ", i[5])


def changescore(nscore):
    global user
    pscore = 0
    import mysql.connector as f
    x = f.connect(host='localhost', user='root', passwd='mysql', charset='utf8')
    c = x.cursor()
    c.execute('use quiz')
    c.execute('select Total_Score from quiz_entries where Username="%s"' % (user))
    data = c.fetchall()
    pscore = data[0][0]
    sc = pscore + nscore
    c.execute('update quiz_entries set Total_Score=%d where Username="%s"' % (sc, user))
    x.commit()


def rethscore():
    """

    :rtype: object
    """
    global user
    import mysql.connector as f
    x = f.connect(host='localhost', user='root', passwd='mysql', charset='utf8')
    c = x.cursor()
    c.execute('use quiz')
    c.execute('select HighScore from quiz_entries where Username="%s"' % (user))
    data = c.fetchall()
    return data[0][0]


def changehscore(hscore):
    global user
    import mysql.connector as f
    x = f.connect(host='localhost', user='root', passwd='mysql', charset='utf8')
    c = x.cursor()
    c.execute('use quiz')
    c.execute('update quiz_entries set HighScore=%d where Username="%s"' % (hscore, user))
    x.commit()
