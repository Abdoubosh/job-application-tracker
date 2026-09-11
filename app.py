from flask import Flask, redirect, render_template, request, url_for

from database import get_connection, initialize_database


app = Flask(__name__)
initialize_database()

STATUSES = ("Applied", "Test", "Interview", "Rejected", "Offer")


@app.route("/")
def index():
    connection = get_connection()
    applications = connection.execute(
        """
        SELECT id, company, position, location, application_date,
               job_url, status, notes, deadline_date, deadline_type
        FROM applications
        ORDER BY application_date DESC, id DESC
        """
    ).fetchall()
    connection.close()

    return render_template("index.html", applications=applications)


@app.route("/applications/new", methods=("GET", "POST"))
def add_application():
    error = None
    form_data = {}

    if request.method == "POST":
        form_data = request.form

        company = request.form.get("company", "").strip()
        position = request.form.get("position", "").strip()
        location = request.form.get("location", "").strip()
        application_date = request.form.get("application_date", "").strip()
        job_url = request.form.get("job_url", "").strip()
        status = request.form.get("status", "").strip()
        notes = request.form.get("notes", "").strip()
        deadline_date = request.form.get("deadline_date", "").strip()
        deadline_type = request.form.get("deadline_type", "").strip()

        if not company or not position or not application_date or not status:
            error = "Company, position, application date, and status are required."
        elif status not in STATUSES:
            error = "Please choose a valid application status."
        else:
            connection = get_connection()
            connection.execute(
                """
                INSERT INTO applications (
                    company, position, location, application_date, job_url,
                    status, notes, deadline_date, deadline_type
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    company,
                    position,
                    location,
                    application_date,
                    job_url,
                    status,
                    notes,
                    deadline_date,
                    deadline_type,
                ),
            )
            connection.commit()
            connection.close()

            return redirect(url_for("index"))

    return render_template(
        "add_application.html",
        error=error,
        form_data=form_data,
        statuses=STATUSES,
    )


if __name__ == "__main__":
    app.run(debug=True)
