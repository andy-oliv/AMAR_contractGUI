class Event:
    def __init__(self,name,location,date,start_time,commuting_fee, payment_type, payment_due_date):
        self.name = name
        self.location = location
        self.date = date
        self.start_time = start_time
        self.commuting_fee = commuting_fee
        self.payment_type = payment_type
        self.payment_due_date = payment_due_date