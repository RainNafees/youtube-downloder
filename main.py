from flask import Flask, render_template, request, send_file, session, redirect,url_for
from pytube import YouTube




app = Flask(__name__)
app.config['SECRET_KEY'] = "NAFEES"


@app.route("/", methods=["Get", "POST"])
def home():
    if request.method == 'POST':
        session['link'] = request.form.get('url')
        try:
          url = YouTube(session['link'])
          url.check_availability()
        except:
           return render_template('error.html')
        return render_template('download.html',url=url)
    return render_template('home.html')


@app.route('/download', methods=['Get', 'POST'])
def downloade_video():
    if request.method == 'POST':
        url = YouTube(session['link'])
        itag = request.form.get('itag')
        video = url.streams.get_by_itag(itag)
        video.download()
        filename = video.download()
        return send_file(filename, as_attachment=True)
    return redirect(url_for('home'))






if __name__ == '__main__':
   app.run(debug=True)