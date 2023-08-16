import argparse
import gradio as gr
from interest import *
def compound(principal,age,salary,saving,debt,promotions,inflation=1.05):
    savings = Assets(float(principal),float(age),float(salary),float(saving),float(inflation))
    return savings.compound_interest()
    
def filter_records(records, gender):
    return records[records["gender"] == gender]


def main():
    with gr.Blocks() as demo:
        principal = gr.Textbox(label="Principal")
        age = gr.Textbox(label="Age")
        salary = gr.Textbox(label="salary")
        saving = gr.Textbox(label="saving")
        inflation = gr.Textbox(label="inflation")

        
        
        debt = gr.Dataframe(
                headers=["name", "Ammount", "interest","payment per month"],
                datatype=["str", "number", "number","number"],
                row_count=3,
                col_count=(4, "fixed"),
                label ="Debts please enter your debts. Once a debt is paid off money goes into savings."
            )
        promotions = gr.Dataframe(
                headers=["age", "Salary increase pre-tax","taxrate of new money"],
                datatype=["number", "number","number"],
                row_count=2,
                col_count=(3, "fixed"),
                label ="Promotions please enter your promotions all money from promotions are put into savings "
                
            )
        greet_btn = gr.Button("calculate")
        output = gr.Textbox(label="Output Box")

        greet_btn.click(fn=compound, inputs=[principal,age,salary,saving,debt,promotions,inflation], outputs=output, api_name="calculate")

    demo.demo = gr.Interface(fn=compound, inputs="text", outputs="text")
    demo.launch() 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--list", nargs="+", type=int, help="a list of inputs input with spaces like : python3 main.py -n 1 2 3 4 ")
    parser.add_argument("-t", "--single_int",type=int, help="A single integer like : python3 main.py -t ")
    parser.add_argument("-q", "--helpful", action="store_true", help="A single boolean like : python3 main.py -q true ")
    args = parser.parse_args() 
    main()
