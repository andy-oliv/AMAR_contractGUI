import customtkinter
from PIL import Image
from src.entities.client import Client
from src.entities.package import package_nuvem, package_ceu, package_sol, package_lua, package_cometa
from src.entities.event import Event
from src.models.pacoteCeu import generate_ceu_contract
from src.models.pacoteNuvem import generate_nuvem_contract
from src.models.pacoteSol import generate_sol_contract
from src.models.pacoteLua import generate_lua_contract
from src.models.pacoteCometa import generate_cometa_contract

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("./src/assets/themes/amar_theme.json")

window = customtkinter.CTk()
window.geometry('600x800')
window.title('Amar - Contratos Rápidos')
window.iconbitmap('./src/assets/favicon.ico')

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

logo = customtkinter.CTkImage(light_image=Image.open('src/assets/logo_tagline.png'), dark_image=Image.open('src/assets/logo_tagline.png'), size=(300,150))

image_label = customtkinter.CTkLabel(window, text="", image=logo)
image_label.grid(row=0, column=0, pady=10, sticky="NS")

client_frame_title = customtkinter.CTkLabel(window, text="Dados do cliente", font=("Poppins", 14))
client_frame_title.grid(row=1, column=0, sticky="W", padx=30, pady=(20, 0))

client_frame = customtkinter.CTkFrame(window, border_width=0)
client_frame.grid(row=2, column=0, sticky="EW", padx=30)

client_label_name = customtkinter.CTkLabel(client_frame, text="Nome:", font=("Poppins", 16))
client_label_name.grid(row=3,column=0, sticky="W", padx=(25,0), pady=10)

client_input_name = customtkinter.CTkEntry(client_frame, width=400, placeholder_text="digite o nome completo do cliente", placeholder_text_color="#a7887b")
client_input_name.grid(row=3, column=1, pady=10)

client_label_address = customtkinter.CTkLabel(client_frame, text="Endereço:", font=("Poppins", 16))
client_label_address.grid(row=4,column=0, padx=(25,20), pady=10)

client_input_address = customtkinter.CTkEntry(client_frame, width=400, placeholder_text="digite o endereço com bairro e cidade", placeholder_text_color="#a7887b")
client_input_address.grid(row=4, column=1, pady=10)

client_label_email = customtkinter.CTkLabel(client_frame, text="Email:", font=("Poppins", 16))
client_label_email.grid(row=5,column=0, sticky="W", padx=(25,0), pady=10)

client_input_email = customtkinter.CTkEntry(client_frame, width=400, placeholder_text="email@mail.com", placeholder_text_color="#a7887b")
client_input_email.grid(row=5, column=1, pady=10)

client_label_cpf = customtkinter.CTkLabel(client_frame, text="CPF:", font=("Poppins", 16))
client_label_cpf.grid(row=6,column=0, sticky="W", padx=(25,0), pady=10)

client_input_cpf = customtkinter.CTkEntry(client_frame, width=400, placeholder_text="digite os 11 dígitos do cpf do cliente", placeholder_text_color="#a7887b")
client_input_cpf.grid(row=6, column=1, pady=10)

event_frame_title = customtkinter.CTkLabel(window, text="Dados do evento", font=("Poppins", 14))
event_frame_title.grid(row=7, column=0, sticky="W", padx=30, pady=(40, 0))

event_frame = customtkinter.CTkScrollableFrame(window, border_width=0, width=530)
event_frame.grid(row=8, column=0, padx=30)

event_label_name = customtkinter.CTkLabel(event_frame, text="Nome:", font=("Poppins", 16))
event_label_name.grid(row=9, column=0, sticky="W", padx=(25,0), pady=10)

event_input_name = customtkinter.CTkEntry(event_frame, placeholder_text="aniversário de 10 anos da Lila", width=280, placeholder_text_color="#a7887b")
event_input_name.grid(row=9, column=1, pady=10, sticky="EW")

event_label_location = customtkinter.CTkLabel(event_frame, text="Endereço:", font=("Poppins", 16))
event_label_location.grid(row=10, column=0, sticky="W", padx=(25,0),  pady=10)

event_input_location = customtkinter.CTkEntry(event_frame, placeholder_text="endereço do evento ou digite apenas casa", placeholder_text_color="#a7887b", width=280)
event_input_location.grid(row=10, column=1, pady=10)

event_label_date = customtkinter.CTkLabel(event_frame, text="Data:", font=("Poppins", 16))
event_label_date.grid(row=11, column=0, sticky="W", padx=(25,0),  pady=10)

event_input_date = customtkinter.CTkEntry(event_frame, placeholder_text='formato dd/mm/aaaa', placeholder_text_color="#a7887b", width=280)
event_input_date.grid(row=11, column=1, pady=10)

event_label_start_time = customtkinter.CTkLabel(event_frame, text="Início da cobertura:", font=("Poppins", 16))
event_label_start_time.grid(row=12, column=0, sticky="W", padx=(25,0), pady=10)

event_input_start_time = customtkinter.CTkEntry(event_frame, placeholder_text='formato hh:mm', placeholder_text_color="#a7887b", width=280)
event_input_start_time.grid(row=12, column=1, pady=10)

event_label_commuting_fee = customtkinter.CTkLabel(event_frame, text="Valor do deslocamento:", font=("Poppins", 16))
event_label_commuting_fee.grid(row=13, column=0, sticky="W", padx=25, pady=10)

event_input_commuting_fee = customtkinter.CTkEntry(event_frame, placeholder_text='sem caracteres especiais (R$ etc)', placeholder_text_color="#a7887b", width=280)
event_input_commuting_fee.grid(row=13, column=1, pady=10)

event_label_payment_type = customtkinter.CTkLabel(event_frame, text="Tipo de pagamento:", font=("Poppins", 16))
event_label_payment_type.grid(row=14, column=0, sticky="W", padx=(25,0), pady=10)

event_input_payment_type = customtkinter.CTkEntry(event_frame, placeholder_text='PIX ou Cartão', placeholder_text_color="#a7887b", width=280)
event_input_payment_type.grid(row=14, column=1, pady=10)

discount_label = customtkinter.CTkLabel(event_frame, text="Desconto: ", font=("Poppins", 16))
discount_label.grid(row=15, column=0, sticky="W", padx=(25,0), pady=10)

discount_input = customtkinter.CTkEntry(event_frame, placeholder_text='apenas os digitos sem o caractere %', placeholder_text_color="#a7887b", width=280)
discount_input.grid(row=15, column=1, pady=10)

event_label_due_date = customtkinter.CTkLabel(event_frame, text="Data de vencimento:", font=("Poppins", 16))
event_label_due_date.grid(row=16, column=0, padx=25, pady=10)

event_input_due_date = customtkinter.CTkEntry(event_frame, placeholder_text='formato dd/mm/aaaa', placeholder_text_color="#a7887b", width=280)
event_input_due_date.grid(row=16, column=1, pady=10)

package_label = customtkinter.CTkLabel(event_frame, text="Pacote:", font=("Poppins", 16))
package_label.grid(row=17, column=0, sticky="W", padx=(25,0), pady=10)

package_input = customtkinter.CTkEntry(event_frame, placeholder_text='Céu, Nuvem, Sol etc', placeholder_text_color="#a7887b", width=280)
package_input.grid(row=17, column=1, sticky="W", pady=10)

contract_label_date = customtkinter.CTkLabel(event_frame, text="Data do contrato:", font=("Poppins", 16))
contract_label_date.grid(row=18, column=0, sticky="W", padx=(25,0), pady=10)

contract_input_date = customtkinter.CTkEntry(event_frame, placeholder_text='ex: Janeiro de 2025', placeholder_text_color="#a7887b", width=280)
contract_input_date.grid(row=18, column=1, sticky="W", pady=10)

submit_button = customtkinter.CTkButton(window, text="Gerar contrato", font=("Poppins", 16), command=lambda: generate_contract(client_input_name.get(),client_input_address.get(),client_input_email.get(),client_input_cpf.get(),event_input_name.get(),event_input_location.get(),event_input_date.get(),event_input_start_time.get(),event_input_commuting_fee.get().replace(",", "."),event_input_payment_type.get(),package_input.get(),contract_input_date.get(), event_input_due_date.get(), discount_input.get()))
submit_button.grid(row=19, column=0, pady=30, padx=30, sticky="W")

window.mainloop()