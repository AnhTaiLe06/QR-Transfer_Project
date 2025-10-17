import os, qrcode, uuid, shutil, threading, time

from flask import Flask, render_template, request, send_from_directory, redirect, url_for

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store room expiration timestamps
room_expirations = {}

def schedule_delete(path, delay=600):
    def delete_path():
        time.sleep(delay)
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
                print(f"Deleted file: {path}")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"Deleted folder: {path}")
    
    threading.Thread(target=delete_path, daemon=True).start()

def schedule_memory_cleanup(room_id, delay=600):
    def delete_memory():
        time.sleep(delay)
        if room_id in room_expirations:
            del room_expirations[room_id]
            print(f"Removed {room_id} from memory")
    
    threading.Thread(target=delete_memory, daemon=True).start()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_room")
def create_room():
    room_id = str(uuid.uuid4())
    folder = os.path.join("uploads", room_id)
    os.makedirs(folder, exist_ok=True)

    # Set expiration timestamp (600 minutes from now)
    expire_timestamp = int(time.time()) + 600
    room_expirations[room_id] = expire_timestamp

    schedule_delete(folder)

     # generate QR code
    local_ip = "192.168.1.227"
    qr_url = f"http://{local_ip}:5000/room/{room_id}"
    os.makedirs("static/qrcodes", exist_ok=True)
    qr_path = f"static/qrcodes/{room_id}.png"
    qrcode.make(qr_url).save(qr_path)

    schedule_delete(qr_path)

    schedule_memory_cleanup(room_id)

    return redirect(url_for("room", room_id=room_id))

@app.route("/room/<room_id>", methods=["GET", "POST"])
def room(room_id):
    folder = os.path.join(UPLOAD_FOLDER, room_id)
    os.makedirs(folder, exist_ok=True)

    if request.method == "POST":
        if "file" in request.files:
            file = request.files["file"]
            if file.filename != '':
                file_path = os.path.join(folder, file.filename)
                file.save(file_path)

    files = os.listdir(folder)

    expire_timestamp = room_expirations.get(room_id, int(time.time()) + 600)
    return render_template("room.html", room_id=room_id, files=files, expire_timestamp=expire_timestamp)


@app.route("/uploads/<room_id>/<filename>")
def download(room_id, filename):
    return send_from_directory(f"uploads/{room_id}", filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



