from tkinter import *
from tkinter import ttk
import requests
import Currency as c
from  tkinter import  messagebox



window = Tk()
window.title("Convertor of Currency")
ob1 = c.CurrencyConverter
# def givevaluea():
#
#     ob1.methoda(firstvalue=drop_b.get())
#
#
# def givevalueb():
#     ob1.methodb(secondvalue=drop_a.get())

# variable.trace_variable("w",options_changed )



def passer():

    drop_b_box.delete(0,'end')
    try:
        i = int(drop_a_box.get())
    except ValueError:
        messagebox.showerror(title="ERROR", message="Please use int as input function")

    finally:
        value = ob1(from_currency= drop_a.get(),to_currency=drop_b.get(),from_currency_value=drop_a_box.get())
        sub_main_title.config(text = value.title())
        drop_b_box.insert(0,value.converter())

main_title = Label(text = " REAL TIME CURRENCY CONVERTOR ", bg = "black", fg = "White", font =("Arial", 18, "bold"))
main_title.grid(column = 0 , row = 0, columnspan = 2)


sub_main_title = Label(text = "",fg= "black",font =("Arial", 18, "bold"))
sub_main_title.grid(column = 0, row = 1, columnspan =2 )

k = StringVar()
drop_a = ttk.Combobox(window,width = 27, textvariable = k)
drop_a['values'] = ("CAD",
                          "HKD",
                          "ISK",
                          "JPY",
                          "INR",
                          "USD" )


drop_a.grid(column = 0, row = 2, padx = 30, pady = 50)

drop_a_box = Entry(width = 40)
drop_a_box.grid(column = 0 , row = 3,padx = 30, pady = 50)

drop_b = ttk.Combobox(window, width=27)
# drop_b.bind(givevaluea())

drop_b['values'] = ("CAD",
                          "HKD",
                          "ISK",
                          "JPY",
                          "INR",
                          "USD" )


drop_b.grid(column=1, row=2,padx = 30, pady = 50)



drop_b_box = Entry(width = 40,validate = 'key')
drop_b_box.grid(column = 1 , row = 3,padx = 30, pady = 50)


convertor_button = Button(text = "CONVERT",width = 40, bg = "blue", command =passer)
convertor_button.grid(column = 0, row = 4, columnspan = 2, padx = 10, pady = 20)



window.mainloop()
