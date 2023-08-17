import argparse
import gradio as gr
from interest import *

def compound(principal,age,salary,saving,debt,promotions,windfall,current_year,inflation=1.05,returns=1.10,four01k=7500,four01k_total=0):
    
    try:
        float(current_year)
    except ValueError:
        current_year = -1
    
    try:
        savings = Assets(float(principal),float(age),float(salary),float(saving),float(current_year),float(inflation),float(returns),float(four01k),float(four01k_total))
        savings.debt_horizon(debt)
        savings.promotion_extraction(promotions)
        savings.windfall_extraction(windfall)
        return savings.compound_interest()
    except ValueError:
        savings = Assets(float(principal),float(age),float(salary),float(saving),float(current_year))
        savings.debt_horizon(debt)
        savings.promotion_extraction(promotions)
        savings.windfall_extraction(windfall)
        return savings.compound_interest()


def main():
    with gr.Blocks() as demo:
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
                headers=["name", "Amount", "interest","payment per month"],
                datatype=["str", "number", "number","number"],
                row_count=3,
                col_count=(4, "fixed"),
                label ="Debts. Once a debt is paid off money goes into savings."
            )
        promotions = gr.Dataframe(
                headers=["name","age", "Salary increase post-tax"],
                datatype=["str","number", "number"],
                row_count=1,
                col_count=(3, "fixed"),
                label ="Promotions money gain in the future in todays money (will be adjusted for inflation) "  
            )
        windfall = gr.Dataframe(
                headers=["name","age", "windfall or payment"],
                datatype=["str","number", "number"],
                row_count=1,
                col_count=(3, "fixed"),
                label ="Please enter a windfall or large payment you made"
                
            )
        greet_btn = gr.Button("calculate")
        output = gr.Textbox(label="Output Box",allow_flagging="manual",flagging_callback=gr.CSVLogger())

        greet_btn.click(fn=compound, inputs=[principal,age,salary,saving,debt,promotions,windfall,current_year,inflation,returns,four01k,four01k_total], outputs=output, api_name="calculate")

    demo.launch(share="true") 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--list", nargs="+", type=int, help="a list of inputs input with spaces like : python3 main.py -n 1 2 3 4 ")
    parser.add_argument("-t", "--single_int",type=int, help="A single integer like : python3 main.py -t ")
    parser.add_argument("-q", "--helpful", action="store_true", help="A single boolean like : python3 main.py -q true ")
    args = parser.parse_args() 
    main()
