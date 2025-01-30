from typing_extensions import ParamSpecKwargs


class Package:
    def __init__(self,name,pix_price,card_price, coverage_duration):
        self.name = name
        self.pix_price = pix_price
        self.card_price = card_price
        self.coverage_duration = coverage_duration

    def discounted_value(self, discount):
            discounted_coverage_price = (discount/100) * self.pix_price
            return discounted_coverage_price

package_nuvem = Package("Nuvem", 450, 548, "1 hora")
package_ceu = Package("Céu", 850, 986, "3 horas")
package_sol = Package("Sol", 1330, 1500, "3 horas")
package_lua = Package("Lua", 1686, 1950, "3 horas")
package_cometa = Package("Cometa", 2430, 2726, "3 horas")
