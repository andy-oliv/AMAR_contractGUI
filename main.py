import customtkinter
import tkcalendar
from PIL import Image
from tkinter import filedialog
from src.entities.client import Client
from src.entities.package import package_1hr, package_2hr, package_3hr, package_video
from src.entities.event import Event
from src.models.contractModel import generate_contract
import os
import sys
import datetime
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme(resource_path("src\\assets\\themes\\amar_theme.json"))

window = customtkinter.CTk()
window.geometry('610x800')
window.title('Amar - Contratos Rápidos')
window.iconbitmap(resource_path('src\\assets\\favicon.ico'))

pop_up = None

def generate_calendar_window(pop_up_window, date_input):
    if pop_up_window is None:
        pop_up_window = customtkinter.CTkToplevel(window)
        pop_up_window.geometry('400x400')
        pop_up_window.attributes("-topmost", True)
        pop_up_window.title("Selecione a data")

        current_date = datetime.datetime.now()

        cal = tkcalendar.Calendar(pop_up_window, background="#936a56", headersbackground="#936a56", headersforeground="#FFFFFF", font="Poppins 14", locale='pt_BR',year=int(current_date.strftime("%Y")), month=int(current_date.strftime("%m")), day=int(current_date.strftime("%d")))
        cal.pack(fill="both", expand=True)

        select_button = customtkinter.CTkButton(pop_up_window, text="Selecionar", font=("Poppins", 14), command= lambda: get_date(pop_up_window, cal, date_input))
        select_button.pack(pady=10)

def get_date(calendar_window,calendar,date_var):
    date_var.delete(0, "end")
    date_var.insert(0, calendar.get_date())
    calendar_window.destroy()

def create_client(client_name, client_address, client_email, client_cpf):

    new_client = Client(client_name, client_address, client_email, client_cpf)
    return new_client

def create_event(event_name, event_location, event_date,
           event_start_time, event_commuting_fee, event_payment_type, due_date):

    if event_commuting_fee == "":
        event_commuting_fee = 0

    new_event = Event(event_name, event_location, event_date, event_start_time, event_commuting_fee, event_payment_type, due_date)
    return new_event

def create_contract(client_name, client_address, client_email, client_cpf, event_name, event_location, event_date,
           event_start_time, event_commuting_fee, event_payment_type, package, event_due_date, discount, additional_service):
    client = create_client(client_name, client_address, client_email, client_cpf)

    event = create_event(event_name, event_location, event_date,
           event_start_time, event_commuting_fee, event_payment_type, event_due_date)

    package_map = {
        "1hr": {
            "package_details": package_1hr,
        },
        "2hr": {
            "package_details": package_2hr,
        },
        "3hr": {
            "package_details": package_3hr,
        },
        "video": {
            "package_details": package_video,
        },
    }
    package = package_map.get(package, None)

    if discount == "":
        discount = 0

    window.filename = filedialog.askdirectory(initialdir="C:/Users", title="Selecione uma pasta para salvar o arquivo")
    folder = window.filename

    generate_contract(client,event,package["package_details"], discount, folder, additional_service)

logo = customtkinter.CTkImage(light_image=Image.open(resource_path('src\\assets\\logo_tagline.png')), dark_image=Image.open(resource_path('src\\assets\\logo_tagline.png')), size=(300,130))

image_label = customtkinter.CTkLabel(window, text="", image=logo)
image_label.grid(row=0, column=0, pady=(30,10), sticky="NS")

client_frame_title = customtkinter.CTkLabel(window, text="Dados do cliente", font=("Poppins", 14))
client_frame_title.grid(row=1, column=0, sticky="W", padx=30, pady=(20, 0))

client_frame = customtkinter.CTkFrame(window, border_width=0)
client_frame.grid(row=2, column=0, sticky="EW", padx=30, ipady=5)

client_label_name = customtkinter.CTkLabel(client_frame, text="Nome:", font=("Poppins", 16))
client_label_name.grid(row=3,column=0, sticky="W", padx=(25,0), pady=(15,10))

client_input_name = customtkinter.CTkEntry(client_frame, width=400, placeholder_text="digite o nome completo do cliente", placeholder_text_color="#a7887b")
client_input_name.grid(row=3, column=1, pady=(15,10))

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

event_input_date = customtkinter.CTkEntry(event_frame, placeholder_text='dd/mm/aaaa', placeholder_text_color="#a7887b", width=150)
event_input_date.grid(row=11, column=1, pady=10, sticky="W")

event_select_button = customtkinter.CTkButton(event_frame, text="Selecionar data", font=("Poppins", 14), command= lambda: generate_calendar_window(pop_up, event_input_date))
event_select_button.grid(row=11, column=1, pady=10, padx=(100, 0))

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

selected_payment_type = customtkinter.StringVar(value="PIX")

payment_radio1 = customtkinter.CTkRadioButton(event_frame, text="PIX", variable = selected_payment_type, value = 'PIX')
payment_radio1.grid(row=14, column=1, sticky="W")

payment_radio2 = customtkinter.CTkRadioButton(event_frame, text="Cartão", variable = selected_payment_type, value = 'cartão')
payment_radio2.grid(row=14, column=1)

discount_label = customtkinter.CTkLabel(event_frame, text="Desconto: ", font=("Poppins", 16))
discount_label.grid(row=15, column=0, sticky="W", padx=(25,0), pady=10)

discount_input = customtkinter.CTkEntry(event_frame, placeholder_text='apenas os digitos sem o caractere %', placeholder_text_color="#a7887b", width=280)
discount_input.grid(row=15, column=1, pady=10)

event_label_due_date = customtkinter.CTkLabel(event_frame, text="Data de vencimento:", font=("Poppins", 16))
event_label_due_date.grid(row=16, column=0, padx=(0,25), pady=10)

event_input_due_date = customtkinter.CTkEntry(event_frame, placeholder_text='dd/mm/aaaa', placeholder_text_color="#a7887b", width=150)
event_input_due_date.grid(row=16, column=1, pady=10, sticky="W")

event_select_button = customtkinter.CTkButton(event_frame, text="Selecionar data", font=("Poppins", 14), command= lambda: generate_calendar_window(pop_up, event_input_due_date))
event_select_button.grid(row=16, column=1, pady=10, padx=(100, 0))

package_label = customtkinter.CTkLabel(event_frame, text="Pacote:", font=("Poppins", 16))
package_label.grid(row=17, column=0, sticky="W", padx=(25,0), pady=10)

selected_package_type = customtkinter.StringVar(value="3hr")

package_radio1 = customtkinter.CTkRadioButton(event_frame, text="1hr", variable = selected_package_type, value = '1hr')
package_radio1.grid(row=17, column=1, sticky="W")

package_radio2 = customtkinter.CTkRadioButton(event_frame, text="2hrs", variable = selected_package_type, value = '2hr')
package_radio2.grid(row=18, column=1, sticky="W", pady=(0,12))

package_radio3 = customtkinter.CTkRadioButton(event_frame, text="3hrs", variable = selected_package_type, value = '3hr')
package_radio3.grid(row=19, column=1, sticky="W", pady=(0,12))

package_radio4 = customtkinter.CTkRadioButton(event_frame, text="3hrs + video", variable = selected_package_type, value = 'video')
package_radio4.grid(row=20, column=1, sticky="W", pady=(0,20))

additional_service_label = customtkinter.CTkLabel(event_frame, text="Com ensaio pré-festa?", font=("Poppins", 16))
additional_service_label.grid(row=21, column=0, sticky="W", padx=(25,0), pady=10)

selected_additional_service = customtkinter.BooleanVar()

additional_service_radio1 = customtkinter.CTkRadioButton(event_frame, text="Sim", variable = selected_additional_service, value = True)
additional_service_radio1.grid(row=21, column=1, sticky="W")

additional_service_radio2 = customtkinter.CTkRadioButton(event_frame, text="Não", variable = selected_additional_service, value = False)
additional_service_radio2.grid(row=21, column=1)

submit_button = customtkinter.CTkButton(window, text="Gerar contrato", font=("Poppins", 16), command=lambda: create_contract(client_input_name.get(),client_input_address.get(),client_input_email.get(),client_input_cpf.get(),event_input_name.get(),event_input_location.get(),event_input_date.get(),event_input_start_time.get(),event_input_commuting_fee.get().replace(",", "."),selected_payment_type.get(),selected_package_type.get(), event_input_due_date.get(), discount_input.get(), selected_additional_service.get()))
submit_button.grid(row=23, column=0, pady=30, padx=30, sticky="W")

window.mainloop()