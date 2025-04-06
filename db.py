import uuid

from src.config.db_config import session
from src.entities.db_models import Client, Event

new_client = Client(name="Andrew Pacheco de Oliveira", email="andrew.pacheco@outlook.com", address="Av. Francisco Brochado da Rocha, 207, Vila City, Cachoeirinha", cpf="02711957039")
new_event = Event(name="formatura do Andrew", address="Oba Oba Casa de Festas", date="12/12/2025", event_start_time="19:00", commuting_fee="0", payment_type="PIX", discount="0", payment_due_date="10/04/2025", package="3hrs", additional_service=True)

client_check = session.query(Client).filter(Client.email == new_client.email).first()
if client_check is None:
    print(f"CLIENTE CRIADO")
else:
    print("CLIENTE JÁ EXISTENTE")