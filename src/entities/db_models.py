import uuid

from sqlalchemy import Column, String, Boolean, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

client_event = Table('client_event', Base.metadata,
    Column('client_id', ForeignKey('clients.id'), primary_key=True),
          Column('event_id', ForeignKey('events.id'), primary_key=True)
)

class Client(Base):
    __tablename__ = 'clients'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50), nullable=False)
    email = Column(String(120), nullable=False)
    address = Column(String(255), nullable=False)
    cpf = Column(String(11), nullable=False)

    events = relationship('Event', secondary=client_event, back_populates='clients')

class Event(Base):
    __tablename__ = 'events'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    date = Column(String(10), nullable=False)
    event_start_time = Column(String(5), nullable=False)
    commuting_fee = Column(String(6), nullable=False)
    payment_type = Column(String(6), nullable=False)
    discount = Column(String(3), nullable=False)
    payment_due_date = Column(String(10), nullable=False)
    package = Column(String(50), nullable=False)
    additional_service = Column(Boolean, nullable=False)

    clients = relationship('Client', secondary=client_event, back_populates='events')