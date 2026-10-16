class controller:  #Decided to implement controller as a class
    def __init__(self):  #Funtion that initialises the controller setting the fixed values 
        self.Kp = 0.15
        self.Kd = 0.6
        self.prev_error = 0 #This is the error term given (e(-1) = 0)

    def getcontrol(self, ref, output):
        error = ref - output #setting the new error term
        control = (self.Kp * error) + (self.Kd * (error - self.prev_error)) #Using the control function to calculate the action 
        self.prev_error = error #setting new previous error 
        return control

    def reseterror(self): #Used to reset the error term if ever needed
        self.prev_error = 0

 
