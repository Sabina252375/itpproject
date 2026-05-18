import threading
import time
from datetime import datetime, timedelta

def start_checker(bot, db):

    def checker():
        while True:
            try:
                tasks = db.get_all()
                now = datetime.now()

                for t in tasks:
                    id = t[0]
                    user_id = t[1]
                    title = t[2]
                    deadline = t[3]
                    photo_id = t[10]

                    n3d = t[5]
                    n2d = t[6]
                    n1d = t[7]
                    n10h = t[8]
                    n5h = t[9]
                    n1h = t[10]

                    diff = deadline - now

                    if diff.total_seconds() < 0:
                        bot.send_message(user_id, f"❌ Expired: {title}")
                        db.delete_task(id)

            except Exception as e:
                print("Notification error:", e)

            time.sleep(60)

    threading.Thread(target=checker, daemon=True).start()