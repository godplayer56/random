#!/usr/bin/env python
# coding: utf-8

# In[68]:


# Import necessary modules from tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *

# Create main window
root = tk.Tk()
root.title("Carbon Calculator")

# Create the input frame
input_frame = ttk.Frame()
input_frame.pack(padx=10, pady=10)

# Create the labels and entry widgets for the input parameters
heading1_label = ttk.Label(input_frame, text="BIOCHAR PERMANENCE CALCULATOR")
heading1_label.grid(row=0, column=0, padx=100, pady=5, sticky="w")


# Create a function to show the selected people
def show_result(people_var):
    result_label.config(text=f"Selected people is {people_var.get()}")

# Function to handle the next button click
def next_tab():
    tab_control.select(tab_control.index("current") + 1)

# Function to handle the previous button click
def prev_tab():
    tab_control.select(tab_control.index("current") - 1)

# Function to quit the application
def quit_app():
    root.destroy()
    
    
    
def calculate_biochar_permanence():
    # Get the input values from the entry widgets
    people = people_entry.get()
    Electricity = float (Electricity_entry.get())
    NaturalGas = float (NaturalGas_entry.get())
    HeatingOil = float (HeatingOil_entry.get())
    Coal = float (fCoal_entry.get())
    massOfBiochar = float (massOfBiochar_entry.get())
    biocharyield = float (biocharyield_entry.get())
    Via = float(Via_entry.get())
    moisture_content_percent = float(moisture_content_percent_entry.get())
    To = float(To_entry.get())
    carbon_percent = float(carbon_percent_entry.get())
    hydrogen_percent = float(hydrogen_percent_entry.get())
    nitrogen_percent = float(nitrogen_percent_entry.get())
    sulphur_percent = float(sulphur_percent_entry.get())
    oxygen_percent = (100 - (carbon_percent + hydrogen_percent + nitrogen_percent + sulphur_percent))
    t50_biochar = float(t50_biochar_entry.get())
    t50_graphite = 885
    r50 = float(t50_biochar/t50_graphite)
    fixed_carbon_percent = float ((massOfBiochar - (moisture_content_percent +  To + Via))/ (massOfBiochar))*100
    bc= float((1.05-((0.616 * 12 * hydrogen_percent)/fixed_carbon_percent)))*100
    
    
          # Calculate the oxygen percent
    oxygen_percent = (100 - (carbon_percent + hydrogen_percent + nitrogen_percent + sulphur_percent))

    
    
    

    
# Create tab control
tab_control = tk.ttk.Notebook(root)

# Tab 1: Disclaimer
tab1 = tk.Frame(tab_control)
tab_control.add(tab1, text="Disclaimer")
tk.Label(tab1, text="\nDISCLAIMER \n\nThis software is developed by Clean Energy Laboratory, IIT Delhi \n\nUnder the project titled “Biochar Production and it’s Permanence for Indian Agro-Residue” \n\nfunded by ReNew Power\n\n\n").pack()

# Push buttons in Tab 1
def agree_and_proceed():
    next_tab()

def end_application():
    messagebox.showinfo("Ending Application", "Thank you")
    quit_app()

tk.Button(tab1, text="\nAgree and proceed\n", command=agree_and_proceed).pack()


tk.Button(tab1, text="\nEnd application\n", command=end_application).pack()


# Tab 2: people


tab2 = tk.Frame(tab_control)
tab_control.add(tab2, text="House")

# Create the input frame
input_frame = ttk.Frame(tab2)
input_frame.pack(padx=10, pady=10)

def calculate_biochar_yield():
    # Get the input values from the entry widgets
    
    Electricity = float (Electricity_entry.get())
    NaturalGas = float (NaturalGas_entry.get())
    HeatingOil = float (HeatingOil_entry.get())
    Coal = float (Coal_entry.get())
    LPG=float (LPG_entry.get())
    Propane=float (Propane_entry.get())
    WoodenPellets=float (WoodenPellets_entry.get())
    biocharyield_percent = float (Electricity*NaturalGas*HeatingOil*Coal)
    
    
   # Display the result in the result label
    result1_label.config(text=f"Approximately biochar yield (in %): {biocharyield_percent:}")

# Create the labels and entry widgets for the input parameters
heading1_label = ttk.Label(input_frame, text="# people")
heading1_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")


people_label = ttk.Label(input_frame, text="How many people in your Household:")
people_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

people_options = ['select','1','2','3','4','5','6','7','8','9','10']
people_var = tk.StringVar(root)
people_var.set(people_options[0])

people_dropdown = ttk.OptionMenu(input_frame, people_var, *people_options)
people_dropdown.grid(row=1, column=1, padx=5, pady=5)

note_label = ttk.Label(input_frame, text="NOTE\n Experiments has been performed in CEL Lab, IIT Delhi to obtain results for Default people")
note_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")



hfp_label = ttk.Label(input_frame, text="# Household footprint parameters")
hfp_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

Electricity_label = ttk.Label(input_frame, text="Electiricity(in kWh) :")
Electricity_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
Electricity_entry = ttk.Entry(input_frame, width=10)
Electricity_entry.grid(row=4, column=1, padx=5, pady=5)

NaturalGas_label = ttk.Label(input_frame, text="Natural Gas :")
NaturalGas_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
NaturalGas_entry = ttk.Entry(input_frame, width=10)
NaturalGas_entry.grid(row=5, column=1, padx=5, pady=5)
NaturalGas_options=['select','kWh','therms']
NaturalGas_var = tk.StringVar(root)
NaturalGas_var.set(NaturalGas_options[0])
NaturalGas_dropdown = ttk.OptionMenu(input_frame, NaturalGas_var, *NaturalGas_options)
NaturalGas_dropdown.grid(row=5, column=2, padx=5, pady=5)

HeatingOil_label = ttk.Label(input_frame, text="Heating oil:")
HeatingOil_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
HeatingOil_entry = ttk.Entry(input_frame, width=10)
HeatingOil_entry.grid(row=6, column=1, padx=5, pady=5)
HeatingOil_options=['select','liters','metric tons','gallons']
HeatingOil_var = tk.StringVar(root)
HeatingOil_var.set(HeatingOil_options[0])
HeatingOil_dropdown = ttk.OptionMenu(input_frame, HeatingOil_var, *HeatingOil_options)
HeatingOil_dropdown.grid(row=6, column=2, padx=5, pady=5)

Coal_label = ttk.Label(input_frame, text="Coal")
Coal_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
Coal_entry = ttk.Entry(input_frame, width=10)
Coal_entry.grid(row=7, column=1, padx=5, pady=5)
Coal_options=['select','metric tonnes','x10kg bags','x20kg bags','x25kg bags','x50kg bags']
Coal_var = tk.StringVar(root)
Coal_var.set(Coal_options[0])
Coal_dropdown = ttk.OptionMenu(input_frame, Coal_var, *Coal_options)
Coal_dropdown.grid(row=7, column=2, padx=5, pady=5)

LPG_label = ttk.Label(input_frame, text="LPG")
LPG_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")
LPG_entry = ttk.Entry(input_frame, width=10)
LPG_entry.grid(row=8, column=1, padx=5, pady=5)
LPG_var = tk.StringVar(root)
LPG_options=['select','kWh','therms','liters','gallons']
LPG_var.set(LPG_options[0])
LPG_dropdown = ttk.OptionMenu(input_frame, LPG_var, *LPG_options)
LPG_dropdown.grid(row=8, column=2, padx=5, pady=5)

Propane_label = ttk.Label(input_frame, text="Propane:")
Propane_label.grid(row=9, column=0, padx=5, pady=5, sticky="w")
Propane_entry = ttk.Entry(input_frame, width=10)
Propane_entry.grid(row=9, column=1, padx=5, pady=5)
Propane_options=['select','liters','gallons']
Propane_var = tk.StringVar(root)
Propane_var.set(NaturalGas_options[0])
Propane_dropdown = ttk.OptionMenu(input_frame, Propane_var, *Propane_options)
Propane_dropdown.grid(row=9, column=2, padx=5, pady=5)

WoodenPellets_label = ttk.Label(input_frame, text="Wooden Pellets")
WoodenPellets_label.grid(row=10, column=0, padx=5, pady=5, sticky="w")
WoodenPellets_entry = ttk.Entry(input_frame, width=10)
WoodenPellets_entry.grid(row=10, column=1, padx=5, pady=5)
WoodenPellets_options=['select','metric tonnes'] 
WoodenPellets_var = tk.StringVar(root)
WoodenPellets_var.set(WoodenPellets_options[0])
WoodenPellets_dropdown = ttk.OptionMenu(input_frame, WoodenPellets_var, *WoodenPellets_options)
WoodenPellets_dropdown.grid(row=10, column=2, padx=5, pady=5)
# Create the calculate button
calculate_button = ttk.Button(tab2, text="Calculate biochar yield", command=calculate_biochar_yield)
calculate_button.pack(padx=7, pady=10)

# Create the result label

result1_label = ttk.Label(tab2, text="")
result1_label.pack(padx=10, pady=10)


# Create the third page
tab3 = tk.Frame(tab_control)
tab_control.add(tab3, text="Flights")

# Create the input frame
input_frame = ttk.Frame(tab3)
input_frame.pack(padx=10, pady=10)

def calculate_fp():
    # Get the input values from the entry widgets
    From = str (From_entry.get())
    Via = str(Via_entry.get())
    To = str(To_entry.get())
    trips=float(Trips_entry.get())
    
    
    # Display the result in the result label
    result2_label.config(text=f"Total emission is: {trips*100:.2f} metric tonnes")
    
    
# Create the labels and entry widgets for the input parameters
heading3_label = ttk.Label(input_frame, text="Flight carbon footprint calculator")
heading3_label.grid(row=0, column=2, padx=0, pady=10, sticky="w")
    
    
# Create the labels and entry widgets for the input parameters
    
From_label = ttk.Label(input_frame, text="From")
From_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
From_entry = ttk.Entry(input_frame, width=20)
From_entry.grid(row=3, column=1, padx=5, pady=5)

To_label = ttk.Label(input_frame, text="To:")
To_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
To_entry = ttk.Entry(input_frame, width=20)
To_entry.grid(row=4, column=1, padx=5, pady=5)
    
Via_label = ttk.Label(input_frame, text="Via(optional):")
Via_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
Via_entry = ttk.Entry(input_frame, width=20)
Via_entry.grid(row=5, column=1, padx=5, pady=5)    

class_label = ttk.Label(input_frame, text="Class:")
class_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

class_options = ['select','Economy class','Premium Economy','Business class','First class','average(unknown class)']
class_var = tk.StringVar(root)
class_var.set(people_options[0])

class_dropdown = ttk.OptionMenu(input_frame, class_var, *class_options,)
class_dropdown.grid(row=1, column=1, padx=5, pady=5)

Trips_label = ttk.Label(input_frame, text="Trips:")
Trips_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
Trips_entry = ttk.Entry(input_frame, width=20)
Trips_entry.grid(row=6, column=1, padx=5, pady=5)    

    
    
# Create the calculate button
calculate_button = ttk.Button(tab3, text="Calculate Flight carbon footprint", command=calculate_fp)
calculate_button.pack(padx=7, pady=10)

# Create the result label

result2_label = ttk.Label(tab3, text="")
result2_label.pack(padx=0, pady=3)
result4_label = ttk.Label(tab3, text="")
result4_label.pack(padx=0, pady=3)
result5_label = ttk.Label(tab3, text="")
result5_label.pack(padx=0, pady=3)
result3_label = ttk.Label(tab3, text="")
result3_label.pack(padx=0, pady=3)
    
    
# Create the fourth page

tab4 = tk.Frame(tab_control)
tab_control.add(tab4, text="Biochar:Physicochemical properties")


# Create the input frame
input_frame = ttk.Frame(tab4)
input_frame.pack(padx=10, pady=10)

def calculate_biochar():
    # Get the input values from the entry widgets
    massOfBiochar = float (massOfBiochar_entry.get())
    Via1 = float(Via1_entry.get())
    moisture_content_percent1 = float(moisture_content_percent1_entry.get())
    To1 = float(To1_entry.get())
    carbon_percent1 = float(carbon_percent1_entry.get())
    hydrogen_percent1 = float(hydrogen_percent1_entry.get())
    
    nitrogen_percent1 = float(nitrogen_percent1_entry.get())
    sulphur_percent1 = float(sulphur_percent1_entry.get())
    oxygen_percent1 = (100 - (carbon_percent1 + hydrogen_percent1 + nitrogen_percent1 + sulphur_percent1))
    fixed_carbon_percent1 = float ((massOfBiochar - (moisture_content_percent1 +  To1 + Via1))/ (massOfBiochar))*100
    hc_ratio1 = float ((hydrogen_percent1*12)/carbon_percent1)
    oc_ratio1 = float ((oxygen_percent1*12)/(carbon_percent1*16))
    
    # Display the result in the result label
    result6_label.config(text=f"Oxygen(O) in Biochar: {oxygen_percent1:.2f} %")
    
      # Display the result in the result label
    result7_label.config(text=f"Fixed Carbon Percentage in Biochar : {fixed_carbon_percent1:.2f} %")
    
    # Display the result in the result label
    result8_label.config(text=f"O/C ratio of Biochar : {oc_ratio1:.2f}")
    
    # Display the result in the result label
    result9_label.config(text=f"H/C ratio of Biochar : {hc_ratio1:.2f}")
    
    

# Create the labels and entry widgets for the input parameters
heading3_label = ttk.Label(input_frame, text="**BIOCHAR CHARACTERISATION**")
heading3_label.grid(row=0, column=2, padx=0, pady=10, sticky="w")


people_label = ttk.Label(input_frame, text="Select default biochar sample:")
people_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

people_options = ["Select", "RSB350", "RSB400", "RSB450", "RSB500", "RSB550", "RSB600", "RSB650", "WSB350", "WSB400", "WSB450", "WSB500", "WSB550", "WSB600", "WSB650", "RHB350", "RHB400", "RHB450", "RHB500", "RHB550", "RHB600", "RHB650"]
people_var = tk.StringVar(root)
people_var.set(people_options[0])

people_dropdown = ttk.OptionMenu(input_frame, people_var, *people_options)
people_dropdown.grid(row=1, column=1, padx=5, pady=5)

note_label = ttk.Label(input_frame, text="NOTE\n*RSB : Rice Straw Biochar\n*WSB : Wheat Straw Biochar \n*RHB : Rice Husk Biochar")
note_label.grid(row=1, column=3, padx=5, pady=5, sticky="w")




# Create the labels and entry widgets for the input parameters
heading1_label = ttk.Label(input_frame, text="# PROXIMATE ANALYSIS")
heading1_label.grid(row=2, column=0, padx=5, pady=5, sticky="w") 
  
massOfBiochar_label = ttk.Label(input_frame, text="Mass of biochar (in grams) : \n(Enter 100 if Ash,VM and MC value is in %):")
massOfBiochar_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
massOfBiochar_entry = ttk.Entry(input_frame, width=10)
massOfBiochar_entry.grid(row=3, column=1, padx=5, pady=5)

To1_label = ttk.Label(input_frame, text="Volatile Matter (VM):")
To1_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
To1_entry = ttk.Entry(input_frame, width=10)
To1_entry.grid(row=4, column=1, padx=5, pady=5)
                                            
Via1_label = ttk.Label(input_frame, text="Ash:")
Via1_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
Via1_entry = ttk.Entry(input_frame, width=10)
Via1_entry.grid(row=5, column=1, padx=5, pady=5)    

moisture_content_percent1_label = ttk.Label(input_frame, text="Moisture Content (MC) (Enter 0 for dry basis):")
moisture_content_percent1_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
moisture_content_percent1_entry = ttk.Entry(input_frame, width=10)
moisture_content_percent1_entry.grid(row=6, column=1, padx=5, pady=5)
    

heading2_label = ttk.Label(input_frame, text="# ULTIMATE ANALYSIS")
heading2_label.grid(row=2, column=3, padx=100, pady=5, sticky="w")

carbon_percent1_label = ttk.Label(input_frame, text="Carbon (C) % :")
carbon_percent1_label.grid(row=3, column=3, padx=100, pady=5, sticky="w")
carbon_percent1_entry = ttk.Entry(input_frame, width=10)
carbon_percent1_entry.grid(row=3, column=4, padx=5, pady=5)

hydrogen_percent1_label = ttk.Label(input_frame, text="Hydrogen (H) % :")
hydrogen_percent1_label.grid(row=4, column=3, padx=100, pady=5, sticky="w")
hydrogen_percent1_entry = ttk.Entry(input_frame, width=10)
hydrogen_percent1_entry.grid(row=4, column=4, padx=5, pady=5)

nitrogen_percent1_label = ttk.Label(input_frame, text="Nitrogen (N) % :")
nitrogen_percent1_label.grid(row=5, column=3, padx=100, pady=5, sticky="w")
nitrogen_percent1_entry = ttk.Entry(input_frame, width=10)
nitrogen_percent1_entry.grid(row=5, column=4, padx=5, pady=5)

sulphur_percent1_label = ttk.Label(input_frame, text="Sulphur (S) % : \n(Enter 0 if not known)")
sulphur_percent1_label.grid(row=6, column=3, padx=100, pady=5, sticky="w")
sulphur_percent1_entry = ttk.Entry(input_frame, width=10)
sulphur_percent1_entry.grid(row=6, column=4, padx=5, pady=5)
    
    
# Create the calculate button
calculate_button = ttk.Button(tab4, text="Calculate Oxygen% , O/C , H/C , Fixed carbon (FC)", command=calculate_biochar)
calculate_button.pack(padx=7, pady=10)

# Create the result label

result6_label = ttk.Label(tab4, text="")
result6_label.pack(padx=0, pady=3)
result8_label = ttk.Label(tab4, text="")
result8_label.pack(padx=0, pady=3)
result9_label = ttk.Label(tab4, text="")
result9_label.pack(padx=0, pady=3)
result7_label = ttk.Label(tab4, text="")
result7_label.pack(padx=0, pady=3)


    
    
    
# Tab 5: Result
tab5 = tk.Frame(tab_control)
tab_control.add(tab5, text="Result / Output ")
result_label = tk.Label(tab5, text="")
result_label.pack()



# Buttons at the bottom
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
next_button = tk.Button(bottomframe, text="Next", command=next_tab, fg ='blue')
next_button.pack(side=tk.RIGHT)
prev_button = tk.Button(bottomframe, text="Previous", command=prev_tab, fg ='black')
prev_button.pack(side=tk.LEFT)
quit_button = tk.Button(bottomframe, text="Quit", command=quit_app, fg ='red')
quit_button.pack(side=tk.BOTTOM, padx=100, pady=10)



# Display tab control
tab_control.pack(expand=1, fill="both")

# Start the application
root.mainloop()


# In[ ]:




