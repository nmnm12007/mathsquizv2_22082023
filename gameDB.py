import sqlite3


def create_db():
    con = sqlite3.connect("game_results.db")
    print("Database Opened Successfully")

    con.execute("create table if not exists game_results (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT "
                "NULL,address TEXT UNIQUE NOT NULL, std INTEGER NOT NULL, score INTEGER)")
    print("Table created Successfully")


def add_user(name, address, std):
    result_notif = ''
    try:
        with sqlite3.connect("game_results.db") as con:
            cur = con.cursor()
            cur.execute("insert into game_results (name, address, std) values (?, ?, ?) ", (name, address, std))
            con.commit()
            result_notif = "User " + name + " Added Successfully"
            print(result_notif)
    except sqlite3.DatabaseError:
        con.rollback()
        result_notif = "User cannot be added, Failed"
        print("sqlite3 DatabaseError Exception")
        print(result_notif)
    except Exception as e:
        con.rollback()
        print("Exception raised " + str(e))
        result_notif = "User cannot be added, Failed" + str(e)
        print(result_notif)
    finally:
        con.close()
        return result_notif


def update_user(i, score):
    result_notif = ""
    try:
        with sqlite3.connect("game_results.db") as con:
            cur = con.cursor()
            cur.execute("update game_results set score = ? where id = ?", (score, i))
            con.commit()
            result_notif = "User " + str(i) + "'s score " + " " + str(score) + " Updated Successfully"
            print(result_notif)
    except sqlite3.DatabaseError:
        con.rollback()
        result_notif = "User cannot be edited, Failed"
        print("sqlite3 DatabaseError Exception")
        print(result_notif)
    except Exception as e:
        con.rollback()
        print("Exception raised " + str(e))
        result_notif = "User cannot be edited, Failed" + str(e)
        print(result_notif)
    finally:
        con.close()
        return result_notif


def get_user_id_std(n):

    try:
        with sqlite3.connect("game_results.db") as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select id, std, score from game_results where name = ?", (n,))
            i, std, sco = cur.fetchone()
            print("get_user_id_std() i : std : score" + str(i) + str(std) + str(sco))
            result_notif = "get_user_id_std() i : std : score" + str(i) + str(std) + str(sco)
            return i, std, sco, result_notif
    except sqlite3.DatabaseError:
        print("get_user_id_std() DatabaseError Exception" + "Returning Default Values")
        result_notif = "get_user_id_std() DatabaseError Exception" + "Returning Default Values"
        return 0, 0, 0, result_notif
    except Exception as e:
        print("Exception raised from get_user_id_std() " + "Returning Default Values  " + str(e))
        result_notif = "Exception raised from get_user_id_std() " + "Returning Default Values  " + str(e)
        return 0, 0, 0, result_notif
    finally:
        con.close()


def get_users():
    con = sqlite3.connect("game_results.db")
    try:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from game_results")
        rows = cur.fetchall()
        return rows
    finally:
        con.close()


def delete_user(n):
    i, s, sco, result_notif = get_user_id_std(n)
    if i == 0:
        result_notif += "Failed Deletion of user " + n
        return result_notif
    else:
        try:
            with sqlite3.connect("game_results.db") as con:
                cur = con.cursor()
                cur.execute("delete from game_results where id = ?", (i,))
                con.commit()
                result_notif = "User " + n + " Deleted Successfully"
                print(result_notif)
        except sqlite3.DatabaseError:
            con.rollback()
            print("User " + n + "Not Deleted Database Error")
            result_notif = "User " + n + "Not Deleted Database Error"
        except Exception as e:
            con.rollback()
            print("Exception raised during User " + n + "'s Deletion" + str(e))
            result_notif = "Exception raised during User " + n + "'s Deletion" + str(e)
        finally:
            con.close()
            return result_notif
