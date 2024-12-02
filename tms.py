# Import necessary libraries
from tkinter import *
from tkinter import ttk
from tkinter import Tk, Label
from PIL import Image, ImageTk  # For image handling
import random   # For generating random numbers
import time     # For time-related functions
import os       # For file path operations
from tkinter import Tk, Button, Toplevel, Text, END, BOTH
from tkinter import Tk, PhotoImage
import tkinter.messagebox  # For message boxes
from reportlab.lib.pagesizes import letter  # For PDF page size
from reportlab.pdfgen import canvas  # For PDF generation

class Travel:
    
    def __init__(self, root):
        self.root = root
        
        # Load and set the application icon
        image_icon = PhotoImage(file="Major Project - TAMS Python/Logo.png")
        root.iconphoto(False, image_icon)
                
        # Set window title and size
        self.root.title("Travel Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="#F2F2F2")  # Set subtle gray background color
        
        # Initialize variables for date, receipt reference, and financial details
        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))  # Set current date
        Receipt_Ref = StringVar() 
        PaidTax = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()
        
        # Initialize IntVar and StringVar for various options and user inputs
        var1 = IntVar()  # Ral Tax
        var2 = IntVar()  # Placeholder for future use
        var3 = IntVar()  # Travelling Insurance
        var4 = IntVar()  # Extra Luggage
        var5 = IntVar()  # Standard Ticket
        var6 = IntVar()  # Single Ticket
        var7 = IntVar()  # Economy Ticket
        var8 = IntVar()  # Return Ticket
        var9 = IntVar()  # First Class Ticket
        var10 = IntVar()  # Special Needs
        var11 = StringVar()  # Placeholder for future use
        var12 = StringVar()  # Placeholder for future use
        var13 = StringVar()  # Accommodation type
        person = IntVar()  # Number of persons
        
        # Customer details variables
        Firstname = StringVar()
        Lastname = StringVar()
        Address = StringVar()
        PostCode = StringVar()
        Mobile1 = StringVar()
        Mobile2 = StringVar()
        Email = StringVar()
        
        # Additional financial variables
        RalTax = StringVar()
        Mile = StringVar()
        Travel_Ins = StringVar()
        Luggage = StringVar()
        
        # Ticket class variables
        Standard = StringVar()
        Economy = StringVar()
        FirstClass = StringVar()
        
        # Initialize financial variables to zero
        RalTax.set("0")
        Mile.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")
        
        Standard.set("0")
        Economy.set("0")
        FirstClass.set("0")
        
        #====================================Functions==============================================
        
        def Exit():
            """Function to exit the application."""
            Exit = tkinter.messagebox.askyesno("Exit", "Confirm if you want to exit")
            if Exit > 0:
                root.destroy()  # Close the application
            
        def Reset(): 
            """Function to reset all fields and variables to their initial state."""
            RalTax.set("0")
            Mile.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")
            
            Standard.set("0")
            Economy.set("0")
            FirstClass.set("0")
            
            # Clear customer details
            Firstname.set("")
            Lastname.set("")
            Address.set("")
            PostCode.set("")
            Mobile1.set("")
            Mobile2.set("")
            Email.set("")
            
            # Clear financial details
            PaidTax.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt.delete("1.0", END)  # Clear receipt text area
                
            # Reset all IntVar and StringVar
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set("0")
            var12.set("0")
            var13.set("0")
            person.set("0")
                    
            self.selected_package.set("")
            self.comboPlace ['values'] = []  # Clear the place options
            self.selected_place.set("")
            self.cboAccommodation.set("")
            self.selected_place.set("")
                    
            # Disable text fields for financial inputs
            self.txtperson.configure(state=DISABLED)
            self.txtRalTax.configure(state=DISABLED)
            self.txtTravelling_Insurance.configure(state=DISABLED)
            self.txtExt_Luggage.configure(state=DISABLED)
            self.txtStandard.configure(state=DISABLED)
            self.txtEconomy.configure(state=DISABLED)
            self.txtFirstClass.configure(state=DISABLED)
            self.txtPlacePrice.configure(state=DISABLED)
            self.txtPlacePrice.delete(0, END)

        def Receipt():
            """Function to generate and display the receipt."""
            self.txtReceipt.delete("1.0", END)  # Clear previous receipt
            x = random.randint(10853, 500831)  # Generate random receipt reference
            randomRef = str(x)
            Receipt_Ref.set("Travel Bill : " + randomRef)
            
            # Insert receipt details into the text area
            self.txtReceipt.insert(END, "Receipt Ref : \t\t\t\t\t" + Receipt_Ref.get() + "\n")
            self.txtReceipt.insert(END, "Date : \t\t\t\t\t" + DateofOrder.get() + "\n")
            self.txtReceipt.insert(END, "------------------------------------------Travelling Details------------------------------------------\n")
            self.txtReceipt.insert(END, 'First Name :\t\t' + Firstname.get() + '\t\t')
            self.txtReceipt.insert(END, 'Last Name :\t\t' + Lastname.get() + '\n')
            self.txtReceipt.insert(END, 'Address :\t\t\t\t\t' + Address.get() + '\n')
            self.txtReceipt.insert(END, 'Postcode :\t\t\t\t\t' + PostCode.get() + '\n')
            self.txtReceipt.insert(END, 'Mobile 1 :\t\t\t\t\t' + Mobile1.get() + '\n')
            self.txtReceipt.insert(END, 'Mobile 2 :\t\t\t\t\t' + Mobile2.get() + '\n')
            self.txtReceipt.insert(END, 'Email :\t\t\t\t\t' + Email.get() + '\n')
            self.txtReceipt.insert(END, 'Package :\t\t\t\t\t' + self.selected_package.get() + '\n')
            self.txtReceipt.insert(END, 'Place :\t\t\t\t\t' + self.selected_place.get() + '\n')
            self.txtReceipt.insert(END, 'Person :\t\t\t\t\t' + str(person.get()) + '\n')
            self.txtReceipt.insert(END, 'Accommodation :\t\t\t\t\t' + var13.get() + '\n')
            self.txtReceipt.insert(END, 'Standard :\t\t\t\t\t' + Standard.get() + '\n')
            self.txtReceipt.insert(END, 'Economy :\t\t\t\t\t' + Economy.get() + '\n')
            self.txtReceipt.insert(END, 'First Class :\t\t\t\t\t' + FirstClass.get() + '\n')
            self.txtReceipt.insert(END, 'Paid Tax :\t\t\t\t\t' + PaidTax.get() + '\n')
            self.txtReceipt.insert(END, 'Sub Total :\t\t\t\t\t' + str(SubTotal.get()) + '\n')
            self.txtReceipt.insert(END, 'Total :\t\t\t\t\t' + str(TotalCost.get()) + '\n')
            
        def Print():
            """Prompt for filename and save the PDF receipt."""
            def save_pdf():
                """Save the receipt as a PDF file."""
                filename = entry_filename.get()
                if filename:
                    pdf_file = os.path.join("Print Receipt", f"{filename}.pdf")  # Define PDF file path
                    c = canvas.Canvas(pdf_file, pagesize=letter)  # Create a PDF canvas
                    width, height = letter  # Get letter page size
                    # Add receipt details to the PDF
                    c.drawString(100, height - 50, "Receipt Ref:      " + Receipt_Ref.get())
                    c.drawString(100, height - 70, "Date:      " + DateofOrder.get())
                    c.drawString(100, height - 90, "------------------------------------------Travelling Details------------------------------------------")
                    c.drawString(100, height - 130, "First Name:      " + Firstname.get())
                    c.drawString(100, height - 150, "Last Name:      " + Lastname.get())
                    c.drawString(100, height - 170, "Address:      " + Address.get())
                    c.drawString(100, height - 190, "Postcode:      " + PostCode.get())
                    c.drawString(100, height - 210, "Mobile 1:      " + Mobile1.get())
                    c.drawString(100, height - 230, "Mobile 2:      " + Mobile2.get())
                    c.drawString(100, height - 250, "Email:      " + Email.get())
                    c.drawString(100, height - 270, "Package:      " + self.selected_package.get())
                    c.drawString(100, height - 290, "Place:      " + self.selected_place.get())
                    c.drawString(100, height - 310, "Person:      " + str(person.get()))
                    c.drawString(100, height - 330, "Accommodation:      " + var13.get())
                    c.drawString(100, height - 350, "Standard:      " + Standard.get())
                    c.drawString(100, height - 370, "Economy:      " + Economy.get())
                    c.drawString(100, height - 390, "First Class:      " + FirstClass.get())
                    c.drawString(100, height - 410, "Paid Tax:      " + PaidTax.get())
                    c.drawString(100, height - 430, "Sub Total:      " + str(SubTotal.get()))
                    c.drawString(100, height - 450, "Total:      " + str(TotalCost.get()))
                    c.save()  # Save the PDF file

                    tkinter.messagebox.showinfo("Print", "Receipt has been printed successfully!")  # Show success message
                    entry_filename.delete(0, END)  # Clear the entry after saving
                    button_save.grid_forget()  # Hide the save button after saving
                    label.grid_forget()  # Hide the label after saving
                    entry_filename.grid_forget()  # Hide the entry after saving
                    
            # Create input fields in ButtonFrame for filename
            label = Label(ButtonFrame, bd=7, font=('arial', 11, 'bold'), text="File_Name:", bg="#F2F2F2", fg="#333")
            label.grid(row=1, column=0)
            entry_filename = Entry(ButtonFrame, font=('arial', 12, 'bold'),
                                   bd=7, insertwidth=2, justify=CENTER)
            entry_filename.grid(row=1, column=1, columnspan=3)
            button_save = Button(ButtonFrame, padx=18, bd=7, font=('arial', 15, 'bold'),
                               width=3, text="Save", command=save_pdf, bg="#A9D0F5", fg="#333")
            button_save.grid(row=1, column=4)
            
        def Ral_Tax():
            """Function to handle Ral Tax checkbox."""
            global paid1
            
            if (var1.get() == 1):
                self.txtRalTax.configure(state=NORMAL)  # Enable Ral Tax entry
                Item1 = float(50)  # Set Ral Tax amount
                RalTax.set("₹ " + str(Item1))  # Update Ral Tax display
            elif var1.get() == 0:
                self.txtRalTax.configure(state=DISABLED)  # Disable Ral Tax entry
                RalTax.set("0")  # Reset Ral Tax display
                
        def Travelling():
            """Function to handle Travelling Insurance checkbox."""
            global Item3
            
            if var3.get() == 1:
                self.txtTravelling_Insurance.configure(state=NORMAL)  # Enable Travelling Insurance entry
                Item3 = float(15500)  # Set Travelling Insurance amount
                Travel_Ins.set("₹ " + str(Item3))  # Update Travelling Insurance display
            elif var3.get() == 0:
                self.txtTravelling_Insurance.configure(state=DISABLED)  # Disable Travelling Insurance entry
                Travel_Ins.set("0")  # Reset Travelling Insurance display
                
        def Lug():
            """Function to handle Extra Luggage checkbox."""
            global Item4
            
            if var4.get() == 1:
                self.txtExt_Luggage.configure(state=NORMAL)  # Enable Extra Luggage entry
                Item4 = float(500)  # Set Extra Luggage amount
                Luggage.set("₹ " + str(Item4))  # Update Extra Luggage display
            elif var4.get() == 0:
                self.txtExt_Luggage.configure(state=DISABLED)  # Disable Extra Luggage entry
                Luggage.set # ... (rest of the code remains the same)

        def Total_Paid():
            """Function to calculate the total paid amount."""
            selected_place = self.selected_place.get()
            
            try:
                num_persons = int(person.get())
                if num_persons <= 0:
                    raise ValueError("Number of persons must be greater than zero")
            except ValueError:
                PaidTax.set("Invalid Number of Persons")
                SubTotal.set("Invalid Number of Persons")
                TotalCost.set("Invalid Number of Persons")
                return

            total_cost = 0.0
            
            place_prices = {
                "Dwarka": 4400,
                "Rajasthan": 6000,
                "Mathura": 7500,
                "Agra": 10800,
                "Jaipur": 9000,
                "Delhi": 10000,
                "Mumbai": 6500,
                "Shimla": 45000,
                "Pune": 5000,
                "Darjeeling": 31000,
                "Chennai": 10000,
                "Kerala": 15000,
                "Ooty": 50000,
                "Sikkim": 20000,
                "Kashmir": 25000,
                "Ladakh": 35000,
                "Manali": 40000,
                "Goa": 12000,
                "Munnar": 51000
            }

            place_price = place_prices.get(selected_place, 0)
            total_cost += place_price * num_persons

            if var1.get() == 1:
                total_cost += 45

            if var3.get() == 1:
                total_cost += 63

            if var4.get() == 1:
                total_cost += 334.59

            if var5.get() == 1:
                total_cost += 274.9

            if var7.get() == 1:
                total_cost += 365.5

            if var9.get() == 1:
                total_cost += 564.3

            Tax = "₹ " + str('%.2f' % (total_cost * 0.05))
            ST = "₹ " + str('%.2f' % total_cost)
            TT = "₹ " + str('%.2f' % (total_cost + (total_cost * 0.05)))

            PaidTax.set(Tax)
            SubTotal.set(ST)
            TotalCost.set(TT)

        def update_place_price(event=None):
            """Function to update the place price based on the selected place."""
            selected_place = self.selected_place.get()
            place_prices = {
                "Dwarka": 4400,
                "Rajasthan": 6000,
                "Mathura": 7500,
                "Agra": 10800,
                "Jaipur": 9000,
                "Delhi": 10000,
                "Mumbai": 6500,
                "Shimla": 45000,
                "Pune": 5000,
                "Darjeeling": 31000,
                "Chennai": 10000,
                "Kerala": 15000,
                "Ooty": 50000,
                "Sikkim": 20000,
                "Kashmir": 25000,
                "Ladakh": 35000,
                "Manali": 40000,
                "Goa": 12000,
                "Munnar": 51000
            }
            price = place_prices.get(selected_place, 0)
            self.txtPlacePrice.configure(state=NORMAL)
            self.txtPlacePrice.delete(0, END)
            self.txtPlacePrice.insert(0, "₹ " + str(price))
            self.txtPlacePrice.configure(state=DISABLED)

        #=============================================================================================
        MainFrame = Frame(self.root)
        MainFrame.grid(sticky=NSEW)  # Make the main frame fill the available space
        
        Tops = Frame(MainFrame, bd=20, width=1350, relief=RIDGE, bg="#000")  # Change to a blue shade
        Tops.pack(side=TOP, fill=X)  # Fill the width of the window
        
        # Load the logo image
        image = Image.open("Major Project - TAMS Python/Logo.png")  # Use the actual path to your image
        resized_image = image.resize((300, 200))  # Replace 'width' and 'height' with desired dimensions
        self.logo = ImageTk.PhotoImage(resized_image)        
        
        # Add the logo to a label (column 0)
        lblLogo = Label(Tops, image=self.logo, bg="#000")
        lblLogo.grid(row=0, column=0, padx=10, pady=10)

        # Add the title to a label (column 1)
        lblTitle = Label(Tops, font=('arial', 70, 'bold'), text="    MK Travels System   ", bg="#000", fg="white")
        lblTitle.grid(row=0, column=1, padx=10, pady=10)
        #=============================================================================================
        CustomerDetailsFrame = Frame(MainFrame, width=1350, height=500, bd=20, pady=5, relief=RIDGE, bg="#F2F2F2")
        CustomerDetailsFrame.pack(side=BOTTOM, fill=BOTH, expand=True)  # Fill the available space
        
        FrameDetails = Frame(CustomerDetailsFrame, width=880, height=400, bd=10, relief=RIDGE, bg="#F2F2F2")
        FrameDetails.pack(side=LEFT, fill=BOTH, expand=True)  # Fill the available space
        
        CustomerName = LabelFrame(FrameDetails, width=150, height=250, bd=10, 
                                  font=('arial', 12, 'bold'), text="Customer Details", relief=RIDGE, bg="#E6E6E6", fg="#333")
        CustomerName.grid(row=0, column=0, sticky=NSEW)
        
        TravelFrame = LabelFrame(FrameDetails, width=300, height=250, bd=10, 
                                  font=('arial', 12 , 'bold'), text="Travel Details", relief=RIDGE, bg="#E6E6E6", fg="#333")
        TravelFrame.grid(row=0, column=1, sticky=NSEW)
        
        Ticket_Frame = LabelFrame(FrameDetails, width=300, height=150, relief=FLAT, bg="#E6E6E6", fg="#333")
        Ticket_Frame.grid(row=1, column=0, sticky=NSEW)
        
        CostFrame = LabelFrame(FrameDetails, width=150, height=150, relief=FLAT, bg="#E6E6E6", fg="#333")
        CostFrame.grid(row=1, column=1, sticky=NSEW)
        #=============================================================================================
        Receipt_ButtonFrame = Frame(CustomerDetailsFrame, bd=10, width=450, height=400, relief=RIDGE, bg="#F2F2F2")
        Receipt_ButtonFrame.pack(side=RIGHT, fill=BOTH, expand=True)  # Fill the available space
        
        ReceiptFrame = LabelFrame(Receipt_ButtonFrame, width=350, height=300, bg="#E6E6E6", fg="#333",
                                  font=('arial', 12, 'bold'), text="Receipt", relief=RIDGE)
        ReceiptFrame.grid(row=0, column=0, sticky=NSEW)
        
        ButtonFrame = LabelFrame(Receipt_ButtonFrame, width=350, height=100, bd=5, relief=RIDGE, bg="#E6E6E6", fg="#333")
        ButtonFrame.grid(row=1, column=0, sticky=NSEW)
        #=====================================CustomerDetails=========================================
        self.lblFirstname = Label(CustomerName, font=('arial', 14, 'bold'), text="First Name", bd=7, bg="#E6E6E6", fg="#333")
        self.lblFirstname.grid(row=0, column=0, sticky=W)
        
        self.txtFirstname = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Firstname,
                                   bd=7, insertwidth=2, justify=CENTER)
        self.txtFirstname.grid(row=0, column=1)
        #---------------------------------------------------------------------------------------------
        self.lblSurname = Label(CustomerName, font=('arial', 14, 'bold'), text="Surname", bd=7, bg="#E6E6E6", fg="#333")
        self.lblSurname.grid(row=1, column=0, sticky=W)
        
        self.txtSurname = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Lastname,
                                   bd=7, insertwidth=2, justify=CENTER)
        self.txtSurname.grid(row=1, column=1)
        #---------------------------------------------------------------------------------------------
        self.lblAddress = Label(CustomerName, font=('arial', 14, 'bold'), text="Address", bd=7, bg="#E6E6E6", fg="#333")
        self.lblAddress.grid(row=2, column=0, sticky=W)
        
        self.txtAddress = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Address,
                                   bd=7, insertwidth=2, justify=CENTER)
        self.txtAddress.grid(row=2, column=1)
        #---------------------------------------------------------------------------------------------
        self.lblPostCode = Label(CustomerName, font=('arial', 14, 'bold'), text="Post Code", bd=7, bg="#E6E6E6", fg="#333")
        self.lblPostCode.grid(row=3, column=0, sticky=W)
        
        self.txtPostCode = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=PostCode,
                                   bd=7, insertwidth=2, justify=CENTER)
        self.txtPostCode.grid(row=3, column=1)
        #---------------------------------------------------------------------------------------------
        self.lblMobile1 = Label(CustomerName, font=('arial', 14, 'bold'), text="Mobile 1", bd=7, bg="#E6E6E6", fg="#333")
        self.lblMobile1.grid(row=4, column=0, sticky=W)
        
        self.txtMobile1 = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Mobile1,
                                   bd=7, insertwidth=2, justify=CENTER)
        self.txtMobile1.grid(row=4, column=1)
        #---------------------------------------------------------------------------------------------
        self.lblMobile2 = Label(CustomerName, font=('arial', 14, 'bold'), text="Mobile 2", bd=7, bg="#E6E6E6", fg="#333")
        self.lblMobile2.grid(row=5, column=0, sticky=W)
        
        self.txtMobile2 = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Mobile2,
                                   bd=7, insertwidth=2, justify=CENTER)
        self.txtMobile2.grid(row=5, column=1)
        #--------------------------------------------------------------------------------------------
        self.lblEmail = Label(CustomerName, font=('arial', 14, 'bold'), text="Email", bd=7, bg="#E6E6E6", fg="#333")
        self.lblEmail.grid(row=6, column=0, sticky=W)
        
        self.txtEmail = Entry(CustomerName, font=('arial', 14, 'bold'), textvariable=Email,
                                   bd=7, insertwidth=2, justify=CENTER)
        self.txtEmail.grid(row=6, column=1)
        #=============================================================================================
        # Variables
        self.selected_package = StringVar()
        self.selected_place = StringVar()
        self.places = {
            "Golden": ["Dwarka", "Rajasthan", "Mathura", "Agra", "Jaipur", "Delhi", "Mumbai"],
            "Silver": ["Shimla", "Pune", "Darjeeling", "Chennai", "Kerala", "Ooty", "Sikkim"],
            "Platinum": ["Kashmir", "Ladakh", "Manali", "Goa", "Munnar"]
        }

        # Package Options
        self.lblPackage = Label(TravelFrame, font=('arial', 14, 'bold'), text="Choose Package", bd=7, bg="#E6E6E6", fg="#333")
        self.lblPackage.grid(row=0, column=0, sticky=W)
        self.comboPackage = ttk.Combobox(TravelFrame, font=('arial', 14, 'bold'), width=20, 
                                         state='readonly', textvariable=self.selected_package)
        self.comboPackage['values'] = ("Golden", "Silver", "Platinum")
        self .comboPackage.grid(row=0, column=1)
        self.comboPackage.bind("<<ComboboxSelected>>", self.update_places)  # Bind the selection event to update places

        # Place Options
        self.lblPlace = Label(TravelFrame, font=('arial', 14, 'bold'), text="Choose Place", bd=7, bg="#E6E6E6", fg="#333")
        self.lblPlace.grid(row=1, column=0, sticky=W)
        self.comboPlace = ttk.Combobox(TravelFrame, font=('arial', 14, 'bold'), width=20, 
                                       state='readonly', textvariable=self.selected_place)
        self.comboPlace.grid(row=1, column=1)
        self.comboPlace.bind("<<ComboboxSelected>>", update_place_price)  # Bind the selection event to update place price

        # Accommodation
        self.lblAccommodation = Label(TravelFrame, font=('arial', 14, 'bold'), text="Accommodation", bd=7, bg="#E6E6E6", fg="#333")
        self.lblAccommodation.grid(row=2, column=0, sticky=W)
        
        self.cboAccommodation = ttk.Combobox(TravelFrame, textvariable=var13, state="readonly",
                                             font=('arial', 20, 'bold'), width=14)
        self.cboAccommodation['values'] = (' ', 'Hotel', 'Guest House', 'Resort')
        self.cboAccommodation.current(0)  # Set default selection
        self.cboAccommodation.grid(row=2, column=1)
        
        # Select Persons
        self.lblPerson = Label(TravelFrame, font=('arial', 14, 'bold'), text="How Many Persons", bd=7, bg="#E6E6E6", fg="#333")
        self.lblPerson.grid(row=3, column=0, sticky=W)
        
        self.txtperson = Entry(TravelFrame, font=('arial', 14, 'bold'), textvariable=person,
                               bd=7, insertwidth=2, justify=RIGHT)
        self.txtperson.grid(row=3, column=1)

        # Place Price Display
        self.lblPlacePrice = Label(TravelFrame, font=('arial', 14, 'bold'), text="Place Price", bd=7, bg="#E6E6E6", fg="#333")
        self.lblPlacePrice.grid(row=4, column=0, sticky=W)
        self.txtPlacePrice = Entry(TravelFrame, font=('arial', 14, 'bold'), bd=7, state=DISABLED)
        self.txtPlacePrice.grid(row=4, column=1)

        #=============================================================================================
        # Checkbox for Ral Tax
        self.chkRalTax = Checkbutton(TravelFrame, text="Ral Tax", variable=var1, onvalue=1, offvalue=0, bg="#E6E6E6", fg="#333",
                                      font=('arial', 16, 'bold'), command=Ral_Tax).grid(row=5, column=0, sticky=W)
        self.txtRalTax = Entry(TravelFrame, font=('arial', 14, 'bold'), textvariable=RalTax, bd=7,
                               insertwidth=2, state=DISABLED, justify=RIGHT)
        self.txtRalTax.grid(row=5, column=1)

        self.chkTravelling_Insurance = Checkbutton(TravelFrame, text="Travelling Insurance", variable=var3, onvalue=1, offvalue=0, bg="#E6E6E6", fg="#333",
                                                   font=('arial', 16, 'bold'), command=Travelling).grid(row=6, column=0, sticky=W)
        self.txtTravelling_Insurance = Entry(TravelFrame, font=('arial', 14, 'bold'), textvariable=Travel_Ins, bd=7,
                                              insertwidth=2, state=DISABLED, justify=RIGHT)
        self.txtTravelling_Insurance.grid(row=6, column=1)
        
        self.chkExt_Luggage = Checkbutton(TravelFrame, text="Ext. Luggage", variable=var4, onvalue=1, offvalue=0, bg="#E6E6E6", fg="#333",
                                           font=('arial', 16, 'bold'), command=Lug).grid(row=7, column=0, sticky=W)
        self.txtExt_Luggage = Entry(TravelFrame, font=('arial', 14, 'bold'), textvariable=Luggage, bd=7,
                                     insertwidth=2, state=DISABLED, justify=RIGHT)
        self.txtExt_Luggage.grid(row=7, column=1)
        
        #===================================Payment Information=======================================
        self.lblPaidTax = Label(CostFrame,font=('arial', 14, 'bold'), text="\tPaid Tax", bd=7, bg="#E6E6E6", fg="#333")
        self.lblPaidTax.grid(row=0, column=2, sticky=W)
        self.txtPaidTax = Entry(CostFrame, font=('arial', 14, 'bold'), textvariable=PaidTax, bd=7,
                                width=26, justify=RIGHT).grid(row=0, column=3)
        
        self.lblSubTotal = Label(CostFrame, font=('arial', 14, 'bold'), text="\tSub Total", bd=7, bg="#E6E6E6", fg="#333")
        self.lblSubTotal.grid(row=1, column=2, sticky=W)
        self.txtSubTotal = Entry(CostFrame, font=('arial', 14, 'bold'), textvariable=SubTotal, bd=7,
                                 width=26, justify=RIGHT).grid(row=1, column=3)
        self.lblTotalCost = Label(CostFrame, font=('arial', 14, 'bold'), text="\tTotal Cost", bd=7, bg="#E6E6E6", fg="#333")
        self.lblTotalCost.grid(row=2, column=2, sticky=W)
        self.txtTotalCost = Entry(CostFrame, font=('arial', 14, 'bold'), textvariable=TotalCost, bd=7,
                                   width=26, justify=RIGHT).grid(row=2, column=3)
        #=============================================================================================
        self.chkStandard = Checkbutton(Ticket_Frame, text="Standard", variable=var5, bg="#E6E6E6", fg="#333",
                                       onvalue=1, offvalue=0, font=('arial', 14, 'bold'), command=Standard).grid(row=0, column=0)
        self.txtStandard = Entry(Ticket_Frame, font=('arial', 14, 'bold'), width=6,
                                 textvariable=Standard, bd=5, state=DISABLED, justify=RIGHT)
        self.txtStandard.grid(row=0, column=1)
        
        self.chkSingle = Checkbutton(Ticket_Frame, text="Single", variable=var6, onvalue=1, bg="#E6E6E6", fg="#333",
                                     offvalue=0, font=('arial', 14, 'bold')).grid(row=0, column=2, sticky=W)
        
        self.chkEconomy = Checkbutton(Ticket_Frame, text="Economy", variable=var7, onvalue=1, bg="#E6E6E6", fg="#333",
                                      offvalue=0, font=('arial', 14, 'bold'), command=Economy).grid(row=1, column=0, sticky=W)
        self.txtEconomy = Entry(Ticket_Frame, font=('arial', 14, 'bold'), width=6,
                                textvariable=Economy, bd=5, state=DISABLED, justify=RIGHT)
        self.txtEconomy.grid(row=1, column=1)
        
        self.chkReturn = Checkbutton(Ticket_Frame, text="Return", variable=var8, onvalue=1, bg="#E6E6E6", fg="#333",
                                     offvalue=0, font=('arial', 14, 'bold')).grid(row=1, column=2, sticky=W)
        
        self.chkFirstClass = Checkbutton(Ticket_Frame, text="First Class", variable=var9, onvalue=1, bg="#E6E6E6", fg="#333",
                                          offvalue=0, font=('arial', 14, 'bold'), command=FirstClass).grid(row=2, column=0)
        self.txtFirstClass = Entry(Ticket_Frame, font=('arial', 14, 'bold'), width=6,
                                   textvariable=FirstClass, bd=5, state=DISABLED, justify=RIGHT)
        self.txtFirstClass.grid(row=2, column=1)
        
        self.chkSpecialNeeds = Checkbutton(Ticket_Frame, text="Special Needs", variable=var10, onvalue=1, bg="#E6E6E6", fg="#333",
                                           offvalue=0, font=('arial', 14, 'bold')).grid(row=2, column=2, sticky=W)
        #=====================================Receipt===================================================
        self.txtReceipt = Text(ReceiptFrame, width=65, height=20, font=('arial', 10, 'bold'), bg="#fff", fg="#333")
        self.txtReceipt.grid(row=0, column=0)    
        #========================================Buttons===============================================
        self.btnTotal = Button(ButtonFrame, padx= 18, bd=7, font=('arial', 15, 'bold'),
                               width=3, text='Total', command=Total_Paid, bg="#4CAF50", fg="white").grid(row=0, column=0)
        self.btnReceipt = Button(ButtonFrame, padx=18, bd=7, font=('arial', 15, 'bold'),
                                 width=3, text='Receipt', command=Receipt, bg="#4CAF50", fg="white").grid(row=0, column=1)
        self.btnReset = Button(ButtonFrame, padx=18, bd=7, font=('arial', 15, 'bold'),
                               width=3, text='Reset', command=Reset, bg="#f44336", fg="white").grid(row=0, column=2)
        self.btnPrint = Button(ButtonFrame, padx=18, bd=7, font=('arial', 15, 'bold'),
                               width=3, text='Print', command=Print, bg="blue", fg="white").grid(row=0, column=3)
        self.btnExit = Button(ButtonFrame, padx=18, bd=7, font=('arial', 15, 'bold'),
                              width=3, text='Exit', command=Exit, bg="#f44336", fg="white").grid(row=0, column=4)
        #=============================================================================================
        
    def update_places(self, event=None):
        """Update the places list based on the selected package."""
        selected_package = self.selected_package.get()
        if selected_package in self.places:
            self.comboPlace['values'] = self.places[selected_package]  # Update place options based on package
            self.comboPlace.set("")  # Clear previous selection
        else:
            self.comboPlace['values'] = []  # Clear place options if no valid package is selected
            self.comboPlace.set("")  # Clear previous selection
        
if __name__ == '__main__':
    root = Tk()  # Create the main application window
    application = Travel(root)  # Instantiate the Travel class
    root.mainloop()  # Start the main event loop
