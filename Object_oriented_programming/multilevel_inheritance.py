class Dad:
    basketball = 1

class Son(Dad):
    dance = 1

    def is_dance(self):
        return f"Yes I dance {self.dance} no. of times a day"

class Grandson(Son):
    pass

ramanand = Dad()
manoj = Son()
akash = Grandson()


print(akash.dance)
print(Son.basketball)
print(akash.basketball)
a = akash.is_dance()
print(a)

