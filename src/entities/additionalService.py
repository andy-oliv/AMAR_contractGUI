class AdditionalService:
    def __init__(self,name,pix_price,card_price):
        self.name = name
        self.pix_price = pix_price
        self.card_price = card_price

    def discounted_value(self, discount):
            discounted_coverage_price = (discount/100) * self.pix_price
            return discounted_coverage_price

pre_party_photoshoot = AdditionalService("Ensaio pré-festa", 400, 450)