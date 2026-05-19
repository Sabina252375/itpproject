# CtrlDeadline Bot

## Project Description
CtrlDeadline Bot is a Telegram bot designed to help users manage tasks and deadlines efficiently. Users can add tasks with a title, deadline date and time, and an optional photo. All data is stored in a PostgreSQL database, and the bot automatically sends reminders before deadlines.

---

## Features
- Add tasks with title, deadline, and optional photo
- View all tasks
- View today’s tasks
- View weekly calendar (next 7 days)
- Delete tasks
- Export tasks to CSV
- Automatic notifications before deadlines:
  - 3 days before
  - 2 days before
  - 1 day before
  - 10 hours before
  - 5 hours before
  - 1 hour before

---

## Technologies Used
- Python
- pyTelegramBotAPI (Telebot)
- PostgreSQL (psycopg2)
- CSV module
- threading
- datetime

---

## Installation Instructions
- Clone the repository  
- Create and activate a virtual environment  
- Install dependencies using pip  
- Create a config.py file and add database credentials and bot token  

---

## How to Run the Project
- Run the bot using `python bot.py`  
- Open Telegram  
- Start the bot by sending `/start`  

---

## Screenshots (if applicable)
**Bot start screen** 
<img width="1437" height="876" alt="2026-05-19_23-21-44" src="https://github.com/user-attachments/assets/4b9f0897-42d5-4cf4-9ea1-57555e970e16" />

**Add task feature** 
<img width="1356" height="876" alt="2026-05-19_23-22-12" src="https://github.com/user-attachments/assets/d24ae13a-4a0b-4088-847f-0ffc367ea89b" />

**Setting deadline**  
<img width="1339" height="529" alt="2026-05-19_23-22-46" src="https://github.com/user-attachments/assets/8d1b5f19-bbe9-47e7-9492-d0d7f2da6b75" />

**Notifications system** 
<img width="1088" height="194" alt="2026-05-19_23-23-26" src="https://github.com/user-attachments/assets/56553476-f2a9-4331-ad8e-495e4aa77958" />

**Today & Calendar view & CSV export**  
<img width="1392" height="595" alt="2026-05-19_23-24-02" src="https://github.com/user-attachments/assets/608d722c-d30d-4989-bf64-4cf653106737" />

**Delete feature & Tasks list**  
<img width="1486" height="529" alt="2026-05-19_23-24-20" src="https://github.com/user-attachments/assets/5342edba-08d3-44af-a8f2-cf01c96d00ad" />

---

## Team Member Roles
- Project idea and Telegram bot development (commands and core logic) — Sabina and Zhanna 
- Code development — Zhanna and Sabina  
- Testing the bot — Sabina  
- Bug fixing and debugging — Zhanna  
