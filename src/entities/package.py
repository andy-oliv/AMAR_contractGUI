class Package:
    def __init__(self,name,pix_price,card_price, coverage_duration):
        self.name = name
        self.pix_price = pix_price
        self.card_price = card_price
        self.coverage_duration = coverage_duration

    def discounted_value(self, discount):
            discounted_coverage_price = (discount/100) * self.pix_price
            return discounted_coverage_price

package_1hr = Package("1hr de cobertura fotográfica", 500, 548, "1 hora")
package_2hr = Package("2hrs de cobertura fotográfica", 700, 850, "2 horas")
package_3hr = Package("3hrs de cobertura fotográfica", 850, 950, "3 horas")
package_video = Package("3hrs de cobertura fotográfica + vídeo de até 6min do evento", 1350, 1480, "3 horas")