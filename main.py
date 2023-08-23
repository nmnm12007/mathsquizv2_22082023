from flask import *
import gameDB
import gameMain

app = Flask(__name__)
u_name, u_id, std, loop_count, correct_ans, res = '', 1, 1, 1, 0, ''


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_user_details")
def add_user():
    return render_template("add_user_details.html")


@app.route("/save_user", methods=["POST", "GET"])
def save_user():
    result_notif = "DEFAULT"
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        std1 = request.form["std"]
        result_notif = gameDB.add_user(name, address, std1)
    return render_template("success.html", result_notif=result_notif)


@app.route("/view_results")
def view_results():
    rows = gameDB.get_users()
    return render_template("view_user.html", rows=rows)


@app.route("/enterUserName", methods=["POST", "GET"])
def enter_username():
    return render_template("enterUserName.html")


@app.route("/showStd", methods=["POST", "GET"])
def show_std():
    global u_name, u_id, std, correct_ans, res
    gameMain.success_cnt = 0
    u_name = request.form["username1"]
    try:
        u_id, std, sco, res = gameDB.get_user_id_std(u_name)
        if std == 0:
            err1 = "Invalid Username entered"
            return render_template("error.html", e=err1)
        else:
            return render_template("showStd.html", username1=u_name, u_id=u_id, std=std, score=sco)
    except TypeError as e:
        print("Exception in fetching record with Username  " + u_name + res + str(e))
        err1 = "Exception in fetching record with Username  " + u_name + res + str(e)
        return render_template("error.html", e=err1)


@app.route("/quizQuestion", methods=["POST", "GET"])
def quiz_question():
    global u_id, std, loop_count, correct_ans
    if loop_count <= 5:
        s11, s21, op11 = gameMain.pose_quiz(std)
        return render_template("quizQuestion.html", a=s11, b=s21, op=op11)
    else:
        result_notif = gameDB.update_user(u_id, correct_ans)
        print("User Update result " + result_notif)
        print("TOTAL CORRECT ANSWERS:  " + str(correct_ans))
        loop_count = 1
        return render_template("quizResult.html", username=u_name, id=u_id, score=correct_ans)


@app.route("/quizAnswer", methods=["POST", "GET"])
def quiz_answer():
    global loop_count, std, correct_ans
    if loop_count <= 5:
        answer = request.form["answer"]
        c_answer, h_answer, correct_ans = gameMain.check_answer(std, answer)
        loop_count += 1
        return render_template("quizAnswer.html", answer=c_answer, h_ans=h_answer)


@app.route("/quitGame", methods=["POST", "GET"])
def quit_game():
    err1 = "Hi  " + u_name + "  You have opted to QUIT the Maths Quiz midway"
    return render_template("error.html", e=err1)


@app.route("/delete_enter_username")
def delete_enter_username():
    return render_template("deleteEnterUsername.html")


@app.route("/deleteUsername", methods=["POST", "GET"])
def delete_username():
    n = request.form["username"]
    result_notif = gameDB.delete_user(n)
    return render_template("deleteUserResult.html", username=n, result_notif=result_notif)


if __name__ == "__main__":
    gameDB.create_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
