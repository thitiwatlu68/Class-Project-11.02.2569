from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
app = Flask(__name__)

@app.route("/myname/<name>")
def hello_world(name):
    return f"Hello, Worlddddddd........! {name}"

@app.route("/myprofile")
def myprofile():
    return render_template("my_profile.html", username="Wanarase", age=26, title="My Profile", is_admin = True)

@app.route("/tickets/<int:ticket_id>")
def ticket_detail(ticket_id):
    return f"Ticket #{ticket_id}"

@app.route("/")
def index():
    return render_template("home.html", title="Home")


@app.route("/about")
def about():
    print("call about page!!!!!!!!!!!")
    return render_template("about.html", title="about")


repair_case = [
    {"id": 1, "case_name": "แจ้งซ่อมพัดลม", "location": "ห้อง 101", "description": None, "created_at": "2026-02-05 10:00"},
    {"id": 2, "case_name": "แจ้งซ่อมแอร์",   "location": "ห้อง 202", "description": None, "created_at": "2026-02-05 10:05"},
    {"id": 3, "case_name": "แจ้งซ่อมประตู",  "location": "ห้อง 303", "description": None, "created_at": "2026-02-05 10:10"},
]

@app.route("/listRequest")
def list_request(): 
    return render_template("request_cases.html", request_cases=repair_case, title = "Case")




def next_id():
    return (max(x["id"] for x in repair_case) + 1) if repair_case else 1

@app.route("/repairs/new", methods=["GET", "POST"])
def new_case():
    if request.method == "POST":
        case_name = (request.form.get("case_name") or "").strip()
        location = (request.form.get("location") or "").strip()
        description = (request.form.get("description") or "").strip()

        errors = {}
        if not case_name:
            errors["case_name"] = "กรุณากรอกหัวข้อ"
        if not location:
            errors["location"] = "กรุณากรอกสถานที่/ห้อง"

        if errors:
            print(f"VALIDATION_FAIL case_name='{case_name}' location='{location}' errors={errors}")
            return render_template("new.html", form=request.form, errors=errors), 400

        case = {
            "id": next_id(),
            "case_name": case_name,
            "location": location,
            "description": description or None,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        repair_case.append(case)
        print(f"CREATED id={case['id']} case_name='{case_name}' location='{location}'")
        return redirect(url_for("list_request"))

    return render_template("new.html", form={}, errors={})





if __name__ == "__main__":
  app.run(debug=True, port =8000, host='0.0.0.0')