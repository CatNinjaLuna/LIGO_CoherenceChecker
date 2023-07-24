import tkinter as tk

class CoherenceChecker:

    def __init__(self):
        self.window = tk.Tk()
        # Create a window
        self.window.title("Coherence Checker")

        # Set size of the window
        self.window.geometry("800x600")

        # A message at the top of the GUI
        self.label = tk.Label(self.window, text="Let's check something about coherence!", font=("Arial", 18))
        # set space around the text
        self.label.pack(padx=20, pady=20)

        # Create a label to ask if the user has the required files
        self.ask_files_label = tk.Label(self.window,
                                        text="Running this program requires both coh_matrix.npz and Fscan.txt,\n"
                                             "do you have the files ready?", font=("Arial", 16))
        self.ask_files_label.pack(pady=10)

        # Create a "Yes" button
        self.yes_button = tk.Button(self.window, text="Yes", font=('Arial', 16), command=self.on_yes_button_click)
        self.yes_button.pack(pady=10)

        self.monthMenu = None
        self.graphMenu = None
        self.comb_vars = []
        self.channel_vars = []
        self.channel_names = [
            "H1:CAL-PCALY_RX_PD_OUT_DQ",
            "H1:ASC-AS_A_DC_NSUM_OUT_DQ",
            "H1:ASC-AS_A_DC_NSUM_OUT_DQ",
            "H1:PEM-EX_VMON_ETMX_ESDPOWER48_DQ",
            "H1:ASC-AS_B_RF36_Q_PIT_OUT_DQ",
        ]
        
        self.back_button = None

        self.window.mainloop()

    # This method is called when the user clicked on the "yes" button. Confirmed they have the files.
    # Then it provide options for user to specify their input
    def on_yes_button_click(self):
        # Remove the "Do you have the files ready?" label and "Yes" button
        self.ask_files_label.pack_forget()
        self.yes_button.pack_forget()

        # Create a drop-down menu for selecting a month
        self.monthMenu = tk.StringVar()
        self.monthMenu.set("Select Month")
        self.monthOptions = tk.OptionMenu(self.window, self.monthMenu, "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
        self.monthOptions.pack(pady=10)

        # Create a drop-down menu for selecting a graph
        self.graphMenu = tk.StringVar()
        self.graphMenu.set("Select Graph")
        self.graphOptions = tk.OptionMenu(self.window, self.graphMenu, "Fscan", "Heatmap")
        self.graphOptions.pack(pady=10)

        # Create a button to confirm month and graph selection
        self.confirm_button = tk.Button(self.window, text="Confirm", font=('Arial', 16), command=self.on_confirm_button_click)
        self.confirm_button.pack(pady=10)

        # Create a "Back" Button
        self.back_button = tk.Button(self.window, text="Back", font=("Arial", 16), command=self.on_back_button_click_after_confirm)
        self.back_button.pack(x=0, y=self.window.winfo_height(),anchor='sw')

    # This method is executed when the user clicks on the "Back" button after confirming they have the required files, 
    def on_back_button_click(self):
        # Remove all widgets from the window
        for widget in self.window.winfo_children():
            widget.pack_forget()

        # Reset month and graph selections
        self.monthMenu.set("Select Month")
        self.graphMenu.set("Select Graph")

        # Re-display the "Do you have the files ready" label and "Yes" button; repack initial widgets onto the window
        self.label.pack(padx=20,pady=20)
        self.ask_files_label.pack(pady=10)
        self.yes_button.pack(pady=10)

        # Place the 'back' button on the lower left corner
        self.on_back_button_click(x=0, y=self.window.winfo_height(), anchor='sw')

    # This method is called when the user clicks on the "Confirm" button after selecting a month and a graph from the respective dropdown menus.
    def on_confirm_button_click(self):
        if self.monthMenu and self.graphMenu:
            # Get the selected month and graph type
            selected_month = self.monthMenu.get()
            selected_graph = self.graphMenu.get()

            # Hide the drop-down menus and confirm button
            self.monthOptions.pack_forget()
            self.graphOptions.pack_forget()
            self.confirm_button.pack_forget()

            # Show the checkboxes for selecting channels
            for name in self.channel_names:
                var = tk.IntVar()
                self.channel_vars.append(var)
                checkbox = tk.Checkbutton(self.window, text=name, variable=var)
                checkbox.pack(anchor=tk.W)

            # Show the checkboxes for selecting comb options
            comb_options = [
                "0.0039", "0.1233", "1.6611", "1.85", "4.9842",
                "9.4743", "9.4745", "9.4805", "18.9507", "29.9695", "99.9986", "99.9987"
            ]
            for option in comb_options:
                var = tk.IntVar()
                self.comb_vars.append(var)
                checkbox = tk.Checkbutton(self.window, text=option, variable=var)
                checkbox.pack(anchor=tk.W)

            # Create a button to confirm selections
            self.confirm_selection_button = tk.Button(self.window, text="Confirm Selections", font=('Arial', 16), command=self.on_confirm_selection_button_click)
            self.confirm_selection_button.pack(pady=10)

            # Update the command of the "Back" button
            self.back_button['command'] = self.on_back_button_click_after_confirm_selection
            
            # Place button on lower left corner of the screen
            self.on_back_button_click(x=0, y=self.window.winfo_height(), anchor='sw')

    # This method handle the actions when the "Back" button is clicked after the user confirms the month and the graph type. 
    def on_back_button_click_after_confirm(self):
        # Remove all the widgets from the window
        for widget in self.window.winfo_children(): # for each widget in a list of child widget
            widget.pack_forget() # Make widget insivisible, does not delete widget, can be retrieved

        # Re-display the drop-down menus and confirm button
        self.monthOptions.pack(pady=10)
        self.graphOptions.pack(pady=10)
        self.confirm_button.pack(pady=10)

        # Re-display the "Back" button with the previous command. This line below had my brain ache.
        self.back_button['command'] = self.on_back_button_click_after_confirm_selection
        self.back_button.pack(side="buttom", pady=10)

    # This method will be called when the "Confirm Selection" button is clicked.
    def on_confirm_selection_button_click(self):
        # Get the selected month and graph type
        selected_month = self.monthMenu.get()
        selected_graph = self.graphMenu.get()

        # Get the selected channels
        selected_channels = [self.channel_names[i] for i, var in enumerate(self.channel_vars) if var.get() == 1]

        # Get the selected comb options
        comb_options = [
            "0.0039", "0.1233", "1.6611", "1.85", "4.9842",
            "9.4743", "9.4745", "9.4805", "18.9507", "29.9695", "99.9986", "99.9987"
        ]
        selected_comb_options = [comb_options[i] for i, var in enumerate(self.comb_vars) if var.get() == 1]

        # Hide the checkboxes and confirm button
        for checkbox in self.window.winfo_children():
            checkbox.pack_forget()
        self.confirm_selection_button.pack_forget()

        # Now, use the 'selected_month', 'selected_graph', 'selected_channels',
        # and 'selected_comb_options' for further processing.

        # For demonstration purposes, let's print the selections:
        print("Selected Month:", selected_month)
        print("Selected Graph:", selected_graph)
        print("Selected Channels:", selected_channels)
        print("Selected Comb Options:", selected_comb_options)

        # Update the command of the "Back" button
        self.back_button['command'] = self.on_back_button_click_after_confirm_selection

        # Place the "Back" button at the lower left corner
        self.back_button.place(x=0, y=self.window.winfo_height(), anchor='sw')

    

    # Set & retrieve values: https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/
    # This method handles what comes after the user clicked "back" after they clicked "confirm".
    def on_back_button_click_after_confirm_selection(self):
        # Remove all widgets from the window
        for widget in self.window.winfo_children():
            widget.pack_forget() # make them invisible

        # Reset the selection for channel and comb options
        for var in self.channel_vars:
            var.set(0)
        for var in self.comb_vars:
            var.set(0)

        # Re-display the checkboxes for selecting channels
        for name, var in zip(self.channel_names, self.channel_vars):
            checkbox = tk.Checkbutton(self.window, text=name, variable=var)
            checkbox.pack(anchor=tk.W) 

        # Re-display the checkboxes for selecting Combs
        comb_options = [
        "0.0039", "0.1233", "1.6611", "1.85", "4.9842",
        "9.4743", "9.4745", "9.4805", "18.9507", "29.9695", "99.9986", "99.9987"]
        
        for option, var in zip(comb_options, self.comb_vars):
            checkbox = tk.Checkbutton(self.window, text=option, variable=var)
            checkbox.pack(anchor=tk.W)
        
        # Re-display the "Confirm Selection" button
        self.confirm_selection_button = tk.Button(self.window,text="Confirm Selections", font=('Arial', 16), command=self.on_confirm_selection_button_click)
        self.confirm_selection_button.pack(pady=10)

        # Redisplay the "Back" button with the previous command
        self.back_button['command'] = self.on_back_button_click_after_confirm
        self.back_button.place(x=0,y=self.window.winfo_height(), anchor='sw')

# Create an instance of CoherenceChecker
if __name__ == "__main__":
    app = CoherenceChecker()
