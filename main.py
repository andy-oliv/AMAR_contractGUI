import tkinter as tk
from src.entities.client import Client
from src.entities.package import package_nuvem, package_ceu, package_sol, package_lua, package_cometa
from src.entities.event import Event
from src.models.pacoteCeu import generate_ceu_contract
from src.models.pacoteNuvem import generate_nuvem_contract
from src.models.pacoteSol import generate_sol_contract
from src.models.pacoteLua import generate_lua_contract
from src.models.pacoteCometa import generate_cometa_contract

window = tk.Tk()
window.geometry('800x600')
window.title('Amar - Contratos Rápidos')

def create_client(client_name, client_address, client_email, client_cpf):

    new_client = Client(client_name, client_address, client_email, client_cpf)
    return new_client

def create_event(event_name, event_location, event_date,
           event_start_time, event_commuting_fee, event_payment_type, due_date):

    if event_commuting_fee == "":
        event_commuting_fee = 0

    new_event = Event(event_name, event_location, event_date, event_start_time, event_commuting_fee, event_payment_type, due_date)
    return new_event

def generate_contract(client_name, client_address, client_email, client_cpf, event_name, event_location, event_date,
           event_start_time, event_commuting_fee, event_payment_type, package, contract_date, event_due_date, discount):

    client = create_client(client_name, client_address, client_email, client_cpf)

    event = create_event(event_name, event_location, event_date,
           event_start_time, event_commuting_fee, event_payment_type, event_due_date)

    contract_map = {
        "Nuvem": {
            "package_details": package_nuvem,
            "contract_model": generate_nuvem_contract
        },
        "Céu": {
            "package_details": package_ceu,
            "contract_model": generate_ceu_contract
        },
        "Sol": {
            "package_details": package_sol,
            "contract_model": generate_sol_contract
        },
        "Lua": {
            "package_details": package_lua,
            "contract_model": generate_lua_contract
        },
        "Cometa": {
            "package_details": package_cometa,
            "contract_model": generate_cometa_contract
        }
    }
    new_contract = contract_map.get(package, None)

    if discount == "":
        discount = 0

    new_contract["contract_model"](client,event,new_contract["package_details"],contract_date, discount)

client_frame_title = tk.Label(window, text="Dados do cliente")
client_frame_title.grid(row=1, column=0)

client_frame = tk.Frame(window, bd=2)
client_frame.grid(row=2, column=0)

client_label_name = tk.Label(client_frame, text="Nome:", font=("Poppins", 11))
client_label_name.grid(row=3,column=0)

client_input_name = tk.Entry(client_frame)
client_input_name.grid(row=3, column=1)

client_label_name = tk.Label(client_frame, text="Endereço:", font=("Poppins", 11))
client_label_name.grid(row=4,column=0)

client_input_address = tk.Entry(client_frame)
client_input_address.grid(row=4, column=1)

client_label_email = tk.Label(client_frame, text="Email:", font=("Poppins", 11))
client_label_email.grid(row=5,column=0)

client_input_email = tk.Entry(client_frame)
client_input_email.grid(row=5, column=1)

client_label_cpf = tk.Label(client_frame, text="CPF:", font=("Poppins", 11))
client_label_cpf.grid(row=6,column=0)

client_input_cpf = tk.Entry(client_frame)
client_input_cpf.grid(row=6, column=1)

event_frame_title = tk.Label(window, text="Dados do evento")
event_frame_title.grid(row=7, column=0)

event_frame = tk.Frame(window, bd=2)
event_frame.grid(row=8, column=0)

event_label_name = tk.Label(event_frame, text="Nome:", font=("Poppins", 11))
event_label_name.grid(row=9, column=0)

event_input_name = tk.Entry(event_frame)
event_input_name.grid(row=9, column=1)

event_label_location = tk.Label(event_frame, text="Endereço:", font=("Poppins", 11))
event_label_location.grid(row=10, column=0)

event_input_location = tk.Entry(event_frame)
event_input_location.grid(row=10, column=1)

event_label_date = tk.Label(event_frame, text="Data:", font=("Poppins", 11))
event_label_date.grid(row=11, column=0)

event_input_date = tk.Entry(event_frame)
event_input_date.grid(row=11, column=1)

event_label_start_time = tk.Label(event_frame, text="Início da cobertura:", font=("Poppins", 11))
event_label_start_time.grid(row=12, column=0)

event_input_start_time = tk.Entry(event_frame)
event_input_start_time.grid(row=12, column=1)

event_label_commuting_fee = tk.Label(event_frame, text="Valor do deslocamento:", font=("Poppins", 11))
event_label_commuting_fee.grid(row=13, column=0)

event_input_commuting_fee = tk.Entry(event_frame)
event_input_commuting_fee.grid(row=13, column=1)

event_label_payment_type = tk.Label(event_frame, text="Tipo de pagamento:", font=("Poppins", 11))
event_label_payment_type.grid(row=14, column=0)

event_input_payment_type = tk.Entry(event_frame)
event_input_payment_type.grid(row=14, column=1)

discount_label = tk.Label(event_frame, text="Desconto: ", font=("Poppins", 11))
discount_label.grid(row=15, column=0)

discount_input = tk.Entry(event_frame)
discount_input.grid(row=15, column=1)

event_label_due_date = tk.Label(event_frame, text="Vencimento do pagamento", font=("Poppins", 11))
event_label_due_date.grid(row=16, column=0)

event_input_due_date = tk.Entry(event_frame)
event_input_due_date.grid(row=16, column=1)

package_label = tk.Label(window, text="Pacote:", font=("Poppins", 11))
package_label.grid(row=17, column=0)

package_input = tk.Entry(window)
package_input.grid(row=17, column=1)

contract_label_date = tk.Label(window, text="Data do contrato:", font=("Poppins", 11))
contract_label_date.grid(row=18, column=0)

contract_input_date = tk.Entry(window)
contract_input_date.grid(row=18, column=1)

submit_button = tk.Button(window, text="Gerar contrato", font=("Poppins", 11), command=lambda: generate_contract(client_input_name.get(),client_input_address.get(),client_input_email.get(),client_input_cpf.get(),event_input_name.get(),event_input_location.get(),event_input_date.get(),event_input_start_time.get(),event_input_commuting_fee.get().replace(",", "."),event_input_payment_type.get(),package_input.get(),contract_input_date.get(), event_input_due_date.get(), discount_input.get()))
submit_button.grid(row=19, column=0)

window.mainloop()