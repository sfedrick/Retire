import gradio as gr


import gradio as gr

def greet(name):
    return "Hello " + name + "!"

def save_to_file(inputs, outputs):
    with open("input.txt", "w") as f:
        f.write(str(inputs))
    with open("output.txt", "w") as f:
        f.write(str(outputs))

demo = gr.Interface(fn=greet, inputs="text", outputs="text", title="Greeting App", 
                    description="Say hello to someone!", examples=[["World"], ["Gradio"]], 
                    live=True, save_to_file=save_to_file)
demo.launch()