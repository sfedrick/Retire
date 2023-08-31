

import gradio as gr

def greet(name):
    return "Hello, " + name + "!"

choices = ["Alice", "Bob", "Charlie"]
dropdown = gr.inputs.Dropdown(choices=choices, label="Select a name")
interface = gr.Interface(fn=greet, inputs=dropdown, outputs="text")
interface.launch()