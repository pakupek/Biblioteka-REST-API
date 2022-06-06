from flask import Flask, request, render_template, redirect, url_for
from forms import MoviesForm, SeriesForm
from models import movies, series


app = Flask(__name__)
app.config["SECRET_KEY"] = "dadadada"

#Wyświetla liste filmów
@app.route("/movies/", methods=["GET", "POST"])
def movies_list():
    form = MoviesForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            movies.create(form.data)
            movies.save_all()
        return redirect(url_for("movies_list"))

    return render_template("movies.html", form=form, movies=movies.all(), error=error)

#Dodawanie filmu
@app.route("/movies/adds/", methods=["GET","POST"])
def add_movies():
    form = MoviesForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            movies.create(form.data)
            movies.save_all()
        return redirect(url_for("movies_list"))
    return render_template("addmovie.html", form=form, movies=movies.all(), error=error)


#Wybranie filmu oraz ewentualna zmiana
@app.route("/movies/<int:movie_id>/", methods=["GET", "POST"])
def todo_details(movie_id):
    movie = movies.get(movie_id - 1)
    form = MoviesForm(data=movie)
    if request.method == "POST":
        if form.validate_on_submit():
            movies.update(movie_id - 1, form.data)
        return redirect(url_for("movies_list"))
    return render_template("movie.html", form=form, movie_id=movie_id)


#Wyświetla liste seriali
@app.route("/series/", methods=["GET", "POST"])
def series_list():
    form = SeriesForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            series.create(form.data)
            series.save_all()
        return redirect(url_for("movies_list"))

    return render_template("series.html", form=form, series=series.all(), error=error)


#Dodawanie serialu
@app.route("/series/adds/", methods=["GET","POST"])
def add_series():
    form = SeriesForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            series.create(form.data)
            series.save_all()
        return redirect(url_for("series_list"))
    return render_template("addseries.html", form=form, series=series.all(), error=error)


#Wybranie serialu oraz ewentualna zmiana
@app.route("/series/<int:series_id>/", methods=["GET", "POST"])
def series_details(series_id):
    serie = series.get(series_id - 1)
    form = SeriesForm(data=serie)
    if request.method == "POST":
        if form.validate_on_submit():
            series.update(series_id - 1, form.data)
        return redirect(url_for("series_list"))
    return render_template("serie.html", form=form, series_id=series_id)




if __name__ == "__main__":
    app.run(debug=True)