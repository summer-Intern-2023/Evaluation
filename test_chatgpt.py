import openai
import os
import pandas as pd
import openpyxl
import time

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = "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"

df = pd.read_excel('score4.xlsx')

def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

j = 2
while j < 5:
    i = j * 4
    title = df.iloc[i, 0]
    print(title + "\n")

    text1 = df.iloc[i, 2]
    print(text1+ "\n")

    i = i + 1
    text2 = df.iloc[i, 2]
    print(text2+ "\n")

    i = i + 1
    text3 = df.iloc[i, 2]
    print(text3+ "\n")

    i = i + 1
    text4 = df.iloc[i, 2]
    print(text4+ "\n")


    prompt = f"""
    text1, text2, text3, text4是四篇根据title写的作文，请你分别给这4篇作文打分，满分10分,7篇文章的分数不能有重复的
    评价标准：句子完整性(20%)，用词正确(10%)，文体正确(10%)，中心明确(10%),运用四字词语(15%)，运用修辞手法(15%)/
    是否符合题意很重要(20%)/
    请根据评价标准打分/
    输出格式：
    text1：分数
    text2：分数
    text3：分数
    text4：分数
    ```{title, text1, text2, text3, text4}```
    """

    response = get_completion(prompt)

    # 打开已存在的Excel文件
    workbook = openpyxl.load_workbook('score4.xlsx')

    # 选择第一个工作表
    sheet = workbook['Sheet1']

    # 在 [0, 3] 单元格中写入数据
    sheet.cell(row=(j * 4) + 2, column= 4 , value=response)

    # 保存文件
    workbook.save('score4.xlsx')

    # 关闭文件
    workbook.close()

    print(response)
    j = j + 1
    time.sleep(40)  # 暂停40秒