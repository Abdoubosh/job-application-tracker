from flask import Flask, render_template

from database import get_connection, initialize_database


app = Flask(__name__)
initialize_database()


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


if __name__ == "__main__":
    app.run(debug=True)
