class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
    
    def __repr__(self):
        return f"< FixedFloat {self.amount:.2f}>"

    @staticmethod  
    def from_sum(value1, value2):
        return  FixedFloat(value1 + value2)    

new_number = FixedFloat.from_sum(19.58, 18.56)
print(new_number)

class dollar(FixedFloat):
    def __init__(self,amount):
     super().__init__(amount)
     self.symbol = '$'
    
    def __repr__(self):
        return f'<Dollar {self.symbol} {self.amount:.2f}>'

    

        
