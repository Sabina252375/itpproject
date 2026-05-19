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

                    photo_id = t[4]

                    n3d = t[5]
                    n2d = t[6]
                    n1d = t[7]
                    n10h = t[8]
                    n5h = t[9]
                    n1h = t[10]

                    diff = deadline - now

                    # 3 d
                    if diff <= timedelta(days=3) and diff > timedelta(days=3) - timedelta(minutes=1) and not n3d:
                        bot.send_message(user_id, f"⏰ 3 days left: {title}")
                        db.update_notify(id, "notified_3d")

                    # 2 d
                    elif diff <= timedelta(days=2) and diff > timedelta(days=2) - timedelta(minutes=1) and not n2d:
                        bot.send_message(user_id, f"⏰ 2 days left: {title}")
                        db.update_notify(id, "notified_2d")

                    # 1 d
                    elif diff <= timedelta(days=1) and diff > timedelta(days=1) - timedelta(minutes=1) and not n1d:
                        bot.send_message(user_id, f"⏰ 1 day left: {title}")
                        db.update_notify(id, "notified_1d")

                    # 10 h
                    elif diff <= timedelta(hours=10) and diff > timedelta(hours=10) - timedelta(minutes=1) and not n10h:
                        bot.send_message(user_id, f"⏰ 10 hours left: {title}")
                        db.update_notify(id, "notified_10h")


                    # 5 h
                    elif diff <= timedelta(hours=5) and diff > timedelta(hours=5) - timedelta(minutes=1) and not n5h:
                        bot.send_message(user_id, f"⏰ 5 hours left: {title}")
                        db.update_notify(id, "notified_5h")

                    # 1 h
                    elif diff <= timedelta(hours=1) and diff > timedelta(hours=1) - timedelta(minutes=1) and not n1h:
                        bot.send_message(user_id, f"⏰ 1 hour left: {title}")
                        db.update_notify(id, "notified_1h")

            except Exception as e:
                print("Notification error:", e)

            time.sleep(60)

    threading.Thread(target=checker, daemon=True).start()