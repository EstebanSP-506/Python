class Patient(object):
    patientID = 0
    def __init__(self, name, allergies):
        Patient.patientID+=1
        self.id = Patient.patientID
        self.name = name
        self.allergies = allergies
        self.bed_number = None
    def printPatientCard(self):
        print "Patient ID: "+str(self.id)
        print "Patient Name: "+self.name
        print "Known Allergies: "+self.allergies
        print "Bed Number: "+str(self.bed_number)
        print "================================================"

pat1 = Patient("Esteban","life itself")
pat2 = Patient("Ana","google stuff")
pat3 = Patient("Stheve","not being a jerk")
pat4 = Patient("Pablo","gluten")
pat5 = Patient("Gerson","none")

pat1.printPatientCard()
pat2.printPatientCard()
pat3.printPatientCard()
pat4.printPatientCard()
pat5.printPatientCard()

class Hospital(object):
    
    def __init__(self,name,capacity):
        self.bed_number = 0
        self.patients_list = []
        self.name = name
        self.capacity = capacity
    def admit(self, *patients):
        for element in patients:
            self.bed_number+=1
            element.bed_number = self.bed_number
            self.patients_list.append(element)     
        return self      
    def discharge(self, *names):
        for element in names:
            for a in self.patients_list:
                if a.name == element:
                    self.patients_list.remove(a)
                    a.bed_number = None
        return self
    def patientsInfo(self):
        for element in self.patients_list:
            print "Hospital name: "+self.name
            print "Patient ID: "+str(element.id)
            print "Patient Name: "+element.name
            print "Known Allergies: "+element.allergies
            print "Bed Number: "+str(element.bed_number)            
            print "=================="
        print "There are "+str(self.capacity-len(self.patients_list))+" beds available"


hosp1 = Hospital("Hospital de los Patitos",5)

hosp1.admit(pat1,pat2,pat3,pat4,pat5).discharge("Stheve","Ana").patientsInfo()



