from flask import Flask, render_template, request, session, url_for, redirect, send_file
from pytube.cli import on_progress
from io import BytesIO
from pytube import YouTube
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = "654c0fb3968af9d5e6a9b3edcbc7051b"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        session['link'] = request.form.get('url')
        try:
            url = YouTube(session['link'])
            url.check_availability()
        except:
            return render_template("error.html")
        x = str(timedelta(seconds=url.length)).split(":")
        #when video is over 60 minutes long it will show the hours
        if int(x[0]) > 0:
            x[1] = f"{x[0]}:{x[1]}"
        size = url.streams.filter(only_audio=True).first(
        ).filesize == None and "Unknown" or f"{round(url.streams.filter(only_audio=True).first().filesize / 1000000, 2)} MB"
        if size == "Unknown":
            pass
        elif float(size.split(" ")[0]) > 1000:
            size = f"{round(float(size.split(' ')[0]) / 1000, 2)} GB"
        return render_template("download.html", url=url, time=f"{x[1]}:{x[2]}", size=size)
    return render_template("home.html")


@app.route("/download", methods=["GET", "POST"])
def download_audio():
    if request.method == "POST":
        buffer = BytesIO()
        url = YouTube(session['link'], on_progress_callback=on_progress)
        if request.form.get("mp3"):
            video = url.streams.filter(only_audio=True).first()
            video.stream_to_buffer(buffer)
            buffer.seek(0)
            download = "Download"
            resp = send_file(buffer, as_attachment=True, download_name=f"{download}.mp3", mimetype="audio/mp3")
            resp.headers["filename"] = f"{video}.mp3"
            return resp
    return redirect(url_for("home"))


app.run(host="0.0.0.0", port=5000, debug=True)

