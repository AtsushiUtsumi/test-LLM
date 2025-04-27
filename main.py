import gradio as gr
from llama_cpp import Llama

llama = Llama(
    model_path="models/Llama-3-ELYZA-JP-8B-q4_k_m.gguf",
    chat_format="llama-3",
    n_ctx=0,
    verbose=False,
    echo=False,
)

def predict(message, history):
    messages = []
    for human_content, system_content in history:
        message_human = {
            "role":"user",
            "content": human_content+"\n",
        }
        message_system = {
            "role":"system",
            "content": system_content+"\n",
        }
        messages.append(message_human)
        messages.append(message_system)
    message_human = {
        "role":"user",
        "content":message+"\n",
    }
    messages.append(message_human)
    # Llama2回答
    streamer = llama.create_chat_completion(messages, stream=True)

    partial_message = ""
    for msg in streamer:
        message = msg['choices'][0]['delta']
        if 'content' in message:
            partial_message += message['content']
            yield partial_message

gr.ChatInterface(predict).queue().launch()