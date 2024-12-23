1. create new files
- .env
```bash 
    OPENAI_API_KEY="" 
```
- .gitignore
``` bash
    .env
```
- main.py
``` bash
    import openai
    from dotenv import find_dotenv, load_dotenv

    load_dotenv()

    client = openai.OpenAI()
    model = "gpt-3.5-turbo-16k"
```
- requirements.txt
``` bash
    python-dotenv
    openai
```
2. set up the environment
``` bash
    python3 -m venev myenv
    source myenv/bin/activate
    pip install -r requierments.txt
```

# new-summarizer
