class Car:
    is_sport_car =False
    brand = False
    model =False
    production_year = False
    horse_power =False
    color = False
    new_color = False
    hp=False
    def __init__(self,brand,model,production_year,horse_power,color,new_color,hp):
        self.brand =brand
        self.model = model
        self.production_year =production_year
        self.horse_power=horse_power
        self.color=color
        self.new_color =new_color
        self.hp=hp
    @property
    def get (self):
        return self.brand,self.model,self.production_year,self.horse_power,self.color,self.new_color,self.hp
    @property
    def change_color(self):
        if (self.new_color) == (self.color):
            return False
        else:
            self.color=self.new_color
            return True
            
    @property   
    def increase_horse_power(self):
        if self.hp>0:
             self.horse_power + self.hp
             return True
        else:
            return  False
car=Car('mersedes','cls',2015,180,'black','white',5) 
print('brend:',car.brand,'model:',car.model,'production_year:',car.production_year,'horse_power:',car.horse_power,'color:',car.color) 
print('change_color is',car.change_color,',new_color:',car.color)
print('hp is greater',car.increase_horse_power)



