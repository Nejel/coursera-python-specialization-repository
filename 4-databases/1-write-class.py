class PartyBus:
    x = 0

    def party(self):
        self.x = self.x + 1 # == an.x = an.x + 1 из примера вызова ниже
        print("So far", self.x)

an = PartyBus()

an.party() # == PartyBus.party(an)
