### Install Ollama and start Qwen2 0.5b model


## Install Ollama in your device

Install Ollama using the below given command. # if already installed ignore this.

```
curl -fsSL https://ollama.com/install.sh | sh
```

## Run Qwen2 0.5b

Run a Qwen 2 0.5b in you localhost using the Ollama framework .

```
ollama run qwen2:0.5b
```
>
> Check if Ollama is running by going to http://localhost:11434/  # it will show 'Ollama is running'
>


### Directory setup

## Unzip and change to the Bayesian directory

After unzipping , change to that directory.

```bash
cd Bayesian/
```



## Create a virtual environment

Create and activate a virtual environment

- Using `venv` (Python 3.3+):
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```


## Project setup 

Install dependencies using requirements.txt

```bash
pip install -r requirements.txt
```


## Usage 

Run the script using a text file.

```
python summarize.py -f text.txt
```


> Rember to give -f or --file if you are giving a text file

Run the script with text as parameter.

```
python summarize.py -f "text_you_want_to_summarize"
```
> Rember to enclose your text in qoutes.


