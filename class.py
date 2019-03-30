import random
import time

class PC():

    def __init__(self, pc_status='Close', pc_files=["Computer", "Files", "Recycle Bin"], pc_portNumbers=4, pc_volume=0,
                 pc_cooler='Open'):
        self.pc_status = pc_status
        self.pc_files = pc_files
        self.pc_portNumers = pc_portNumbers
        self.pc_volume = pc_volume
        self.pc_cooler = pc_cooler

    def pc_opener(self):

        if self.pc_status == 'Close':
            self.pc_status = 'Open'
            print("Pc is opening...")
        else:
            print("Pc is alredy open...")

    def pc_closer(self):

        if self.pc_status == 'Open':
            self.pc_status = 'Close'
            print("Pc is Closing...")
        else:
            print("Pc is alredy Close...")

    def add_File(self, NewFile):
        print("File is adding...")
        time.sleep(1)
        self.pc_files.append(NewFile)

    def del_File(self, DeleteFile):
        print("File is deleting...")
        time.sleep(1)
        self.pc_files.pop(DeleteFile)

    def pc_CoolerOpener(self):

        if self.pc_cooler == 'Close':
            self.pc_cooler = 'Open'
            print("Cooler is opening...")
        else:
            print("Pc Cooler is alredy open...")

    def pc_CoolerCloser(self):

        if self.pc_cooler == 'Open':
            self.pc_cooler = 'Close'
            print("Cooler is Closing...")
        else:
            print("Pc Cooler is alredy Close...")

    def Volume(self):

        while True:
            effect = input(
                "If you want Increase the volume.Press '+'\n If you want Reduce the volume. Press '-' \n Exit = 'exit'")

            if effect == '+':
                if self.pc_volume != 12:
                    self.pc_volume += 1
                    print("Volume: ", self.pc_volume)

            elif effect == '-':
                if self.pc_volume != 0:
                    self.pc_volume -= 1
                    print("Volume: ", self.pc_volume)

            elif effect == 'exit':
                print("Volume: ", self.pc_volume)
                print("You just exit the volume menu...")
                break
            else:
                print("Undefined sign")

    def __len__(self):
        return len(self.pc_files)

    def __str__(self):
        return "Status: {} \n Files: {} \n Port Num: {} \n Volume: {} \n Cooler: {}".format(self.pc_status,
                                                                                            self.pc_files,
                                                                                            self.pc_portNumers,
                                                                                            self.pc_volume,
                                                                                            self.pc_cooler)


computer = PC()

print("""
Terminal

1 - Open the Pc
2 - Close the Pc
3 - Add File
4 - Delete File
5 - Open Cooler
6 - Close Cooler
7 - Volume Editor
8 - See File Count
9 - Show All Status

Press
'q'
for exit...
""")

while True:
    reply = input("Your Choose: ")

    if reply == "q":
        print("GoodBye")
        break

    elif reply == "1":
        computer.pc_opener()
    elif reply == "2":
        computer.pc_closer()
    elif reply == "3":
        Add = input("File Name (split files with ','): ")
        Addlist = Add.split(",")

        for WillAdd in Addlist:
            computer.add_File(WillAdd)

    elif reply == "4":
        print("Files:")

        for i in range(0, computer.__len__()):
            print("{}- {} \n".format(i, computer.pc_files[i]))

        while True:

            selection = int(input("Which File You Want Delete(exit = -1): "))
            if selection == -1:
                break

            else:
                computer.del_File(selection)

    elif reply == '5':
        computer.pc_CoolerOpener()

    elif reply == '6':
        computer.pc_CoolerCloser()

    elif reply == '7':
        computer.Volume()

    elif reply == '8':
        print("File Count: ", computer.__len__())

    elif reply == '9':
        print("File Count: ", computer.__str__())


    else:
        print("Unedifend Reply, Please Choose Again...")


