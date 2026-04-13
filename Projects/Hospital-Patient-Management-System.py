class Patient:

    def __init__(self,name,status):
        self.name = name
        self.status = status
        
    def status_formatting(self):
        if self.status == 0:
            return "Normal"
        elif self.status == 1:
            return "Urgent"
        elif self.status == 2:
            return "Super Urgent"
        
    def __str__(self):
        return f"{self.name} ({self.status_formatting()})"

class Specialization():

    def __init__(self,name,capacity=10):
        self.name = name
        self.capacity = capacity
        self.patient_queue = []

    def add_patient(self,patient):

        if len(self.patient_queue) >= self.capacity:
            print("Queue is full")
            return
        
        if patient.status == 2:
            self.patient_queue.insert(0,patient)
        elif patient.status == 1:
            pos = 0
            while pos < len(self.patient_queue) and self.patient_queue[pos].status == 2:
                pos += 1
            self.patient_queue.insert(pos, patient)
        else:
            self.patient_queue.append(patient)

        print(f"Patient {patient.name} added to {self.name}")

    def retriving_patient(self):
        if len(self.patient_queue) == 0:
            print("No patient")
        else:
            return self.patient_queue.pop(0)
        
    def remove_patient(self,name):
        for patient in self.patient_queue:
            if patient.name == name:
                self.patient_queue.remove(patient)
                print(f"{name} is removed")
                return
            
    def check_capacity(self):
        if len(self.patient_queue) >= self.capacity:
            print("Capacity is full")
        else:
            capacity_count = 0
            for patient in self.patient_queue:
                capacity_count += 1
            print("Capacity: ", self.capacity - capacity_count)

    def list_patients(self):
        print(f"\nPatients in {self.name}:")
        if not self.patient_queue:
            print("No patients")
        else:
            for patient in self.patient_queue:
                print(patient)


class OperationsManager:

    def __init__(self):
        
        self.Specialization = { 
            1: Specialization("Orthopedics"),
            2: Specialization("Neurology"),
            3: Specialization("Cardiology")
        }

        while True:
            choice = input('''
            Welcome to the Hospital Patient Queue System
            1. Adding patient
            2. List patient
            3. Retrive next patient
            4. Remove patient
            5.exit
            ''')

            if choice == '1':
                self.add_patient()
            elif choice == '2':
                self.list_patient()
            elif choice == '3':
                self.next_patient()
            elif choice == '4':
                self.remove_patient()
            elif choice == '5':
                print("Thank you!")
                break
            else:
                print("Invalid choice")

    def add_patient(self):
        spec = int(input("Enter specialization (1-Orthopedics, 2-Neurology, 3-Cardiology): "))
        name = input("Enter patient name: ")
        status = int(input("Enter status (0-Normal, 1-Urgent, 2-Super-Urgent): "))

        patient = Patient(name,status)
        self.Specialization[spec].add_patient(patient)

    def list_patient(self):

        spec = int(input("Enter Specialization: "))
        self.Specialization[spec].list_patients()

    def next_patient(self):
        spec = int(input("Enter Specialization: "))
        patient = self.Specialization[spec].retriving_patient()

        if patient:
            print("Next Patient: ",patient)

    def remove_patient(self):
        spec = int(input("Enter Specialization: "))
        name = input("Enter name: ")
        self.Specialization[spec].remove_patient(name)

manager = OperationsManager()
