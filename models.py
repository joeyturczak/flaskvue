from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    email = Column(String(80))

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    employee_id = Column(String(10), nullable=False)
    start_date = Column(DateTime(timezone=True), default=func.now())

class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True)
    attendance_type = Column(String(80), nullable=False)
    date_occurred = Column(DateTime(timezone=True), default=func.now())
    date_entered = Column(DateTime(timezone=True), default=func.now())
    user = relationship(User)
    user_id = Column(Integer, ForeignKey(user.id))
    employee = relationship(Employee)
    employee_id = Column(Integer, ForeignKey(employee.id))
