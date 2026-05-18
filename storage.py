import csv

class CSVStorage:

    def export(self, tasks):
        try:
            with open("deadlines.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "user_id", "title", "deadline"])

                for t in tasks:
                    writer.writerow([t[0], t[1], t[2], t[3]])

            return True

        except Exception as e:
            print("CSV error:", e)
            return False