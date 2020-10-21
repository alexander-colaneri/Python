from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()

engine = create_engine('sqlite:///todo.db?check_same_thread=False')


# Creating the table metadata:
class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return str(self.task)  # This part was not allowing me to show the
        # dates, got a __str__ error. I had to force a string formatting here
        # to make it work.


Base.metadata.create_all(engine)

# Activating the Session Maker:
Session = sessionmaker(bind=engine)
session = Session()


class Todolist:
    def __init__(self):
        self.menu = "1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) " \
                    "Missed tasks\n5) Add task\n6) Delete task\n0) Exit "

    def main_menu(self):
        while True:
            print(self.menu)
            option = int(input())
            print()
            if option == 1:
                self.todays_tasks()
            elif option == 2:
                self.weeks_tasks()
            elif option == 3:
                self.all_tasks()
            elif option == 4:
                self.missed_tasks()
            elif option == 5:
                self.add_task()
            elif option == 6:
                self.delete_task()
            elif option == 0:
                print('\nBye!')
                break
            else:
                print('Invalid option')

    @staticmethod
    def todays_tasks():
        today = datetime.today().date()
        print(f"Today {today.strftime('%d %b')}:")
        # The query() method, for asking what you need.
        rows = session.query(Table).filter(Table.deadline == today).all()
        if not rows:
            print('Nothing to do!\n')
        else:
            counter = 1
            for r in rows:
                print(f'{counter}. {r}')
                counter += 1
            print()

    @staticmethod
    def weeks_tasks():
        today = datetime.today()
        for c in range(7):
            day_of_task = today + timedelta(days=c)
            daily_task = session.query(Table).filter(
                Table.deadline == day_of_task.date()).all()
            if not daily_task:
                print(day_of_task.strftime('%A %d %b'))
                print('Nothing to do!\n')
            else:
                counter = 1
                print(day_of_task.strftime('%A %d %b'))
                for task in daily_task:
                    print(f'{counter}. {task}')
                    counter += 1
                print()

    @staticmethod
    def all_tasks():
        rows = session.query(Table).order_by(Table.deadline).all()
        print('All tasks:')
        if not rows:
            print('Nothing to do!\n')
        else:
            today = datetime.today()
            rows = session.query(Table).order_by(Table.deadline).all()
            counter = 1
            for r in rows:
                if str(r.deadline) == str(today.date()):
                    print(f"{counter}. {r.task}. Deadline is today. "
                          f"{r.deadline.strftime('%#d %b')}")  # The %#d is the
                    # way to show "1" instead of "01".
                else:
                    print(
                        f"{counter}. {r.task}. {r.deadline.strftime('%#d %b')}")
                counter += 1
            print()

    @staticmethod
    def missed_tasks():
        today = datetime.today()
        rows = session.query(Table).filter(
            Table.deadline < today.date()).order_by(Table.deadline).all()
        counter = 1
        if not rows:
            print('Nothing is missed!')
        else:
            for r in rows:
                print(f"{counter}. {r.task}. {r.deadline.strftime('%#d %b')}")
                counter += 1
            print()

    @staticmethod
    def add_task():
        print('Enter task')
        task_input = str(input())
        print('Enter deadline')
        deadline_input = str(input())
        deadline = datetime.strptime(deadline_input, '%Y-%m-%d')  # I almost
        # forgot to turn the input from "string" to "date" format,
        # using strptime() method.
        new_task = Table(task=task_input, deadline=deadline.date())
        session.add(new_task)
        session.commit()
        print('The task has been added!\n')

    @staticmethod
    def delete_task():
        print('Choose the number of the task you want to delete:')
        rows = session.query(Table).order_by(Table.deadline).all()
        counter = 1
        for r in rows:
            print(f"{counter}. {r.task}. {r.deadline.strftime('%#d %b')}")
            counter += 1
        # Don't use Table.id to choose which row to delete, use indexes.
        delete_task_number = int(input()) - 1
        row_to_delete = rows[delete_task_number]
        session.delete(row_to_delete)
        session.commit()
        print('The task has been deleted!')


todolist = Todolist()
todolist.main_menu()
