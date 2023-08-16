import argparse
import gradio as gr
from interest import *
def compound(principal,age,salary,saving):
    savings = Assets(int(principal),int(age),int(salary),int(saving))
    return savings.compound_interest()
    


def main():
    with gr.Blocks() as demo:
        principal = gr.Textbox(label="Principal")
        age = gr.Textbox(label="Age")
        salary = gr.Textbox(label="salary")
        saving = gr.Textbox(label="saving")

        output = gr.Textbox(label="Output Box")
        greet_btn = gr.Button("calculate")
        greet_btn.click(fn=compound, inputs=[principal,age,salary,saving], outputs=output, api_name="calculate")

    demo.demo = gr.Interface(fn=compound, inputs="text", outputs="text")
    demo.launch() 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--list", nargs="+", type=int, help="a list of inputs input with spaces like : python3 main.py -n 1 2 3 4 ")
    parser.add_argument("-t", "--single_int",type=int, help="A single integer like : python3 main.py -t ")
    parser.add_argument("-q", "--helpful", action="store_true", help="A single boolean like : python3 main.py -q true ")
    args = parser.parse_args() 
    main()
