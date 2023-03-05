import main
import nurse

m = main.Main(cleardbs=True)

m.register_patient(1,"Joe","Foster")

m.register_nurse(nurse.Nurse(1,None,None,None,"1",None))

