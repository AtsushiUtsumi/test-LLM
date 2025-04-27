# 「https://huggingface.co/mmnga/Llama-3-ELYZA-JP-8B-gguf/tree/main」から
# 「Llama-3-ELYZA-JP-8B-q4_k_m.gguf」をダウンロードして「models」に入れておく

from llama_cpp import Llama

llm = Llama(
    model_path="models/Llama-3-ELYZA-JP-8B-q4_k_m.gguf",
    chat_format="llama-3",
    n_ctx=0,
    verbose=False,
    echo=False,
)
response = llm.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": "あなたは誠実で優秀な日本人のアシスタントです。特に指示が無い場合は、常に日本語で回答してください。",
        },
        {
            "role": "user",
            "content": "日本の総理大臣は誰ですか？",
        },
    ],
    max_tokens=1024,
)

print(response["choices"][0]["message"]["content"])
