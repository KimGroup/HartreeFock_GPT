import argparse
import json
import openai
from dotenv import load_dotenv
import os

model_params = {
    'model': "gpt-4",
    'temperature': 0,
}

load_dotenv('../.env')
openai.api_key  = os.getenv('OPENAI_API_KEY')




def load_prompt_template(file):
    prompt_dict = {}
    current_task = None  # Track the current task, initialized to None

    with open(file, 'r') as f:
        for line in f:
            stripped_line = line.strip()

            # Skip comments
            if stripped_line.startswith('<!--'):
                continue
            
            if stripped_line.startswith('## '):
                # New task starts
                current_task = stripped_line[3:]
                prompt_dict[current_task] = ''
            elif not stripped_line.startswith('# ') and current_task:
                # If this line is part of a task (not a task declaration or a section),
                # and a task is currently being tracked, append this line to the task.
                if not stripped_line.startswith('**Prompt:**'):
                    prompt_dict[current_task] += line

    return prompt_dict

def generate_prompt(kwargs,prompt_dict):
    message={
    'role':
    'user',
    'content':
    prompt_dict[kwargs['task']].format(
        **kwargs).strip()
}
    return message

def assembly_message(sys_msg,user_msg,AI_msg):
    messages = sys_msg
    assert len(user_msg)-len(AI_msg)==1, f'# of user message {len(user_msg)} is not compatible with # of AI_message {len(AI_msg)}'
    messages.append(user_msg[0])
    for user, AI in zip(user_msg[1:],AI_msg):
        messages.append(AI)
        messages.append(user)
    return messages

def extract_var(prompt):
    string='Use the following conventions for the symbols'
    contains=False
    var_list=[]
    for line in prompt.split('\n'):
        if contains:
            if len(line.strip())==0:
                break
            var_list.append(line)

        if line.startswith(string):
            contains=True
        
    return var_list

def summarizer(summarization, prompt, response,prompt_dict):
    '''Summarize the background (summarization) + question (prompt) + answer (response)'''
    var_old=extract_var(summarization)
    var_new=extract_var(prompt)
    var=var_old+var_new
    
    summarization_prompt=prompt_dict['Conversation summarizer'].format(background=summarization,question=prompt, answer=response)
    messages= [{'role':'user','content': summarization_prompt}]
    rs= openai.ChatCompletion.create(messages=messages, **model_params)

    summarized=rs['choices'][0]['message'].content

    
    if len(var)>0:
        if 'Use the following conventions for the symbols:  ' in summarized:
            summarized += '\n'+'\n'.join(var)
        else:
            summarized += '\n\nUse the following conventions for the symbols:  \n' +'\n'.join(var)
    return summarized

def solver(summarization, prompt,prompt_dict):
    '''
    Solve the problem in the prompt
    '''
    sys_msg=[{'role': 'system', 'content': prompt_dict['Problem-solver']}]
    question_prompt='**Background**  \n{background}\n\n**Question**  \n{question}'.format(background=summarization,question=prompt)
    user_msg=[{'role':'user','content':question_prompt}]
    messages = sys_msg + user_msg
    rs= openai.ChatCompletion.create(messages=messages, **model_params)

    response=rs['choices'][0]['message'].content
    return response


def run(prompt_template, arxiv_number):
    '''Load the prompt_template, and the descriptor file from arxiv number
    Generate prompts, and feed into `solver`.
    The response will be summarized by `summarizer`.
    Write all responses to `{arxiv_number}_auto.md`

    Should run from each directory 'arxiv_number'.'''
    prompt_dict=load_prompt_template(prompt_template)
    with open(f'{arxiv_number}.jsonl','r') as f:
        kwargs= [json.loads(line) for line in f]

    prompts=[generate_prompt(kwarg,prompt_dict=prompt_dict) for kwarg in kwargs]
    
    answers=[]
    for idx,prompt_i in enumerate(prompts):
        print(f'Asking {idx}..')
        prompt=prompt_i['content']
        if idx==0:
            summarization=''
            response=solver(summarization=summarization, prompt=prompt,prompt_dict=prompt_dict)
        else:
            summarization=summarizer(summarization=summarization, prompt=prompt, response=response,prompt_dict=prompt_dict)        
            response=solver(summarization=summarization, prompt=prompt,prompt_dict=prompt_dict)
        answers.append(response)
        string=''

    for kwarg,prompt_i,answer in zip(kwargs,prompts,answers):
        task=kwarg['task']
        prompt=prompt_i['content']
        added=f'## {task}  \n**Prompt:**  \n{prompt}\n\n**Completion:**  \n{answer}\n\n'

    with open(f'{arxiv_number}_auto.md','w') as f:
        f.write(string)

def main():
    parser = argparse.ArgumentParser(description='Run problem solving with AI based on given template and Arxiv paper.')
    parser.add_argument('prompt_template', type=str, help='Path to the prompt template file.')
    parser.add_argument('arxiv_number', type=str, help='Arxiv paper number.')

    args = parser.parse_args()

    run(args.prompt_template, args.arxiv_number)

if __name__ == "__main__":
    main()

# To run this script, use the following exemplary command:
# python ../utils.py ../Prompt_template.md 2111.01152