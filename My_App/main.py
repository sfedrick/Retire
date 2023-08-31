import argparse
import gradio as gr
from interest import *
import pandas as pd
import os

import re
# global variables 
save_directory = Assets.save_directory

def save_inputs(principal,age,salary,saving,debt,promotions,windfall,current_year,inflation=1.05,returns=1.10,four01k=7500,four01k_total=0,save_name = "default"):
    input_array = [principal,age,salary,saving,debt,promotions,windfall,current_year,inflation,returns,four01k,four01k_total]
    output =""
    global save_directory
    if(save_name == ""):
        save_name = "default"
    df = pd.DataFrame(input_array)
    df.to_csv(os.path.join(save_directory, save_name), index=False)
    df = pd.read_csv(os.path.join(save_directory, save_name))
    def replace_spaces_with_comma(text):
        string = re.sub(r' +', ',', text)
        string = string.strip(',')
        return string
        
    df = df.applymap(replace_spaces_with_comma)
    df.to_csv(os.path.join(save_directory, save_name), index=False)
    for item in input_array:
        if(len(item)==0):
            item = ""
        output = output + str(item) +"\n"

    return "Saved file "+save_name +" with values : \n"+output
    pass

def main():
    global save_directory
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    choices = os.listdir(save_directory)
    choices.insert(0, "   None   ")
    with gr.Blocks() as demo:
        load_btn = gr.inputs.Dropdown(choices=choices, label="Load in saved data")
        calculate_btn_loaded = gr.Button("calculate with loaded data ")
        principal = gr.Textbox(label="Principal*")
        age = gr.Textbox(label="Age*")
        salary = gr.Textbox(label="take home salary*")
        saving = gr.Textbox(label="saving*")
        current_year = gr.Textbox(label="current year")
        inflation = gr.Textbox(label="inflation")
        returns = gr.Textbox(label="expected investment returns")
        four01k_total = gr.Textbox(label="Principal ammount of 401k")
        four01k = gr.Textbox(label="401k savings and fixed savings") 
        
        debt = gr.Dataframe(
                headers=["name", "Amount", "interest","payment_per_month"],
                datatype=["str", "number", "number","number"],
                row_count=3,
                col_count=(4, "fixed"),
                label ="Debts. Once a debt is paid off money goes into savings."
            )
        promotions = gr.Dataframe(
                headers=["name","age", "Salary_increase_post-tax"],
                datatype=["str","number", "number"],
                row_count=1,
                col_count=(3, "fixed"),
                label ="Promotions money gain in the future in todays money (will be adjusted for inflation) "  
            )
        windfall = gr.Dataframe(
                headers=["name","age", "windfall_or_payment"],
                datatype=["str","number", "number"],
                row_count=1,
                col_count=(3, "fixed"),
                label ="Please enter a windfall or large payment you made"
                
            )
        
        calculate_btn = gr.Button("calculate")
        output = gr.Textbox(label="Output Box",allow_flagging="manual",flagging_callback=gr.CSVLogger())
        save_name = gr.Textbox(label="Save name ")
        input_array = [principal,age,salary,saving,debt,promotions,windfall,current_year,inflation,returns,four01k,four01k_total,save_name]
        save_btn = gr.Button("Save Button")
        output_save = gr.Textbox(label="Save Status",allow_flagging="manual",flagging_callback=gr.CSVLogger())
        save_btn.click(fn=save_inputs, inputs=input_array, outputs=output_save, api_name="save name")
        calculate_btn.click(fn=Assets.compound, inputs=input_array, outputs=output, api_name="calculate")
        calculate_btn_loaded.click(fn=Assets.compound_load, inputs=load_btn, outputs=output, api_name="load_calculate")
        
    demo.launch(share="true") 

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--list", nargs="+", type=int, help="a list of inputs input with spaces like : python3 main.py -n 1 2 3 4 ")
    parser.add_argument("-t", "--single_int",type=int, help="A single integer like : python3 main.py -t ")
    parser.add_argument("-q", "--helpful", action="store_true", help="A single boolean like : python3 main.py -q true ")
    args = parser.parse_args() 
    main()
