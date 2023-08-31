import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = "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"
def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]



title = f"""
春天到了，一颗颗种子发芽了，钻出了地面，它们会看到什么?联系你看到过的春天景色，展开想像，写一段话。
"""
text = f"""
春天到了，一颗颗种子发芽了，露出了嫩叶。
"""
prompt = f"""
text是根据title写的作文,请你给这篇作文打分/
评价标准：结构完整(20%)，构思新颖(5%)，文章流畅(10%)，语音清晰(5%)，中心明确(10%),运用四字词语(15%)，运用修辞手法(15%)/
是否符合题意很重要(20%)/
请根据评价标准打分/
输出格式“这篇文章得分：...(满分10分)”
```{title, text}```
"""
response = get_completion(prompt)
print(response)