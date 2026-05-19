from datetime import datetime

def get_color(deadline):
    diff = deadline - datetime.now()

    if diff.days >= 3:
        return "🟢"
    elif diff.days >= 1:
        return "🟡"
    return "🔴"