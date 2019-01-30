class Pico_placa:

# This class indicates if a vehicle should go out on the streets on a certain day, and time
# Parameters: license: ejm - PBM0309
#	      date: ejm - lunes
#	      time: ejm - 13.45

    def __init__(self, license, date, time):

        self.license = license
        self.date = date
        self.time = time
                
    def show_data(self):
    # This method shows the information of a license
        
        print('Placa: ', self.license)
        print('Dia: ', self.date)
        print('Hora: ', self.time)
        
    def validate_input(self):
    # This method validates the input
        
        if (len(self.license) == 7) and (0.00 <= float(self.time) <= 24.59):
            #print('The licese number is: CORRECT')
            return 1
        else:
            #print('The licese number is: INCORRECT')
            return 0
        
    def last_digit(self):
    # This method returns the last digit of a license
        
        self.last_digit = self.license[-1:]
        #print('The last digit is: ' + str(self.last_digit))
        
    def request(self):
    # This method makes the request if the car should be or not outside

        Pico_placa.last_digit(self)
        
        if Pico_placa.validate_input(self) == 1:
            
            if self.date == 'lunes':
                if ((7 <= float(self.time) <= 9.30) or (16 <= float(self.time) <= 19.30)) and (self.last_digit == '1' or self.last_digit == '2'):
                    return('Can be on the road: NO')
                else:
                    return('Can be on the road: YES')

            if self.date == 'martes':
                if ((7 <= float(self.time) <= 9.30) or (16 <= float(self.time) <= 19.30)) and (self.last_digit == '3' or self.last_digit == '4'):
                    return('Can be on the road: NO')
                else:
                    return('Can be on the road: YES')

            if self.date == 'miercoles':
                if ((7 <= float(self.time) <= 9.30) or (16 <= float(self.time) <= 19.30)) and (self.last_digit == '5' or self.last_digit == '6'):
                    return('Can be on the road: NO')
                else:
                    return('Can be on the road: YES')

            if self.date == 'jueves':
                if ((7 <= float(self.time) <= 9.30) or (16 <= float(self.time) <= 19.30)) and (self.last_digit == '7' or self.last_digit == '8'):
                    return('Can be on the road: NO')
                else:
                    return('Can be on the road: YES')

            if self.date == 'viernes':
                if ((7 <= float(self.time) <= 9.30) or (16 <= float(self.time) <= 19.30)) and (self.last_digit == '9' or self.last_digit == '0'):
                    return('Can be on the road: NO')
                else:
                    return('Can be on the road: YES')

            if self.date == 'sabado' or self.date == 'domingo':
                return('Can be on the road: YES')
	    else:
        	return('Check the given license')

        else:
            
            return('Check the given license')
